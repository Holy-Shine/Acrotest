from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QMessageBox, QLineEdit, QApplication, QTableView, QHeaderView

from PyQt5 import QtCore,QtGui,QtWidgets

from Qiandao.UI_Qiandao_face_Main import Ui_UIQiandaoFace
import sys
import time
from Date2Week import DateAndWeek as timefunction

#人脸识别系统
from Qiandao.process_camera_info import Camera
from newMember.logic_MemberCAMChose import LogicMemberCAMChose
import cv2

import Login.CheckDBandFace as ckdf

class LogicQiandaoFace(Ui_UIQiandaoFace,QDialog):
    def __init__(self,MySQL,facefunction):
        super().__init__()
        self.setupUi(self)
        self.MySQL = MySQL
        self.faceFunction = facefunction
        self.dianlist = None
        self.data_meminfo_search = None
        self.data_meminfo_table = None

        # 摄像头系统参数
        self.timer_camera = QtCore.QTimer()

        self.timer_face = QtCore.QTimer()
        self.cap = cv2.VideoCapture()
        self.image = None
        self.LogicMemberCAMChose = None
        self.cameranum = None
        self.camtag = False
        self.tableflag = None

        self.facefeature = []

        self.dian2int={
            '10点':10,
            '11点':11,
            '12点': 12,
            '13点': 13,
            '14点': 14,
            '15点':15,
            '16点': 16,
            '17点': 17,
            '18点': 18,
            '19点': 19,
            '20点': 20,
            '21点': 21,
        }

        self.int2dian = {
            10:'10点' ,
            11:'11点' ,
            12:'12点' ,
            13:'13点' ,
            14:'14点' ,
            15:'15点' ,
            16:'16点' ,
            17:'17点' ,
            18:'18点' ,
            19:'19点' ,
            20:'20点' ,
            21:'21点' ,
        }


        self.week2day = { 1:"周一",
                     2:"周二",
                     3:"周三",
                     4:"周四",
                     5:"周五",
                     6:"周六",
                     7:"周日"}

        self.meminfo_data = {
            '学生姓名': '',
            '课程种类': '',
            '联系方式': '',
            '上课时间': '',
            '是否签到': '',
            '教练姓名': '',
            '剩余次数': '',
        }

        self.cardtype = {
            '轮滑': 0,
            '滑步车': 1
        }

        self.type2card = {
            0:'轮滑',
            1:'滑步车'
        }

        self.init()
        self.slot_init()

    def init(self):
        self.headers_StudentList = ['学生姓名', '联系方式','办卡种类','课程种类','上课时间', '是否签到', '教练姓名', '剩余次数']
        self.data_model = QStandardItemModel()
        # 学生表初始化
        self.data_model.setHorizontalHeaderLabels(self.headers_StudentList)
        self.tv_student.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        self.tv_student.setSelectionBehavior(QTableView.SelectRows)  # 选中行
        self.tv_student.setModel(self.data_model)
        self.tv_student.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.initday()
        self.initcoach()

        #显示et不可用
        self.et_cishu.setEnabled(False)
        self.et_name.setEnabled(False)
        self.et_phone.setEnabled(False)
        self.et_classtime.setEnabled(False)
        self.bt_qiandao_confrim.setEnabled(False)

        self.bt_opencam.setEnabled(False)

    def slot_init(self):
        self.bt_search.clicked.connect(self.searchlist)
        self.bt_search.setShortcut(Qt.Key_Return)
        # 表内选择
        self.tv_student.selectionModel().selectionChanged.connect(self.row_sel_change)

        #确认签到
        self.bt_qiandao_confrim.clicked.connect(self.on_bt_click_qiandao)

        self.bt_opencam.clicked.connect(self.on_bt_clicked_opencam)

        self.timer_camera.timeout.connect(self.show_camera)

        self.timer_camera.timeout.connect(self.recon_face)

        self.bt_clear.clicked.connect(self.myclear)

    '''
    #############################################################
    签到功能
    ############################################################
    '''

    #初始化当前日期
    def initday(self):
        tm = time.gmtime()
        week,weekday = timefunction.FromDatetoWeek(year=tm.tm_year,
                                                month=tm.tm_mon,
                                                day=tm.tm_mday)
        self.lb_time.setText("当前日期：{}年{}月{}日 第{}周 {}".format(tm.tm_year,tm.tm_mon,tm.tm_mday,week,self.week2day[int(weekday)]))

    #初始化教练
    def initcoach(self):
        self.cb_coach.clear()
        try:
            sql = 'SELECT coa_name FROM coach;'
            _,coachname = self.MySQL.SelectFromDataBse(sql)
            for name in coachname:
                self.cb_coach.addItem(name[0])
        except Exception as e:
            print(e)

    #按照要求查找课程
    def searchlist(self):
        self.close_camera()
        try:
            self.initcoach()
            self.dianlist = self.cb_dian.Selectlist()
            if (len(self.dianlist) == 0):
                QMessageBox.information(self, '提示', '没有选择具体时间点！', QMessageBox.Ok, QMessageBox.Ok)
            else:
                self.selectClassList()
                self.add_table()
                self.initfacefeature()
                self.bt_opencam.setEnabled(True)
        except Exception as e:
            print(e)

    #点击列表数据存储
    def addtomeminfo_data(self,result):
        try:
            self.meminfo_data['学生姓名'] = result[0]
            self.meminfo_data['联系方式'] = result[1]
            self.meminfo_data['课程种类'] = result[2]
            self.meminfo_data['上课时间'] = self.int2dian[result[5]]
            self.meminfo_data['是否签到'] = result[6]
            self.meminfo_data['教练姓名'] = result[3]
            self.meminfo_data['剩余次数'] = result[4]

        except Exception as e:
            print(e)

    #点击列表左侧显示
    def maketext(self):
        self.et_name.setText(self.meminfo_data['学生姓名'] )
        self.et_phone.setText(self.meminfo_data['联系方式'])
        self.et_cishu.setText(str(self.meminfo_data['剩余次数']))
        self.et_classtime.setText(self.meminfo_data['上课时间'])

    #列表点击函数
    def row_sel_change(self):
        try:
            current_row = self.tv_student.currentIndex().row()
            if current_row < len(self.data_meminfo_table):
                result = self.data_meminfo_table[current_row]
                self.addtomeminfo_data(result)
                self.maketext()
                if(int(result[4])>0):
                    self.bt_qiandao_confrim.setEnabled(True)
                    if(result[6]==0):
                        self.bt_qiandao_confrim.setText('确认签到')
                    else:
                        self.bt_qiandao_confrim.setText('取消签到')
                else:
                    self.bt_qiandao_confrim.setEnabled(False)
        except Exception as e:
            print(e)

    #添加数据至表格
    def add_table(self):
        self.data_model.clear()
        self.data_model.setHorizontalHeaderLabels(self.headers_StudentList)
        for i, (mem_name, mem_phone, mem_type, mem_coa_name, mem_cls_left,
                ctime, mem_signed,_,mem_cardtype) in enumerate(self.data_meminfo_table):
            if(mem_signed==0):
                signed = '否'
            else:
                signed = '是'
            if (mem_cls_left > 1000):
                mem_cls_left = '无限'
            self.data_model.appendRow([
                QStandardItem(mem_name),
                QStandardItem(mem_phone),
                QStandardItem(mem_cardtype),
                QStandardItem(self.type2card[mem_type]),
                QStandardItem('{}点'.format(ctime)),
                QStandardItem(signed),
                QStandardItem(mem_coa_name),
                QStandardItem(str(mem_cls_left)),
            ])

    #查询课程
    def selectClassList(self):
        try:
            tm = time.gmtime()
            week, weekday = timefunction.FromDatetoWeek(year=tm.tm_year,
                                                        month=tm.tm_mon,
                                                        day=tm.tm_mday)
            diansql = 'ctime={}'.format(self.dian2int[self.dianlist[0]])
            for i in range(1, len(self.dianlist)):
                diansql += ' OR ctime={}'.format(self.dian2int[self.dianlist[i]])

            sql = 'SELECT distinct mem_class.mem_name, ' \
                  'mem_class.mem_phone, ' \
                  'mem_class.mem_type,' \
                  'mem_class.mem_coa_name,' \
                  'mem_info.mem_cls_left,' \
                  'mem_class.ctime, ' \
                  'mem_class.mem_signed,' \
                  'mem_info.mem_facefeature, ' \
                  'mem_info.mem_cardtype ' \
                  ' FROM mem_info JOIN  mem_class WHERE ' \
                  'mem_class.mem_name = mem_info.mem_name ' \
                  ' AND mem_class.year={}  ' \
                  ' AND mem_class.week={} ' \
                  ' AND mem_class.cday={}' \
                  ' AND ({})'.format(
                tm.tm_year,
                week,
                weekday,
                diansql
            )
            print(sql)
            flag, self.data_meminfo_search = self.MySQL.SelectFromDataBse(sql)
            # self.data_meminfo_table = self.selectone(data = self.data_meminfo_search,name='裴正蒙',phone='12312312312')
            self.data_meminfo_table = self.data_meminfo_search
        except Exception as e:
            print(e)


    def initfacefeature(self):
        self.facefeature.clear()

        for i, (mem_name, mem_phone, _, _, _,
            _, _, mem_facefeature, _) in enumerate(self.data_meminfo_search):
            if not(mem_facefeature==b'NULL'):
                data = {
                    'name':mem_name,
                    'phone':mem_phone,
                    'mem_facefeature':self.faceFunction.getFeature(mem_facefeature)
                }
                if not (data in self.facefeature):
                    self.facefeature.append(data)
        print(self.facefeature)
    #签到
    def on_bt_click_qiandao(self):
        if(self.bt_qiandao_confrim.text()=='确认签到'):
            self.confrim_qiandao()
        elif(self.bt_qiandao_confrim.text()=='取消签到'):
            self.cancel_qiandao()
        else:
            QMessageBox.information(self, '提示', '出现了一个问题！', QMessageBox.Ok, QMessageBox.Ok)

    #已经签到的取消签到
    def cancel_qiandao(self):
        try:

            if not(self.et_name==''):
                if (int(self.meminfo_data['剩余次数']) > 1000):
                    mem_cls_left = '无限'
                    hint = '学生姓名：{}\n联系方式：{}\n课程种类：{}\n上课时间：{}\n剩余次数：{}+1={}\n'.format(
                        self.meminfo_data['学生姓名'],
                        self.meminfo_data['联系方式'],
                        self.type2card[self.meminfo_data['课程种类']],
                        self.meminfo_data['上课时间'],
                        mem_cls_left,
                        mem_cls_left,
                    )
                else:
                    mem_cls_left = self.meminfo_data['剩余次数']
                    hint = '学生姓名：{}\n联系方式：{}\n课程种类：{}\n上课时间：{}\n剩余次数：{}+1={}\n'.format(
                        self.meminfo_data['学生姓名'],
                        self.meminfo_data['联系方式'],
                        self.type2card[self.meminfo_data['课程种类']],
                        self.meminfo_data['上课时间'],
                        mem_cls_left,
                        int(mem_cls_left)+1,
                    )
                reply = QMessageBox.warning(self, '确认删除？', hint, QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                if reply == QMessageBox.Yes:
                    tm = time.gmtime()
                    week, weekday = timefunction.FromDatetoWeek(year=tm.tm_year,
                                                                month=tm.tm_mon,
                                                                day=tm.tm_mday)
                    sql_update_cishu = 'UPDATE  mem_info  SET mem_cls_left={} WHERE mem_name=\'{}\' and mem_phone=\'{}\' and mem_type={};'.format(
                        int(self.meminfo_data['剩余次数']) + 1,
                        self.meminfo_data['学生姓名'],
                        self.meminfo_data['联系方式'],
                        self.meminfo_data['课程种类']
                    )
                    sql_update_class = 'UPDATE  mem_class  SET mem_signed=0  WHERE mem_name=\'{}\' ' \
                                       'and mem_phone=\'{}\' ' \
                                       'and mem_type={} ' \
                                       'and year={} and week ={} and cday={} and ctime = {};'.format(
                        self.meminfo_data['学生姓名'],
                        self.meminfo_data['联系方式'],
                        self.meminfo_data['课程种类'],
                        tm.tm_year,week,weekday,
                        self.dian2int[self.meminfo_data['上课时间']]
                    )
                    print(sql_update_class)

                    flag1 = self.MySQL.UpdateFromDataBse(sql_update_cishu)
                    flag2 = self.MySQL.UpdateFromDataBse(sql_update_class)

                    if (flag1 and flag2):
                        self.selectClassList()
                        self.add_table()
                        QMessageBox.information(self, '提示', '签到成功！', QMessageBox.Ok, QMessageBox.Ok)
                    else:
                        QMessageBox.information(self, '提示', '签到失败！', QMessageBox.Ok, QMessageBox.Ok)
            else:
                QMessageBox.information(self, '提示', '没有选择学生课程！', QMessageBox.Ok, QMessageBox.Ok)
        except Exception as e:
            print(e)

    #未签到的确认签到
    def confrim_qiandao(self):
        try:
            if not (self.et_name == ''):
                if (int(self.meminfo_data['剩余次数']) > 1000):
                    mem_cls_left = '无限'
                    hint = '学生姓名：{}\n联系方式：{}\n课程种类：{}\n 教练姓名：{}\n上课时间：{}\n剩余次数：{}-1={}\n'.format(
                        self.meminfo_data['学生姓名'],
                        self.meminfo_data['联系方式'],
                        self.type2card[self.meminfo_data['课程种类']],
                        self.cb_coach.currentText(),
                        self.meminfo_data['上课时间'],
                        mem_cls_left,
                        mem_cls_left,
                    )
                else:
                    mem_cls_left = self.meminfo_data['剩余次数']
                    hint = '学生姓名：{}\n联系方式：{}\n课程种类：{}\n 教练姓名：{}\n上课时间：{}\n剩余次数：{}-1={}\n'.format(
                        self.meminfo_data['学生姓名'],
                        self.meminfo_data['联系方式'],
                        self.type2card[self.meminfo_data['课程种类']],
                        self.cb_coach.currentText(),
                        self.meminfo_data['上课时间'],
                        mem_cls_left,
                        int(mem_cls_left)-1,
                    )
                reply = QMessageBox.warning(self, '确认删除？', hint, QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                if reply == QMessageBox.Yes:
                    tm = time.gmtime()
                    week, weekday = timefunction.FromDatetoWeek(year=tm.tm_year,
                                                                month=tm.tm_mon,
                                                                day=tm.tm_mday)
                    sql_update_cishu = 'UPDATE  mem_info  SET mem_cls_left={} WHERE mem_name=\'{}\' and mem_phone=\'{}\' and mem_type={};'.format(
                        int(self.meminfo_data['剩余次数']) - 1,
                        self.meminfo_data['学生姓名'],
                        self.meminfo_data['联系方式'],
                        self.meminfo_data['课程种类']
                    )
                    sql_update_class = 'UPDATE  mem_class  SET mem_signed=1, mem_coa_name=\'{}\' WHERE mem_name=\'{}\' ' \
                                       'and mem_phone=\'{}\' ' \
                                       'and mem_type={} ' \
                                       'and year={} and week ={} and cday={} and ctime = {};'.format(
                        self.cb_coach.currentText(),
                        self.meminfo_data['学生姓名'],
                        self.meminfo_data['联系方式'],
                        self.meminfo_data['课程种类'],
                        tm.tm_year,week,weekday,
                        self.dian2int[self.meminfo_data['上课时间']]
                    )
                    print(sql_update_class)

                    flag1 = self.MySQL.UpdateFromDataBse(sql_update_cishu)
                    flag2 = self.MySQL.UpdateFromDataBse(sql_update_class)

                    if (flag1 and flag2):
                        self.selectClassList()
                        self.add_table()
                        QMessageBox.information(self, '提示', '签到成功！', QMessageBox.Ok, QMessageBox.Ok)
                    else:
                        QMessageBox.information(self, '提示', '签到失败！', QMessageBox.Ok, QMessageBox.Ok)
            else:
                QMessageBox.information(self, '提示', '没有选择学生课程！', QMessageBox.Ok, QMessageBox.Ok)
        except Exception as e:
            print(e)

    #关闭函数
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示',
                                     "确定退出本系统吗?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    '''
    #############################################################
    人脸识别功能
    ############################################################
    '''

    def on_bt_clicked_opencam(self):
        self.cameranum = Camera().get_cam_num()
        print(self.cameranum)
        if (self.cameranum > 0):
            try:
                self.open_camera()
            except Exception as e:
                print(e)

        else:
            QMessageBox.warning(self, u"Warning", u"请检查摄像头",
                                buttons=QMessageBox.Ok,
                                defaultButton=QMessageBox.Ok)

    def open_camera(self):
        try:
            if self.timer_camera.isActive() == False:
                my = LogicMemberCAMChose(Camnum=self.cameranum)
                my.mySignal.connect(self.get_camera)
                my.exec_()
            else:
                self.data_meminfo_table = self.data_meminfo_search
                self.add_table()
                self.timer_face.stop()
                self.timer_camera.stop()
                self.cap.release()
                self.image = None
                self.lb_cam.clear()
                self.bt_opencam.setText(u'打开摄像头')
        except Exception as e:
            print(e)

    def selectone(self,data, name, phone):
        res = []
        for i, item in enumerate(data):
            if (item[0] == name and item[1] == phone):
                res.append(item)
        return res

    def recon_face(self):
        try:
            if not (len(self.image) == None and len(self.facefeature)>0):
                res = self.faceFunction.mutifacerecon(facelist=self.facefeature,img = self.image)
                if res == None and not res == self.tableflag:
                    self.tableflag = None
                    self.data_meminfo_table = self.data_meminfo_search
                    self.add_table()
                elif not res == None and not res == self.tableflag:
                    self.data_meminfo_table = self.selectone(data=self.data_meminfo_search,
                                                             name=res[0],
                                                             phone=res[1])
                    self.add_table()
                    self.tableflag = res

        except Exception as e:
            print(e)

    #打开摄像头
    def get_camera(self,camnum):
        try:
            if self.timer_camera.isActive() == False:
                flag = self.cap.open(int(camnum))
                if flag == False:
                    QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确",
                                                        buttons=QMessageBox.Ok,
                                                        defaultButton=QMessageBox.Ok)
                else:
                    self.timer_camera.start(30)
                    # if len(self.facefeature)>0:
                    #     self.timer_face.start(30000)
                    self.bt_opencam.setText(u'关闭摄像头')
        except Exception as e:
            print(e)

    def show_camera(self):
        try:
            flag, self.image = self.cap.read()
            show = self.image
            show = self.faceFunction.showMaxFace(show)
            show = cv2.resize(show, (260, 346))
            show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
            showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
            self.lb_cam.setPixmap(QtGui.QPixmap.fromImage(showImage))
        except Exception as e:
            print(e)


    def myclear(self):
        self.close_camera()
        self.data_model.clear()
        self.data_model.setHorizontalHeaderLabels(self.headers_StudentList)
        self.et_phone.clear()
        self.et_name.clear()
        self.et_cishu.clear()
        self.et_classtime.clear()
        self.bt_qiandao_confrim.setEnabled(False)
        self.cb_dian.clear()
        self.bt_opencam.setEnabled(False)
        self.facefeature = []
        self.tableflag = None




    def close_camera(self):
        self.image = None
        self.lb_cam.clear()
        if self.timer_camera.isActive() == True:
            self.timer_camera.stop()
            self.timer_face.stop()
            self.cap.release()
            self.lb_cam.clear()

if __name__ == '__main__':
    f1, MySQL = ckdf.CheckDB()
    f2, facefunction = ckdf.CheckFace()
    app = QtWidgets.QApplication(sys.argv)
    window = LogicQiandaoFace(MySQL=MySQL, facefunction=facefunction)
    window.show()
    sys.exit(app.exec_())