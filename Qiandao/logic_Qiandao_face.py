from PyQt5.QtWidgets import QDialog,QMessageBox,QLineEdit,QApplication

from PyQt5 import QtCore,QtGui,QtWidgets
from multiprocessing import Process
import cv2
from UI_Qiandao_face_Main import UIQiandaoFace
from Face_Util import FaceRecognition,FaceInfo
import os,sys

Appkey=b'2FzzVsnbAkk9q8eLx2s1Q7tft3dY1NZXdnLN8xK6UtXf'
SDKey=b'DAEJTcePD4TWaWKej3xRpPxBhCWGkFf4nxdYnooLWDuP'

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
    def show_index(self):
        tz = self.function.getFaceFutrue(self.img)
        info = self.function.getMaxPro(currentFeature = tz, FeatueList =self.facelist)
        return info

    def run(self):
        if not self.count== 20:
            self.count = self.count+1
            return None
        else:
            self.count = 0
            try:
                info =self.show_index()
                return info
            except Exception as e:
                print(e)


class LogicQiandaoFace(UIQiandaoFace,QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.timer_camera = QtCore.QTimer()
        self.cap = cv2.VideoCapture()
        self.CAM_NUM = -1

        #传入特征序列
        self.face_featureslist = []

        self.facerecognition = FaceRecognition(FaceInfo(Appkey=Appkey, SDKey=SDKey))

        self.thread = ShowFD()

        self.slot_init()


    def setCamNum(self,cam):
        self.CAM_NUM = int(cam)
        self.getCamOpen()

    def setFeaturesList(self,featureslist):
        self.face_featureslist = featureslist

    def getCamOpen(self):
        self.open_camera()
        self.timer_camera.timeout.connect(self.show_camera)

    def getCamClose(self):
        try:
            self.label.clear()
            if self.timer_camera.isActive() == True:
                self.timer_camera.stop()
                self.cap.release()
                self.label.clear()
        except Exception as e:
            print(e)

    def slot_init(self):
        self.bt_qiandao_confrim.clicked.connect(self.qiandao_confrim)
        # self.bt_trackback.clicked.connect(self.close)

        try:
            self.thread.getmsg(facelist=self.face_featureslist, function=self.facerecognition)
            self.thread.start()
        except Exception as e:
            print(e)


    #打开显示摄像头
    def open_camera(self):
        if self.timer_camera.isActive() == False and self.CAM_NUM>=0:
            flag = self.cap.open(self.CAM_NUM)
            if flag == False:
                msg = QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确",
                                                    buttons=QMessageBox.Ok,
                                                    defaultButton=QMessageBox.Ok)
            else:
                self.timer_camera.start(30)


    def show_camera(self):
        flag, self.image = self.cap.read()
        show = cv2.resize(self.image, (260,346))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        # show = self.facerecognition.showMaxFace(show)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(showImage))

        # 检测人脸
        try:
            self.thread.getimg(self.image)
            index = self.thread.run()
            if not index == None:
                self.showinfoface(index)
        except Exception as e:
            print(e)


    #显示检测信息
    def showinfoface(self,index):
        print("检测系统正在运行")


    #确认签到
    def qiandao_confrim(self):
        print(2)




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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = LogicQiandaoFace()
    login.setCamNum(0)
    login.show()
    sys.exit(app.exec_())