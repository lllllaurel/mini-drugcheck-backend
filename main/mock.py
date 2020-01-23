import main.judge_ques as Jg
import main.judge_image as Img
import main.utils as Utils


def recognition_test(request):
    openid = 'test'
    image = request.files.get('file')
    path_list = Utils.saveImage(image, openid)
    Img.judgeimage(path_list[0], path_list[1])