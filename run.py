from flask import Flask, request, render_template
import main.judge_ques as Jg
import main.judge_image as Img
import main.utils as Utils
import main.mock as Mock
import os

app = Flask(__name__)

#index
@app.route('/')
def admin():
    return render_template('admin.html')

#drugcheck 路由
#调查问卷
@app.route('/mini/questionnaire')
def questionnaire():
    args = request.args.get('paper')
    return Jg.judge(args)
#图像识别
@app.route('/mini/recognition', methods=['GET', 'POST'])
def recognition():  
    openid = Utils.fetchOpenId()
    image = request.files.get('file')
    path_list = Utils.saveImage(image, openid)
    return Img.judgeimage(path_list[0], path_list[1])
#图像识别测试模块
@app.route('/mini/recognition/test')
def recognition_test():
    return Mock.recognition_test(request)
#整体测试路由
@app.route('/mini/test')
def test():
    return render_template('test.html')


if __name__ == '__main__':
    # 服务器配置
    app.run(host="0.0.0.0", port=3000, debug=True, threaded=True)