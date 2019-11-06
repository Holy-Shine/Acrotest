# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qiandao_chaxun.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class UI_Qiandao_chaxun(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(502, 185)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(90, 90, 171, 31))
        self.textEdit.setObjectName("textEdit")
        self.lb_topline = QtWidgets.QLabel(Form)
        self.lb_topline.setGeometry(QtCore.QRect(170, 40, 111, 20))
        self.lb_topline.setObjectName("lb_topline")
        self.bt_select = QtWidgets.QPushButton(Form)
        self.bt_select.setGeometry(QtCore.QRect(300, 90, 75, 31))
        self.bt_select.setObjectName("bt_select")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">请输入学员姓名</p></body></html>"))
        self.lb_topline.setText(_translate("Form", "查 询 签 到 界 面"))
        self.bt_select.setText(_translate("Form", "查询"))

