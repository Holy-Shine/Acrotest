from PyQt5.QtWidgets import QDialog,QMessageBox,QLineEdit,QApplication
import cv2
from PyQt5 import QtCore,QtGui,QtWidgets

from UI_OldMember import Ui_OldMember
import os,sys



class LogicOldMember(Ui_OldMember,QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)