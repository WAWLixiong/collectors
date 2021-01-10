#!/usr/bin/env python3
# coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from sqlalchemy import func

app = Flask(__name__)


class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Qazwsx@123@192.168.199.163:3306/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True


app.config.from_object(Config)

# 创建数据库操作对象
db = SQLAlchemy(app)

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


# @app.route('/index')
# def index():
#     return 'hello world'


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000)
    # # 清楚数据库里边所有数据
    # db.drop_all()
    #
    # # 创建所有表
    # db.create_all()
    #
    # # 添加数据
    # role1 = Roles(name='admin')
    # db.session.add(role1)
    # role2 = Roles(name='stuff')
    # db.session.add(role2)
    # db.session.commit()
    #
    # user1 = User(name='zzlion', email='1@1', age=1, role_id=role1.id)
    # user2 = User(name='xiong', email='2@2', age=2, role_id=role2.id)
    # user3 = User(name='li', email='3@3', age=3, role_id=role1.id)
    # user4 = User(name='xx', email='4@4', age=4, role_id=role2.id)
    #
    # data_li = [ user1, user2, user3, user4 ]
    # db.session.add_all(data_li)
    # db.session.commit()

    # 查询操作

    # 查询所有
    # roles = Roles.query.all()
    # roles = db.session(Roles).all() 结果相同, caution 这个是sqlalchemy 原始的查询方式
    # print(roles)
    # print(roles[0].name)

    # 查询第一条
    # role = Roles.query.first()
    # print(role)
    # print(role.name)

    # 通过主键查询
    # role = Roles.query.get(2)
    # print(role)
    # print(role.name)

    # learn 查询前过滤
    # user = User.query.filter_by(name='zzlion').all()
    # print(user[0].name)
    # user = User.query.filter_by(name='zzlion', role_id=1).first()
    # print(user.name)

    # user = User.query.filter(or_(User.name=='zzlion', User.role_id==2)).all()
    # print(user)

    # caution order_by需要在limit ,offset之前调用
    # user = User.query.filter(or_(User.name=='zzlion', User.role_id==2)).order_by().offset(1).limit(10).all()
    # print(user)
    # user = User.query.order_by(User.id.desc()).all() #升序 .asc
    # print(user)

    # caution group_by之后返回的不再是User，或Roles对象了
    # ret = db.session.query(User.role_id, func.count(User.role_id)).group_by(User.role_id).all()
    # print(ret)

    # learn 关系查询
    # ro = Roles.query.get(1)
    # users = ro.users
    # print(users)

    # caution user.roles
    # user = User.query.get(1)
    # # print(user.name)
    # roles = user.roles
    # print(roles)

    # learn 修改 删除

    # 更新
    # user = User.query.get(1)
    # print(user.name)
    # user.name = 'xiaoxiong'
    # db.session.add(user)
    # db.session.commit()

    # 查询时更新
    # ret = User.query.filter_by(name='xiaoxiong').update({'name': 'zzlion'})
    # db.session.commit()

    # 删除
    user = User.query.get(3)
    db.session.delete(user)
    db.session.commit()

