# -*- coding: utf-8 -*-
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
#===============================================
# configuration part for the whole project
#===============================================
__version__ = '0.1'
app = Flask('project')
app.config['SECRET_KEY'] = '8WEAy3VyhxXiviiAlklghk6N7jWnqoFptd8NvRs3lXE' # some salt we added to the cookies ;)
app.debug = False # Enable / Disable debuging of the app
toolbar = DebugToolbarExtension(app)
from project.controllers import * #import of all the controllers in the project
