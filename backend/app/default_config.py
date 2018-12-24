import os

SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
    os.environ.get('POSTGRES_DB_USER','fgvaultuser'),
    os.environ.get('POSTGRES_DB_PWD','fgvaultpass'),
    os.environ.get('POSTGRES_DB_HOST','127.0.0.1'),
    os.environ.get('POSTGRES_DB_PORT','5432'),
    os.environ.get('POSTGRES_DB_NAME','fgvault'))

SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
GRAPHIQL = False