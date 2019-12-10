from PyQt5.QtGui import QStandardItemModel, QStandardItem, QBrush, QColor
from PyQt5.QtWidgets import QDialog, QMessageBox, QLineEdit, QApplication, QTableView, QHeaderView

from PyQt5 import QtCore,QtGui,QtWidgets

from Qiandao.UI_Qiandao_face_Main import Ui_UIQiandaoFace
import os,sys
import time
from Date2Week import DateAndWeek as timefunction

class LogicQiandaoFace(Ui_UIQiandaoFace,QDialog):
    def __init__(self,MySQL,facefunction):
        super().__init__()
        self.setupUi(self)
        self.MySQL = MySQL
        self.faceFunction = facefunction
        self.dianlist = None
        self.data_meminfo_search = None



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
            10 :'10点',
            11 :'11点',
            12 :'12点',
            13 :'13点',
            14 :'14点',
            15 :'15点',
            16 :'16点',
            17 :'17点',
            18 :'18点',
            19 :'19点',
            20 :'20点',
            21 :'21点',
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
            '平衡车': 1
        }

        self.type2card = {
            0:'轮滑',
            1:'平衡车'
        }

        self.init()
        self.slot_init()

    def init(self):
        self.headers_StudentList = ['学生姓名', '联系方式','课程种类','上课时间', '是否签到', '教练姓名', '剩余次数']
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

    def slot_init(self):
        self.bt_search.clicked.connect(self.searchlist)

        # 表内选择
        self.tv_student.selectionModel().selectionChanged.connect(self.row_sel_change)

        #确认签到
        self.bt_qiandao_confrim.clicked.connect(self.confrim_qiandao)


    def initday(self):
        tm = time.gmtime()
        week,weekday = timefunction.FromDatetoWeek(year=tm.tm_year,
                                                month=tm.tm_mon,
                                                day=tm.tm_mday)
        self.lb_time.setText("当前日期：{}年{}月{}日 第{}周 {}".format(tm.tm_year,tm.tm_mon,tm.tm_mday,week,self.week2day[int(weekday)]))


    def initcoach(self):
        self.cb_coach.clear()
        try:
            sql = 'SELECT coa_name FROM coach;'
            _,coachname = self.MySQL.SelectFromDataBse(sql)
            for name in coachname:
                self.cb_coach.addItem(name[0])
        except Exception as e:
            print(e)

    def searchlist(self):
        try:
            self.initcoach()
            self.dianlist = self.cb_dian.Selectlist()
            if (len(self.dianlist) == 0):
                QMessageBox.information(self, '提示', '没有选择具体时间点！', QMessageBox.Ok, QMessageBox.Ok)
            else:
                self.selectClassList()
                self.add_table()
        except Exception as e:
            print(e)

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

    def maketext(self):
        self.et_name.setText(self.meminfo_data['学生姓名'] )
        self.et_phone.setText(self.meminfo_data['联系方式'])
        self.et_cishu.setText(str(self.meminfo_data['剩余次数']))
        self.et_classtime.setText(self.meminfo_data['上课时间'])

    def row_sel_change(self):
        try:
            current_row = self.tv_student.currentIndex().row()
            if current_row < len(self.data_meminfo_search):
                result = self.data_meminfo_search[current_row]
                self.addtomeminfo_data(result)
                self.maketext()
                if(result[6]==0):
                    self.bt_qiandao_confrim.setEnabled(True)
                else:
                    self.bt_qiandao_confrim.setEnabled(False)
        except Exception as e:
            print(e)




    def add_table(self):
        self.data_model.clear()
        self.data_model.setHorizontalHeaderLabels(self.headers_StudentList)
        # print(self.data_meminfo_search)
        for i, (mem_name, mem_phone, mem_type, mem_coa_name, mem_cls_left,
                ctime, mem_signed,_) in enumerate(self.data_meminfo_search):
            if(mem_signed==0):
                signed = '否'
            else:
                signed = '是'
            self.data_model.appendRow([
                QStandardItem(mem_name),
                QStandardItem(mem_phone),
                QStandardItem(self.type2card[mem_type]),
                QStandardItem(self.int2dian[ctime]),
                QStandardItem(signed),
                QStandardItem(mem_coa_name),
                QStandardItem(str(mem_cls_left)),
            ])

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
                  'mem_info.mem_facefeature ' \
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
        except Exception as e:
            print(e)


    def confrim_qiandao(self):
        try:
            hint = '学生姓名：{}\n联系方式：{}\n课程种类：{}\n 教练姓名：{}\n上课时间：{}\n剩余次数：{}-1={}\n'.format(
                self.meminfo_data['学生姓名'],
                self.meminfo_data['联系方式'],
                self.type2card[self.meminfo_data['课程种类']],
                self.cb_coach.currentText(),
                self.meminfo_data['上课时间'],
                self.meminfo_data['剩余次数'],
                int(self.meminfo_data['剩余次数'])-1,
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
                sql_update_class = 'UPDATE  mem_class  SET mem_signed=1 WHERE mem_name=\'{}\' ' \
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



        except Exception as e:
            print(e)


def getOR(dian):
    res = 'ctime={}'.format(dian[0])
    for i in range(1,len(dian)):
        res+=' OR ctime={}'.format(dian[i])
    print(res)
    return res
if __name__ == '__main__':
    dian = [1,2]
    getOR(dian)
    # app = QApplication(sys.argv)
    # login = LogicQiandaoFace(MySQL,facefunction)

    # login.show()
    # sys.exit(app.exec_())