from PyQt5.QtWidgets import QDialog, QMessageBox, QLineEdit, QApplication, QStackedWidget, QWidget

from Logic_StudentMain import LogicStudentMain
from MainTest import Ui_MainWindow
from PyQt5 import QtCore,QtGui,QtWidgets

from newMember.logic_Newmember import LogicNewMember
from GUI.logic_updateClass import logicUpdateClass
from newMember.logic_OldMember import LogicOldMember


#导入签到系统
from Qiandao.logic_qiandao_chose import LogicQiandaoChose
from Qiandao.logic_Qiandao_face import LogicQiandaoFace
from Qiandao.logic_qiandao_camera import LogicQiandaoCamrea
from Qiandao.logic_Qiandao_chaxun import LogicQiandaoChaxun

import os,sys

from process_camera_info import Camera




class LogicMain(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(LogicMain, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        self.CameraNum = Camera().get_cam_num()

        self.init()
        self.slot_init()

    def init(self):
        self.stackedWidget = QStackedWidget()
        self.Layout.addWidget(self.stackedWidget)

        #子界面
        self.FormBlank = QWidget()  #空白界面

        self.FormStudentMain = LogicStudentMain()

        self.FormLesson = logicUpdateClass()  # 排课系统

        self.FormNewMember = LogicNewMember(self.CameraNum) #新学员录入系统
        self.FormOldMember = LogicOldMember() #老学员续卡系统

        self.FormChaxunQiandao = LogicQiandaoChaxun() #签到查询系统

        self.FormLesson = logicUpdateClass()  # 排课系统

        self.ChaxunChose = LogicQiandaoChose() #选择签到方式
        self.CamChose = LogicQiandaoCamrea(cameranum=self.CameraNum) #摄像头选择
        self.FormFaceQiandao = LogicQiandaoFace()  # 人脸查询系统


        self.stackedWidget.addWidget(self.FormBlank)
        self.stackedWidget.addWidget(self.FormNewMember)
        self.stackedWidget.addWidget(self.FormLesson)
        self.stackedWidget.addWidget(self.FormOldMember)
        self.stackedWidget.addWidget(self.FormChaxunQiandao)
        self.stackedWidget.addWidget(self.FormFaceQiandao)
        self.stackedWidget.addWidget(self.FormStudentMain)

        #初始设定为学生界面
        self.stackedWidget.setCurrentWidget(self.FormStudentMain)


    def slot_init(self):
        #新学员录入系统嵌入
        self.pb_main_NewMemberSystem.clicked.connect(self.on_pb_main_NewMemberSystem_clicked)
        self.FormNewMember.lb_toOld.clicked.connect(self.on_pb_main_toOldMemberSystem_clicked)
        self.FormOldMember.lb_toNew.clicked.connect(self.on_pb_main_toNewMemberSystem_clicked)

        #排课系统嵌入
        self.pb_main_LessonSystem.clicked.connect(self.on_pb_main_LessonSystem_clicked)

        #签到系统
        self.pb_main_QiandaoSystem.clicked.connect(self.on_pb_main_QiandaoSystem_clicked)

        # 签到系统
        self.pb_main_StudentSystem.clicked.connect(self.on_pb_main_StudentSystem_clicked)

    #学员管理系统
    def on_pb_main_StudentSystem_clicked(self):
        self.FormFaceQiandao.getCamClose()
        self.stackedWidget.setCurrentWidget(self.FormStudentMain)

    #新学员系统
    def on_pb_main_NewMemberSystem_clicked(self):
        self.FormFaceQiandao.getCamClose()
        self.stackedWidget.setCurrentWidget(self.FormNewMember)

    #排课系统
    def on_pb_main_LessonSystem_clicked(self):
        self.FormFaceQiandao.getCamClose()
        self.FormNewMember.close_camera()
        self.stackedWidget.setCurrentWidget(self.FormLesson)

    #新转老学员
    def on_pb_main_toOldMemberSystem_clicked(self):
        self.FormFaceQiandao.getCamClose()
        self.FormNewMember.close_camera()
        self.stackedWidget.setCurrentWidget(self.FormOldMember)

    #老转新学员
    def on_pb_main_toNewMemberSystem_clicked(self):
        self.FormFaceQiandao.getCamClose()
        self.FormNewMember.close_camera()
        self.stackedWidget.setCurrentWidget(self.FormNewMember)

    #签到系统
    def on_pb_main_QiandaoSystem_clicked(self):
        self.FormFaceQiandao.getCamClose()
        self.stackedWidget.setCurrentWidget(self.FormBlank)
        self.ChaxunChose.show()
        self.ChaxunChose.bt_secletqiandao.clicked.connect(self.open_select_qiandao)
        self.ChaxunChose.bt_faceqiandao.clicked.connect(self.open_cam_chose)

    def open_select_qiandao(self):
        self.ChaxunChose.close()
        self.stackedWidget.setCurrentWidget(self.FormChaxunQiandao)

    def open_cam_chose(self):
        self.ChaxunChose.close()
        self.CamChose.show()
        self.CamChose.bt_confrim.clicked.connect(self.open_face_qiandao)

    def open_face_qiandao(self):
        self.FormFaceQiandao.setCamNum(self.CamChose.comboBox.currentText())
        self.stackedWidget.setCurrentWidget(self.FormFaceQiandao)
        self.CamChose.close()



    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示',
                                     "确定退出本系统吗?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LogicMain()
    window.show()
    sys.exit(app.exec_())
