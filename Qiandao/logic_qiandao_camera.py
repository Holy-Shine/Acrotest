from PyQt5.QtWidgets import QDialog,QMessageBox,QLineEdit,QApplication


from UI_Qiandao_camera import UI_Qiandao_camera
from logic_Qiandao_face import LogicQiandaoFace
import os,sys


class LogicQiandaoCamrea(UI_Qiandao_camera,QDialog):
    mySignal = pyqtSignal(str)
    def __init__(self,cameranum):
        super().__init__()
        self.setupUi(self)
        self.cameranum = cameranum

        self.face = None
        self.init()
        self.slot_init()

    def init(self):
        for i in range(self.cameranum):
            self.comboBox.addItem(str(i))

    def slot_init(self):
        self.bt_confrim.clicked.connect(self.goto_face)


    #选择摄像头，打开人脸签到界面
    def goto_face(self):

        #此处添加加载特征序列的代码（开子线程完成)
        self.face_featurelist = []

        self.face = LogicQiandaoFace(cam=self.comboBox.currentText(),face_featureslist=self.face_featurelist)
        self.face.show()
        self.close()


