from PyQt5.QtCore import QDateTime, QTimer
from PyQt5.QtWidgets import QDialog, QMessageBox, QLineEdit, QApplication, QStackedWidget, QWidget

from StudentSystem.Logic_StudentMain import LogicStudentMain
from MainTest.UI_Main import Ui_MainWindow
from PyQt5 import QtCore,QtGui,QtWidgets

from newMember.logic_Newmember import LogicNewMember
#排课系统
from UpdateClass.logic_updateClass import logicUpdateClass

#教练系统
from  CoachSystem.logic_sysCoach import logicSysCoach
#签到系统
from Qiandao.logic_Qiandao_face import LogicQiandaoFace
#统计系统
from SummarySystem.logic_sysSum import logicSysSum
#评价录入系统
from EvaluationSystem.logic_Evaluation import LogicEvaluationMain

# 仓库系统
from GoodsSystem.logicGoods import logicGoods

#修改密码和二级密码
from MainTest.logic_ModefyPwd import LogicModifyPwd
from MainTest.Logic_ModifyVerify import LogicModifyVerify

import Login.CheckDBandFace as ckdf


#二级验证码
from CoachSystem.logic_verify import logicVerify

import os,sys





class LogicMain(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,MySQL,facefunction,user):
        super(LogicMain, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        self.MySQL = MySQL
        self.facefunction = facefunction
        self.username = user
        self.init()
        self.slot_init()

    def init(self):


        self.stackedWidget = QStackedWidget()
        self.Layout.addWidget(self.stackedWidget)

        #用户和时间
        self.gottaUser()
        #实时显示时间
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()

        #
        #子界面
        self.FormBlank = QWidget()  #空白界面

        self.FormStudentMain = LogicStudentMain(MySQL=self.MySQL)

        self.FormLesson = logicUpdateClass(MySQL=self.MySQL)  # 排课系统

        self.FormNewMember = LogicNewMember(MySQL=self.MySQL, facefunction = self.facefunction) #新学员录入系统

        self.FormSumSys = logicSysSum(MySQL=self.MySQL)  # 统计系统


        self.FormFaceQiandao = LogicQiandaoFace(MySQL=self.MySQL,facefunction=self.facefunction)  # 人脸查询系统

        self.FormCoach = logicSysCoach(MySQL=self.MySQL)  # 教练系统

        self.Evaluation = LogicEvaluationMain(MySQL=self.MySQL) #评价系统

        self.FromGoods = logicGoods(MySQL=self.MySQL)  # 仓库系统

        self.stackedWidget.addWidget(self.FormBlank)
        self.stackedWidget.addWidget(self.FormNewMember)
        self.stackedWidget.addWidget(self.FormLesson)
        self.stackedWidget.addWidget(self.FormFaceQiandao)
        self.stackedWidget.addWidget(self.FormStudentMain)
        self.stackedWidget.addWidget(self.FormCoach)
        self.stackedWidget.addWidget(self.Evaluation)
        self.stackedWidget.addWidget(self.FormSumSys)

        self.stackedWidget.addWidget(self.FromGoods)

        #初始设定为学生界面
        self.stackedWidget.setCurrentWidget(self.FormStudentMain)


    def slot_init(self):
        #新学员录入系统嵌入
        self.pb_main_NewMemberSystem.clicked.connect(self.on_pb_main_NewMemberSystem)


        #排课系统嵌入
        self.pb_main_LessonSystem.clicked.connect(self.on_pb_main_LessonSystem)
        self.pb_main_LessonSystem.clicked.connect(self.FormLesson.myclear)

        #签到系统
        self.pb_main_QiandaoSystem.clicked.connect(self.on_pb_main_QiandaoSystem)
        self.pb_main_QiandaoSystem.clicked.connect(self.FormFaceQiandao.myclear)

        # 签到系统
        self.pb_main_StudentSystem.clicked.connect(self.on_pb_main_StudentSystem)
        self.pb_main_StudentSystem.clicked.connect(self.FormStudentMain.frash_studentList)

        # 教练系统
        self.pb_main_CoachSystem.clicked.connect(self.on_pb_main_CoachSystem)
        self.pb_main_CoachSystem.clicked.connect(self.FormCoach.myclear)


        # 统计系统
        self.pb_main_StatisticSystem.clicked.connect(self.on_pb_main_StatisticSystem)
        self.pb_main_StatisticSystem.clicked.connect(self.FormSumSys.myclear)

        #密码修改
        self.action_pwd.triggered.connect(self.ModifyPwd)
        self.action_verify.triggered.connect(self.ModifyVerify)

        #评价录入系统
        self.pb_main_EvaluationSystem.clicked.connect(self.on_pb_main_EvaluationSystem)


        # 仓库系统
        self.pb_main_CangkuSystem.clicked.connect(self.on_pb_main_GoodsSystem)
        self.pb_main_CangkuSystem.clicked.connect(self.FromGoods.myclear)

    def ModifyPwd(self):
        self.LogicModifyPwd = LogicModifyPwd(username=self.username)
        self.LogicModifyPwd.setWindowModality(QtCore.Qt.ApplicationModal)
        self.LogicModifyPwd.show()

    def ModifyVerify(self):
        if(self.username == 'Jessie' or self.username == 'WangAn'):
            self.LogicModifyVerify = LogicModifyVerify(username=self.username)
            self.LogicModifyVerify.setWindowModality(QtCore.Qt.ApplicationModal)
            self.LogicModifyVerify.show()
        else:
            QMessageBox.information(self, '提示', '无权限！', QMessageBox.Ok, QMessageBox.Ok)

    def gottaUser(self):
        if(self.username =='Jessie'):
            self.lb_main_username.setText('当前用户：{}'.format('苏总'))
        elif (self.username == 'WangAn'):
                self.lb_main_username.setText('当前用户：{}'.format('王总'))
        elif (self.username == 'WangliPing'):
                self.lb_main_username.setText('当前用户：{}'.format('王力平'))
        else:
            self.lb_main_username.setText('当前用户：{}'.format('其他'))


    def showtime(self):
        datetime = QDateTime.currentDateTime()
        text = datetime.toString()
        self.lb_main_time.setText(text)

    # 教练系统
    def on_pb_main_CoachSystem(self):
        self.stackedWidget.setCurrentWidget(self.FormCoach)

    #学员管理系统
    def on_pb_main_StudentSystem(self):
        self.stackedWidget.setCurrentWidget(self.FormStudentMain)

    #新学员系统
    def on_pb_main_NewMemberSystem(self):
        self.stackedWidget.setCurrentWidget(self.FormNewMember)

    #排课系统
    def on_pb_main_LessonSystem(self):
        self.stackedWidget.setCurrentWidget(self.FormLesson)


    # 统计系统
    def on_pb_main_StatisticSystem(self):
        if (self.username == 'Jessie' or self.username == 'WangAn'):
            self.stackedWidget.setCurrentWidget(self.FormSumSys)
        else:
            QMessageBox.information(self, '提示', '无权限！', QMessageBox.Ok, QMessageBox.Ok)


    #评价系统
    def on_pb_main_EvaluationSystem(self):
        self.stackedWidget.setCurrentWidget(self.Evaluation)


    #签到系统
    def on_pb_main_QiandaoSystem(self):
        # self.FormFaceQiandao.getCamClose()
        self.stackedWidget.setCurrentWidget(self.FormFaceQiandao)

    # 仓库系统
    def on_pb_main_GoodsSystem(self):
        self.stackedWidget.setCurrentWidget(self.FromGoods)




    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示',
                                     "确定退出本系统吗?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    f1, MySQL = ckdf.CheckDB()
    f2, facefunction = ckdf.CheckFace()
    app = QtWidgets.QApplication(sys.argv)
    window = LogicMain( MySQL=MySQL,facefunction=facefunction,user='Jessie')
    window.show()
    sys.exit(app.exec_())
