

from Qiandao.UI_Qiandao_camera import UIQiandaoCamera

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class LogicQiandaoCamrea(UIQiandaoCamera,QDialog):
    mySignal = pyqtSignal(str)
    def __init__(self,cameranum):
        super().__init__()
        self.setupUi(self)
        self.cameranum = cameranum

        self.face = None
        self.init()
        # self.slot_init()

    def init(self):
        for i in range(self.cameranum):
            self.comboBox.addItem(str(i))

    # def slot_init(self):
    #     self.bt_confrim.clicked.connect(self.goto_face)
    #
    #
    # #选择摄像头，打开人脸签到界面
    # def goto_face(self):
    #     #此处添加加载特征序列的代码（开子线程完成)
    #     self.face_featurelist = []
    #
    #     self.face = LogicQiandaoFace()
    #     self.face.setCamNum(0)
    #     self.face.show()
    #     self.close()


