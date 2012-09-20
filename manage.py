#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   Manager for pywebase
#

import os
import sys
import logging

import settings
from packages import bottle
from packages import pyservice


# monkey patching for BaseHTTPRequestHandler.log_message
def log_message(obj, format, *args):
    logging.info("%s %s" % (obj.address_string(), format%args))

# -----------------------------------------------
#   Application
# -----------------------------------------------

# favicon.ico handling
@bottle.get('/favicon.ico')
def handle_favicon():
    return bottle.static_file('images/favicon.ico', root=settings.STATIC_PATH)

# static files handling
@bottle.route('/static/<filepath:path>')
def handle_static(filepath):
    return bottle.static_file(filepath, root=settings.STATIC_PATH)
    
@bottle.get('/')
@bottle.view('index')
def handle_index():
    return dict(name='pywebase')

# -----------------------------------------------
# Process to run
class BottleProcess(pyservice.Process):

    pidfile = settings.PYWEBASE_PIDFILE
    logfile = settings.PYWEBASE_LOGFILE

    def __init__(self):
        super(BottleProcess, self).__init__()
        
        from BaseHTTPServer import BaseHTTPRequestHandler
        BaseHTTPRequestHandler.log_message = log_message
            
    def run(self):
        logging.info('bottle.py {} server starting up'.format(bottle.__version__))
        bottle.TEMPLATE_PATH.append(settings.TEMPLATE_PATH)
        bottle.run(host='localhost', port=8080, debug=settings.DEBUG_MODE)

if __name__ == '__main__':

    if len(sys.argv) == 2 and sys.argv[1] in 'start stop restart status'.split():
        pyservice.service('manage.BottleProcess', sys.argv[1])
    else:
        print 'usage: manager <start,stop,restart,status>'

