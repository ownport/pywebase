# pywebase

Small platform for local web application. It's based on the next components:

 - [bottle.py](http://bottlepy.org/) is a fast, simple and lightweight WSGI micro web-framework for Python. It is distributed as a single file module and has no dependencies other than the Python Standard Library.
 - [pyservice](https://github.com/ownport/pyservice) is simple library to make service on python more easy
 - [bootstrap](https://github.com/twitter/bootstrap) is HTML, CSS, and JS toolkit from Twitter
 
## Installation

To install pywebase you need just download [latest pywebase package](https://github.com/ownport/pywebase/zipball/master), unpack it in your directory, in pywebase directory create two new directories `log/` and `run/`. These directories will be needed for logs and pidfile when pywebase is running.

After these operation you should see the next directory structure
```
log/
run/
static/
packages/
templates/
NOTICE
manage.py
README.md
settings.py
```

## Manage pywebase

pywebase supports to run bottle.py as service
```
$ python manage.py start
Starting process with BottleProcess...
$
```
To check status of pywebase
```
$ python manage.py status
Process BottleProcess is running, pid: 5409
$
```
To stop pywebase
```
$ python manage.py stop
Stopping process BottleProcess...
$
$ python manage.py status
Process is not running
$
```
In case you need to restart pywebase
```
$ python manage.py restart
Stopping process BottleProcess...
Starting process with BottleProcess...
$ 
```

