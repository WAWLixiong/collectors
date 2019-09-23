# 会话机制，存放状态信息


from flask import Flask, make_response, request, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dafdafafdasdfas'

# flask 是将session保存到cookie中，通过secret_key加密
@app.route('/login', methods=['GET'])
def login():
    # 设置session数据
    session['name'] = 'zzlion'
    session['age'] = 18
    return  'login success'

@app.route('/req')
def req():
    name = session.get('name')
    age = session.get('age')
    return f'{name} {age}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
