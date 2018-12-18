from flask_graphql import GraphQLView
from app import app, db
from app.models import Game
from .schema import schema
import os

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=os.environ.get('ENV','') != 'production'  # for having the GraphiQL interface
    )
)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()


if __name__ == '__main__':
    db.create_all()
    app.run()
