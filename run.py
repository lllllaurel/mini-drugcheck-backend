from flask import Flask, request, render_template
import main.judge_ques as Jg
import main.judge_image as Img
import main.utils as Utils
import os

app = Flask(__name__)

@app.route('/')
def helloworld():
    return 'welcome to drug check 小程序'

@app.route('/mini/questionnaire')
def questionnaire():
    args = request.args.get('paper')
    return Jg.judge(args)

@app.route('/mini/recognition', methods=['GET', 'POST'])
def recognition():  
    openid = Utils.fetchOpenId()
    image = request.files.get('file')
    path_list = Utils.saveImage(image, openid)
    return path_list[1]
    # return Img.judgeimage(path_list[0], path_list[1])

@app.route('/mini/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    # 服务器配置
    app.run(host="0.0.0.0", port=3000, debug=True, threaded=True)

    # local配置
    # app.run(debug=True)