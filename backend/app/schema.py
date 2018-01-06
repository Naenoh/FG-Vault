import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from graphql_relay import from_global_id

from .models import Game as GameModel, Post as PostModel, Link as LinkModel, Char as CharModel, db


class Game(SQLAlchemyObjectType):
    class Meta:
        model = GameModel
        interfaces = (relay.Node,)
    dbid = graphene.Int()

    def resolve_dbid(self,info):
        return self.id


class Post(SQLAlchemyObjectType):
    class Meta:
        model = PostModel
        interfaces = (relay.Node,)
    dbid = graphene.Int()

    def resolve_dbid(self,info):
        return self.id


class Link(SQLAlchemyObjectType):
    class Meta:
        model = LinkModel
        interfaces = (relay.Node,)
    dbid = graphene.Int()

    def resolve_dbid(self,info):
        return self.id


class Char(SQLAlchemyObjectType):
    class Meta:
        model = CharModel
        interfaces = (relay.Node,)
    dbid = graphene.Int()

    def resolve_dbid(self,info):
        return self.id


class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        game_id = graphene.String()
        char_id = graphene.String()
        links = graphene.List(graphene.String)

    ok = graphene.Boolean()
    post = graphene.Field(Post)

    def mutate(self, info, title, game_id, char_id, links):
        newpost = PostModel(title=title, game_id=game_id, char_id=char_id)
        for link in links:
            db.session.add(LinkModel(url=link, post=newpost))
        db.session.commit()
        ok = True
        return Post(newpost)


class CreateGame(graphene.Mutation):
    class Arguments:
        name = graphene.String()
    ok = graphene.Boolean()
    game = graphene.Field(Game)

    def mutate(self, info, name):
        newgame = GameModel(name=name)
        db.session.add(newgame)
        db.session.commit(newgame)


class Mutations(graphene.ObjectType):
    create_post = CreatePost.Field()
    create_game = CreateGame.Field()


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_posts = SQLAlchemyConnectionField(Post)
    all_games = SQLAlchemyConnectionField(Game)


schema = graphene.Schema(query=Query, mutation=Mutations)
