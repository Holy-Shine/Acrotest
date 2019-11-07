import face_dll
import  face_class as face_class
import face_function as fun
import cv2


Appkey=b'2FzzVsnbAkk9q8eLx2s1Q7tft3dY1NZXdnLN8xK6UtXf'
SDKey=b'DAEJTcePD4TWaWKej3xRpPxBhCWGkFf4nxdYnooLWDuP'

class FaceInfo():
    def __init__(self,Appkey,SDKey):
        self.Appkey = Appkey
        self.SDKey = SDKey

class FaceList():
    def __init__(self,info,img,feature):
        self.info = info
        self.img = img
        self.feature = feature

class FaceRecognition():
    def __init__(self, faceinfo):
        # SDK码
        self.faceinfo = faceinfo
        #确认是否激活成功
        self.activation = self.ConfrimActivation(fun.JH(faceinfo.Appkey, faceinfo.SDKey))
        self.initialface = self.ConfrimActivation(fun.CSH())

    def makeIM(self, img):
        sp = img.shape
        im = face_class.IM()
        im.data = img
        im.width = sp[1]
        im.height = sp[0]
        return im

    #判断图片中是否有人脸
    def isHaveFace(self,img):
        try:
            im = self.makeIM(img)
            #识别人脸
            ret = fun.RLSB2(im)
            if(ret.faceNum>0):
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


    #图片并识别其中最大的人脸
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

    def ConfrimFaceSDK(self,ret):
        if ret[0] == 0:
            print('初始化成功:', ret, '句柄', fun.Handle)
            return True
        else:
            print('初始化失败:', ret)
            return False


    def ConfrimActivation(self,ret):
        if ret == 0 or ret == 90114:
            # print('激活成功:', ret)
            return True
        else:
            # print('激活失败:', ret)
            return False

if __name__ == '__main__':
    fun2 = FaceRecognition(FaceInfo(Appkey=Appkey, SDKey=SDKey))
    img = cv2.imread('3.jpg')
    tz = fun2.getFaceFutrue(img)
    print(tz)