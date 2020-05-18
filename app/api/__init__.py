from flask import flash, render_template, redirect, url_for, Blueprint
from flask_restful import Api

bp = Blueprint('api', __name__)

from .hello.hello_world import HelloWorld
from .login.login import Login
from .login.query import Query

# api = Api(app)
api = Api(bp, catch_all_404s=True)

api.add_resource(HelloWorld, '/')

api.add_resource(Login, '/login')

api.add_resource(Query, '/query')
