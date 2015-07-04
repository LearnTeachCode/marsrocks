# Mars Rocks app


Our webapp allows users to identify interesting features on Mars using the Mars rover images.

[Mars Rocks live site](https://marsrocks.herokuapp.com/)


[![Build Status](https://travis-ci.org/LearnToCodeLA/marsrocks.svg)](https://travis-ci.org/LearnToCodeLA/marsrocks)

## project setup

We are using Python 2.7.x., postgres database, and Flask.

Read [computer setup](https://github.com/LearnToCodeLA/marsrocks/wiki/Computer-setup) to make sure you have the basic requirements installed.

1) create a postgres database
```
$ createdb marsrocks
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

4) install python packages.

```
$ pip install -r requirements.txt
```
if you get errors during installation, try:

```
$ sudo pip install -r requirements.txt
```

5) Follow these steps to [set up environment variables](https://github.com/LearnToCodeLA/marsrocks/wiki/setup-environmental-variables,--virtual-environments). If you have autoenv, copy these two lines into .env file. If you have virtualenvwrapper, copy these two lines into the postactivate file.

```
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL="postgresql://localhost/marsrocks"
```

6) start the server

```
$ python app.py
```

7) visit the website

[http://127.0.0.1:5000/](http://127.0.0.1:5000/) or [http://locahost:5000/](http://locahost:5000/)

8) start coding

Follow the guidelines for our [git workflow](https://github.com/LearnToCodeLA/marsrocks/wiki/Github-workflow).
