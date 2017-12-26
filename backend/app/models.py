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
    game = relationship('Game', backref='post')

    def __repr__(self):
        return '<Post %r>' % self.title


class Game(db.Model):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)

    def __repr__(self):
        return '<Game %r>' % self.name

