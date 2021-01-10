from flask import Flask, request, abort, Response, make_response, jsonify
import json

app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'])
def login():
    # json 就是字符串
    data = {
        'age': 18,
        'name': 'zz',
        'school': True
    }
    # return json.dumps(data), 200, {"Content-Type": "application/json"}
    # return jsonify(data)
    return jsonify(city='hh', name='hi')






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
