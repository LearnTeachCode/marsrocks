# Transit app

[setup computer](https://gist.github.com/wykhuh/53a2008fdf56bb4b137d/)

[demo](https://transit-py-staging.herokuapp.com/)


## project setup

We are using Python 2.7.10

clone repo
```
$ git clone git@github.com:LearnToCodeLA/transit.git
```

create virtual environment.

If you don't have virtualenv, see [setup computer](https://gist.github.com/wykhuh/53a2008fdf56bb4b137d/).

```
$  mkvirtualenv --python=/path/to/python transit
```
install packages

Psycopg is a Python adapter for Postgre.
SQLAlchemy is a Python ORM.
Flask-Migrate is database migration library.
```
(transit) $ pip install psycopg2 Flask-SQLAlchemy Flask-Migrate
```

add project path to enviroment

```
(transit) $ atom $VIRTUAL_ENV/bin/postactivate

```
add to postactivate file

```
cd ~/path/to/your/project
```

launch app

```
(transit) $ python app.py
```
