# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from .database import Base
from app import db

Column = db.Column
Integer = db.Integer
String = db.String
relationship = db.relationship
ForeignKey = db.ForeignKey


class Post(db.Model):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    game_id = Column(Integer, ForeignKey('games.id'))
    game = relationship('Game', backref='posts')

    def __repr__(self):
        return '<Post %r>' % self.title


class Game(db.Model):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)

    def __repr__(self):
        return '<Game %r>' % self.name


class Char(db.Model):
    __tablename__ = 'chars'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    game_id = Column(Integer, ForeignKey('games.id'))
    game = relationship('Game', backref='chars')

    def __repr__(self):
        return '<Char %r>' % self.name


class Link(db.Model):
    __tablename__ = 'links'
    id = Column(Integer, primary_key=True)
    url = Column(String(255), unique=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship('Post', backref='links')

    def __repr__(self):
        return '<Link %r>' % self.url
