from app import app,db
# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     db_session.remove()
from app.models import Game


@app.route('/')
def hello_world():
    bla = Game.query.first()
    return 'Hello %s' % bla.name

if __name__ == '__main__':
    db.create_all()
    app.run()
