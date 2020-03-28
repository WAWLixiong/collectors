# request session都是请求上下文, 即虽然request是全局变量， 但是不同的人的调用request得到不同request对象
# current_app 和 g 都是应用上下文
# 线程局部变量, request = {'th1':[],'th2':[]}

# learn g对象，每次请求进来的app的时候都会被清空
from flask import current_app, g

from flask import Flask, make_response, request, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dafdafafdasdfas'

# flask 是将session保存到cookie中，通过secret_key加密
@app.route('/login', methods=['GET'])
def login():
    # 设置session数据
    session['name'] = 'zzlion'
    session['age'] = 18
    g.name = 'zzlion'
    return  'login success'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
