# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\waibao\mainWin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_add_user = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add_user.setGeometry(QtCore.QRect(30, 230, 131, 28))
        self.btn_add_user.setObjectName("btn_add_user")
        self.btn_search_update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search_update.setGeometry(QtCore.QRect(30, 290, 131, 28))
        self.btn_search_update.setObjectName("btn_search_update")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_add_user.setText(_translate("MainWindow", "新用户"))
        self.btn_search_update.setText(_translate("MainWindow", "信息查询更改"))
