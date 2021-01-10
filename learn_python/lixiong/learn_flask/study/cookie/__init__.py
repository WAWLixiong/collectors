from flask import Flask, make_response, request

app = Flask(__name__)


@app.route('/index', methods=['GET'])
def set_cookie():
    resp = make_response('hello world')
    # resp.status = '200'
    # 设置cookie，默认有效期是临时cookie，浏览器关闭cookie失效
    resp.set_cookie('name', 'zzlion')
    resp.set_cookie('age', '19', max_age=3600)  # 单位是s
    resp.headers['Set-Cookie'] = 'home=lingshi; Expires=Thu, 19-Sep-2019 15:32:33 GMT; Max-Age=3600; Path=/'
    return resp


@app.route('/get_cookie')
def get_cookie():
    name = request.cookies.get('name')
    age = request.cookies.get('age')

    return f'{name}, {age}'

@app.route('/delete_cookie')
def delete_cookie():
     resp = make_response('del successful')
     resp.delete_cookie('name')
     return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
