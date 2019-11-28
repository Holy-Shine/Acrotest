from PyQt5.QtWidgets import QDialog,QMessageBox,QLineEdit,QApplication

from Qiandao.UI_Qiandao_chose import UiQiandaoChose
from Qiandao.logic_Qiandao_face import LogicQiandaoFace

import os,sys

day = ["周一","周二","周三","周四","周五","周六","周日"]

class LogicQiandaoChose(UiQiandaoChose,QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.init()

        self.slot_init()

    def init(self):
        self.cb_day.addItems(day)
        for i in range(2019,2099):
            self.cb_year.addItem('{}'.format(i))

        for i in range(1,53):
            self.cb_week.addItem('第{}周'.format(i))

        for i in range(10,21):
            self.cb_cam.addItem('{}点'.format(i))


    def slot_init(self):
        # self.bt_confrim.clicked.connect(self.open_face_qiandao)
        self.bt_back.clicked.connect(self.close)


    def open_face_qiandao(self):
        try:
            self.face = LogicQiandaoFace()
            self.face.show()
            self.close()
        except Exception as e:
            print(e)







if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = LogicQiandaoChose()
    login.show()
    sys.exit(app.exec_())