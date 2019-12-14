from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QMessageBox, QLineEdit, QApplication, QTableView, QHeaderView

from StudentSystem.ClassInfoCheck import Ui_ClassInfoCheck
import time
from Date2Week import DateAndWeek as timefunction

class LogicClassInfoCheck(Ui_ClassInfoCheck,QDialog):
    def __init__(self,MySQL,mem_info,cardtype,type2card):
        super().__init__()
        self.setupUi(self)
        self.MySQL = MySQL
        self.meminfo = mem_info
        self.class_info = None

        self.cardtype = cardtype
        self.type2card = type2card

        self.headers_ClassList = ['学生姓名', '联系方式', '办卡种类', '教练姓名', '年', '月', '日', '点', '是否签到']
        self.data_model = QStandardItemModel()
        self.data_model.setHorizontalHeaderLabels(self.headers_ClassList)
        # 课程表初始化

        self.tv_classlist.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        self.tv_classlist.setSelectionBehavior(QTableView.SelectRows)  # 选中行
        self.tv_classlist.setModel(self.data_model)
        self.tv_classlist.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.int2week2day = { 1:"周一",
                     2:"周二",
                     3:"周三",
                     4:"周四",
                     5:"周五",
                     6:"周六",
                     7:"周日"}

        self.weekday2int = { "周一":1,
                              "周二":2,
                              "周三":3,
                              "周四":4,
                              "周五":5,
                              "周六":6,
                              "周日":7}

        self.type2card = {
            0:'轮滑',
            1:'滑步车'
        }

        self.init()
        self.slot_init()

    def init(self):
        self.lb_init()
        self.cb_init()
        self.event_label_status_change()




    def slot_init(self):
        self.cb_year.currentIndexChanged.connect(self.event_label_status_change)
        self.cb_week.currentIndexChanged.connect(self.event_label_status_change)
        self.bt_search.clicked.connect(self.on_clicked_bt_search)

    def cb_init(self):
        year = time.gmtime().tm_year
        self.cb_year.addItems([str(year-1),str(year),str(year+1)])
        for i in range(1,54):
            self.cb_week.addItem('{}'.format(i))




    def lb_init(self):
        tm = time.gmtime()
        week, weekday = timefunction.FromDatetoWeek(year=tm.tm_year,
                                                    month=tm.tm_mon,
                                                    day=tm.tm_mday)
        self.lb_time.setText("当前日期：{}年{}月{}日 第{}周 {}".format(tm.tm_year, tm.tm_mon, tm.tm_mday, week, self.int2week2day[int(weekday)]))

        self.lb_student.setText("学生:{},联系方式：{},课程种类:{}，办卡种类:{}".format(self.meminfo['学生姓名'],
                                                     self.meminfo['联系方式'],
                                                     self.type2card[self.meminfo['课程种类']],
                                                     self.meminfo['办卡种类'],))

    def event_label_status_change(self):
        try:
            year = int(self.cb_year.currentText())
            week = int(self.cb_week.currentText()) - 1
            F = timefunction.FromWeektoDate(year, week, 1)
            T = timefunction.FromWeektoDate(year, week, 7)
            begin_m = F[1]
            begin_d = F[2]
            end_m = T[1]
            end_d = T[2]
            if week == 0:
                weekday = timefunction.getFirstWeekDate(year)

                # 使得一些日子不可用
                begin_d = 1
                begin_m = 1
            elif week == 52:
                weekday = timefunction.getLastWeekDate(year)

                # 使得一些日子不可用
                end_d = 31
                end_m = 12
            text = '''{}-{}-{}至{}-{}-{}'''.format(year, begin_m, begin_d, year, end_m, end_d)
            self.lb_selectone.setText(text)

        except Exception as e:
            print(e)

    def selectcheckinfo(self):
        print(1)


    def on_clicked_bt_search(self):
        weekdaylist = self.cb_weekday.Selectlist()
        year = self.cb_year.currentText()
        week = self.cb_week.currentText()
        if(len(weekdaylist)==0):
            QMessageBox.information(self, '提示', '请选择查询的周天数！', QMessageBox.Ok, QMessageBox.Ok)
        try:
            diansql = 'cday={}'.format(self.weekday2int[weekdaylist[0]])
            for i in range(1, len(weekdaylist)):
                diansql += ' OR cday={}'.format(self.weekday2int[weekdaylist[i]])

            sql = 'SELECT * FROM mem_class WHERE ' \
                  ' mem_phone=\'{}\' ' \
                  ' AND mem_name=\'{}\' ' \
                  ' AND mem_type={}  ' \
                  ' AND year={}  ' \
                  ' AND week={} ' \
                  ' AND ({})'.format(
                self.meminfo['联系方式'],
                self.meminfo['学生姓名'],
                self.meminfo['课程种类'],
                year,
                week,
                diansql
            )
            print(sql)
            flag, self.class_info = self.MySQL.SelectFromDataBse(sql)
            if (flag and len(self.class_info)>0):
                self.add_table()
            else:
                QMessageBox.information(self, '提示', '未查询到课程信息！', QMessageBox.Ok, QMessageBox.Ok)

        except Exception as e:
            print(e)

    # self.headers_ClassList = ['学生姓名', '联系方式', '办卡种类', '教练姓名', '年', '月', '日', '点', '是否签到']
    def add_table(self):
        self.data_model.clear()
        self.data_model.setHorizontalHeaderLabels(self.headers_ClassList)
        for i, (mem_phone, mem_name, mem_type, mem_coa_name, year,
                week, cday, ctime, _,mem_signed) in enumerate(self.class_info):
            _,mon,day = timefunction.FromWeektoDate(year,int(week)-1,cday)
            if(mem_signed==0):
                signed = '否'
            else:
                signed = '是'
            self.data_model.appendRow([
                QStandardItem(mem_name),
                QStandardItem(mem_phone),
                QStandardItem(self.type2card[mem_type]),
                QStandardItem(mem_coa_name),
                QStandardItem('{}年'.format(year)),
                QStandardItem('{}月'.format(mon)),
                QStandardItem('{}日'.format(day)),
                QStandardItem('{}点'.format(ctime)),
                QStandardItem(signed),
            ])

