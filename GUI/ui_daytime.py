# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\waibao\daytime.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_classTime(object):
    def setupUi(self, classTime):
        classTime.setObjectName("classTime")
        classTime.resize(341, 88)
        classTime.setMinimumSize(QtCore.QSize(341, 88))
        classTime.setMaximumSize(QtCore.QSize(341, 88))
        self.groupBox = QtWidgets.QGroupBox(classTime)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 321, 61))
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(30, 19, 281, 31))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.cb_daytime = QtWidgets.QComboBox(self.widget)
        self.cb_daytime.setObjectName("cb_daytime")
        self.cb_daytime.addItem("")
        self.cb_daytime.addItem("")
        self.cb_daytime.addItem("")
        self.cb_daytime.addItem("")
        self.cb_daytime.addItem("")
        self.cb_daytime.addItem("")
        self.cb_daytime.addItem("")
        self.cb_daytime.addItem("")
        self.cb_daytime.addItem("")
        self.cb_daytime.addItem("")
        self.cb_daytime.addItem("")
        self.cb_daytime.addItem("")
        self.gridLayout.addWidget(self.cb_daytime, 0, 0, 1, 1)
        self.btn_ok = QtWidgets.QPushButton(self.widget)
        self.btn_ok.setObjectName("btn_ok")
        self.gridLayout.addWidget(self.btn_ok, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)

        self.retranslateUi(classTime)
        QtCore.QMetaObject.connectSlotsByName(classTime)

    def retranslateUi(self, classTime):
        _translate = QtCore.QCoreApplication.translate
        classTime.setWindowTitle(_translate("classTime", "上课时间"))
        self.groupBox.setTitle(_translate("classTime", "选择时间"))
        self.cb_daytime.setItemText(0, _translate("classTime", "10:00"))
        self.cb_daytime.setItemText(1, _translate("classTime", "11:00"))
        self.cb_daytime.setItemText(2, _translate("classTime", "12:00"))
        self.cb_daytime.setItemText(3, _translate("classTime", "13:00"))
        self.cb_daytime.setItemText(4, _translate("classTime", "14:00"))
        self.cb_daytime.setItemText(5, _translate("classTime", "15:00"))
        self.cb_daytime.setItemText(6, _translate("classTime", "16:00"))
        self.cb_daytime.setItemText(7, _translate("classTime", "17:00"))
        self.cb_daytime.setItemText(8, _translate("classTime", "18:00"))
        self.cb_daytime.setItemText(9, _translate("classTime", "19:00"))
        self.cb_daytime.setItemText(10, _translate("classTime", "20:00"))
        self.cb_daytime.setItemText(11, _translate("classTime", "21:00"))
        self.btn_ok.setText(_translate("classTime", "确定"))
