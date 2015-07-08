# Mars Rocks app


Our webapp allows users to identify interesting features on Mars using the Mars rover images.

[Mars Rocks live site](https://marsrocks.herokuapp.com/)


[![Build Status](https://travis-ci.org/LearnToCodeLA/marsrocks.svg)](https://travis-ci.org/LearnToCodeLA/marsrocks)

## project setup

We are using Python 2.7.x., sqlite3, postgres, and Flask.

Read [computer setup](https://github.com/LearnToCodeLA/marsrocks/wiki/Computer-setup) to make sure you have the basic requirements installed.


1) download the repo

if you have ssh set up

```
$ git clone git@github.com:LearnToCodeLA/marsrocks.git
```

if you don't have ssh
```
$ git clone https://github.com/LearnToCodeLA/marsrocks.git
```

2) change into the directory of the repo

```
$ cd marsrocks
```

3) install python packages.

```
$ pip install -r requirements.txt
```
if you get errors during installation, try:

```
$ sudo pip install -r requirements.txt
```

4) create a sqlite3 database
```
$ python db_create_db.py
```

5) start the server

```
$ python app.py
```

6) visit the website

[http://127.0.0.1:5000/](http://127.0.0.1:5000/) or [http://locahost:5000/](http://locahost:5000/)

7) start coding

Follow the guidelines for our [git workflow](https://github.com/LearnToCodeLA/marsrocks/wiki/Github-workflow).
