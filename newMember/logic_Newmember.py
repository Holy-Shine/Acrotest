
import cv2
import os,sys

from PyQt5.QtWidgets import QDialog,QMessageBox,QLineEdit,QApplication
from PyQt5 import QtCore,QtGui,QtWidgets

from newMember.UI_NewMember import Ui_NewMember
from newMember.logic_MemberCAMChose import LogicMemberCAMChose

from Qiandao.process_camera_info import Camera

import Date2Week.DateAndWeek as dateweek


class LogicNewMember(Ui_NewMember,QDialog):
    def __init__(self,MySQL):
        super().__init__()
        self.setupUi(self)
        #导入数据库
        self.MySQL = MySQL
    #     self.cameranum = camnum
        self.timer_camera = QtCore.QTimer()
        self.cap = cv2.VideoCapture()
        self.image = None
    #
    #
        self.LogicMemberCAMChose = None
        self.cameranum = None
        self.camtag = False

        self.init()
        self.slot_init()
    #
    #
    def init(self):
        self.listFunc.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)
    #     self.clearLineEdit()
        #添加条目
        card = ["年卡", "季卡", "月卡", '次卡']
        classitem = ["平衡车", "轮滑"]
        self.cb_card_new.addItems(card)
        self.cb_classitem_new.addItems(classitem)
        self.cb_card_old.addItems(card)
        self.cb_classitem_old.addItems(classitem)

        #限制lineEdit的输入
        #年龄只让输入数字
        self.et_age_new.setValidator(QtGui.QIntValidator())
        self.et_age_old.setValidator(QtGui.QIntValidator())

        #课时次数让输入数字
        self.et_cichu__old.setValidator(QtGui.QIntValidator())
        self.et_cichu_new.setValidator(QtGui.QIntValidator())

        #办卡金额只让输入数字
        self.et_money_new.setValidator(QtGui.QIntValidator())
        self.et_money_old.setValidator(QtGui.QIntValidator())

        self.cardtype = {
            '轮滑':0,
            '平衡车':1
        }

        self.meminfo_data = {
            '学生姓名': '',
            '学生性别':'',
            '学生年龄':'',
            '学生家长':'',
            '联系方式':'',
            '课程种类': '', #平衡车or轮滑
            '课时次数': '',
            '办卡种类': '', #年卡，月卡，季度卡等等
        }
        self.banka_data = {
            '学生姓名': '',
            '学生电话': '',
            '办卡续卡': '',
            '金额': '',
            '日期': '',
        }
    #
    #
    # def clearLineEdit(self):
    #     self.et_cichu.setText('')
    #     self.et_age.setText('')
    #     self.et_parent.setText('')
    #     self.et_money.setText('')
    #
    def slot_init(self):
        #打开摄像机
        self.bt_opencam_new.clicked.connect(self.open_camera_new)
        self.pb_opencam_old.clicked.connect(self.open_camera_old)
        #切换界面时关闭摄像头
        self.listFunc.itemClicked.connect(self.close_camera)

        #清空图像
        self.bt_clearpic_new.clicked.connect(self.clearpic_new)
        self.pb_clearpic_old.clicked.connect(self.clearpic_old)

        #确认录入
        self.bt_confrim_new.clicked.connect(self.confrim_and_insert_new)

        self.rb_man_new.clicked.connect(self.gender_new_man)
        self.rb_woman_new.clicked.connect(self.gender_new_woman)

    #新学员性别选择
    def gender_new_man(self):
        self.meminfo_data['学生性别'] = self.rb_man_new.text()

    def gender_new_woman(self):
        self.meminfo_data['学生性别'] = self.rb_woman_new.text()
    #关闭摄像头
    def close_camera(self):
        self.lb_cam_new.clear()
        self.lb_cam_old.clear()
        if self.timer_camera.isActive() == True:
            self.timer_camera.stop()
            self.cap.release()
            self.lb_cam_new.clear()
            self.lb_cam_old.clear()
            self.bt_opencam_new.setText(u'打开摄像头')
            self.pb_opencam_old.setText(u'打开摄像头')

    #新学员界面打开摄像头
    def open_camera_new(self):
        self.cameranum = Camera().get_cam_num()
        if(self.cameranum>0):
            self.camtag = True
            self.open_camera()

        else:
            QMessageBox.warning(self, u"Warning", u"请检查摄像头",
                                            buttons=QMessageBox.Ok,
                                            defaultButton=QMessageBox.Ok)

    #老学员界面打开摄像头
    def open_camera_old(self):
            self.cameranum = Camera().get_cam_num()
            if (self.cameranum > 0):
                try:
                    self.camtag = False
                    self.open_camera()
                except Exception as e:
                    print(e)

            else:
                QMessageBox.warning(self, u"Warning", u"请检查摄像头",
                                    buttons=QMessageBox.Ok,
                                    defaultButton=QMessageBox.Ok)

    #打开摄像头函数
    def open_camera(self):
        try:
            if self.timer_camera.isActive() == False:
                my = LogicMemberCAMChose(Camnum=self.cameranum)
                my.mySignal.connect(self.getCAMNO)
                my.exec_()
            else:
                self.timer_camera.stop()
                self.cap.release()
                print(self.camtag)
                if (self.camtag):
                    self.lb_cam_new.clear()
                    self.bt_opencam_new.setText(u'打开摄像头')
                else:
                    self.lb_cam_old.clear()
                    self.pb_opencam_old.setText(u'打开摄像头')
        except Exception as e:
            print(e)

    #获取摄像头
    def getCAMNO(self, camnum):
        self.get_camera(int(camnum))
        self.timer_camera.timeout.connect(self.show_camera)
    #
    # #打开摄像头
    def get_camera(self,camnum):
        try:
            if self.timer_camera.isActive() == False:
                flag = self.cap.open(camnum)
                if flag == False:
                    QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确",
                                                        buttons=QMessageBox.Ok,
                                                        defaultButton=QMessageBox.Ok)
                else:
                    self.timer_camera.start(30)
                if(self.camtag):
                    self.bt_opencam_new.setText(u'关闭摄像头')
                else:
                    self.pb_opencam_old.setText(u'关闭摄像头')
        except Exception as e:
            print(e)
    #
    #
    # #显示图像
    def show_camera(self):
        flag, self.image = self.cap.read()
        # print(self.image.shape)
        # show = self.image[0:128, 0:512]
        show = cv2.resize(self.image, (260,346))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)

        # show = self.facerecognition.showMaxFace(show)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        if(self.camtag):
            self.lb_cam_new.setPixmap(QtGui.QPixmap.fromImage(showImage))
        else:
            self.lb_cam_old.setPixmap(QtGui.QPixmap.fromImage(showImage))


        '''
        此处写框人脸接口 改变self.image 的值
        '''
    #

    #新学生界面清空图像（如果摄像头打开，就关闭摄像头）
    def clearpic_new(self):
        self.lb_cam_new.clear()
        if self.timer_camera.isActive() == True:
            self.timer_camera.stop()
            self.cap.release()
            self.bt_opencam_new.setText(u'打开摄像头')

    #老学生界面清空图像（如果摄像头打开，就关闭摄像头）
    def clearpic_old(self):
        self.lb_cam_old.clear()
        if self.timer_camera.isActive() == True:
            self.timer_camera.stop()
            self.cap.release()
            self.bt_opencam_old.setText(u'打开摄像头')



    '''
    ###########################
    新学员录入，插入数据库
    ###########################
    '''
    #插入新学员后，清空数据库
    def clearEditAfterNewMemberInsert(self):
        self.et_name_new.clear()
        self.et_age_new.clear()
        self.et_parent_new.clear()
        self.et_phone_new.clear()
        self.et_cichu_new.clear()
        self.et_money_new.clear()

    def confrim_and_insert_new(self):
    #数据库段
        self.meminfo_data['学生姓名'] = self.et_name_new.text()
        self.meminfo_data['学生年龄'] = self.et_age_new.text()
        self.meminfo_data['学生家长'] = self.et_parent_new.text()
        self.meminfo_data['联系方式'] = self.et_phone_new.text()
        self.meminfo_data['课程种类'] = self.cardtype[self.cb_classitem_new.currentText()]
        self.meminfo_data['课时次数'] = self.et_cichu_new.text()
        self.meminfo_data['办卡种类'] = self.cb_card_new.currentText()

        self.banka_data['学生姓名'] = self.et_name_new.text()
        self.banka_data['学生电话'] = self.et_phone_new.text()
        self.banka_data['办卡续卡'] = 0   #'0'是办卡 ‘1’是续卡
        self.banka_data['金额'] = self.et_money_new.text()
        self.banka_data['日期'] = dateweek.getCurrentYMD()

        if(self.meminfo_data['学生姓名']==''):
            QMessageBox.warning(self, u"温馨提示", u"请输入学生姓名",
                                buttons=QMessageBox.Ok,)
        elif (self.meminfo_data['学生性别'] == ''):
            QMessageBox.warning(self, u"温馨提示", u"请选择学生性别",
                                buttons=QMessageBox.Ok, )
        elif (self.meminfo_data['学生家长'] == ''):
            QMessageBox.warning(self, u"温馨提示", u"请输入学生家长姓名",
                                buttons=QMessageBox.Ok, )
        elif (self.meminfo_data['联系方式'] == ''):
            QMessageBox.warning(self, u"温馨提示", u"请输入联系手机号码",
                                buttons=QMessageBox.Ok, )
        elif not(self.PhoneCheck(self.meminfo_data['联系方式'])):
            QMessageBox.warning(self, u"温馨提示", u"请输入正确的11位手机号码",
                                buttons=QMessageBox.Ok,)
        elif (self.meminfo_data['课时次数']== ''):
            QMessageBox.warning(self, u"温馨提示", u"请输入录入的课时次数",
                                buttons=QMessageBox.Ok, )
        elif (self.banka_data['金额']== ''):
            QMessageBox.warning(self, u"温馨提示", u"请输入此次录入学生的办卡费用",
                                buttons=QMessageBox.Ok, )
        else:
            print(self.meminfo_data)
            print(self.banka_data)
            hint = '学生姓名：{}\n学生性别：{}\n学生年龄：{}\n学生家长：{}\n联系方式：{}\n课时次数：{}\n' \
                   '金额：{}\n课程种类：{}\n办卡种类：{}'.format(
                self.meminfo_data['学生姓名'],
                self.meminfo_data['学生性别'],
                self.meminfo_data['学生年龄'],
                self.meminfo_data['学生家长'],
                self.meminfo_data['联系方式'],
                self.meminfo_data['课时次数'],
                self.banka_data['金额'],
                self.cb_classitem_new.currentText(),
                self.cb_card_new.currentText()
            )
            reply = QMessageBox.warning(self, '确认信息', hint, QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                flag1,flag2 = False,False
                if(self.image == None):
                    reply2 = QMessageBox.warning(self,'确认信息','您还没有录入人脸图像\n确认继续录入吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                    if(reply2 == QMessageBox.Yes):
                        try:
                            flag1 = self.Insert2Banka()
                            flag2 = self.Insert2Meminfo()
                        except Exception as e:
                            print(e)
                    else:
                        print(1)
                else:
                    try:
                        flag1 = self.Insert2Banka()
                        flag2 = self.Insert2Meminfo()
                    except Exception as e:
                        print(e)

                if(flag1 and flag2):
                    QMessageBox.information(self, '提示', '录入成功！', QMessageBox.Ok, QMessageBox.Ok)
                    self.clearEditAfterNewMemberInsert()
                else:
                    QMessageBox.information(self, '提示', '录入失败！', QMessageBox.Ok, QMessageBox.Ok)

    def Insert2Meminfo(self):
        sql = 'INSERT INTO mem_info  VALUES(\'{}\', \'{}\', {},{},\'{}\',\'{}\',{},\'{}\')'.format(
            self.meminfo_data['联系方式'],
            self.meminfo_data['学生姓名'],
            self.meminfo_data['课程种类'],
            self.meminfo_data['学生年龄'],
            self.meminfo_data['学生家长'],
            self.meminfo_data['学生性别'],
            self.meminfo_data['课时次数'],
            self.meminfo_data['办卡种类']
        )
        print(sql)

        try:
            flag = self.MySQL.InsertFromDataBse(sql)
            # print('flag meminfo{}'.format(flag))
            return flag
        except:
            QMessageBox.critical(self, '错误', '数据库异常！', QMessageBox.Ok, QMessageBox.Ok)

    def Insert2Banka(self):
        sql = 'INSERT INTO banka  VALUES(\'{}\', \'{}\',{},{},\'{}\')'.format(
            self.banka_data['学生电话'],
            self.banka_data['学生姓名'],
            self.banka_data['办卡续卡'],
            self.banka_data['金额'],
            self.banka_data['日期']
        )
        print(sql)
        try:
            flag = self.MySQL.InsertFromDataBse(sql)
            # print('flag meminfo{}'.format(flag))
            return flag
        except:
            QMessageBox.critical(self, '错误', '数据库异常！', QMessageBox.Ok, QMessageBox.Ok)



    def PhoneCheck(self,s):
        # 检测号码是否长度是否合法。
        if len(s) != 11:
            return False
        elif(s.isdigit()):
            return True
        else:
            return False


    # def cut_pic(self):
    #     try:
    #         if self.timer_camera.isActive() == False:
    #             QMessageBox.warning(self, u"Warning", u"请先打开摄像头",
    #                                 buttons=QMessageBox.Ok,
    #                                 defaultButton=QMessageBox.Ok)
    #         else:
    #             self.timer_camera.stop()
    #             self.cap.release()
    #             self.bt_opencam.setText(u'打开摄像头')
    #     except Exception as e:
    #         print(e)
    #
    # #录入信息
    # def confrim(self):
    #     print(1)
    #
    # #返回
    # def back(self):
    #     self.clearLineEdit()
    #     self.close_camera()
    #
    #
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

if __name__ == '__main__':
    from ConnextMySQL.MySQLBase import MySQLBaseFunction
    host = '121.199.17.205',  # IP
    user = 'Jessie',  # 用户名
    password = 'Jessie.121406',  # 密码
    database = 'meminfo',
    MySQL = MySQLBaseFunction(HostIP=host,
                      Username=user,
                      Password=password,
                      DataBase=database)
    MySQL.ConnectMySQL()
    app = QApplication(sys.argv)
    login = LogicNewMember(MySQL=MySQL)
    login.show()
    sys.exit(app.exec_())