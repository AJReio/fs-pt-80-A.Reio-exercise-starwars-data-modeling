import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    email = Column(String, nullable = False, unique = True)
    password = Column(String, nullable = False)

    def to_dict(self):
        return{
            'id': self.id,
            'email': self.email
        }
    
class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key = True)
    title = Column(String, nullable = False)
    content = Column(String, nullable = False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('Users', backref = 'posts')
    def to_dict(self):
        return{
            'id': self.id,
            'content': self.content
        }

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key = True)
    content = Column(String, nullable = False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('Users', backref = 'comments')
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship('Posts', backref = 'comments')
    def to_dict(self):
        return{
            'id': self.id,
            'content': self.content
        }
    
class Medias(Base):
    __tablename__ = 'medias'
    id = Column(Integer, primary_key = True)
    src = Column(String, nullable = False)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship('Posts', backref = 'medias')
    def to_dict(self):
        return{
            'id': self.id,
            'content': self.content
        }


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e