#!/usr/bin/env python3
# coding:utf-8

from flask import Flask, flash, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fdagdadasfdas'

flag = True


@app.route('/index')
def index():
    global flag

    if flag == True:
        flash('welcome')
        flash('see you again')
        flash('nice to meet you')
        flag = False
    return  render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
