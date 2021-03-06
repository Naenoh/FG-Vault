# FG Vault - [fgvault.net](https://fgvault.net)

## What is this ?

This is a website made to centralize and store links to fighting games related resources.

## Why did you make it ?

A lot of resources are scattered in many places (wikis, discords, forums, subreddits, youtube, twitter...) with no convenient way to look for them all at once. The goal of this website is to have a place where people can post resources they create or find to allow others to look for them easily.

## How is it made ?

The secondary (might be primary if it goes unused) goal of this website for me was to learn about new technologies and tools. I tried to go for a stack I knew almost nothing about. The Frontend is built with Vue.js and Bulma. The Backend is made with Flask and SQLAlchemy. To connect the two parts, I decided to go for a GraphQL based API. To do that, i'm using Graphene on the server side and Apollo for the client. The database is Graphene and I'm using Docker with Docker Compose to facilitate deployement. I'm also using Fabric to easily run various tasks remotely. 

## Can I contribute ?

Sure ! The following section should allow you to setup your local development environement. If you need any more help just ask me.

## Local development setup and usage

### Frontend

Every command here is meant to be run in the `frontend` directory

- Requirements : nodeJS (6.0.0+) with npm(3.0.0+)
- Installing the app dependencies : `npm install`
- Running the app : `npm run dev`
- Building the app (can be useful to check file size for example) : `npm run build`
- Additional commands may be found in the `README.md` file located inside the `frontend` folder

### Backend

Every command here is meant to be run in the `backend` directory

- Requirements :
 - Python 3.6+ with pip (previous versions aren't tested but might work)
 - Postgresql 10.6 (other versions aren't tested but might work)
 - (Recommended) A dedicated Python virtual environnement (see [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/))

- Installing the app :
  - If using one, activate your virtual environnement
  - create an empty postgresql database (in psql, as postgres/admin user) : `CREATE DATABASE yourdbname; CREATE USER yourdbuser WITH ENCRYPTED PASSWORD 'yourdbpass'; GRANT ALL PRIVILEGES ON DATABASE yourdbname TO yourdbuser;`
  - configure the database URI by creating a `dev_config.py` file in the app folder with `SQLALCHEMY_DATABASE_URI = 'postgresql://YOURDBUSER:YOURDBPASS@127.0.0.1:YOURDBPORT/YOURDBNAME'`. You can also set `GRAPHIQL = True` inside to get access to the graphql console.
  - Install dependencies : `pip install -r requirements.txt`
  - Create (or reset) database tables : `python resetdb.py`
  - Load the base data for the app : 
    - `psql -U YOURDBUSER YOURDBNAME -f categories.sql`
    - `python charscript.py && psql -U YOURDBUSER YOURDBNAME -f gamechars.sql && rm gamechars.sql`
- Run the app `python manage.py runserver`
- Generate new migrations after altering the models : `python manage.py db migrate`
- Update the database from migrations : `python manage.py db migrate`

### Additional notes

Some of the files in the repository are only meant for deployement (everything related to Fabric and Docker for example).

## Docs

- [Vue](https://vuejs.org/v2/api/)
- [Vue-test-utils](https://vue-test-utils.vuejs.org/)
- [Vue-Apollo](https://akryum.github.io/vue-apollo/guide/)
- [Bulma](https://bulma.io/documentation/)


- [Flask](http://flask.pocoo.org/docs/1.0/)
- [SQL Alchemy](https://docs.sqlalchemy.org/en/latest/)
- [Flask-SQL Alchemy](http://flask-sqlalchemy.pocoo.org/2.3/)
- [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/#)
- [Graphene](https://docs.graphene-python.org/en/latest/)
- [PostgreSQL](https://www.postgresql.org/docs/current/static/index.html)


- [Fabric](http://docs.fabfile.org/en/2.4/)