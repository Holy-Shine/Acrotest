import sys,os,cv2

from PyQt5 import QtGui,QtCore,QtWidgets

from FaceFunction import cameraui
from FaceFunction.FaceUtil import FaceRecognition
from multiprocessing import Process

Appkey=b'2FzzVsnbAkk9q8eLx2s1Q7tft3dY1NZXdnLN8xK6UtXf'
SDKey=b'DAEJTcePD4TWaWKej3xRpPxBhCWGkFf4nxdYnooLWDuP'

#
# class Savepkl(Process):
#     def __init__(self):
#         super(Savepkl, self).__init__()
#         self.mem_data = None
#         self.mem_phone = None
#
#     def getmsg(self,mem_data,mem_phone):
#         self.mem_data = mem_data
#         self.mem_phone = mem_phone
#
#     def saveinfo(self):
#         try:
#             pkf.SavePickle(data=self.mem_data, mem_phone=self.mem_phone)
#         except Exception as e:
#             print(e)
#
#     def run(self):
#         self.saveinfo()

class Uiwindow(QtWidgets.QMainWindow, cameraui.Ui_Form):
    def __init__(self, parent=None):
        super(Uiwindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('人脸检测测试')
        self.timer_camera = QtCore.QTimer()
        self.cap = cv2.VideoCapture()
        self.CAM_NUM = 0

        self.init()
        # self.Savepkl = Savepkl()
        self.slot_init()

    def init(self):
        self.facefunction = FaceRecognition(Appkey=Appkey, SDKey=SDKey)
        flag = self.facefunction.ActivationFace()
        if not flag:
            QtWidgets.QMessageBox.warning(self, u"Warning", u"人脸识别检测初始化失败，请检查人脸识别SDK",
                                          buttons=QtWidgets.QMessageBox.Ok)


    def slot_init(self):
        self.opencamrea.clicked.connect(self.button_open_camera_click)
        self.timer_camera.timeout.connect(self.show_camera)
        self.cutPic.clicked.connect(self.button_cut_pic_click)
        self.save.clicked.connect(self.button_save_pic_click)

    def button_open_camera_click(self):
        if self.timer_camera.isActive() == False:
            flag = self.cap.open(self.CAM_NUM)
            if flag == False:
                QtWidgets.QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确",
                                                    buttons=QtWidgets.QMessageBox.Ok,
                                                    defaultButton=QtWidgets.QMessageBox.Ok)
            else:
                self.timer_camera.start(30)
                self.opencamrea.setText(u'关闭相机')


        else:
            self.timer_camera.stop()
            self.cap.release()
            self.camera.clear()
            self.opencamrea.setText(u'打开相机')



    def closecam(self):
        try:
            if self.timer_camera.isActive() == True:
                self.timer_camera.stop()
                self.cap.release()
                self.camera.clear()
                self.opencamrea.setText(u'打开相机')
        except Exception as e:
            print(e)

    def button_cut_pic_click(self):
        try:
            if(self.facefunction.IsHaveFace(self.image)):
                self.closecam()
                self.cutimgage = self.image
                show = cv2.resize(self.cutimgage, (140, 105))
                show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)

                showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
                self.cut_imgshow.setPixmap(QtGui.QPixmap.fromImage(showImage))
            else:
                QtWidgets.QMessageBox.about(self, "提示", "未检测到人脸")
        except Exception as e:
            print(e)


    def button_save_pic_click(self):
        try:
            if(self.ageinput.text() == "" or self.naninput.text() == "" ):
                QtWidgets.QMessageBox.about(self, "提示", "信息输入不完整")
            else:
                data = self.facefunction.MakePickleData(mem_name=self.naninput.text(),
                                                        mem_phone=self.ageinput.text(),
                                                        mem_img=self.image)
                print(data['feature'])
                print(len(data['feature']))
                # self.Savepkl.getmsg(mem_data=data,mem_phone=self.ageinput.text())
                # self.Savepkl.run()
                # QtWidgets.QMessageBox.about(self, "提示", "人脸信息录入成功")
        except Exception as e:
            print(e)


    def show_camera(self):
        try:
            flag, self.image = self.cap.read()
            show = cv2.resize(self.image, (280,210))
            show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
            show = self.facefunction.showMaxFace(show)
            showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
            self.camera.setPixmap(QtGui.QPixmap.fromImage(showImage))
        except Exception as e:
            print(e)









    def closeEvent(self, event):
        ok = QtWidgets.QPushButton()
        cacel = QtWidgets.QPushButton()

        msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, u"关闭", u"是否关闭！")

        msg.addButton(ok, QtWidgets.QMessageBox.ActionRole)
        msg.addButton(cacel, QtWidgets.QMessageBox.RejectRole)
        ok.setText(u'确定')
        cacel.setText(u'取消')
        # msg.setDetailedText('sdfsdff')
        if msg.exec_() == QtWidgets.QMessageBox.RejectRole:
            event.ignore()
        else:
            #             self.socket_client.send_command(self.socket_client.current_user_command)
            if self.cap.isOpened():
                self.cap.release()
            if self.timer_camera.isActive():
                self.timer_camera.stop()
            event.accept()
            try:
                os._exit(0)
            except Exception as e:
                print(e)



def main():
    app = QtWidgets.QApplication(sys.argv)     # 创建QApplication对象
    mywindow = Uiwindow()        # 创建MyWindow对象
    mywindow.show()          # 显示窗口
    app.exec_()           # 进入消息循环
    app = QtWidgets.QApplication(sys.argv)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
