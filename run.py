from flask import Flask, request, render_template, jsonify
import main.judge_ques as Jg
import main.judge_image as Img
import main.utils as Utils
import main.mock as Mock
import os,json
import main.db as db 
from main.WXBizDataCrypt import WXBizDataCrypt
from config.conf import Remote

app = Flask(__name__)

'''
@project: 官网
@author: Laurel
'''
@app.route('/')
def admin():
    return render_template('admin.html')
#整体测试路由
@app.route('/mini/test')
def test():
    d = db.DB()
    r = d.already_in('sfdasdf', '13333333333')
    if r is None:
        return "None"
    else:
        return r['phone']
    return ('sfdsdf', '13333333333')
#重定向到图像识别测试模块
@app.route('/mini/recognition/front')
def recognition_front():
    return render_template('drugcheck.html')
#图像识别测试模块
@app.route('/mini/recognition/test', methods=['GET', 'POST'])
def recognition_test():
    return Mock.recognition_test(request, render_template)


'''
@project: questionnaire
@author: Laurel
@updated_at: 20200322
'''
#调查问卷
@app.route('/mini/questionnaire')
def questionnaire():
    args = request.args.get('paper')
    return Jg.judge(args)

'''
@project: drug check image recognition
@author: Laurel
@updated_at: -
'''
#图像识别
@app.route('/mini/recognition', methods=['GET', 'POST'])
def recognition():  
    openid = request.form.get('openid')
    image = request.files.get('file')
    path_list = Utils.saveImage(image, openid)
    return Img.judgeimage(path_list[0], path_list[1])

#上传个人信息
@app.route('/mini/recognition/information', methods=['POST'])
def recognitionInformation():
    import requests, urllib
    app.config.from_object(Remote)
    params = json.loads(request.get_data(as_text=True))
    information = params['information']
    try:
        requests.post(url = app.config['RECORD_INFO'], data = information)
    except Exception as e:
        return jsonify({'responseCode': 500})
    return jsonify({'responseCode': 200})

'''
    public
'''
#登陆获取openid和sessionKey
@app.route('/mini/loginstatus')
def login_status():
    r, openid, sessionkey = Utils.fetchOpenIdAndSession(request)
    registed = Utils.is_registed(openid)
    if registed is None:
        return json.dumps({'status': 'unregisted', 'openid':openid, 'session_key':sessionkey})
    else:
        return r 

#小程序注册
@app.route('/mini/regist', methods=['GET', 'POST'])
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
    

if __name__ == '__main__':
    # 服务器配置
    app.run(host="0.0.0.0", port=3000, debug=True, threaded=True)