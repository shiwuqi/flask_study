from flask import flash, render_template, redirect, url_for, Blueprint, make_response, request
from flask_restful import Resource
from app.models import Role
from app import db

class AddRole(Resource):
    def get(self):
        return make_response(render_template('role.html'))

    def post(self):
        name = request.form.get('name')
        role = Role(name=name)
        db.session.add(role)
        db.session.commit()
        return make_response('添加成功')