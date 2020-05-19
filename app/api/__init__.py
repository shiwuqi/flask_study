from flask import flash, render_template, redirect, url_for, Blueprint
from flask_restful import Api

bp = Blueprint('api', __name__)

from .hello.hello_world import HelloWorld
from .login.login import Login
from .login.query import Query
from .login.user_info import UserInfo
from .login.add_role import AddRole
from .login.query_role import QueryRole

# api = Api(app)
api = Api(bp, catch_all_404s=True)

api.add_resource(HelloWorld, '/')

api.add_resource(Login, '/login')

api.add_resource(Query, '/query')

api.add_resource(UserInfo, '/user/info')

api.add_resource(AddRole, '/add/role')

api.add_resource(QueryRole, '/query/role')
