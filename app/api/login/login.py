from flask import flash, render_template, redirect, url_for, make_response, request
from flask_restful import Resource
from app.models import User
from app import db

class Login(Resource):
    def get(self):
        return make_response(render_template('login.html'))


    def post(self):
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role')
        user = User(username=username, email=email, password=password, role_id=role)
        db.session.add(user)
        db.session.commit()
        return make_response('登录成功')
