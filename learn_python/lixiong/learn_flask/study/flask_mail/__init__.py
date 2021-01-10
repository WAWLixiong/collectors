#!/usr/bin/env python3
# coding:utf-8


from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config.update(
    DEBUG=True,
    MAIL_SERVER='',
    MAIL_PORT='',
    MAIL_USE_TLS='',
    MAIL_USERNAME='',
    MAIL_PASSWORD='',
)

mail = Mail()
# message = Message('content', )


# 发送邮件 mail.send()