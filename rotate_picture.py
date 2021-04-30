# 旋转图片，无损失
import cv2
from math import *
def rotate(img_file_path,save_file_path,degree):
    """
    无损失的选择图片，使用pil的旋转会产生黑边
    :param img_file_path: 图片路径
    :param save_file_path: 图片保存路径
    :param degree:旋转角度
    :return:
    """
    img = cv2.imread(img_file_path)

    height,width=img.shape[:2]

    #旋转后的尺寸
    heightNew=int(width*fabs(sin(radians(degree)))+height*fabs(cos(radians(degree))))
    widthNew=int(height*fabs(sin(radians(degree)))+width*fabs(cos(radians(degree))))

    matRotation=cv2.getRotationMatrix2D((width/2,height/2),degree,1)

    matRotation[0,2] +=(widthNew-width)/2  #重点在这步
    matRotation[1,2] +=(heightNew-height)/2  #重点在这步

    imgRotation=cv2.warpAffine(img,matRotation,(widthNew,heightNew),borderValue=(255,255,255))


    cv2.imwrite(f"{save_file_path}", imgRotation)
