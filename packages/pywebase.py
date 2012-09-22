#
#   pywebase core
#

import logging
import settings

from packages import bottle
from packages import pyservice

# monkey patching for BaseHTTPRequestHandler.log_message
def log_message(obj, format, *args):
    logging.info("%s %s" % (obj.address_string(), format%args))

# -----------------------------------------------
# Process to run
# -----------------------------------------------
class PywebaseProcess(pyservice.Process):

    pidfile = settings.PYWEBASE_PIDFILE
    logfile = settings.PYWEBASE_LOGFILE

    def __init__(self):
        super(PywebaseProcess, self).__init__()
        
        from BaseHTTPServer import BaseHTTPRequestHandler
        BaseHTTPRequestHandler.log_message = log_message
            
    def run(self):
        logging.info('pywebase {} server starting up'.format(bottle.__version__))
        bottle.TEMPLATE_PATH.append(settings.TEMPLATE_PATH)
        bottle.run(host='localhost', port=8080, debug=settings.DEBUG_MODE)

# -----------------------------------------------
# utils
# -----------------------------------------------
def add_routes(*routes):
    ''' add static/dynamic routes '''
    for url, method, handler in routes:
        bottle.route(url, method, handler)

# -----------------------------------------------
# Request handlers
# -----------------------------------------------

# favicon.ico handling
def handle_favicon():
    return bottle.static_file('images/favicon.ico', root=settings.STATIC_PATH)

# static files handling
def handle_static(filepath):
    return bottle.static_file(filepath, root=settings.STATIC_PATH)
    
# main/index page
def handle_index():
    return bottle.template('index', dict(name='pywebase'))

# login form
def handle_login():
    return 
    
# logout
def handle_logout():
    return     
    
    
    
