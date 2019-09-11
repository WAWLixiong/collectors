from flask import Flask, current_app, redirect, url_for
from werkzeug.routing import BaseConverter

# 创建flask应用对象
# __name__ 当前的模块名字
# flask 以这个模块所在的目录为根目录，static为静态目录，templates为模板目录
app = Flask(__name__,
            static_url_path='/python', # 访问静态资源的url前缀，默认值是static
            static_folder = 'static', # 这个是静态文件的目录，默认是static
            template_folder= 'templates' # 模板文件目录，默认是templates
            )

# 如何判断是静态网址，还是视图  通过static_url_path, /static/index.html, 在请求的时候将/static去掉，然后在静态文件中
# 找index.html，静态文件在static_folder参数下边找


# learn 配置参数的使用方式
# 1.配置文件的使用
# app.config.from_pyfile('config.cfg')

# 2.通过配置对象
class Config:
    DEBUG = True
    DEV = 'TEST'
app.config.from_object(Config)

# 3.操作app.config
# app.config.update({'DEBUG':True})
# app.config['DEBUG'] = True


@app.route('/')
def index():
    """
    定义的视图函数
    """
    # learn 读取配置文件
    # 1.通过app
    dev = app.config.get('DEV')
    print(dev)

    # 2.通过current_app获取参数
    dev = current_app.config.get('DEV')
    print(dev)
    return 'hello world'


# learn 设置post请求方式
@app.route('/post_only', methods=['GET', 'POST'])
def post_only():
    return 'post only page'


# learn 相同的视图函数(路径，请求方式)，根据url_map顺序访问路由
@app.route('/hello')
def hello():
    return 'hello'


@app.route('/hello')
def hello2():
    return 'hello2'


# learn 不同的路由对应同一个视图函数
@app.route('/hi1')
@app.route('/hi2')
def hi():
    return 'hi'


# learn 跳转
@app.route('/login')
def login():
    # url = '/'
    # 视图函数的名字, django中 urls = [(r'/index', index, name = 'index_view')]
    url = url_for('index')
    return redirect(url)


# learn 路由提取参数
# 转换器，e.g. <int:good_id>
# int, float, path
# @app.route('/goods/<int:good_id>')
@app.route('/goods/<good_id>') #不加转换器类型，默认是普通字符串规则，除了/的字符
def goods_detail(good_id):
    return 'goods detail page: {}'.format(good_id)


# learn 自定义转换器
# 1.定义转换器类
class RegexConverter(BaseConverter):
    """"""
    def __init__(self, url_map, regex):
        # 调用父类的构造方法
        super().__init__(url_map)
        # 将正则表达式的参数，保存到对象属性中, flask会去使用这个属性进行路由的正则匹配
        self.regex = regex

    def to_python(self, value):
        print('正则提取到的值，首先经过 to_python 函数处理')
        return int(value)

    def to_url(self, value):
        """使用url_for的方法的时候被调用"""
        return '17601241441'
        # return value

# 2.将自定义的转换器，添加到flask应用中
app.url_map.converters['re'] = RegexConverter # converters保存转换器

# 3.使用转化器
@app.route("/send/<re(r'1[3456789]\d{9}'):phone>")
def send_message(phone):
    return 'send message to {} successful'.format(phone)

# 定义一个单一的转换器
class PhoneConverter(BaseConverter):
    regex = r'1[3456789]\d{9}'

app.url_map.converters['phone'] = PhoneConverter
@app.route("/send/<phone:phone>")
def send_info(phone):
    return 'send info to {}'.format(phone)

# to_url实现的作用
@app.route('/ooo')
def ooo():
    url = url_for('send_message', phone='13643546246')
    print(url)
    # /hello/17601241441
    return redirect(url)



if __name__ == '__main__':
    # 通过url_map 查看flask中的路由信息
    # print(app.url_map)
    #开启测试服务器
    # app.run(host='192.168.199.163')
    app.run(host='0.0.0.0', port=5000, debug=True)
