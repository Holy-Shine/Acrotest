# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\waibaoTest\SummarySystem\sumSys.ui'
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
        item = QtWidgets.QListWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resource/fluid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.listFunc.addItem(item)
        self.label_13 = QtWidgets.QLabel(self.left_widget)
        self.label_13.setGeometry(QtCore.QRect(40, 20, 81, 21))
        self.label_13.setStyleSheet("font: 75 14pt \"黑体\";")
        self.label_13.setObjectName("label_13")
        self.stackedWidget = QtWidgets.QStackedWidget(sumSys)
        self.stackedWidget.setGeometry(QtCore.QRect(200, 60, 1061, 551))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 141, 31))
        self.label_3.setStyleSheet("font: 75 14pt \"黑体\";")
        self.label_3.setObjectName("label_3")
        self.gb_banka = QtWidgets.QGroupBox(self.page)
        self.gb_banka.setGeometry(QtCore.QRect(30, 110, 391, 411))
        self.gb_banka.setObjectName("gb_banka")
        self.gb_bankhis = QtWidgets.QGroupBox(self.page)
        self.gb_bankhis.setGeometry(QtCore.QRect(439, 110, 601, 411))
        self.gb_bankhis.setObjectName("gb_bankhis")
        self.groupBox = QtWidgets.QGroupBox(self.page)
        self.groupBox.setGeometry(QtCore.QRect(30, 40, 391, 61))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 371, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.cb_bar_year = QtWidgets.QComboBox(self.layoutWidget)
        self.cb_bar_year.setObjectName("cb_bar_year")
        self.cb_bar_year.addItem("")
        self.cb_bar_year.addItem("")
        self.cb_bar_year.addItem("")
        self.gridLayout.addWidget(self.cb_bar_year, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.cb_bar_month = QtWidgets.QComboBox(self.layoutWidget)
        self.cb_bar_month.setObjectName("cb_bar_month")
        self.cb_bar_month.addItem("")
        self.cb_bar_month.addItem("")
        self.cb_bar_month.addItem("")
        self.cb_bar_month.addItem("")
        self.cb_bar_month.addItem("")
        self.cb_bar_month.addItem("")
        self.cb_bar_month.addItem("")
        self.cb_bar_month.addItem("")
        self.cb_bar_month.addItem("")
        self.cb_bar_month.addItem("")
        self.cb_bar_month.addItem("")
        self.cb_bar_month.addItem("")
        self.gridLayout.addWidget(self.cb_bar_month, 0, 3, 1, 1)
        self.btn_show_bar = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_show_bar.setObjectName("btn_show_bar")
        self.gridLayout.addWidget(self.btn_show_bar, 0, 4, 1, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.page)
        self.groupBox_6.setGeometry(QtCore.QRect(440, 40, 601, 61))
        self.groupBox_6.setObjectName("groupBox_6")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_6)
        self.layoutWidget1.setGeometry(QtCore.QRect(18, 20, 571, 30))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.cb_show_num_month = QtWidgets.QComboBox(self.layoutWidget1)
        self.cb_show_num_month.setObjectName("cb_show_num_month")
        self.cb_show_num_month.addItem("")
        self.cb_show_num_month.addItem("")
        self.cb_show_num_month.addItem("")
        self.cb_show_num_month.addItem("")
        self.gridLayout_7.addWidget(self.cb_show_num_month, 0, 0, 1, 1)
        self.btn_show_BXline = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_show_BXline.setObjectName("btn_show_BXline")
        self.gridLayout_7.addWidget(self.btn_show_BXline, 0, 1, 1, 1)
        self.gridLayout_7.setColumnStretch(0, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(10, 0, 141, 31))
        self.label_4.setStyleSheet("font: 75 14pt \"黑体\";")
        self.label_4.setObjectName("label_4")
        self.gb_money = QtWidgets.QGroupBox(self.page_2)
        self.gb_money.setGeometry(QtCore.QRect(30, 110, 831, 421))
        self.gb_money.setObjectName("gb_money")
        self.groupBox_7 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_7.setGeometry(QtCore.QRect(30, 40, 601, 61))
        self.groupBox_7.setObjectName("groupBox_7")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_7)
        self.layoutWidget2.setGeometry(QtCore.QRect(18, 20, 571, 30))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.cb_show_num_month_money = QtWidgets.QComboBox(self.layoutWidget2)
        self.cb_show_num_month_money.setObjectName("cb_show_num_month_money")
        self.cb_show_num_month_money.addItem("")
        self.cb_show_num_month_money.addItem("")
        self.cb_show_num_month_money.addItem("")
        self.cb_show_num_month_money.addItem("")
        self.gridLayout_8.addWidget(self.cb_show_num_month_money, 0, 0, 1, 1)
        self.btn_show_MoneyLine = QtWidgets.QPushButton(self.layoutWidget2)
        self.btn_show_MoneyLine.setObjectName("btn_show_MoneyLine")
        self.gridLayout_8.addWidget(self.btn_show_MoneyLine, 0, 1, 1, 1)
        self.gridLayout_8.setColumnStretch(0, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_2.setGeometry(QtCore.QRect(50, 40, 451, 80))
        self.groupBox_2.setObjectName("groupBox_2")
        self.widget = QtWidgets.QWidget(self.groupBox_2)
        self.widget.setGeometry(QtCore.QRect(20, 30, 411, 23))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.cb_fluid_year = QtWidgets.QComboBox(self.widget)
        self.cb_fluid_year.setObjectName("cb_fluid_year")
        self.gridLayout_2.addWidget(self.cb_fluid_year, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 2, 1, 1)
        from SummarySystem.myUI import ComboCheckBox
        items = ['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']
        self.cb_fluid_month = ComboCheckBox(items, self.widget)
        self.cb_fluid_month.setObjectName("cb_fluid_month")
        self.gridLayout_2.addWidget(self.cb_fluid_month, 0, 3, 1, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(3, 1)
        self.tv_fluid = QtWidgets.QTableView(self.page_3)
        self.tv_fluid.setGeometry(QtCore.QRect(45, 131, 961, 381))
        self.tv_fluid.setObjectName("tv_fluid")
        self.groupBox_3 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_3.setGeometry(QtCore.QRect(520, 40, 481, 80))
        self.groupBox_3.setObjectName("groupBox_3")
        self.widget1 = QtWidgets.QWidget(self.groupBox_3)
        self.widget1.setGeometry(QtCore.QRect(40, 17, 411, 51))
        self.widget1.setObjectName("widget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn_fluid_excrt = QtWidgets.QPushButton(self.widget1)
        self.btn_fluid_excrt.setObjectName("btn_fluid_excrt")
        self.gridLayout_3.addWidget(self.btn_fluid_excrt, 0, 1, 1, 1)
        self.btn_fluid_expall = QtWidgets.QPushButton(self.widget1)
        self.btn_fluid_expall.setObjectName("btn_fluid_expall")
        self.gridLayout_3.addWidget(self.btn_fluid_expall, 0, 2, 1, 1)
        self.btn_fluid_getDB = QtWidgets.QPushButton(self.widget1)
        self.btn_fluid_getDB.setObjectName("btn_fluid_getDB")
        self.gridLayout_3.addWidget(self.btn_fluid_getDB, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.page_3)
        self.label_7.setGeometry(QtCore.QRect(10, 0, 141, 31))
        self.label_7.setStyleSheet("font: 75 14pt \"黑体\";")
        self.label_7.setObjectName("label_7")
        self.stackedWidget.addWidget(self.page_3)
        self.lb_head = QtWidgets.QLabel(sumSys)
        self.lb_head.setGeometry(QtCore.QRect(530, 20, 431, 41))
        self.lb_head.setStyleSheet("font: 75 28pt \"楷体\";")
        self.lb_head.setObjectName("lb_head")

        self.retranslateUi(sumSys)
        self.stackedWidget.setCurrentIndex(2)
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
        item = self.listFunc.item(2)
        item.setText(_translate("sumSys", "办卡续卡流水"))
        self.listFunc.setSortingEnabled(__sortingEnabled)
        self.label_13.setText(_translate("sumSys", "菜单栏"))
        self.label_3.setText(_translate("sumSys", "办卡续卡统计"))
        self.gb_banka.setTitle(_translate("sumSys", "某月的办卡续卡人数"))
        self.gb_bankhis.setTitle(_translate("sumSys", "近几个月的办卡续卡人数趋势"))
        self.groupBox.setTitle(_translate("sumSys", "选择展示的年月"))
        self.label.setText(_translate("sumSys", "年："))
        self.cb_bar_year.setItemText(0, _translate("sumSys", "2019"))
        self.cb_bar_year.setItemText(1, _translate("sumSys", "2020"))
        self.cb_bar_year.setItemText(2, _translate("sumSys", "2021"))
        self.label_2.setText(_translate("sumSys", "月："))
        self.cb_bar_month.setItemText(0, _translate("sumSys", "1"))
        self.cb_bar_month.setItemText(1, _translate("sumSys", "2"))
        self.cb_bar_month.setItemText(2, _translate("sumSys", "3"))
        self.cb_bar_month.setItemText(3, _translate("sumSys", "4"))
        self.cb_bar_month.setItemText(4, _translate("sumSys", "5"))
        self.cb_bar_month.setItemText(5, _translate("sumSys", "6"))
        self.cb_bar_month.setItemText(6, _translate("sumSys", "7"))
        self.cb_bar_month.setItemText(7, _translate("sumSys", "8"))
        self.cb_bar_month.setItemText(8, _translate("sumSys", "9"))
        self.cb_bar_month.setItemText(9, _translate("sumSys", "10"))
        self.cb_bar_month.setItemText(10, _translate("sumSys", "11"))
        self.cb_bar_month.setItemText(11, _translate("sumSys", "12"))
        self.btn_show_bar.setText(_translate("sumSys", "展示"))
        self.groupBox_6.setTitle(_translate("sumSys", "选择显示多少个月"))
        self.cb_show_num_month.setItemText(0, _translate("sumSys", "3个月"))
        self.cb_show_num_month.setItemText(1, _translate("sumSys", "6个月"))
        self.cb_show_num_month.setItemText(2, _translate("sumSys", "9个月"))
        self.cb_show_num_month.setItemText(3, _translate("sumSys", "12个月"))
        self.btn_show_BXline.setText(_translate("sumSys", "展示"))
        self.label_4.setText(_translate("sumSys", "营业额统计"))
        self.gb_money.setTitle(_translate("sumSys", "点线图展示"))
        self.groupBox_7.setTitle(_translate("sumSys", "选择显示多少个月"))
        self.cb_show_num_month_money.setItemText(0, _translate("sumSys", "3个月"))
        self.cb_show_num_month_money.setItemText(1, _translate("sumSys", "6个月"))
        self.cb_show_num_month_money.setItemText(2, _translate("sumSys", "9个月"))
        self.cb_show_num_month_money.setItemText(3, _translate("sumSys", "12个月"))
        self.btn_show_MoneyLine.setText(_translate("sumSys", "展示"))
        self.groupBox_2.setTitle(_translate("sumSys", "选择栏(默认可选近3年的流水)"))
        self.label_5.setText(_translate("sumSys", "年："))
        self.label_6.setText(_translate("sumSys", "月："))
        self.groupBox_3.setTitle(_translate("sumSys", "操作栏"))
        self.btn_fluid_excrt.setText(_translate("sumSys", "导出当前流水"))
        self.btn_fluid_expall.setText(_translate("sumSys", "导出全部流水"))
        self.btn_fluid_getDB.setText(_translate("sumSys", "获取数据库流水信息"))
        self.label_7.setText(_translate("sumSys", "办卡续卡流水"))
        self.lb_head.setText(_translate("sumSys", "统 计 系 统"))
