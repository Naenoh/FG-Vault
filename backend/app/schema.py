import graphene
import sqlalchemy
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import text

from .models import Game as GameModel, Post as PostModel, Link as LinkModel, Char as CharModel, \
    Category as CategoryModel, db


class Category(SQLAlchemyObjectType):
    class Meta:
        model = CategoryModel


class Game(SQLAlchemyObjectType):
    class Meta:
        model = GameModel


class Post(SQLAlchemyObjectType):
    class Meta:
        model = PostModel


class Link(SQLAlchemyObjectType):
    class Meta:
        model = LinkModel


class Char(SQLAlchemyObjectType):
    class Meta:
        model = CharModel


class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        game_id = graphene.Int()
        char_id = graphene.Int()
        categories_id = graphene.List(graphene.Int)
        links = graphene.List(graphene.String)

    ok = graphene.Boolean()
    post = graphene.Field(Post)

    def mutate(self, info, title, game_id, char_id, categories_id, links):
        newpost = PostModel(title=title, game_id=game_id, char_id=char_id, associations_ids=categories_id)
        for link in links:
            db.session.add(LinkModel(url=link, post=newpost))
        db.session.commit()
        ok = True
        return CreatePost(ok=ok, post=newpost)


class CreateGame(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    ok = graphene.Boolean()
    game = graphene.Field(Game)
    error = graphene.String()

    def mutate(self, info, name):
        try:
            newgame = GameModel(name=name)
            db.session.add(newgame)
            db.session.commit()
            return CreateGame(game=newgame, ok=True)
        except sqlalchemy.exc.IntegrityError:
            return CreateGame(ok=False, error="erreur")


class CreateChar(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        game_id = graphene.Int()

    ok = graphene.Boolean()
    char = graphene.Field(Char)
    error = graphene.String()

    def mutate(self, info, name, game_id):
        try:
            newchar = CharModel(name=name, game_id=game_id)
            db.session.add(newchar)
            db.session.commit()
            return CreateChar(char=newchar, ok=True)
        except sqlalchemy.exc.IntegrityError as err:
            return CreateChar(ok=False, error=err)


class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    ok = graphene.Boolean()
    cat = graphene.Field(Category)
    error = graphene.String()

    def mutate(self, info, name):
        try:
            newcat = CategoryModel(name=name)
            db.session.add(newcat)
            db.session.commit()
            return CreateCategory(cat=newcat, ok=True)
        except sqlalchemy.exc.IntegrityError:
            return CreateCategory(ok=False, error="erreur")


class DeleteGame(graphene.Mutation):
    class Arguments:
        game_id = graphene.Int()

    ok = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, game_id):
        try:
            db.session.delete(GameModel.query.get(game_id))
            db.session.commit()
            return CreateGame(ok=True)
        except sqlalchemy.exc.IntegrityError:
            return CreateGame(ok=False, error="erreur")


class AllPosts(graphene.ObjectType):
    posts = graphene.List(Post)


class Mutations(graphene.ObjectType):
    create_post = CreatePost.Field()
    create_game = CreateGame.Field()
    create_char = CreateChar.Field()
    create_cat = CreateCategory.Field()
    delete_game = DeleteGame.Field()


class FilteredPosts(graphene.ObjectType):
    posts = graphene.List(Post)
    size = graphene.Int()


class Query(graphene.ObjectType):
    all_posts = graphene.Field(AllPosts)
    all_games = graphene.List(Game)
    filtered_posts = graphene.Field(FilteredPosts, title=graphene.String(default_value=""),
                                    game_id=graphene.Int(default_value=-1), char_id=graphene.Int(default_value=-1))

    def resolve_all_posts(self, info):
        return AllPosts(posts=PostModel.query.all())

    def resolve_all_games(self, info):
        return GameModel.query.all()

    def resolve_filtered_posts(self, info, title, game_id, char_id):
        print("blabla")
        terms = title.split(" ")
        regexp = "(?=.*" + ")(?=.*".join(terms) + ")"
        current_query = PostModel.query.filter(text("title ~* :regexp")).params(regexp=regexp)
        if char_id != -1:
            current_query = current_query.filter(PostModel.char_id == char_id)
        if game_id != -1:
            current_query = current_query.filter(PostModel.game_id == game_id)
        return FilteredPosts(posts=current_query, size=current_query.count())


schema = graphene.Schema(query=Query, mutation=Mutations)
