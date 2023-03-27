from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///superlatives.db')

Base = declarative_base()


class User(Base):
  
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username = Column(String())
    password = Column(String())

    superlatives_created = relationship('Superlative', backref=backref('user'))
    superlatives_voted = relationship('Votes', backref=backref('user'))

class Nominees(Base):
    __tablename__ = 'nominees'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    
    superlatives_nominated = relationship('Votes', backref=backref('nominees'))



class Superlative(Base):

    __tablename__ = 'superlatives'

    id = Column(Integer(),primary_key=True)
    name = Column(String())
    author_id = Column(Integer(), ForeignKey('users.id'))
    date_created = Column(DateTime(), server_default=func.now())
    date_expired = Column(DateTime(), server_default=func.now())

    superlative_votes = relationship('Votes', backref=backref('superlative'))




class Votes(Base):

    __tablename__ = 'votes'

    id = Column(Integer(), primary_key=True)
    voter_id = Column(Integer(), ForeignKey('users.id'))
    superlative_id = Column(Integer(), ForeignKey('superlatives.id'))
    nominee_id = Column(Integer(), ForeignKey('nominees.id'))
    date_voted = Column(DateTime(), server_default=func.now())


