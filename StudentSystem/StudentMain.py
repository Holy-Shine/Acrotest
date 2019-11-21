# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StudentMain.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StudentMain(object):
    def setupUi(self, StudentMain):
        StudentMain.setObjectName("StudentMain")
        StudentMain.resize(1290, 651)
        self.groupBox = QtWidgets.QGroupBox(StudentMain)
        self.groupBox.setGeometry(QtCore.QRect(60, 40, 751, 591))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.tableView = QtWidgets.QTableView(self.groupBox)
        self.tableView.setGeometry(QtCore.QRect(10, 20, 721, 561))
        self.tableView.setObjectName("tableView")
        self.groupBox_2 = QtWidgets.QGroupBox(StudentMain)
        self.groupBox_2.setGeometry(QtCore.QRect(830, 40, 381, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(40, 30, 191, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(260, 30, 71, 31))
        self.pushButton.setObjectName("pushButton")
        self.groupBox_3 = QtWidgets.QGroupBox(StudentMain)
        self.groupBox_3.setGeometry(QtCore.QRect(820, 130, 381, 501))
        self.groupBox_3.setObjectName("groupBox_3")

        self.retranslateUi(StudentMain)
        QtCore.QMetaObject.connectSlotsByName(StudentMain)

    def retranslateUi(self, StudentMain):
        _translate = QtCore.QCoreApplication.translate
        StudentMain.setWindowTitle(_translate("StudentMain", "Form"))
        self.groupBox_2.setTitle(_translate("StudentMain", "查询"))
        self.pushButton.setText(_translate("StudentMain", "PushButton"))
        self.groupBox_3.setTitle(_translate("StudentMain", "预留功能菜单"))

