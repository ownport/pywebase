#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   Manager for pywebase
#

import os
import sys
import settings

from packages import bottle
from packages import pywebase

# -----------------------------------------------
#   Application functions
# -----------------------------------------------

bottle.route('/', 'GET', pywebase.handle_index)
bottle.route('/favicon.ico', 'GET', pywebase.handle_favicon)
bottle.route('/static/<filepath:path>', 'GET', pywebase.handle_static)

# -----------------------------------------------
#   Application
# -----------------------------------------------

if __name__ == '__main__':
    
    from packages import pyservice

    if len(sys.argv) == 2 and sys.argv[1] in 'start stop restart status'.split():
        pyservice.service('packages.pywebase.PywebaseProcess', sys.argv[1])
    else:
        print 'usage: manager <start,stop,restart,status>'

