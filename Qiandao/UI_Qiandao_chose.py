# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qiandao_chose.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_qiandao_chose(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 150)
        self.bt_secletqiandao = QtWidgets.QPushButton(Form)
        self.bt_secletqiandao.setGeometry(QtCore.QRect(50, 50, 91, 51))
        self.bt_secletqiandao.setObjectName("bt_secletqiandao")
        self.bt_faceqiandao = QtWidgets.QPushButton(Form)
        self.bt_faceqiandao.setGeometry(QtCore.QRect(220, 50, 91, 51))
        self.bt_faceqiandao.setObjectName("bt_faceqiandao")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.bt_secletqiandao.setText(_translate("Form", "查询签到"))
        self.bt_faceqiandao.setText(_translate("Form", "人脸签到"))

