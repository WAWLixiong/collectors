from flask import Flask, request, abort, Response

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    name = request.form.get('name')
    pwd = request.form.get('password')
    if name != 'zzlion' or pwd != 'admin':
        # 使用abort函数可以立即终止视图函数的执行，并返回特定信息给前端
        # 1 传递状态码信息，必须是标准的http状态码
        abort(404)
        # 2 返回相应对象, Response
        # abort(Response('login failed'))
    else:
        return 'login failed'

@app.errorhandler(404)
def handle_404_error(err):
    """自定义处理404错误"""
    print(err)
    return 'hi  404 happened'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
