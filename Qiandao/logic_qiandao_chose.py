from PyQt5.QtWidgets import QDialog,QMessageBox,QLineEdit,QApplication

from UI_Qiandao_chose import Ui_qiandao_chose
from logic_Qiandao_chaxun import LogicQiandaoChaxun
from logic_qiandao_camera import LogicQiandaoCamrea

from process_camera_info import Camera
import os,sys

class LogicQiandaoChose(Ui_qiandao_chose,QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.chaxun = LogicQiandaoChaxun()

        self.camera = Camera()
        self.slot_init()

    def slot_init(self):
        self.bt_secletqiandao.clicked.connect(self.open_select_qiandao)
        self.bt_faceqiandao.clicked.connect(self.open_face_qiandao)
        self.cameranum =self.camera.get_cam_num()
        self.facechaxun = LogicQiandaoCamrea(self.cameranum)


    def open_select_qiandao(self):
        self.close()
        self.chaxun.show()

    def open_face_qiandao(self):
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