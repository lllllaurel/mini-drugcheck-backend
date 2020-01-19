from flask import Flask, request
import main.judge_ques as Jg
import os

app = Flask(__name__)

@app.route('/')
def helloworld():
    return 'kj hello flask'

@app.route('/mini/judge')
def judge():
    args = request.args.get('paper')
    return Jg.judge(args)

@app.route('/test')
def test():
    return os.path.join(__file__,'static')

if __name__ == '__main__':
    # 服务器配置
    app.run(host="0.0.0.0", port=3000, debug=True, threaded=True)

    # local配置
    app.run(debug=True)