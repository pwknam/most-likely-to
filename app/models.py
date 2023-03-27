from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///superlatives.db')

Base = declarative_base()


class User(Base):
    # def __init__(self, username, password):
    #    self._id = None
    #    self._username = username
    #    self._password = password

    # @property
    # def username(self):
    #     return self._username
    
    # @property
    # def password(self):
    #     return self._password


    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username = Column(String())
    password = Column(String())

    # superlatives_created = relationship('Superlative', backref=backref('user'))
    superlatives_voted = relationship('Votes', backref=backref('user'))
    # user_nominations = relationship('Votes', backref=backref('user'))

class Nominees(Base):
    __tablename__ = 'nominees'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    
    superlatives_nominated = relationship('Votes', backref=backref('nominees'))



class Superlative(Base):
    # def __init__(self, name):
    #     self._id = None
        
    #     if isinstance(name, str):
    #        self._name = name
    #     else: print("Superlative must be a string")

    # @property
    # def name(self):
    #     return self._name

    __tablename__ = 'superlatives'

    id = Column(Integer(),primary_key=True)
    name = Column(String())
    # user_id = Column(Integer(), ForeignKey('users.id'))
    date_created = Column(DateTime(), server_default=func.now())
    # date_expired = Column(DateTime(), server_default=func.now() + 10000)

    superlative_votes = relationship('Votes', backref=backref('superlative'))




class Votes(Base):
    # def __init__(self, superlative_id, candidate_id):
    #     self._superlative_id = superlative_id
    #     self._candidate_id = candidate_id
    
    # @property
    # def superlative_id(self):
    #     return self._superlative_id
    
    # @property
    # def candidate_id(self):
    #     return self._candidate_id

    __tablename__ = 'votes'

    id = Column(Integer(), primary_key=True)
    voter_id = Column(Integer(), ForeignKey('users.id'))
    superlative_id = Column(Integer(), ForeignKey('superlatives.id'))
    candidate = Column(String(), ForeignKey('nominees.id'))
    date_voted = Column(DateTime(), server_default=func.now())


