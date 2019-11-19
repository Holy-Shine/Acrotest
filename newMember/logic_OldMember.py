from PyQt5.QtWidgets import QDialog,QMessageBox,QLineEdit,QApplication
import cv2
from PyQt5 import QtCore,QtGui,QtWidgets

from UI_OldMember import Ui_OldMember
import os,sys



class LogicOldMember(Ui_OldMember,QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.init()
        self.slot_init()

    def init(self):
        card = ["年卡", "季卡", "次卡"]
        self.cb_card.addItems(card)

        self.clearLineEdit()



    def clearLineEdit(self):
        self.et_cichu.setText('')
        self.et_age.setText('')
        self.et_parent.setText('')
        self.et_money.setText('')

        self.et_cichu.setEnabled(False)
        self.et_age.setEnabled(False)
        self.et_parent.setEnabled(False)
        self.cb_card.setEnabled(False)
        self.et_money.setEnabled(False)

        self.et_cichu.setStyleSheet('background-color: rgb(221, 221, 221);')
        self.et_age.setStyleSheet('background-color: rgb(221, 221, 221);')
        self.et_parent.setStyleSheet('background-color: rgb(221, 221, 221);')
        self.cb_card.setStyleSheet('background-color: rgb(221, 221, 221);')
        self.et_money.setStyleSheet('background-color: rgb(221, 221, 221);')



    def slot_init(self):
        self.pb_query.clicked.connect(self.Info_Query)
        self.bt_confrim.clicked.connect(self.Confrim)
        self.bt_back.clicked.connect(self.Back)

    #信息查询
    def Info_Query(self):
        #当查询到时作以下操作
        self.et_cichu.setEnabled(True)
        self.et_age.setEnabled(True)
        self.et_parent.setEnabled(True)
        self.cb_card.setEnabled(True)
        self.et_money.setEnabled(True)

        self.et_cichu.setStyleSheet('background-color: rgb(255,255, 255);')
        self.et_age.setStyleSheet('background-color: rgb(255,255, 255);')
        self.et_parent.setStyleSheet('background-color: rgb(255,255, 255);')
        self.cb_card.setStyleSheet('background-color: rgb(255,255, 255);')
        self.et_money.setStyleSheet('background-color: rgb(255,255, 255);')
        print(1)

    # 确认
    def Confrim(self):
        print(2)

    # 返回
    def Back(self):
        self.init()
        print(3)