from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime
from flask import current_app
from app import db


class User(db.Model):
    """用户表"""
    __tablename__ = "users"  # 指明数据库的表名

    id = db.Column(db.Integer, primary_key=True)  # 整型的主键，会默认设置为自增主键
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))

    def __repr__(self):
        return "User %r" % self.username

    
# flask_sqlalchemy增删改查
# 增 user1 = User(username='zhangsan', email='123456@qq.com', password='123456')
# db.session.add(user1) --> db.session.commit()
# 查
# result = User.query.filter(User.username='zhangsan').first()
# 改
# user2 = User.query.filter(User.username='zhangsan').first()
# user1.username = 'lisi'
# db.session.commit()
# 删
# user1 = User.query.filter(User.username='zhangsan').first()
# db.session.delete(user1)
# db.session.commit()