import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Float, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    img_url = Column(String(250))
    description = Column(Text)
    gender = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    hair_color = Column(String(250))
    height = Column(Float)
    birth_year = Column(Integer)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    img_url = Column(String(250))
    description = Column(Text)
    model = Column(String(250))
    manufacturer = Column(String(250))
    crew = Column(Integer)
    length = Column(Integer)
    cost_in_credits = Column(Float)
    max_atmosphering_speed = Column(Float)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    img_url = Column(String(250))
    description = Column(Text)
    climate = Column(String(250))
    population = Column(Integer)
    terrain = Column(String(250))
    diameter = Column(Float)
    surface_water = Column(Integer)
    orbital_period = Column(Float)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    body = Column(Text)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    created_at = Column(DateTime)
    modified_at = Column(DateTime)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment = Column(Text)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    created_at = Column(DateTime)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)
    vehicle_id =  Column(Integer, ForeignKey('vehicle.id'))
    vehicle = relationship(Vehicle)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')