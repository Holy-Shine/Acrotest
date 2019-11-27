from PyQt5.QtWidgets import QDialog, QMessageBox, QLineEdit, QApplication, QStackedWidget, QWidget

from StudentSystem.Logic_StudentMain import LogicStudentMain
from MainTest.UI_Main import Ui_MainWindow
from PyQt5 import QtCore,QtGui,QtWidgets


#导入学员录入系统
from newMember.logic_Newmember import LogicNewMember

#导入排课系统
from GUI.logic_updateClass import logicUpdateClass
from GUI.logic_sysCoach import logicSysCoach



#导入签到系统
from Qiandao.logic_qiandao_chose import LogicQiandaoChose
from Qiandao.logic_Qiandao_face import LogicQiandaoFace
from Qiandao.logic_Qiandao_chaxun import LogicQiandaoChaxun

import os,sys

from Qiandao.process_camera_info import Camera


#数据库操作
from ConnextMySQL.MySQLBase import MySQLBaseFunction
host='121.199.17.205',  # IP
user='Jessie',  # 用户名
password='Jessie.121406',  # 密码
database = 'meminfo',




class LogicMain(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(LogicMain, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        self.CameraNum = Camera().get_cam_num()

        self.init()
        self.slot_init()

    def init(self):
        #初始化数据库
        self.MySQL = MySQLBaseFunction(HostIP=host,
                                       Username=user,
                                       Password=password,
                                       DataBase=database)
        self.MySQL.ConnectMySQL()


        #初始化界面
        self.stackedWidget = QStackedWidget()
        self.Layout.addWidget(self.stackedWidget)

        #子界面
        self.FormBlank = QWidget()  #空白界面

        self.FormStudentMain = LogicStudentMain()

        self.FormLesson = logicUpdateClass()  # 排课系统

        self.FormNewMember = LogicNewMember(self.CameraNum) #新学员录入系统

        self.FormChaxunQiandao = LogicQiandaoChaxun() #签到查询系统

        self.FormLesson = logicUpdateClass()  # 排课系统

        self.ChaxunChose = LogicQiandaoChose(camnum=self.CameraNum) #选择签到方式
        self.ChaxunChose.setWindowModality(QtCore.Qt.ApplicationModal)

        self.FormFaceQiandao = LogicQiandaoFace()  # 人脸查询系统

        self.FromCoach = logicSysCoach(MySQL=self.MySQL)


        self.stackedWidget.addWidget(self.FormBlank)
        self.stackedWidget.addWidget(self.FormNewMember)
        self.stackedWidget.addWidget(self.FormLesson)
        self.stackedWidget.addWidget(self.FormChaxunQiandao)
        self.stackedWidget.addWidget(self.FormFaceQiandao)
        self.stackedWidget.addWidget(self.FormStudentMain)
        self.stackedWidget.addWidget(self.FromCoach)

        #初始设定为学生界面
        self.stackedWidget.setCurrentWidget(self.FormStudentMain)


    def slot_init(self):
        #新学员录入系统嵌入
        self.pb_main_NewMemberSystem.clicked.connect(self.on_pb_main_NewMemberSystem_clicked)

        #排课系统嵌入
        self.pb_main_LessonSystem.clicked.connect(self.on_pb_main_LessonSystem_clicked)

        #签到系统
        self.pb_main_QiandaoSystem.clicked.connect(self.on_pb_main_QiandaoSystem_clicked)

        # 签到系统
        self.pb_main_StudentSystem.clicked.connect(self.on_pb_main_StudentSystem_clicked)


        #教练系统
        self.pb_main_CoachSystem.clicked.connect(self.on_pb_main_CoachSystem_clicked)


    #教练管理系统
    def on_pb_main_CoachSystem_clicked(self):
        self.FormFaceQiandao.getCamClose()
        self.stackedWidget.setCurrentWidget(self.FromCoach)

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

    #签到系统
    def on_pb_main_QiandaoSystem_clicked(self):
        self.FormFaceQiandao.getCamClose()
        self.stackedWidget.setCurrentWidget(self.FormBlank)
        self.ChaxunChose.show()
        self.ChaxunChose.bt_confrim.clicked.connect(self.open_qiandao)


    def open_qiandao(self):
        try:
            self.FormFaceQiandao.setCamNum(cam=self.ChaxunChose.cb_cam.currentText(),
                                           year=self.ChaxunChose.cb_year.currentText(),
                                           week = self.ChaxunChose.cb_week.currentText(),
                                           day = self.ChaxunChose.cb_day.currentText())
            self.stackedWidget.setCurrentWidget(self.FormFaceQiandao)
            self.ChaxunChose.close()
        except Exception as e:
            print(e)



    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示',
                                     "确定退出本系统吗?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = LogicMain()
    window.show()
    sys.exit(app.exec_())
