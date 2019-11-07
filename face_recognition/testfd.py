import sys
import cv2
import os
import pickle
from PyQt5 import QtGui,QtCore,QtWidgets
import cameraui
from Face_Util import FaceRecognition,FaceInfo,FaceList
import time
from multiprocessing import Process

from io import BytesIO
from ctypes import *

Appkey=b'2FzzVsnbAkk9q8eLx2s1Q7tft3dY1NZXdnLN8xK6UtXf'
SDKey=b'DAEJTcePD4TWaWKej3xRpPxBhCWGkFf4nxdYnooLWDuP'

abpath = './fddata'

class Savepkl(Process):
    def __init__(self):
        super(Savepkl, self).__init__()
        self.msg = None

    def getmsg(self,msg):
        self.msg = msg
    def saveinfo(self):
        path = './fddata/{}.pkl'.format(int(time.time()))

        try:
            with open(path, 'wb') as fw:
                pickle.dump(self.msg, fw)
        except Exception as e:
            print(e)

    def run(self):
        self.saveinfo()



class ShowFD(Process):
    def __init__(self):
        super(ShowFD, self).__init__()
        self.function = None
        self.facelist = None
        self.img = None
        self.count = 0

    def getmsg(self,facelist,function):
        self.function = function
        self.facelist = facelist

    def getimg(self,img):
        self.img = img
        # print("new img")
    def show_index(self):
        tz = self.function.getFaceFutrue(self.img)
        info = self.function.getMaxPro(currentFeature = tz, FeatueList =self.facelist)
        return info

    def run(self):
        if not self.count==10:
            self.count = self.count+1
            return None
        else:
            self.count = 0
            try:
                info =self.show_index()
                return info
            except Exception as e:
                print(e)


class Uiwindow(QtWidgets.QMainWindow, cameraui.Ui_Form):

    def __init__(self, parent=None):
        super(Uiwindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('人脸检测测试')
        self.setFixedSize(self.width(), self.height())
        self.timer_camera = QtCore.QTimer()
        self.cap = cv2.VideoCapture()
        self.CAM_NUM = 0
        self.slot_init()



        #人脸识别模块
        self.facerecognition = FaceRecognition(FaceInfo(Appkey=Appkey, SDKey=SDKey))
        # self.faceinfolist = self.LoadFaceInfo()
        self.faceinfolist = []

        self.thread = ShowFD()

        self.saver = Savepkl()

        self.loadFeature()

        self.image = None
    # def LoadFaceInfo(self):

    def loadFeature(self):
        path = './fddata/'
        items = os.listdir(path)

        for item in items:
            newpath = os.path.join(path, item)
            try:
                with open(newpath, 'rb') as rw:
                    data = pickle.load(rw)
                    # img = data['img']
                    # info = data['info']
                    # feature = fun.process(data['feature'])
                    # facemsg = FaceList(feature=feature, info=info, img=img)
                    self.faceinfolist.append(data)
            except Exception as e:
                print(e)

    def slot_init(self):
        self.opencamrea.clicked.connect(self.button_open_camera_click)
        self.timer_camera.timeout.connect(self.show_camera)
        self.cutPic.clicked.connect(self.button_cut_pic_click)
        self.save.clicked.connect(self.button_save_pic_click)


    def button_save_pic_click(self):
        if(self.ageinput.text() == "" or self.naninput.text() == "" or self.inputsex.text() ==""):
            QtWidgets.QMessageBox.about(self, "提示", "信息输入不完整")
        else:
            info = {"姓名":self.naninput.text(),"性别":self.inputsex.text(),"年龄":self.ageinput.text()}
            feature = self.facerecognition.getFaceFutrue(self.cutimgage)

            data = {"img": self.cutimgage,
                    "info": info,
                    "feature":BytesIO(string_at(feature.feature,feature.featureSize)).getvalue()}

            self.faceinfolist.append(data)

            try:
                self.saver.getmsg(data)
                self.saver.start()
            except Exception as e:
                print(e)

            # self.saveinfo(facemsg)
            self.ageinput.setVisible(False)
            self.naninput.setVisible(False)
            self.inputsex.setVisible(False)
            self.cut_imgshow.setVisible(False)

            self.save.setVisible(False)
            self.sex.setVisible(False)
            self.name.setVisible(False)
            self.age.setVisible(False)
            QtWidgets.QMessageBox.about(self, "提示", "信息录入成功")




    #截图输入信息
    def button_cut_pic_click(self):
        if(self.facerecognition.isHaveFace(self.image)):
            self.cutimgage = self.image
            show = cv2.resize(self.cutimgage, (140, 105))
            show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)


            showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
            self.cut_imgshow.setVisible(True)
            self.cut_imgshow.setPixmap(QtGui.QPixmap.fromImage(showImage))

            self.ageinput.setText("")
            self.naninput.setText("")
            self.inputsex.setText("")

            self.ageinput.setVisible(True)
            self.naninput.setVisible(True)
            self.inputsex.setVisible(True)

            self.save.setVisible(True)
            self.sex.setVisible(True)
            self.name.setVisible(True)
            self.age.setVisible(True)
        else:
            QtWidgets.QMessageBox.about(self, "提示", "未检测到人脸")




    def button_open_camera_click(self):
        if self.timer_camera.isActive() == False:
            flag = self.cap.open(self.CAM_NUM)
            if flag == False:
                msg = QtWidgets.QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确",
                                                    buttons=QtWidgets.QMessageBox.Ok,
                                                    defaultButton=QtWidgets.QMessageBox.Ok)
            else:
                self.timer_camera.start(30)
                self.opencamrea.setText(u'关闭相机')
                self.cutPic.setVisible(True)

                try:
                    self.thread.getmsg(facelist=self.faceinfolist, function=self.facerecognition)
                    self.thread.start()
                except Exception as e:
                    print(e)



        else:
            self.timer_camera.stop()
            self.cap.release()
            self.camera.clear()
            self.opencamrea.setText(u'打开相机')
            self.cutPic.setVisible(False)
            try:
                self.thread.terminate()
            except Exception as e:
                print(e)



    def show_camera(self):
        flag, self.image = self.cap.read()
        show = cv2.resize(self.image, (280,210))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        show = self.facerecognition.showMaxFace(show)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.camera.setPixmap(QtGui.QPixmap.fromImage(showImage))
        try:
            self.thread.getimg(self.image)
            index = self.thread.run()
            if not index == None:
                self.showinfoface(index)
        except Exception as e:
            print(e)





    def showinfoface(self,index):
        if not index == -1:
            ret = self.faceinfolist[index]
            showImage = cv2.resize(ret['img'], (140, 105))
            showImage = cv2.cvtColor(showImage, cv2.COLOR_BGR2RGB)
            showImage = QtGui.QImage(showImage, showImage.shape[1], showImage.shape[0], QtGui.QImage.Format_RGB888)
            self.showinfo.setPixmap(QtGui.QPixmap.fromImage(showImage))
            info = ret['info']
            self.showage.setText("年龄：{}".format(info["年龄"]))
            self.showname.setText("姓名：{}".format(info["姓名"]))
            self.showsex.setText("性别：{}".format(info["性别"]))
        else:
            self.showinfo.setPixmap(QtGui.QPixmap(""))
            self.showage.setText("")
            self.showname.setText("")
            self.showsex.setText("")


    def closeEvent(self, event):
        ok = QtWidgets.QPushButton()
        cacel = QtWidgets.QPushButton()

        msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, u"关闭", u"是否关闭！")

        msg.addButton(ok, QtWidgets.QMessageBox.ActionRole)
        msg.addButton(cacel, QtWidgets.QMessageBox.RejectRole)
        ok.setText(u'确定')
        cacel.setText(u'取消')
        # msg.setDetailedText('sdfsdff')
        if msg.exec_() == QtWidgets.QMessageBox.RejectRole:
            event.ignore()
        else:
            #             self.socket_client.send_command(self.socket_client.current_user_command)
            if self.cap.isOpened():
                self.cap.release()
            if self.timer_camera.isActive():
                self.timer_camera.stop()
            event.accept()
            try:
                os._exit(0)
            except Exception as e:
                print(e)



def main():
    app = QtWidgets.QApplication(sys.argv)     # 创建QApplication对象
    mywindow = Uiwindow()        # 创建MyWindow对象
    mywindow.show()          # 显示窗口
    app.exec_()           # 进入消息循环
    app = QtWidgets.QApplication(sys.argv)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
