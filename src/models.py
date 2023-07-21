import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er



Base = declarative_base()
class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(Integer, primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.id'), nullable=False)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250))
    first_name = Column(String(250))
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), ForeignKey('follower.user_from_id'))

    # Relaciones inversas para User-Follower
    followers = relationship('Follower', backref='user_from', foreign_keys=[Follower.user_to_id])
    following = relationship('Follower', backref='user_to', foreign_keys=[Follower.user_from_id])

    def to_dict(self):
        return {}

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    comment_text = Column(String)
    post_id = Column(Integer, ForeignKey('post.id'))

    author = relationship('User', backref='comments')
    post = relationship('Post', backref='comments')

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_text = Column(String)

    author = relationship('User', backref='posts')

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(250))
    url= Column(String)
    post_id = Column(Integer, ForeignKey('post.id'))

    post = relationship('Post')





## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
