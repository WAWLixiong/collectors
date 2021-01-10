# coding:utf-8

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
def index():
    # return render_template('index.html', name='python', age=18)
    data = {
        'name': 'python',
        'age': 18,
        'my_dict': {'city': 'beijing'},
        'my_list': [1, 2, 3, ],
        'my_int': 0,

    }
    return render_template('index.html', **data)

# learn 自定义过滤器的2种方式
# 1
def list_step_2(li):
    return li[::2]

#注册过滤器
app.add_template_filter(list_step_2, 'li2')

# 2
@app.template_filter("li3")
def list_step_3(li):
    return li[::3]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
