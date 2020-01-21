import os

#返回openid 
def fetchOpenId():
    return 'test_open_id'

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