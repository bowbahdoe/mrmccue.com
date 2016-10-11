'''
Starting point for execution of the server
'''

import warnings
import mrmccue.helpers
import flask
from flask import Flask

#####################################################
# Flask MongoEngine Currently has an annoying       #
# warning about ExtDepreciation, so we disable that #
# Then import MongoEngine, which we use for the db  #
#####################################################

from flask.exthook import ExtDeprecationWarning

with warnings.catch_warnings():
    warnings.simplefilter('ignore', ExtDeprecationWarning)
    from flask_mongoengine import MongoEngine

###########################################################
# The main app instance                                   #
#                                                         #
# This is passed around the application to handle routing #
###########################################################
app = Flask(__name__)

############################################################
# Load in configuration instead of defining explicitly     #
# within this file. consult the file if a change is needed #
############################################################
app.config.from_pyfile('config.py')

#######################################################################
# When Jinja renders a template it doesnt care about whitespace       #
# So if we are debugging, We want the document to be nicely formatted #
#                                                                     #
# On the flipside, if we aren't debugging, we want to minimize the    #
# size of the html getting sent out                                   #
#######################################################################
if app.debug:
    flask.render_template = helpers.prettify(flask.render_template)
else:
    flask.render_template = helpers.uglify(flask.render_template)

###############################################################
# Sets the variable db to represent our connection to MongoDB #
# This is needed by blueprints that want to define their own  #
# models                                                      #
###############################################################
db = MongoEngine(app)
app.static_url_path = '/'

from location_tracker.views import location_tracker
app.register_blueprint(location_tracker)
