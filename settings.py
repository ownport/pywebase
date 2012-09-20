#
#   Settings
#
import os

# During early development, the debug mode can be very helpful.
# In this mode, Bottle is much more verbose and provides helpful 
# debugging information whenever an error occurs. It also 
# disables some optimisations that might get in your way and adds 
# some checks that warn you about possible misconfiguration.
# Here is an incomplete list of things that change in debug mode:
#
# - The default error page shows a traceback.
# - Templates are not cached.
# - Plugins are applied immediately.
#
# Just make sure not to use the debug mode on a production server.
DEBUG_MODE = True

# The absolute path to the directory where static files are located
STATIC_PATH = os.path.join(os.getcwd(), 'static')

# The absolute path to the directory where template files (*.tpl) are 
# located
TEMPLATE_PATH = os.path.join(os.getcwd(), 'templates')


