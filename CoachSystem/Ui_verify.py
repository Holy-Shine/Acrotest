# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\waibaoTest\CoachSystem\verify.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_verify(object):
    def setupUi(self, verify):
        verify.setObjectName("verify")
        verify.resize(399, 121)
        verify.setMinimumSize(QtCore.QSize(399, 121))
        verify.setMaximumSize(QtCore.QSize(399, 16777215))
        self.layoutWidget = QtWidgets.QWidget(verify)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 355, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.btn_confirm = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_confirm.setObjectName("btn_confirm")
        self.gridLayout.addWidget(self.btn_confirm, 0, 2, 1, 1)
        self.le_pwd = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_pwd.setObjectName("le_pwd")
        self.gridLayout.addWidget(self.le_pwd, 0, 1, 1, 1)

        self.retranslateUi(verify)
        QtCore.QMetaObject.connectSlotsByName(verify)

    def retranslateUi(self, verify):
        _translate = QtCore.QCoreApplication.translate
        verify.setWindowTitle(_translate("verify", "Dialog"))
        self.label.setText(_translate("verify", "二级密码："))
        self.btn_confirm.setText(_translate("verify", "确认"))
