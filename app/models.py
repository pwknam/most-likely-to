from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///superlatives.db')

Base = declarative_base()


class User(Base):
    def __init__(self, username, password):
       self._username = username
       self._password = password
       
    
    @property
    def username(self):
        return self._username
    
    @property
    def password(self):
        return self._password


    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username = Column(String())
    password = Column(String())

    superlatives_created = relationship('Superlative',)

class Superlative(Base):
    def __init__(self, name, create_date):
        if isinstance(name, str):
           self._name = name
        else: print("Superlative must be a string")

        # if isinstance(create_date, str):
        #    self._create_date = SOME FUNCTION THAT PULLS IND ATE

    @property
    def name(self):
        return self._name

    __tablename__ = 'superlatives'

    id = Column(Integer(),primary_key=True)
    name = Column(String())
    user_id = Column(Integer(), ForeignKey('users.id'))



    # def get_create_date(self):
    #     return self._create_date
    # phone = property(get_create_date)

class Votes:
    def __init__(self, superlative_id, candidate_id):
        self._superlative_id = superlative_id
        self._candidate_id = candidate_id
    
    def get_superlative_id(self):
        return self._superlative_id

    superlative = property(get_superlative)

    def get_candidate_id(self):
        return self._candidate_id

    candidate_id = property(get_candidate_id)
