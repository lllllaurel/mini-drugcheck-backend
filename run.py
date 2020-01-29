from flask import Flask, request, render_template
import main.judge_ques as Jg
import main.judge_image as Img
import main.utils as Utils
import main.mock as Mock
import os,json
import main.db as db 
from main.WXBizDataCrypt import WXBizDataCrypt

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
    openid = request.form.get('openid')
    image = request.files.get('file')
    path_list = Utils.saveImage(image, openid)
    return Img.judgeimage(path_list[0], path_list[1])

#重定向到图像识别测试模块
@app.route('/mini/recognition/front')
def recognition_front():
    return render_template('drugcheck.html')

#登陆获取openid和sessionKey
@app.route('/mini/loginstatus')
def login_status():
    r, openid, sessionkey = Utils.fetchOpenIdAndSession(request)
    registed = Utils.is_registed(openid)
    if registed is None:
        return json.dumps({'status': 'unregisted', 'openid':openid, 'session_key':sessionkey})
    else:
        return r 

#drug小程序注册
@app.route('/mini/drug/regist', methods=['GET', 'POST'])
def drug_regist():
    params = json.loads(request.get_data(as_text=True))
    appid = params['appid']
    iv = params['iv']
    session_key = params['session_key']
    en_data = params['encryptedData']
    openid = params['openid']
    pc = WXBizDataCrypt(appid, session_key)
    un_data = pc.decrypt(en_data, iv)
    return Utils.regist(openid, un_data['phoneNumber'])
    

#图像识别测试模块
@app.route('/mini/recognition/test', methods=['GET', 'POST'])
def recognition_test():
    return Mock.recognition_test(request, render_template)

#整体测试路由
@app.route('/mini/test')
def test():
    return Utils.regist('sfdsdf', '13333333333')


if __name__ == '__main__':
    # 服务器配置
    app.run(host="0.0.0.0", port=3000, debug=True, threaded=True)