from PyQt5.QtWidgets import QDialog, QMessageBox, QLineEdit, QApplication, QStackedWidget, QWidget

from StudentSystem.Logic_StudentMain import LogicStudentMain
from MainTest.UI_Main import Ui_MainWindow
from PyQt5 import QtCore,QtGui,QtWidgets

from newMember.logic_Newmember import LogicNewMember
#排课系统
from UpdateClass.logic_updateClass import logicUpdateClass

#教练系统
from  CoachSystem.logic_sysCoach import logicSysCoach
#导入签到系统
from Qiandao.logic_qiandao_chose import LogicQiandaoChose
from Qiandao.logic_Qiandao_face import LogicQiandaoFace
from SummarySystem.logic_sysSum import logicSysSum

from FaceFunction.FaceUtil import FaceRecognition


import os,sys

from Qiandao.process_camera_info import Camera
from ConnextMySQL.MySQLBase import MySQLBaseFunction


host='121.199.17.205',  # IP
user='Jessie',  # 用户名
password='Jessie.121406',  # 密码
database = 'meminfo',

Appkey=b'2FzzVsnbAkk9q8eLx2s1Q7tft3dY1NZXdnLN8xK6UtXf'
SDKey=b'DAEJTcePD4TWaWKej3xRpPxBhCWGkFf4nxdYnooLWDuP'

class LogicMain(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(LogicMain, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        self.MySQL = MySQLBaseFunction(HostIP=host,
                                       Username = user,
                                       Password= password,
                                       DataBase= database)

        self.MySQL.ConnectMySQL()

        self.init()
        self.slot_init()

    def init(self):
        self.facefunction = FaceRecognition(Appkey=Appkey, SDKey=SDKey)
        flag = self.facefunction.ActivationFace()
        if not flag:
            QtWidgets.QMessageBox.warning(self, u"Warning", u"人脸识别检测初始化失败，请检查人脸识别SDK",
                                          buttons=QtWidgets.QMessageBox.Ok)

        self.stackedWidget = QStackedWidget()
        self.Layout.addWidget(self.stackedWidget)

        #子界面
        self.FormBlank = QWidget()  #空白界面

        self.FormStudentMain = LogicStudentMain()

        self.FormLesson = logicUpdateClass(MySQL=self.MySQL)  # 排课系统

        self.FormNewMember = LogicNewMember(MySQL=self.MySQL, facefunction = self.facefunction) #新学员录入系统

        self.FormSumSys = logicSysSum(MySQL=self.MySQL)  # 统计系统


        self.ChaxunChose = LogicQiandaoChose() #选择签到方式
        self.ChaxunChose.setWindowModality(QtCore.Qt.ApplicationModal)
        self.FormFaceQiandao = LogicQiandaoFace()  # 人脸查询系统

        self.FormCoach = logicSysCoach(MySQL=self.MySQL)  # 教练系统


        self.stackedWidget.addWidget(self.FormBlank)
        self.stackedWidget.addWidget(self.FormNewMember)
        self.stackedWidget.addWidget(self.FormLesson)
        self.stackedWidget.addWidget(self.FormFaceQiandao)
        self.stackedWidget.addWidget(self.FormStudentMain)
        self.stackedWidget.addWidget(self.FormCoach)

        self.stackedWidget.addWidget(self.FormSumSys)

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

        # 教练系统
        self.pb_main_CoachSystem.clicked.connect(self.on_pb_main_CoachSystem_clicked)


        # 统计系统
        self.pb_main_StatisticSystem.clicked.connect(self.on_pb_main_StatisticSystem_clicked)

    # 教练系统
    def on_pb_main_CoachSystem_clicked(self):
        # self.FormFaceQiandao.getCamClose()
        self.stackedWidget.setCurrentWidget(self.FormCoach)

    #学员管理系统
    def on_pb_main_StudentSystem_clicked(self):
        # self.FormFaceQiandao.getCamClose()
        self.stackedWidget.setCurrentWidget(self.FormStudentMain)

    #新学员系统
    def on_pb_main_NewMemberSystem_clicked(self):
        # self.FormFaceQiandao.getCamClose()
        self.stackedWidget.setCurrentWidget(self.FormNewMember)

    #排课系统
    def on_pb_main_LessonSystem_clicked(self):
        # self.FormFaceQiandao.getCamClose()
        # self.FormNewMember.close_camera()
        self.stackedWidget.setCurrentWidget(self.FormLesson)


    # 统计系统
    def on_pb_main_StatisticSystem_clicked(self):
        self.stackedWidget.setCurrentWidget(self.FormSumSys)

    #新转老学员
    def on_pb_main_toOldMemberSystem_clicked(self):
        # self.FormFaceQiandao.getCamClose()
        # self.FormNewMember.close_camera()
        self.stackedWidget.setCurrentWidget(self.FormOldMember)

    #老转新学员
    def on_pb_main_toNewMemberSystem_clicked(self):
        # self.FormFaceQiandao.getCamClose()
        # self.FormNewMember.close_camera()
        self.stackedWidget.setCurrentWidget(self.FormNewMember)

    #签到系统
    def on_pb_main_QiandaoSystem_clicked(self):
        # self.FormFaceQiandao.getCamClose()
        self.stackedWidget.setCurrentWidget(self.FormBlank)
        try:
            self.ChaxunChose.show()
            self.ChaxunChose.bt_confrim.clicked.connect(self.open_qiandao)
        except Exception as e:
            print(e)


    def open_qiandao(self):
        try:
            # self.FormFaceQiandao.setCamNum(cam=self.ChaxunChose.cb_cam.currentText(),
            #                                year=self.ChaxunChose.cb_year.currentText(),
            #                                week = self.ChaxunChose.cb_week.currentText(),
            #                                day = self.ChaxunChose.cb_day.currentText())
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

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LogicMain()
    window.show()
    sys.exit(app.exec_())
