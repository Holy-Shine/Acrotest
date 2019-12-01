
import cv2
import os,sys

from PyQt5.QtWidgets import QDialog,QMessageBox,QLineEdit,QApplication
from PyQt5 import QtCore,QtGui,QtWidgets

from newMember.UI_NewMember import Ui_NewMember
from newMember.logic_MemberCAMChose import LogicMemberCAMChose

from Qiandao.process_camera_info import Camera

card = ["年卡","季卡","月卡"]
classitem  = ["平衡车", "轮滑"]

class LogicNewMember(Ui_NewMember,QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    #     self.cameranum = camnum
        self.timer_camera = QtCore.QTimer()
        self.cap = cv2.VideoCapture()
        self.image = None
    #
    #
        self.LogicMemberCAMChose = None
        self.cameranum = None
        self.camtag = False

        self.init()
        self.slot_init()
    #
    #
    def init(self):
        self.listFunc.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)
    #     self.clearLineEdit()
        self.cb_card_new.addItems(card)
        self.cb_classitem_new.addItems(card)
    #     self.cb_card.addItems(card)
    #     self.cb_classitem.addItems(classitem)
    #     self.cb_card_2.addItems(card)
    #     self.cb_classitem_2.addItems(classitem)
    #
    #
    # def clearLineEdit(self):
    #     self.et_cichu.setText('')
    #     self.et_age.setText('')
    #     self.et_parent.setText('')
    #     self.et_money.setText('')
    #
    def slot_init(self):

        self.bt_opencam_new.clicked.connect(self.open_camera_new)
        self.pb_opencam_old.clicked.connect(self.open_camera_old)
    #
    #     self.bt_cutpic.clicked.connect(self.cut_pic)
    #
    #
    #     self.bt_confrim.clicked.connect(self.confrim)
    #
    #     self.bt_back.clicked.connect(self.back)
    #
    #
    #
    #
    # def cut_pic(self):
    #     try:
    #         if self.timer_camera.isActive() == False:
    #             QMessageBox.warning(self, u"Warning", u"请先打开摄像头",
    #                                 buttons=QMessageBox.Ok,
    #                                 defaultButton=QMessageBox.Ok)
    #         else:
    #             self.timer_camera.stop()
    #             self.cap.release()
    #             self.bt_opencam.setText(u'打开摄像头')
    #     except Exception as e:
    #         print(e)
    #
    # def close_camera(self):
    #     self.lb_cam.clear()
    #     if self.timer_camera.isActive() == True:
    #         self.timer_camera.stop()
    #         self.cap.release()
    #         self.lb_cam.clear()
    #         self.bt_opencam.setText(u'打开摄像头')
    #
    #
    def open_camera_new(self):
        self.cameranum = Camera().get_cam_num()
        if(self.cameranum>0):
            self.camtag = True
            self.open_camera()

        else:
            QMessageBox.warning(self, u"Warning", u"请检查摄像头",
                                            buttons=QMessageBox.Ok,
                                            defaultButton=QMessageBox.Ok)

    def open_camera_old(self):
            self.cameranum = Camera().get_cam_num()
            if (self.cameranum > 0):
                try:
                    self.camtag = False
                    self.open_camera()
                except Exception as e:
                    print(e)

            else:
                QMessageBox.warning(self, u"Warning", u"请检查摄像头",
                                    buttons=QMessageBox.Ok,
                                    defaultButton=QMessageBox.Ok)
    #
    def open_camera(self):
        try:
            if self.timer_camera.isActive() == False:
                my = LogicMemberCAMChose(Camnum=self.cameranum)
                my.mySignal.connect(self.getCAMNO)
                my.exec_()
            else:
                self.timer_camera.stop()
                self.cap.release()
                print(self.camtag)
                if (self.camtag):
                    self.lb_cam_new.clear()
                    self.bt_opencam_new.setText(u'打开摄像头')
                else:
                    self.lb_cam_old.clear()
                    self.pb_opencam_old.setText(u'打开摄像头')
        except Exception as e:
            print(e)



    #获取摄像头
    def getCAMNO(self, camnum):
        self.get_camera(int(camnum))
        self.timer_camera.timeout.connect(self.show_camera)
    #
    # #打开摄像头
    def get_camera(self,camnum):
        try:
            if self.timer_camera.isActive() == False:
                flag = self.cap.open(camnum)
                if flag == False:
                    QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确",
                                                        buttons=QMessageBox.Ok,
                                                        defaultButton=QMessageBox.Ok)
                else:
                    self.timer_camera.start(30)
                if(self.camtag):
                    self.bt_opencam_new.setText(u'关闭摄像头')
                else:
                    self.pb_opencam_old.setText(u'关闭摄像头')
        except Exception as e:
            print(e)
    #
    #
    # #显示图像
    def show_camera(self):
        flag, self.image = self.cap.read()
        # print(self.image.shape)
        # show = self.image[0:128, 0:512]
        show = cv2.resize(self.image, (260,346))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)

        # show = self.facerecognition.showMaxFace(show)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        if(self.camtag):
            self.lb_cam_new.setPixmap(QtGui.QPixmap.fromImage(showImage))
        else:
            self.lb_cam_old.setPixmap(QtGui.QPixmap.fromImage(showImage))


        '''
        此处写框人脸接口 改变self.image 的值
        '''
    #
    # #录入信息
    # def confrim(self):
    #     print(1)
    #
    # #返回
    # def back(self):
    #     self.clearLineEdit()
    #     self.close_camera()
    #
    #
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
    login = LogicNewMember()
    login.show()
    sys.exit(app.exec_())