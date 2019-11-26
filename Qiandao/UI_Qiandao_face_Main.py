# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qiandao_face_Main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class UIQiandaoFace(object):
    def setupUi(self, UIQiandaoFace):
        UIQiandaoFace.setObjectName("UIQiandaoFace")
        UIQiandaoFace.resize(1291, 651)
        UIQiandaoFace.setToolTipDuration(-1)
        UIQiandaoFace.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.lb_toplabel = QtWidgets.QLabel(UIQiandaoFace)
        self.lb_toplabel.setGeometry(QtCore.QRect(440, 20, 401, 51))
        self.lb_toplabel.setStyleSheet("font: 75 28pt \"楷体\";")
        self.lb_toplabel.setTextFormat(QtCore.Qt.AutoText)
        self.lb_toplabel.setObjectName("lb_toplabel")
        self.GB_qiandao = QtWidgets.QGroupBox(UIQiandaoFace)
        self.GB_qiandao.setGeometry(QtCore.QRect(530, 70, 641, 531))
        self.GB_qiandao.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.GB_qiandao.setObjectName("GB_qiandao")
        self.lb_name = QtWidgets.QLabel(self.GB_qiandao)
        self.lb_name.setGeometry(QtCore.QRect(40, 80, 81, 31))
        self.lb_name.setStyleSheet("font: 14pt \"宋体\";")
        self.lb_name.setObjectName("lb_name")
        self.lb_nameinfo = QtWidgets.QLabel(self.GB_qiandao)
        self.lb_nameinfo.setGeometry(QtCore.QRect(150, 90, 131, 21))
        self.lb_nameinfo.setStyleSheet("background-color: rgb(152, 152, 152);\n"
"font: 14pt \"楷体\";")
        self.lb_nameinfo.setObjectName("lb_nameinfo")
        self.lb_date = QtWidgets.QLabel(self.GB_qiandao)
        self.lb_date.setGeometry(QtCore.QRect(40, 160, 81, 20))
        self.lb_date.setStyleSheet("font: 14pt \"宋体\";")
        self.lb_date.setObjectName("lb_date")
        self.label = QtWidgets.QLabel(self.GB_qiandao)
        self.label.setGeometry(QtCore.QRect(330, 30, 260, 346))
        self.label.setStyleSheet("background-color: rgb(172, 172, 172);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.bt_trackback = QtWidgets.QPushButton(self.GB_qiandao)
        self.bt_trackback.setGeometry(QtCore.QRect(390, 440, 101, 51))
        self.bt_trackback.setObjectName("bt_trackback")
        self.bt_qiandao_confrim = QtWidgets.QPushButton(self.GB_qiandao)
        self.bt_qiandao_confrim.setGeometry(QtCore.QRect(130, 440, 101, 51))
        self.bt_qiandao_confrim.setObjectName("bt_qiandao_confrim")
        self.lb_coach = QtWidgets.QLabel(self.GB_qiandao)
        self.lb_coach.setGeometry(QtCore.QRect(40, 230, 81, 20))
        self.lb_coach.setStyleSheet("font: 14pt \"宋体\";")
        self.lb_coach.setObjectName("lb_coach")
        self.lb_rest = QtWidgets.QLabel(self.GB_qiandao)
        self.lb_rest.setGeometry(QtCore.QRect(40, 300, 81, 20))
        self.lb_rest.setStyleSheet("font: 14pt \"宋体\";")
        self.lb_rest.setObjectName("lb_rest")
        self.lb_dateinfo = QtWidgets.QLabel(self.GB_qiandao)
        self.lb_dateinfo.setGeometry(QtCore.QRect(150, 160, 131, 21))
        self.lb_dateinfo.setStyleSheet("background-color: rgb(152, 152, 152);\n"
"font: 14pt \"楷体\";")
        self.lb_dateinfo.setObjectName("lb_dateinfo")
        self.lb_coach_info = QtWidgets.QLabel(self.GB_qiandao)
        self.lb_coach_info.setGeometry(QtCore.QRect(150, 230, 131, 20))
        self.lb_coach_info.setStyleSheet("background-color: rgb(152, 152, 152);\n"
"font: 14pt \"楷体\";")
        self.lb_coach_info.setObjectName("lb_coach_info")
        self.lb_restinfo = QtWidgets.QLabel(self.GB_qiandao)
        self.lb_restinfo.setGeometry(QtCore.QRect(150, 300, 131, 21))
        self.lb_restinfo.setStyleSheet("background-color: rgb(152, 152, 152);\n"
"font: 14pt \"楷体\";")
        self.lb_restinfo.setObjectName("lb_restinfo")
        self.GBstudent = QtWidgets.QGroupBox(UIQiandaoFace)
        self.GBstudent.setGeometry(QtCore.QRect(100, 70, 411, 541))
        self.GBstudent.setTitle("")
        self.GBstudent.setObjectName("GBstudent")
        self.tableView = QtWidgets.QTableView(self.GBstudent)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 391, 521))
        self.tableView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableView.setObjectName("tableView")

        self.retranslateUi(UIQiandaoFace)
        QtCore.QMetaObject.connectSlotsByName(UIQiandaoFace)

    def retranslateUi(self, UIQiandaoFace):
        _translate = QtCore.QCoreApplication.translate
        UIQiandaoFace.setWindowTitle(_translate("UIQiandaoFace", "Form"))
        self.lb_toplabel.setText(_translate("UIQiandaoFace", "学 生 签 到 系 统 "))
        self.GB_qiandao.setTitle(_translate("UIQiandaoFace", "签到信息"))
        self.lb_name.setText(_translate("UIQiandaoFace", "学生姓名"))
        self.lb_nameinfo.setText(_translate("UIQiandaoFace", "暂无"))
        self.lb_date.setText(_translate("UIQiandaoFace", "上课时间"))
        self.bt_trackback.setText(_translate("UIQiandaoFace", "返回"))
        self.bt_qiandao_confrim.setText(_translate("UIQiandaoFace", "确认签到"))
        self.lb_coach.setText(_translate("UIQiandaoFace", "教练姓名"))
        self.lb_rest.setText(_translate("UIQiandaoFace", "剩余次数"))
        self.lb_dateinfo.setText(_translate("UIQiandaoFace", "暂无"))
        self.lb_coach_info.setText(_translate("UIQiandaoFace", "暂无"))
        self.lb_restinfo.setText(_translate("UIQiandaoFace", "暂无"))

