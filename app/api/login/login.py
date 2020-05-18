from flask import flash, render_template, redirect, url_for, Blueprint, make_response, request
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
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return make_response(render_template('login.html'))
