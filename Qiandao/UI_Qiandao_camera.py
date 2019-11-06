# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Qiandao_CAMERA.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class UI_Qiandao_camera(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(271, 65)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(100, 20, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(33, 20, 71, 20))
        self.label.setObjectName("label")
        self.bt_confrim = QtWidgets.QPushButton(Form)
        self.bt_confrim.setGeometry(QtCore.QRect(190, 20, 51, 23))
        self.bt_confrim.setObjectName("bt_confrim")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "选择摄像头"))
        self.bt_confrim.setText(_translate("Form", "确定"))

