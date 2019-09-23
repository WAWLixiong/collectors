from flask import Flask, request, abort, Response, make_response

app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'])
def login():
    # 1 使用元组返回自定义的相应信息
    #
    # return 'login failed', 666, [('city','beijing'),('content_type','text')]
    # return 'login failed', 666, {'city': 'beijing', 'content_type': 'text'}
    # return 'login failed', '666 diy status', {'city': 'beijing', 'content_type': 'text'}
    # return 'login failed', 666

    # 2 make_response 构造响应信息
    resp = make_response('index page 2')
    resp.status = '999 diy status'
    resp.headers = {'city': 'shanghai', 'name': 'china'}
    return resp




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
