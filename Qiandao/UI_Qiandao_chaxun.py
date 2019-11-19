# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qiandao_chaxun.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class UIQiandaoChaxun(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1291, 651)
        Form.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(330, 90, 421, 31))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"宋体\";")
        self.textEdit.setObjectName("textEdit")
        self.lb_topline = QtWidgets.QLabel(Form)
        self.lb_topline.setGeometry(QtCore.QRect(450, 20, 361, 41))
        self.lb_topline.setStyleSheet("font: 75 28pt \"楷体\";")
        self.lb_topline.setObjectName("lb_topline")
        self.bt_select = QtWidgets.QPushButton(Form)
        self.bt_select.setGeometry(QtCore.QRect(800, 80, 91, 41))
        self.bt_select.setObjectName("bt_select")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(300, 140, 681, 491))
        self.groupBox.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.groupBox.setObjectName("groupBox")
        self.lb_name = QtWidgets.QLabel(self.groupBox)
        self.lb_name.setGeometry(QtCore.QRect(40, 80, 81, 31))
        self.lb_name.setStyleSheet("font: 14pt \"宋体\";")
        self.lb_name.setObjectName("lb_name")
        self.lb_nameinfo = QtWidgets.QLabel(self.groupBox)
        self.lb_nameinfo.setGeometry(QtCore.QRect(150, 90, 131, 21))
        self.lb_nameinfo.setStyleSheet("background-color: rgb(152, 152, 152);\n"
"font: 14pt \"楷体\";")
        self.lb_nameinfo.setObjectName("lb_nameinfo")
        self.lb_date = QtWidgets.QLabel(self.groupBox)
        self.lb_date.setGeometry(QtCore.QRect(40, 160, 81, 20))
        self.lb_date.setStyleSheet("font: 14pt \"宋体\";")
        self.lb_date.setObjectName("lb_date")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(340, 10, 260, 390))
        self.label.setStyleSheet("background-color: rgb(172, 172, 172);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.bt_trackback = QtWidgets.QPushButton(self.groupBox)
        self.bt_trackback.setGeometry(QtCore.QRect(410, 410, 101, 51))
        self.bt_trackback.setObjectName("bt_trackback")
        self.bt_qiandao_confrim = QtWidgets.QPushButton(self.groupBox)
        self.bt_qiandao_confrim.setGeometry(QtCore.QRect(140, 410, 101, 51))
        self.bt_qiandao_confrim.setObjectName("bt_qiandao_confrim")
        self.lb_coach = QtWidgets.QLabel(self.groupBox)
        self.lb_coach.setGeometry(QtCore.QRect(40, 230, 81, 20))
        self.lb_coach.setStyleSheet("font: 14pt \"宋体\";")
        self.lb_coach.setObjectName("lb_coach")
        self.lb_rest = QtWidgets.QLabel(self.groupBox)
        self.lb_rest.setGeometry(QtCore.QRect(40, 300, 81, 20))
        self.lb_rest.setStyleSheet("font: 14pt \"宋体\";")
        self.lb_rest.setObjectName("lb_rest")
        self.lb_dateinfo = QtWidgets.QLabel(self.groupBox)
        self.lb_dateinfo.setGeometry(QtCore.QRect(150, 160, 131, 21))
        self.lb_dateinfo.setStyleSheet("background-color: rgb(152, 152, 152);\n"
"font: 14pt \"楷体\";")
        self.lb_dateinfo.setObjectName("lb_dateinfo")
        self.lb_coach_info = QtWidgets.QLabel(self.groupBox)
        self.lb_coach_info.setGeometry(QtCore.QRect(150, 230, 131, 20))
        self.lb_coach_info.setStyleSheet("background-color: rgb(152, 152, 152);\n"
"font: 14pt \"楷体\";")
        self.lb_coach_info.setObjectName("lb_coach_info")
        self.lb_restinfo = QtWidgets.QLabel(self.groupBox)
        self.lb_restinfo.setGeometry(QtCore.QRect(150, 300, 131, 21))
        self.lb_restinfo.setStyleSheet("background-color: rgb(152, 152, 152);\n"
"font: 14pt \"楷体\";")
        self.lb_restinfo.setObjectName("lb_restinfo")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'宋体\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.lb_topline.setText(_translate("Form", "查 询 签 到 系 统"))
        self.bt_select.setText(_translate("Form", "查询"))
        self.groupBox.setTitle(_translate("Form", "签到信息"))
        self.lb_name.setText(_translate("Form", "学生姓名"))
        self.lb_nameinfo.setText(_translate("Form", "暂无"))
        self.lb_date.setText(_translate("Form", "上课时间"))
        self.bt_trackback.setText(_translate("Form", "返回"))
        self.bt_qiandao_confrim.setText(_translate("Form", "确认签到"))
        self.lb_coach.setText(_translate("Form", "教练姓名"))
        self.lb_rest.setText(_translate("Form", "剩余次数"))
        self.lb_dateinfo.setText(_translate("Form", "暂无"))
        self.lb_coach_info.setText(_translate("Form", "暂无"))
        self.lb_restinfo.setText(_translate("Form", "暂无"))

