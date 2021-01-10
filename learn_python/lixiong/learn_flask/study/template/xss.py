# coding:utf-8
# 文档中是这么说的： Flask 将会在 templates 文件夹中寻找模版。
# 因此如果你的应用是个模块，这个文件夹在模块的旁边，
# 如果它是一个包，那么这个文件夹在你的包里面:
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/xss', methods=['get', 'post'])
def xss():
    print('hi')
    text = ''
    if request.method == 'POST':
        text = request.form.get('text')

    return render_template('xss.html', text=text)





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
