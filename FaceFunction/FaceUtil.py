
import FaceFunction.face_function as fun
import FaceFunction.face_class as face_class

from ctypes import *
from io import BytesIO

import os,cv2,pickle
import base64

Appkey=b'2FzzVsnbAkk9q8eLx2s1Q7tft3dY1NZXdnLN8xK6UtXf'
SDKey=b'DAEJTcePD4TWaWKej3xRpPxBhCWGkFf4nxdYnooLWDuP'



class FaceRecognition():
    def __init__(self, Appkey,SDKey):
        # SDK码
        self.Appkey = Appkey
        self.SDKey = SDKey


    #更换SDK码
    def ModifySDK(self,Appkey,SDKey):
        self.Appkey = Appkey
        self.SDKey = SDKey


    def ActivationFace(self):
        flag1 = self.ConfrimActivation(fun.JH(self.Appkey, self.SDKey))
        ret = fun.CSH()
        if(ret[0]==0 and flag1):
            return True
        else:
            return False

    def ConfrimActivation(self,ret):
        if ret == 0 or ret == 90114:
            # print('激活成功:', ret)
            return True
        else:
            # print('激活失败:', ret)
            return False

    #制作人脸识别的图像字典
    def makeIM(self, img):
        sp = img.shape
        im = face_class.IM()
        im.data = img
        im.width = sp[1]
        im.height = sp[0]
        return im

    #判断图片中是否有人脸
    def IsHaveFace(self,img):
        try:
            im = self.makeIM(img)
            #识别人脸
            ret = fun.RLSB2(im)
            if(ret.faceNum>0 and ret.faceNum<3):
                return True
            else:
                return False
        except Exception:
            print("图片错误")

    def getMaxFace(self, img):
        try:
            im = self.makeIM(img)
            #识别人脸
            ret = fun.RLSB2(im)
            #找到最大脸
            index = fun.getMaxFace(ret)
            return ret,index
        except Exception as e:
            print(e)

    #图片并识别其中最大的人脸，并框出来，返回cv_img
    def showMaxFace(self,img):
        try:
            ret,index = self.getMaxFace(img)
            ra = ret.faceRect[index]
            cv2.rectangle(img, (ra.left1, ra.top1), (ra.right1, ra.bottom1), (255, 0, 0,), 2)
            return img
        except Exception:
            print("图片错误")

    #由路径打开一张图片
    def OpenIMG(self,imgpath):
        try:
            im = face_class.IM()
            im.filepath = '1.jpg'
            im = fun.LoadImg(im)
            return im
        except Exception:
            print("图片错误")


    #提取特征
    def getFaceFutrue(self,image):
        try:
            im = self.makeIM(image)
            ret,index = self.getMaxFace(image)
            ret = fun.RLSB(im)
            ft = fun.getsingleface(ret[1],index)
            tz = fun.RLTZ(im, ft)[1]
            return tz
        except Exception as e:
            print(e)

    #特征比对
    #输入 1,输入图片的特征 2.候选特征和特征码序列
    def getMaxPro(self,currentFeature, FeatueList):
        max = 0
        ret = -1
        for index in range (len(FeatueList)):
            item = FeatueList[index]
            rate = fun.BD(currentFeature, fun.process(item['feature']))
            #比对相似度找最大 且特征阈值大于0.75
            if rate[1]>max and rate[1]>0.75:
                ret = index
                max = rate[1]
        return ret

    def MakeFeature(self,mem_img):
        feature = self.getFaceFutrue(mem_img)
        data = BytesIO(string_at(feature.feature, feature.featureSize)).getvalue()
        data = base64.b64encode(data).decode()
        return data

    def getFeature(self,input):
        return base64.b64decode(input)

    def BiDui(self,tz1,tz2):
        rate = fun.BD(fun.process(tz1), fun.process(tz2))
        return rate


if __name__ == '__main__':
    fun2 = FaceRecognition(Appkey=Appkey, SDKey=SDKey)
    flag = fun2.ActivationFace()
    if(flag):
        img = cv2.imread('3.jpg')
        tz = fun2.MakeFeature(img)
        print(tz)
        print(fun2.getFeature(tz))
    else:
        print("人脸识别激活失败")
