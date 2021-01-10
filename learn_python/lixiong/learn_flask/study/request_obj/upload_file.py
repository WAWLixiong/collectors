from flask import Flask, request



app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    """
    接收前端传过来的文件对象
    """
    file_obj = request.files.get('pic')
    if file_obj is None:
        return '未上传文件'
    # 将文件保存到本地
    with open('./mm.gif', 'wb') as f:
        data = file_obj.read()
        f.write(data)
    return '上传成功'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
