# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\waibao\mainWin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWin(object):
    def setupUi(self, mainWin):
        mainWin.setObjectName("mainWin")
        mainWin.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(mainWin)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_add_user = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add_user.setGeometry(QtCore.QRect(30, 230, 131, 28))
        self.btn_add_user.setObjectName("btn_add_user")
        self.btn_class_update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_class_update.setGeometry(QtCore.QRect(30, 290, 131, 28))
        self.btn_class_update.setObjectName("btn_class_update")
        self.btn_syscoach = QtWidgets.QPushButton(self.centralwidget)
        self.btn_syscoach.setGeometry(QtCore.QRect(50, 350, 93, 28))
        self.btn_syscoach.setObjectName("btn_syscoach")
        mainWin.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWin)
        self.statusbar.setObjectName("statusbar")
        mainWin.setStatusBar(self.statusbar)

        self.retranslateUi(mainWin)
        QtCore.QMetaObject.connectSlotsByName(mainWin)

    def retranslateUi(self, mainWin):
        _translate = QtCore.QCoreApplication.translate
        mainWin.setWindowTitle(_translate("mainWin", "MainWindow"))
        self.btn_add_user.setText(_translate("mainWin", "新用户"))
        self.btn_class_update.setText(_translate("mainWin", "更新排课"))
        self.btn_syscoach.setText(_translate("mainWin", "教练系统"))
