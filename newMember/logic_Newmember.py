
import cv2
import os,sys

from PyQt5.QtWidgets import QDialog,QMessageBox,QLineEdit,QApplication
from PyQt5 import QtCore,QtGui,QtWidgets

from newMember.UI_NewMember import Ui_NewMember
from newMember.logic_MemberCAMChose import LogicMemberCAMChose


class LogicNewMember(Ui_NewMember,QDialog):
    def __init__(self,camnum):
        super().__init__()
        self.setupUi(self)

        self.cameranum = camnum
        self.timer_camera = QtCore.QTimer()
        self.cap = cv2.VideoCapture()
        self.image = None


        self.init()
        self.slot_init()


    def init(self):
        self.listFunc.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)
        self.clearLineEdit()
        card = ["年卡","季卡","次卡"]
        classitem  = ["平衡车", "轮滑"]
        self.cb_card.addItems(card)
        self.cb_classitem.addItems(classitem)
        self.cb_card_2.addItems(card)
        self.cb_classitem_2.addItems(classitem)


    def clearLineEdit(self):
        self.et_cichu.setText('')
        self.et_age.setText('')
        self.et_parent.setText('')
        self.et_money.setText('')

    def slot_init(self):

        self.bt_opencam.clicked.connect(self.open_camera)

        self.bt_cutpic.clicked.connect(self.cut_pic)


        self.bt_confrim.clicked.connect(self.confrim)

        self.bt_back.clicked.connect(self.back)




    def cut_pic(self):
        try:
            if self.timer_camera.isActive() == False:
                QMessageBox.warning(self, u"Warning", u"请先打开摄像头",
                                    buttons=QMessageBox.Ok,
                                    defaultButton=QMessageBox.Ok)
            else:
                self.timer_camera.stop()
                self.cap.release()
                self.bt_opencam.setText(u'打开摄像头')
        except Exception as e:
            print(e)

    def close_camera(self):
        self.lb_cam.clear()
        if self.timer_camera.isActive() == True:
            self.timer_camera.stop()
            self.cap.release()
            self.lb_cam.clear()
            self.bt_opencam.setText(u'打开摄像头')


    def open_camera(self):
        try:
            if self.timer_camera.isActive() == False:
                my = LogicMemberCAMChose(cameranum = self.cameranum)
                my.mySignal.connect(self.getCAMNO)
                my.exec_()
            else:
                self.timer_camera.stop()
                self.cap.release()
                self.lb_cam.clear()
                self.bt_opencam.setText(u'打开摄像头')
        except Exception as e:
            print(e)

    #获取摄像头
    def getCAMNO(self, camnum):

        self.get_camera(int(camnum))
        self.timer_camera.timeout.connect(self.show_camera)

    #打开摄像头
    def get_camera(self,camnum):
        if self.timer_camera.isActive() == False:
            flag = self.cap.open(camnum)
            if flag == False:
                msg = QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确",
                                                    buttons=QMessageBox.Ok,
                                                    defaultButton=QMessageBox.Ok)
            else:
                self.timer_camera.start(30)

            self.bt_opencam.setText(u'关闭摄像头')


    #显示图像
    def show_camera(self):
        flag, self.image = self.cap.read()
        # print(self.image.shape)
        # show = self.image[0:128, 0:512]
        show = cv2.resize(self.image, (260,346))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)

        # show = self.facerecognition.showMaxFace(show)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.lb_cam.setPixmap(QtGui.QPixmap.fromImage(showImage))


        '''
        此处写框人脸接口 改变self.image 的值
        '''

    #录入信息
    def confrim(self):
        print(1)

    #返回
    def back(self):
        self.clearLineEdit()
        self.close_camera()


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
    login = LogicNewMember(camnum=1)
    login.show()
    sys.exit(app.exec_())