#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   Manager for pywebase
#

from packages import pywebase

# -----------------------------------------------
#   Application functions (they can be changed 
#   in your application)
# -----------------------------------------------

pywebase.add_routes(
    ('/', 'GET', pywebase.handle_index),
    ('/favicon.ico', 'GET', pywebase.handle_favicon),
    ('/static/<filepath:path>', 'GET', pywebase.handle_static),
    ('/login', 'GET', pywebase.handle_login),
    ('/logout', 'GET', pywebase.handle_logout),
)

# -----------------------------------------------
#   Main
# -----------------------------------------------

if __name__ == '__main__':
    
    import sys
    from packages import pyservice

    if len(sys.argv) == 2 and sys.argv[1] in 'start stop restart status'.split():
        pyservice.service('packages.pywebase.PywebaseProcess', sys.argv[1])
    else:
        print 'usage: manage <start,stop,restart,status>'

