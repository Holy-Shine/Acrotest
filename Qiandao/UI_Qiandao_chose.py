# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qiandao_chose.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class UiQiandaoChose(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(443, 182)
        Form.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.bt_secletqiandao = QtWidgets.QPushButton(Form)
        self.bt_secletqiandao.setGeometry(QtCore.QRect(70, 60, 121, 61))
        self.bt_secletqiandao.setObjectName("bt_secletqiandao")
        self.bt_faceqiandao = QtWidgets.QPushButton(Form)
        self.bt_faceqiandao.setGeometry(QtCore.QRect(260, 60, 121, 61))
        self.bt_faceqiandao.setObjectName("bt_faceqiandao")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.bt_secletqiandao.setText(_translate("Form", "查询签到"))
        self.bt_faceqiandao.setText(_translate("Form", "人脸签到"))

