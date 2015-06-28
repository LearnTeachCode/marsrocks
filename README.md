# Mars Rocks app

Our webapp allows users to identify interesting features on Mars using the Mars rover images.

[Mars Rocks live site](https://marsrocks.herokuapp.com/)


## project setup

We are using Python 2.7.x., postgres database, and Flask.

Read [computer setup](https://github.com/LearnToCodeLA/marsrocks/wiki/Computer-setup) to make sure you have the basic requirements installed.

clone repo
```
$ git clone git@github.com:LearnToCodeLA/transit.git
```

install packages.

Flask is a framework to create web apps.
Psycopg is a Python adapter for Postgres.
SQLAlchemy is a Python ORM.
Flask-Migrate is database migration library.
gunicorn is a server.
```
$ pip install  Flask  psycopg2 Flask-SQLAlchemy Flask-Migrate gunicorn
```

launch app

```
$ python app.py
```
