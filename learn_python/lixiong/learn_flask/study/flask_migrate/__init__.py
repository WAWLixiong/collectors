#!/usr/bin/env python3
# coding:utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager


app = Flask(__name__)


class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Qazwsx@123@192.168.199.163:3306/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True

app.config.from_object(Config)

manager = Manager(app)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


class Roles(db.Model):
    """角色表"""
    __tablename__ = 'fl_roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    users = db.relationship("User", backref='roles') # 从模型类考虑


# 创建数据库模型类
class User(db.Model):
    """用户表"""
    __tablename__ = 'fl_user'

    id = db.Column(db.Integer, primary_key=True) # caution 整形的主键会默认设置为自增主键
    name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    age = db.Column(db.Integer)
    email = db.Column(db.String(50), unique=True)

    # 角色外键
    role_id = db.Column(db.Integer, db.ForeignKey('fl_roles.id')) # 从表考虑

    def __repr__(self):
        """
        定义之后 对象打印更直观
        """
        return "User object: name={},age={},email={}".format(self.name, self.age, self.email)


if __name__ == '__main__':
    manager.run()

    # python __init__.py db init #caution
    # python __init__.py db migrate -m '初次创建' #caution 生成迁移文件,
    # python __init__.py db upgrade #caution 升级
    # python __init__.py db history # caution 查看历史
    # python __init__.py db downgrade `version` #caution 降级


