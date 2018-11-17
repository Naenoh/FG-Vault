# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.sql import func

# from .database import Base
from app import db

Column = db.Column
Integer = db.Integer
String = db.String
relationship = db.relationship
ForeignKey = db.ForeignKey
DateTime = db.DateTime
backref = db.backref

Base = declarative_base()
# We will need this for querying
Base.query = db.session.query_property()


cats = db.Table('cats',
                Column('post_id', Integer, ForeignKey('posts.id'), primary_key=True),
                Column('category_id', Integer, ForeignKey('categories.id'), primary_key=True))


class Category(db.Model):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)

    def __repr__(self):
        return '<Category %r>' % self.name


class Post(db.Model):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(String(10000))
    game_id = Column(Integer, ForeignKey('games.id'))
    game = relationship('Game', backref='posts', lazy=False)
    char_id = Column(Integer, ForeignKey('chars.id'))
    char = relationship('Char', backref='posts', lazy=False)
    categories = relationship('Category', secondary=cats, lazy=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())

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
    name = Column(String(64))
    game_id = Column(Integer, ForeignKey('games.id'))
    game = relationship('Game', backref=backref('chars', lazy=False))

    def __repr__(self):
        return '<Char %r>' % self.name


class Link(db.Model):
    __tablename__ = 'links'
    id = Column(Integer, primary_key=True)
    url = Column(String(255), unique=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship('Post', backref=backref('links', lazy=False))

    def __repr__(self):
        return '<Link %r>' % self.url


class CatsAssociation(Base):
    __table__ = cats
    post = relationship(Post, backref="association_recs")

Post.associations_ids = association_proxy("association_recs", "category_id",
                                          creator=lambda uid: CatsAssociation(category_id=uid))