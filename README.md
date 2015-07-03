# Mars Rocks app


Our webapp allows users to identify interesting features on Mars using the Mars rover images.

[Mars Rocks live site](https://marsrocks.herokuapp.com/)


[![Build Status](https://travis-ci.org/LearnToCodeLA/marsrocks.svg)](https://travis-ci.org/LearnToCodeLA/marsrocks)

## project setup

We are using Python 2.7.x., postgres database, and Flask.

Read [computer setup](https://github.com/LearnToCodeLA/marsrocks/wiki/Computer-setup) to make sure you have the basic requirements installed.

1) install python packages.

Flask is a framework to create web apps.  
Psycopg is a Python adapter for Postgres.  
SQLAlchemy is a Python ORM.  
Flask-Migrate is database migration library.  
gunicorn is a server.  
```
$ pip install  Flask  psycopg2 Flask-SQLAlchemy Flask-Migrate gunicorn
```

2) download the repo

if you have ssh set up

```
$ git clone git@github.com:LearnToCodeLA/marsrocks.git
```

if you don't have ssh
```
$ git clone https://github.com/LearnToCodeLA/marsrocks.git
```

3) change into the directory of the repo

```
$ cd marsrocks
```

4) start the server

```
$ python app.py
```

5) visit the website

[http://127.0.0.1:5000/](http://127.0.0.1:5000/) or [http://locahost:5000/](http://locahost:5000/)

6) start coding

Follow the guidelines for our [git workflow](https://github.com/LearnToCodeLA/marsrocks/wiki/Github-workflow).
