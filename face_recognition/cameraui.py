# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testcamrea.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(672, 506)
        self.opencamrea = QtWidgets.QPushButton(Form)
        self.opencamrea.setGeometry(QtCore.QRect(20, 110, 81, 41))
        self.opencamrea.setObjectName("opencamrea")
        self.cutPic = QtWidgets.QPushButton(Form)
        self.cutPic.setGeometry(QtCore.QRect(20, 210, 81, 41))
        self.cutPic.setObjectName("cutPic")
        self.camera = QtWidgets.QLabel(Form)
        self.camera.setGeometry(QtCore.QRect(150, 40, 54, 12))
        self.camera.setObjectName("camera")
        self.cut_imgshow = QtWidgets.QLabel(Form)
        self.cut_imgshow.setGeometry(QtCore.QRect(100, 300, 54, 12))
        self.cut_imgshow.setObjectName("cut_imgshow")


        self.showinfo = QtWidgets.QLabel(Form)
        self.showinfo.setGeometry(QtCore.QRect(450, 20, 54, 12))
        self.showinfo.setObjectName("showinfo")
        self.showinfo.setFixedSize(140, 105)
        self.showinfo.setAutoFillBackground(False)

        self.showname = QtWidgets.QLabel(Form)
        self.showname.setGeometry(QtCore.QRect(450, 150, 84, 24))

        self.showname.setObjectName("showname")
        self.showsex = QtWidgets.QLabel(Form)
        self.showsex.setGeometry(QtCore.QRect(450, 200, 54, 12))
        self.showsex.setObjectName("showsex")
        self.showage = QtWidgets.QLabel(Form)
        self.showage.setGeometry(QtCore.QRect(450, 250, 54, 12))
        self.showage.setObjectName("showage")


        self.name = QtWidgets.QLabel(Form)
        self.name.setGeometry(QtCore.QRect(290, 300, 31, 20))
        self.name.setObjectName("name")
        self.sex = QtWidgets.QLabel(Form)
        self.sex.setGeometry(QtCore.QRect(290, 350, 41, 20))
        self.sex.setObjectName("sex")
        self.age = QtWidgets.QLabel(Form)
        self.age.setGeometry(QtCore.QRect(290, 390, 41, 20))
        self.age.setObjectName("age")
        self.save = QtWidgets.QPushButton(Form)
        self.save.setGeometry(QtCore.QRect(230, 440, 81, 41))
        self.save.setObjectName("save")


        self.naninput = QtWidgets.QLineEdit(Form)
        self.naninput.setGeometry(QtCore.QRect(330, 300, 113, 20))
        self.naninput.setObjectName("naninput")
        self.ageinput = QtWidgets.QLineEdit(Form)
        self.ageinput.setGeometry(QtCore.QRect(330, 390, 113, 20))
        self.ageinput.setObjectName("ageinput")
        self.inputsex = QtWidgets.QLineEdit(Form)
        self.inputsex.setGeometry(QtCore.QRect(330, 350, 113, 20))
        self.inputsex.setObjectName("inputsex")

        self.ageinput.setVisible(False)
        self.naninput.setVisible(False)
        self.inputsex.setVisible(False)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.opencamrea.setText(_translate("Form", "打开相机"))
        self.cutPic.setText(_translate("Form", "截图识别"))
        self.cutPic.setVisible(False)
        self.camera.setFixedSize(280,210)
        self.camera.setAutoFillBackground(False)
        self.cut_imgshow.setFixedSize(140, 105)
        self.cut_imgshow.setAutoFillBackground(False)
        self.showinfo.setText(_translate("Form", ""))
        self.showname.setText(_translate("Form", ""))
        self.showsex.setText(_translate("Form", ""))
        self.showage.setText(_translate("Form", ""))
        self.name.setText(_translate("Form", "姓名"))
        self.sex.setText(_translate("Form", "性别"))
        self.age.setText(_translate("Form", "年龄"))
        self.save.setText(_translate("Form", "保存"))
        self.save.setVisible(False)
        self.sex.setVisible(False)
        self.name.setVisible(False)
        self.age.setVisible(False)


