# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainTest.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1314, 892)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fr_main_menu = QtWidgets.QFrame(self.centralwidget)
        self.fr_main_menu.setGeometry(QtCore.QRect(0, 0, 1301, 141))
        self.fr_main_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_main_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_main_menu.setObjectName("fr_main_menu")
        self.pb_main_StudentSystem = QtWidgets.QPushButton(self.fr_main_menu)
        self.pb_main_StudentSystem.setGeometry(QtCore.QRect(30, 10, 141, 111))
        self.pb_main_StudentSystem.setObjectName("pb_main_StudentSystem")
        self.pb_main_NewMemberSystem = QtWidgets.QPushButton(self.fr_main_menu)
        self.pb_main_NewMemberSystem.setGeometry(QtCore.QRect(500, 10, 131, 111))
        self.pb_main_NewMemberSystem.setObjectName("pb_main_NewMemberSystem")
        self.pb_main_LessonSystem = QtWidgets.QPushButton(self.fr_main_menu)
        self.pb_main_LessonSystem.setGeometry(QtCore.QRect(350, 10, 131, 111))
        self.pb_main_LessonSystem.setObjectName("pb_main_LessonSystem")
        self.pb_main_QiandaoSystem = QtWidgets.QPushButton(self.fr_main_menu)
        self.pb_main_QiandaoSystem.setGeometry(QtCore.QRect(190, 10, 141, 111))
        self.pb_main_QiandaoSystem.setObjectName("pb_main_QiandaoSystem")
        self.pb_main_CoachSystem = QtWidgets.QPushButton(self.fr_main_menu)
        self.pb_main_CoachSystem.setGeometry(QtCore.QRect(660, 10, 141, 111))
        self.pb_main_CoachSystem.setObjectName("pb_main_CoachSystem")
        self.pb_main_StatisticSystem = QtWidgets.QPushButton(self.fr_main_menu)
        self.pb_main_StatisticSystem.setGeometry(QtCore.QRect(820, 10, 141, 111))
        self.pb_main_StatisticSystem.setObjectName("pb_main_StatisticSystem")
        self.pb_main_CangkuSystem = QtWidgets.QPushButton(self.fr_main_menu)
        self.pb_main_CangkuSystem.setGeometry(QtCore.QRect(980, 10, 131, 111))
        self.pb_main_CangkuSystem.setObjectName("pb_main_CangkuSystem")
        self.pb_main_EvaluationSystem = QtWidgets.QPushButton(self.fr_main_menu)
        self.pb_main_EvaluationSystem.setGeometry(QtCore.QRect(1130, 10, 131, 111))
        self.pb_main_EvaluationSystem.setObjectName("pb_main_EvaluationSystem")
        self.fr_main_show = QtWidgets.QFrame(self.centralwidget)
        self.fr_main_show.setGeometry(QtCore.QRect(10, 150, 1291, 651))
        self.fr_main_show.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_main_show.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_main_show.setObjectName("fr_main_show")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.fr_main_show)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1291, 651))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.Layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.setObjectName("Layout")
        self.fr_main_bottom = QtWidgets.QFrame(self.centralwidget)
        self.fr_main_bottom.setGeometry(QtCore.QRect(10, 810, 1291, 31))
        self.fr_main_bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_main_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_main_bottom.setObjectName("fr_main_bottom")
        self.lb_main_time = QtWidgets.QLabel(self.fr_main_bottom)
        self.lb_main_time.setGeometry(QtCore.QRect(1130, 10, 161, 20))
        self.lb_main_time.setScaledContents(True)
        self.lb_main_time.setObjectName("lb_main_time")
        self.lb_main_username = QtWidgets.QLabel(self.fr_main_bottom)
        self.lb_main_username.setGeometry(QtCore.QRect(10, 10, 151, 16))
        self.lb_main_username.setObjectName("lb_main_username")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1314, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_pwd = QtWidgets.QAction(MainWindow)
        self.action_pwd.setObjectName("action_pwd")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_info = QtWidgets.QAction(MainWindow)
        self.action_info.setObjectName("action_info")
        self.action_verify = QtWidgets.QAction(MainWindow)
        self.action_verify.setObjectName("action_verify")
        self.action_close = QtWidgets.QAction(MainWindow)
        self.action_close.setObjectName("action_close")
        self.menu.addAction(self.action_pwd)
        self.menu.addAction(self.action_verify)
        self.menu.addSeparator()
        self.menu.addAction(self.action_close)
        self.menu_3.addAction(self.action_info)
        self.menu_3.addSeparator()
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pb_main_StudentSystem.setText(_translate("MainWindow", "学员系统"))
        self.pb_main_NewMemberSystem.setText(_translate("MainWindow", "录入系统"))
        self.pb_main_LessonSystem.setText(_translate("MainWindow", "排课系统"))
        self.pb_main_QiandaoSystem.setText(_translate("MainWindow", "签到系统"))
        self.pb_main_CoachSystem.setText(_translate("MainWindow", "教练系统"))
        self.pb_main_StatisticSystem.setText(_translate("MainWindow", "统计系统"))
        self.pb_main_CangkuSystem.setText(_translate("MainWindow", "仓库管理"))
        self.pb_main_EvaluationSystem.setText(_translate("MainWindow", "课后评价"))
        self.lb_main_time.setText(_translate("MainWindow", "时间在此显示"))
        self.lb_main_username.setText(_translate("MainWindow", "当前用户：某某"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.menu_3.setTitle(_translate("MainWindow", "关于"))
        self.action_pwd.setText(_translate("MainWindow", "修改密码"))
        self.action_3.setText(_translate("MainWindow", "人脸识别"))
        self.action_5.setText(_translate("MainWindow", "数据库调试"))
        self.action_info.setText(_translate("MainWindow", "基本信息"))
        self.action_verify.setText(_translate("MainWindow", "修改二级密码"))
        self.action_close.setText(_translate("MainWindow", "关闭"))

