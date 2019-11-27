from PyQt5.QtWidgets import QDialog,QMessageBox,QLineEdit,QApplication

from Qiandao.UI_Qiandao_camera import UIQiandaoCamera
from PyQt5.QtCore import pyqtSignal
import os,sys

class LogicMemberCAMChose(UIQiandaoCamera,QDialog):
    mySignal = pyqtSignal(str)
    def __init__(self,cameranum):
        super().__init__()
        self.setupUi(self)
        self.cameranum = cameranum

        self.init()
        self.slot_init()

    def init(self):
        for i in range(self.cameranum):
            self.comboBox.addItem(str(i))

    def slot_init(self):
        self.bt_confrim.clicked.connect(self.chosecam)

    def chosecam(self):
        content = self.comboBox.currentText()
        self.mySignal.emit(content)  # 发射信
        self.close()