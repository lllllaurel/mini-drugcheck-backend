import numpy as np
# import cv2
import os, sys 
import main.utils as Utils

ROOT_DIR = Utils.rootPath()

def judgeimage(image,image_output):
    #image 待处理图片文件名， image_output 处理后文件名
    save_image = os.path.join(ROOT_DIR, 'static', 'upload', image_output)
    #设定颜色HSV范围，假定为红色
    redLower = np.array([156, 43, 46])
    redUpper = np.array([179, 255, 255])

    #读取图像
    img = cv2.imread(image)

    #将图像转化为HSV格式
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #去除颜色范围外的其余颜色
    mask = cv2.inRange(hsv, redLower, redUpper)

    # 二值化操作
    ret, binary = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY)

    #膨胀操作，因为是对线条进行提取定位，所以腐蚀可能会造成更大间隔的断点，将线条切断，因此仅做膨胀操作
    kernel = np.ones((5, 5), np.uint8)
    dilation = cv2.dilate(binary, kernel, iterations=1)

    #获取图像轮廓坐标，其中contours为坐标值，此处只检测外形轮廓
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    string_return = ""
    if len(contours) > 0:
        #cv2.boundingRect()返回轮廓矩阵的坐标值，四个值为x, y, w, h， 其中x, y为左上角坐标，w,h为矩阵的宽和高
        boxes = [cv2.boundingRect(c) for c in contours]
        #print(boxes)
        for box in boxes:
            x, y, w, h = box
            #绘制矩形框对轮廓进行定位
            origin_pic = cv2.rectangle(img, (x, y), (x+w, y+h), (153, 153, 0), 2)
        #保存标记后的图片并且返回判断结果
        cv2.imwrite(save_image, origin_pic)
        if len(boxes) == 1:
            string_return = "吸毒"
        if len(boxes) == 2:
            string_return = "未吸毒"
        if len(boxes)>= 3 or len(boxes)<1:
            string_return = "样本质量不佳，重新采样"
    return string_return

if __name__ == '__main__':
    # main(sys.argv)
    private_key = 'jujiao_test'
    image = 'jujiao_before.jpg'