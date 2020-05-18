from flask import Flask
from flask_cors import CORS
from config import config
from flask_sqlalchemy import SQLAlchemy

# 简历数据库关系
db = SQLAlchemy()

# from app import routes
def create_app(config_name):
    app = Flask(__name__)
    print(config[config_name])
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    CORS(app)
    db.init_app(app)
    from . import api
    app.register_blueprint(api.bp)
    return app
