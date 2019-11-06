from PyQt5.QtWidgets import QDialog,QMessageBox,QLineEdit,QApplication

from UI_Qiandao_chaxun import UI_Qiandao_chaxun
import os,sys


class LogicQiandaoChaxun(UI_Qiandao_chaxun,QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = LogicQiandaoChaxun()
    login.show()
    sys.exit(app.exec_())