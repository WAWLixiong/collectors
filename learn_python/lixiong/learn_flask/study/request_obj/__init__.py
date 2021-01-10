from flask import Flask, request

app = Flask(__name__)

# 接口 api
# 0.0.0.0:5000/index?city=beijing 查询字符串QueryString
@app.route('/index', methods=['GET','POST'])
def index():
    # request中包含了从前端发送回来的所有数据
    # 通过request.form可以提取请求体中的表单格式的数据，是一个字典类型的对象
    # form只能拿到多个同名参数的第一个
    name = request.form.get('name')
    age = request.form.get('age')
    city = request.args.get('city')
    name_li = request.args.getlist('name')
    city_li = request.form.getlist('city')

    return 'hello name=%s age=%s city=%s names=%s citys=%s' % (name, age, city, name_li, city_li)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
