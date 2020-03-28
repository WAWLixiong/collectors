# 钩子， 别人留下的占位的东西，别人代码执行的时候能够顺带将我的代码执行,
# 钩子，类似于scrapy中的中间件的那个东西

# Flask支持以下四种请求钩子：
# 1. before_first_request
# 2. before_request
# 3. after_request, 报错的话after_request的逻辑不会执行
# 4. teardown_request, 报错的话teardown_request的罗技仍然会被执行


from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    print('first run')
    return 'index page'


@app.before_first_request
def handle_before_first_request():
    print('before_first_request')


@app.before_request
def handle_before_request():
    print('every request')


@app.after_request
def handle_after_request(response):
    print('after request')
    return response


@app.teardown_request
def handle_teardown_request(response):
    """
    debug = False的情况下才能运行
    """
    print('teardown request')
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
