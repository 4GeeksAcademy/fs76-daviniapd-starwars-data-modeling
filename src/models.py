import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)

class Character(Base):
    __tablename__ = 'Characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    specie = Column(String(250), nullable=False)
    role = Column(String(250), nullable=False)
    lifeStatus = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    homeworld_id = Column(Integer, ForeignKey('planet.id'))

class User_Character(Base):
    __tablename__ = 'User_Character'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))

class Planet(Base):
    __tablename__ = 'Planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False) 
    galactic_location = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    native_species = Column(String(250), nullable=False)
    government  = Column(String(250), nullable=False)

class User_Planet(Base):
    __tablename__ = 'User_Planet'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))

class Vehicle(Base):
    __tablename__ = 'Vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    vehicles_class = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    autonomy = Column(String(250), nullable=False)
    weapons = Column(String(250), nullable=False)
    passengers  = Column(String(250), nullable=False)

class User_Vehicle(Base):
    __tablename__ = 'User_Vehicle'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
