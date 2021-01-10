#!/usr/bin/env python3
# coding:utf-8


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

class Config:
    SQLALCHEMY_DSATABASE_URI = 'mysql://root:"Qazwsx@123"@192.168.199.163:3306/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True

app.config.from_object(Config)

# 创建数据库操作对象
db = SQLAlchemy(app)



# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:"Qazwsx@123"@192.168.199.163:3306/flask'
#
# # 设置每次请求后自动提交数据库的改动,
# # caution 官方现在不推荐
# # app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
#
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# # 查询时 显示完整的语句
# app.config['SQLALCHEMY_ECHO'] = True

@app.route('/index')
def index():
    return 'hello world'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



