# Mars Rocks app

Our webapp allows users to identify interesting features on Mars using the Mars rover images.

[Mars Rocks live site](https://marsrocks.herokuapp.com/)


## project setup

We are using Python 2.7.x., postgres database, and Flask.

Read [computer set](https://github.com/LearnToCodeLA/marsrocks/wiki/Computer-setup) to make sure you have the basic requirements installed.

install python packages.

Flask is a framework to create web apps.  
Psycopg is a Python adapter for Postgres.  
SQLAlchemy is a Python ORM.  
Flask-Migrate is database migration library.  
gunicorn is a server.  
```
$ pip install  Flask  psycopg2 Flask-SQLAlchemy Flask-Migrate gunicorn
```

download the repo
```
$ git clone git@github.com:LearnToCodeLA/marsrocks.git
```

change into the directory of the repo

```
$ cd marsrocks
```

start the server

```
$ python app.py
```
visit the website

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

or 

[http://locahost:5000/](http://locahost:5000/)
