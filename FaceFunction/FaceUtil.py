from ctypes import string_at

import FaceFunction.face_function as fun
import FaceFunction.face_class as face_class

from io import BytesIO

import os,cv2,pickle
import base64




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
            rate = fun.BD(currentFeature, item['feature'])
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
        rate = fun.BD(tz1, tz2)
        return rate

    def mutifacerecon(self,facelist,img):
        try:
            currentFeature = self.getFaceFutrue(img)
            max = 0
            ret = -1
            for index in range(len(facelist)):
                rate = self.BiDui(currentFeature, fun.process(facelist[index]['mem_facefeature']))
                # 比对相似度找最大 且特征阈值大于0.8
                if rate[1] > max and rate[1] > 0.8:
                    ret = index
                    max = rate[1]
            if(ret == -1):
                return None
            else:
                return [facelist[ret]['name'],facelist[ret]['phone']]
        except  Exception as e:
            print(e)


if __name__ == '__main__':
    # print(1)
    data = [
        {'phone': '12312312312',
         'mem_facefeature': b'\x00\x00\xfaD\x00\x00tC\x0c~\x91=\xf7\xac\xe4=\x8c\xd9\xff<\x83[}\xbd?m\xd0\xbdd\xbd\xc1\xbdy\x8eR=M\xc3\x9a=\x8a\xd9\x8a\xbb\x14\x9f\x98\xbc\xf4\xcbe\xbdk\n\x04\xbd\x0f\xed\xe3\xbdJ\xfc\xc5<tti\xbc\x1au\x88\xbd\xe8B\xb2<E-\x85=\x8dX?;\xa2\x8c\xa9\xbc\xdc\x8b\xc1=\x83\x99\xbf\xbby\xd6M\xbd)\x820\xbd8b\x80=\x00\xe4\x12=\xbdr\xa7=\x91\x90\x05=>\xdeX=1Y\xde=\x1a\xb8]\xbd\x91\x86\x9d\xbb\xc3M\x82=\x89\xab[=\xdei\x88\xbcc\xd4\x95<\x05\xc8$<^l\x91:B[\t\xbd\xbd\xcc\x94\xbc<\xae\xd6\xbd.a\xbb<\xd6\xab\xce=\x8f\xc5w\xbc\x02\x95\xa5=\xce\x0b9\xbc\xf4\xa9U=\xec\xfc\xa4\xbd\x8f\xf1\xe4\xbd\xcd\xb3n\xbc\xc8CM<y\xa3q\xbda\x08\x93=/\x17\x82=\xefEL\xbd]\x0f\xb6<\xba\xec1=[d\x1a\xbdn*r\xbd\xd9\xa8]\xbc\x10AS=\x8f\xdd\xc5=\x8b\xb4\xd1\xbd\xac\x953=\xeb^U\xbd\xfe\x94*\xbcWN\x05<\xce\xc8\xc3<\x08BT\xbd\t0h=\xf8\x9f\x8e<\x00+\x13=kF\x118\xfb5\xfc<\xc1}\x9b\xbc\x8aV#\xbd\xd4\x7f\xa9\xbd\x10\xb3L\xbclU\x88<$\x19\xee<\xab\xaf\xd5=\xfdK%=\x05\xd2\x02\xbd\xe3\xab\x99=e\x8b\xcd\xbb\xd54\xfc6\xb2Ta=\xce\x1a\xed=\xc8]g=i\xb8\xcd<\x1a\x93\x94=6fE=\x05\xba\x86\xbd\xb4\xbf!\xbd?\x9d\x13=\xe6\x1ew\xbb6\x06J\xbb1\x9a\x04<p\xe6\xaa\xbdNa\xd9\xbct\x0e\xc7\xbc_\xd1\x0e\xbc.\xf2~\xbd\xc9\xae\xa3\xbdl\x05\xf0=\x84\x0f\xf4<\x14\xdc\x91\xb8\x8d\xd5=\xbd\xb6P\x8c\xba\x1cg\x00\xbc\xc4[9\xba\x1c\xd4\xd3\xbc\x0eQ\xa0\xbcI6"\xbb;\xb2K\xbd\x85 \x11>g&\x83=\xba\x8cz\xbd\x07K\xe9<\xc7\xdc\xc3;G\xe6\x97<\xab=P<\xa9F0\xbdr\x96\xa9\xb9\xfe?\xb4;\x96r\x0e>\xc8\xe4C=}(\x17>=q\x02\xbd\t\x190=\x15\xe1J\xbc\xfb\x08\xd4\xbd\x18x\t=\x9ay\xfe<\xd2\xf1\xda<\xd97:=:\xfe\x92<\x964A<\xda\x14\xca\xbb\xb2;\xb2\xbd\xba\xea\xa6\xbc\x90\xaf5\xbd\'\x8e\x80\xbdl"2\xbc\xc9`D\xbd\xb1\xc5\xef;\xb8\x08\x99\xbdSR\x9f\xbdF\x91\x03=$\xb4q\xbd\xeb\xf0\xde<\xe7\x8d\x0e\xbey\x0cS\xbd\x1af\x8d\xbd\xee\xbc\x85\xbd\x04(\xc2\xbc?\x1b\x14\xbe\xbe\x00\xd5<\x1a2\xf8\xbc\xf1\tY\xbd\r\xcf*\xbd\xd9\xab\xff;\xe5\'\x85<\x0f\xb6\xc8\xbc\xdc\xbf)=j\n&\xbe\x14\xcc\x99\xbc\xaav\x16>\x83bN\xbd\x96\xae\x93<\x19\xce\xa6\xbd\x1d\xec\xa1\xbc\xe9\x04\xaa\xbd\r~ \xbd\xddV%\xbd.\xbc\xc9;M\'\x15=\xdd\x04}\xbdy.O=d\x17\xa5\xbc\xa3G\x92=\x19\x80y<\xcf\xd5i;\xb2"\xe5<\x0c\x90\x1f\xbb2=\xe9<\x9d\xe2\x1f>5\xf7\xc6=\xecP\xbd=q\x11\x05\xbd\x05\x10\xa0=\xec\xaf\x1c\xbd^*\xb4\xbc\xa1\xf7\xa7=\x96\xfad=rx$\xbe\xf2g\xd1\xbd\xb9\x13\xe9;\xe1\xbbc\xbc\xea\x01H=\x8d\xcc\x9a\xbd\xaa\x8e\x8d;\xa4w@\xbd\xcf\xd8\xbc\xbd*@\x82\xbd\x85\x8b\xa1<*\xee\xe4\xbdI\'\xdf\xbd\x14\x12\x89\xbc\x0c\xe0\x15<\xf0\xb7:\xbch`\x9a=F\xfc\x8e\xbd.\x9d\xad<\xcb\xb2\x85;NQ\xc8=\xa2\x1a@<\x1ex\x06\xbc\xb0\xce\x91\xbdwf?=g\x1c\x80=\xbf\x15\xc3=\x85\x91\xc0\xbdZ\xbcL\xbcF\x02!=Zm+\xbd\x1f\xb4\xb7<\x82\x18\t\xbe\xfbn\xbb;[\x06\xe1=K\x95J\xbd\xd2`\xbb=\x0e\xdc\x14\xbe6\xd2\xfd=\xff\xe4\xd7=O\x1b\x0f<B\xe3\xe5\xbb\x83\xf8\xd2\xbcFWz=\xd2\xcd\xb7\xbd\x807\xa2<\x0cY\xb9=$\xfd\xa4\xbd\xc9@\xfe\xbbZ\x8d\xb2\xbc\x13\xa7\x84=\xa6l\xb9=\xe8P\xdb=\xd9ZJ\xbdo\xaf]=s%\xde=\r\x05g\xbd\xb54M=\x82\xad\xbd\xbc\xbdR\xf5\xbd\x8b\x1c\xce=',
         'name': '裴正蒙'},
        {'phone': '12312312312',
         'mem_facefeature': b'\x00\x00\xfaD\x00\x00tC<\xdf\x1a\xbd\xa6`\x8e\xbbe\xce\xad=\xc8\x1f\xf7\xba\x15\xb6\xa7\xbdK\xa8D<6hN<\xb3\xae\xe9<\x84\x14\x89\xbd4\xd2\x0e\xbe\xe8{\x91\xbd\x80W<\xbd\x8aT\xc0\xbd\x1dn@=\xc39\x80\xbd\x90\xe6\x06\xbd\x16r\xc6\xbd\x1b\xf4\x10=\x1d\xf6V\xbb\x96,\xbc\xbd\xd0;:\xbc\xad\xe6=\xbdU\x1b\x83\xbcZJ"\xbb\xc0\x93\xae=]\xa3\x11=\xd7\xe6\xc3\xbc\x07\xa2\xa2=[\x1a\x83=\xdd\xeeH<q\xcf\xf4\xbc)\x94n=\x89\xce\x17=\xca\xa0\x95=\xe0\xb6\xa2\xbdb\xfa\x96\xbd\xaeJ\xd1\xbc\xd2\xb6\x1c>$\x84\x0e\xbcO\x9e\xfc\xbc\x9f\x1d\x05\xbd\x83\x8c\xc5\xbd\xed\xdek\xbd-hA\xbd\x17\x10`\xbdk\r\x8f\xbd\x9f\x1e\xab=\xca\xca\x99:\xa1\x9fj\xbd]l\x959 \xf9\xc3=li\x93=q\r!>c\\+\xbcS\x95\x8e;Y\x1dJ\xbc\x9a\xcd\x8b\xbd\x0e\x7f\x1d\xbd\xb1\xd3\xc0\xbc\xec\xb0z=\xe9\x82\xb0=&\x98\x82<K\xb3\x80=}\x800\xbcp\x11\xa6<\xdf\x1c~=\xabL\x16\xbd\xaf\xa2\x9a\xbdL\xa3\xea\xbcRde:\x19\xf7R=z\xe3\xcc\xbc\x83kO\xbd\xa3\xb9\x86\xbb\x9f\x11\xe5\xbb\xd3^\x17>\xe3\xce=\xbd\xb3\xb4K\xbd\xdf\x11\xbb=\xb5\x99\x9d=xG\xc5\xbc\xb8*\xbe\xbc\xcd3\x8c=\xa7?\xc0\xbc\xd3zq<\r\x81p=\x88h\xd5\xbd=h[\xbd\x82P\x99=]\x80\x80=\x15\x83\xcd=\xd8\xb67\xbd;=\'\xbd9\xaa\x9a=H\xa1I<$\xbd\xc0\xbcT(\x95\xbd\xbb\xdc\xe2\xbcS\x05p\xbdG,\xa0<\not= \xe6\x16\xbed\xe9\xbc<\x04\xa3\x10=\x8bp\x1f\xbd\x05s\xe8\xbc\xb6\x93\xb5<\x86h+<v\x07@\xbd\xf2\xe6\x9e\xbc\xbe\'\x82\xba\x1b-I=\\\xd5\xc3\xbd\xb1\x10|\xbd\x03\x92\x85\xbd\x91\x064<c\xfep\xbd\xc6\x83\x98<Q}5\xbd\x1e\x19-\xbd\x9c\r\xc1<\xbe\x04\x9e\xbc=\x98\xca\xbc\xa0\xaf\x0f\xbd\x8c\xcfo\xbd\xb2\x19\xeb=\xa43\x18\xbe\xa8\x02x\xbc\xd3\n\xce\xbc\xc7\xbe\xeb\xbc\x11\x9b\xeb;\xacA\xa1\xbdY,\x00=\xb2\x8b\x91</\xda\x94<\xf6`a=\x1a\xbe\xb4\xbd`\xcb\x8e\xbcx\x1f\xe2;h\xd9\xad;\x03\x9a\'=\xa9\xb0x\xbb\x9e\x06\xf8\xbc\xdf\x10<\xbd\x7f\xaaY<\xf9\x88\xd1;\x15}c=~\xd6\xa4\xbd\x81J\xb3\xbd\xb3f\x9f\xbd\x01\x1c\xcd;0g\x81\xbd\xf6\x17o\xbc\x85\x01\x10=Ze\xc9=fd+<\x11nb\xbdv;\x89=\xb3\xc6\xcc\xbc_1T\xbd\x89!\xbf<\xcc\x009=\x05\xa4h=w\xb10\xbd>Mj\xbd\xa7\n\x1e\xbe%\x15\x94\xbd`\xfc\x87\xbc\xd2\xb5\x02\xbd\xfb62\xbdM\xf4\xe8\xba\xde\x92\xa2<\xc5[X\xbd\n\x1f\xf0;g\x95\xbd\xbc\xae\xcf|\xbc\x8b\xcdI=\x10\\\x0c\xbdwtH\xbe\x8a\xeez\xbc\xc6\xcc|\xbc\xdd\xbf\x88=\xb1\xec\xb9<\x1e~\xd9<f\xd24=\xde\xbdj=f{\x82=\xe0r\xb3<=~\xb2=\xac\xe0\xb6=\xa81%>\x1eg&<Et\xfe\xbd\xf6\xffw\xbd 3\x08\xbe\xffE\xb4\xbdK\xa4\x0b\xbd\xe9g\xcf\xbcCQ\xf7<g\x07\x8c=\x82A\xae\xbd\x82\x98\x8d=\x0b\xb3\xa4\xbd!p\xf8;\xa4\xe9*\xbd\'-\x8c\xbd\xf1\x1f\xf5=\xe3\xa1J\xbd\x123\x8d\xbcg\x15\x99<\xfc@\xdd;\xe0\xc4\'\xbdt\xf6\xb6\xbbQ>\xf8=Y\xfe\xf9\xbb\x8e\xdd\xdb=J).=\xfe\xec\x88=\x17\x14\x00<\x1b\xf2\xf0=\xf7\x87*\xbcM0\x1e<H\xbd#=\x9f\xe1\x8e<\x00\xe5\x12\xbe\x99>\xd7<q\xed\x81\xbd3)\x14=N\x04\x02\xbd\xacu\x14\xbd\xc7\xcfj\xbd\xa6Q\xae\xbd\xf9(\xa9\xbd\x07\x9c =\xb2L>\xbd\xe8\xf5\x13\xbdv\x95\x9b=X\xeeE;}\xc8\xd5=+\x80\x89=\x7fn\t\xbb8\xef\xbe\xbd\x7f\xf3\x9a=\xd9\xdc\x1f\xbeX\xfd\xd3:{\t\xc0=_\x93\xe9=\x94Q\xc0=\x11C[\xbd{\xaf\\\xbd\x15\x91,\xb9\xa9K\xc9\xbbw\x17\xcd=\x80\x91\x94=\x04\x7f\xef\xbc\xfbw*<',
         'name': '魏传征'}]

    fun2 = FaceRecognition(Appkey=Appkey, SDKey=SDKey)
    flag = fun2.ActivationFace()
    if(flag):
        img = cv2.imread('3.jpg')
        print(fun2.mutifacerecon(facelist=data,img=img))
    else:
        print("人脸识别激活失败")
