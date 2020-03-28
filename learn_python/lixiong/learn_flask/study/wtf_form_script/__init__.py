# coding:utf-8

# flask-wtf
# 动态生成表单的HTML代码和验证提交的表单数据，
# 并且提供跨站请求伪造（Cross-Site Request Forgery）保护的功能

from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


app = Flask(__name__)
app.config['SECRET_KEY'] = 'fdafdasgasf'


# 定义表单的模型类
class RegisterForm(FlaskForm):
    """
    定义注册表单模型类
    """
    # label,
    user_name = StringField(label='用户名', validators=[DataRequired(message='用户名不能为空')])
    password = PasswordField(label='密码', validators=[DataRequired(message='密码不能为空')])
    password2 = PasswordField(label='确认密码',
                              validators=[DataRequired(message='确认密码不能为空'), EqualTo('password', message='密码不同')])
    submit = SubmitField(label='提交')



@app.route('/register', methods=['post', 'get'])
def register():
    # 创建表单对象，如果是post请求，前端发送了数据，flask会把数据在构造form对象的时候，
    # 存放到对象中
    form = RegisterForm()
    if form.validate_on_submit():
        # 表示验证合格
        # 提取数据
        user_name = form.user_name.data
        password = form.password.data
        password2 = form.password2.data
        print(user_name)
        print(password)
        print(password2)
        session['user_name'] = user_name
        session['password'] = password
        return redirect(url_for('index'))
    return  render_template('register.html', form=form)


@app.route('/index')
def index():
    user_name = session.get('user_name')
    return 'register user_name:{}'.format(user_name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
