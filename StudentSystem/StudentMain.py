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
        StudentMain.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.groupBox = QtWidgets.QGroupBox(StudentMain)
        self.groupBox.setGeometry(QtCore.QRect(60, 40, 751, 591))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.table_studentList = QtWidgets.QTableView(self.groupBox)
        self.table_studentList.setGeometry(QtCore.QRect(10, 20, 721, 561))
        self.table_studentList.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table_studentList.setObjectName("table_studentList")
        self.groupBox_2 = QtWidgets.QGroupBox(StudentMain)
        self.groupBox_2.setGeometry(QtCore.QRect(830, 50, 381, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.et_query = QtWidgets.QLineEdit(self.groupBox_2)
        self.et_query.setGeometry(QtCore.QRect(40, 30, 191, 31))
        self.et_query.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.et_query.setObjectName("et_query")
        self.bt_query = QtWidgets.QPushButton(self.groupBox_2)
        self.bt_query.setGeometry(QtCore.QRect(260, 30, 71, 31))
        self.bt_query.setObjectName("bt_query")
        self.groupBox_3 = QtWidgets.QGroupBox(StudentMain)
        self.groupBox_3.setGeometry(QtCore.QRect(820, 170, 391, 111))
        self.groupBox_3.setObjectName("groupBox_3")
        self.st_studentInfo = QtWidgets.QPushButton(self.groupBox_3)
        self.st_studentInfo.setGeometry(QtCore.QRect(60, 30, 101, 51))
        self.st_studentInfo.setObjectName("st_studentInfo")
        self.btstuclass = QtWidgets.QPushButton(self.groupBox_3)
        self.btstuclass.setGeometry(QtCore.QRect(240, 30, 101, 51))
        self.btstuclass.setObjectName("btstuclass")

        self.retranslateUi(StudentMain)
        QtCore.QMetaObject.connectSlotsByName(StudentMain)

    def retranslateUi(self, StudentMain):
        _translate = QtCore.QCoreApplication.translate
        StudentMain.setWindowTitle(_translate("StudentMain", "Form"))
        self.groupBox_2.setTitle(_translate("StudentMain", "查询"))
        self.bt_query.setText(_translate("StudentMain", "查询"))
        self.groupBox_3.setTitle(_translate("StudentMain", "功能菜单"))
        self.st_studentInfo.setText(_translate("StudentMain", "学生信息"))
        self.btstuclass.setText(_translate("StudentMain", "排课信息"))

