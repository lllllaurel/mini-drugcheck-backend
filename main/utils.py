import os,json
import requests as sender
import main.db as db

#返回openid 
def fetchOpenIdAndSession(request):
    #GET https://api.weixin.qq.com/sns/jscode2session?appid=APPID&secret=SECRET&js_code=JSCODE&grant_type=authorization_code
    api = 'https://api.weixin.qq.com/sns/jscode2session'
    args = {}
    args['appid'] = request.args.get('appid')
    args['secret'] = request.args.get('secret')
    args['js_code'] = request.args.get('js_code')
    args['grant_type'] = 'authorization_code'
    response = sender.get(url=api, params=args)
    r = response.json()
    return response.json(), r['openid'], r['session_key']

#返回根目录
def rootPath():
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

#保存用户上传图片
def saveImage(img, openid):
    suffix = ('.jpg', '.png')
    save_path = os.path.join(rootPath(), 'static', 'upload', openid+'_before'+suffix[0])
    output_path = os.path.join(rootPath(), 'static', 'upload', openid+'_after'+suffix[0])
    if os.path.exists(save_path):
        os.remove(save_path)
    img.save(save_path)
    return save_path, output_path

#判断是否注册
def is_registed(openid):
    database = db.DB()
    result = database.is_registed(openid)
    return result if result is not None else None

def regist(openid, phone):
    database = db.DB()
    return database.regist(openid, phone)


#判断是否登陆
def is_logged(openid):
    return False