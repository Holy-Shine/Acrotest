from PyQt5.QtWidgets import QDialog,QMessageBox,QLineEdit,QApplication

from UI_Qiandao_chose import UiQiandaoChose
from logic_Qiandao_face import LogicQiandaoFace

import os,sys

day = ["周一","周二","周三","周四","周五","周六","周日"]

class LogicQiandaoChose(UiQiandaoChose,QDialog):
    def __init__(self,camnum):
        super().__init__()
        self.setupUi(self)


        self.camera = camnum
        self.init()

        self.slot_init()

    def init(self):
        self.cb_day.addItems(day)
        for i in range(2019,2099):
            self.cb_year.addItem('{}'.format(i))

        for i in range(1,53):
            self.cb_week.addItem('第{}周'.format(i))

        for i in range(0,self.camera):
            self.cb_cam.addItem('{}'.format(i))

    def slot_init(self):
        self.bt_back.clicked.connect(self.close)


    def open_face_qiandao(self):
        self.face = LogicQiandaoFace()
        if self.cameranum > 0:
            self.facechaxun.show()
            self.close()
        else:
            QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确",
                                          buttons=QMessageBox.Ok,
                                          defaultButton=QMessageBox.Ok)







if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = LogicQiandaoChose()
    login.show()
    sys.exit(app.exec_())