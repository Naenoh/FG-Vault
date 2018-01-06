import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from .models import Game as GameModel, Post as PostModel, Link as LinkModel, Char as CharModel, db


class Game(SQLAlchemyObjectType):
    class Meta:
        model = GameModel
        interfaces = (relay.Node,)


class Post(SQLAlchemyObjectType):
    class Meta:
        model = PostModel
        interfaces = (relay.Node,)


class Link(SQLAlchemyObjectType):
    class Meta:
        model = LinkModel
        interfaces = (relay.Node,)


class Char(SQLAlchemyObjectType):
    class Meta:
        model = CharModel
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_posts = SQLAlchemyConnectionField(Post)


schema = graphene.Schema(query=Query)
