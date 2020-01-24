import main.judge_ques as Jg
import main.judge_image as Img
import main.utils as Utils


def recognition_test(request, render_template):
    openid = 'test'
    image = request.files.get('file')
    path_list = Utils.saveImage(image, openid)
    Img.judgeimage(path_list[0], path_list[1])
    origin_path = '/static/upload/'+path_list[0].split('/')[-1]
    after_path = '/static/upload/'+path_list[1].split('/')[-1]
    return render_template('drugcheck.html', origin=origin_path, after=after_path)