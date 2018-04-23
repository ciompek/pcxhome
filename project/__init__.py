# -*- coding: utf-8 -*-
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
import config as cfg
#===============================================
# configuration part for the whole project
#===============================================
__version__ = cfg.app['version']
app = Flask('project')
app.config['SECRET_KEY'] = cfg.app['SECRET_KEY'] # some salt we added to the cookies ;)
app.debug = cfg.app['debug'] # Enable / Disable debuging of the app

toolbar = DebugToolbarExtension(app)
from project.controllers import * #import of all the controllers in the project
