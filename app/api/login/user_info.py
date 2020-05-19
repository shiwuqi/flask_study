from flask import flash, render_template, redirect, url_for, Blueprint, make_response, request
from flask_restful import Resource
from app.models import Info
from app import db

class UserInfo(Resource):
    def get(self):
        return make_response(render_template('user_info.html'))


    def post(self):
        username = request.form.get('username')
        age = request.form.get('age')
        school = request.form.get('school')
        degree = request.form.get('degree')
        hometown = request.form.get('hometown')
        print(username, age, school, degree, hometown)
        # role = Roles(username=username)
        info = Info(username=username, age=age, school=school, degree=degree, hometown=hometown)
        db.session.add(info)
        db.session.commit()
        return make_response('添加成功')