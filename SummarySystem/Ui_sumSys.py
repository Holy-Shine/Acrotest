# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\waibao\ImgDisplay\sumSys.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sumSys(object):
    def setupUi(self, sumSys):
        sumSys.setObjectName("sumSys")
        sumSys.resize(1291, 651)
        sumSys.setMinimumSize(QtCore.QSize(1291, 651))
        sumSys.setMaximumSize(QtCore.QSize(1291, 651))
        self.left_widget = QtWidgets.QWidget(sumSys)
        self.left_widget.setGeometry(QtCore.QRect(0, 0, 161, 661))
        self.left_widget.setStyleSheet("background:#DDDDDD")
        self.left_widget.setObjectName("left_widget")
        self.listFunc = QtWidgets.QListWidget(self.left_widget)
        self.listFunc.setGeometry(QtCore.QRect(10, 60, 131, 441))
        self.listFunc.setStyleSheet("QListWidget#listFunc{\n"
"    outline: 0px;\n"
"    border:0px;\n"
"    min-width: 120px;\n"
"    color: Black;\n"
"    background: #DDDDDD;\n"
"}\n"
"\n"
"QListWidget#listFunc::Item{\n"
"     height:30px;\n"
"}\n"
"QListWidget#listFunc::Item:selected {\n"
"    background: rgb(49, 194, 124);\n"
"    border-radius:1.5px;\n"
"   \n"
"}\n"
"")
        self.listFunc.setObjectName("listFunc")
        item = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource/card.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        self.listFunc.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resource/money.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.listFunc.addItem(item)
        self.label_13 = QtWidgets.QLabel(self.left_widget)
        self.label_13.setGeometry(QtCore.QRect(40, 20, 81, 21))
        self.label_13.setStyleSheet("font: 75 14pt \"黑体\";")
        self.label_13.setObjectName("label_13")
        self.stackedWidget = QtWidgets.QStackedWidget(sumSys)
        self.stackedWidget.setGeometry(QtCore.QRect(200, 60, 881, 521))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 141, 31))
        self.label_3.setStyleSheet("font: 75 14pt \"黑体\";")
        self.label_3.setObjectName("label_3")
        self.gb_banka = QtWidgets.QGroupBox(self.page)
        self.gb_banka.setGeometry(QtCore.QRect(30, 80, 831, 451))
        self.gb_banka.setObjectName("gb_banka")
        self.btn_show = QtWidgets.QPushButton(self.page)
        self.btn_show.setGeometry(QtCore.QRect(50, 40, 93, 28))
        self.btn_show.setObjectName("btn_show")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.btn_show_money = QtWidgets.QPushButton(self.page_2)
        self.btn_show_money.setGeometry(QtCore.QRect(50, 40, 93, 28))
        self.btn_show_money.setObjectName("btn_show_money")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(10, 0, 141, 31))
        self.label_4.setStyleSheet("font: 75 14pt \"黑体\";")
        self.label_4.setObjectName("label_4")
        self.gb_money = QtWidgets.QGroupBox(self.page_2)
        self.gb_money.setGeometry(QtCore.QRect(30, 80, 831, 451))
        self.gb_money.setObjectName("gb_money")
        self.stackedWidget.addWidget(self.page_2)
        self.lb_head = QtWidgets.QLabel(sumSys)
        self.lb_head.setGeometry(QtCore.QRect(530, 20, 431, 41))
        self.lb_head.setStyleSheet("font: 75 28pt \"楷体\";")
        self.lb_head.setObjectName("lb_head")

        self.retranslateUi(sumSys)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(sumSys)

    def retranslateUi(self, sumSys):
        _translate = QtCore.QCoreApplication.translate
        sumSys.setWindowTitle(_translate("sumSys", "统计系统"))
        __sortingEnabled = self.listFunc.isSortingEnabled()
        self.listFunc.setSortingEnabled(False)
        item = self.listFunc.item(0)
        item.setText(_translate("sumSys", "办卡续卡统计"))
        item = self.listFunc.item(1)
        item.setText(_translate("sumSys", "营业额统计"))
        self.listFunc.setSortingEnabled(__sortingEnabled)
        self.label_13.setText(_translate("sumSys", "菜单栏"))
        self.label_3.setText(_translate("sumSys", "办卡续卡统计"))
        self.gb_banka.setTitle(_translate("sumSys", "直方图展示"))
        self.btn_show.setText(_translate("sumSys", "展示"))
        self.btn_show_money.setText(_translate("sumSys", "展示"))
        self.label_4.setText(_translate("sumSys", "营业额统计"))
        self.gb_money.setTitle(_translate("sumSys", "点线图展示"))
        self.lb_head.setText(_translate("sumSys", "统 计 系 统"))
