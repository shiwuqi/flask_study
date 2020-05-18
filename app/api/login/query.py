from flask import flash, render_template, redirect, url_for, Blueprint, make_response, request
from flask_restful import Resource
from app.models import User
from app import db
from ..util import model_to_dict

class Query(Resource):
    def post(self):
        username = request.form.get('username')
        result = User.query.filter_by(username=username).first()
        if result is None:
            return make_response('未查询到该用户')
        else:
            _data = model_to_dict(result)
            return make_response(_data)