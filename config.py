import os

class Config(object):
    SECRET_KEY = 'a9087FFJFF9nnvc2@#$%FSD'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/test?charset=utf8'

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}