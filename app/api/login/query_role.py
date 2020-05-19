from flask import flash, render_template, redirect, url_for, Blueprint, make_response, request
from flask_restful import Resource
from app.models import User, Role
from app import db

class QueryRole(Resource):
    def get(self):
        return make_response(render_template('query_role.html'))

    def post(self):
        name = request.form.get('name')
        user = User.query.filter_by(username=name).first()
        if user is None:
            return make_response('未查询到该用户')
        role_id = user.role_id
        role = Role.query.filter_by(id=role_id).first()
        if role is None:
            return make_response('未查询到该用户的角色')
        return make_response(role.name)