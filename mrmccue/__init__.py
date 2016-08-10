'''
Starting point for execution of the server
'''

from flask import Flask

###########################################################
# The main app instance                                   #
#                                                         #
# This is passed around the application to handle routing #
###########################################################
app = Flask(__name__)

import mrmccue.views

app.run(debug=True)
