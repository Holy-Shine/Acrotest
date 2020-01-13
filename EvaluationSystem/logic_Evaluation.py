from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QMessageBox, QLineEdit, QApplication, QTableView, QHeaderView, QTreeWidgetItem
from qtpy import QtCore
from Date2Week import DateAndWeek as weekfun

from EvaluationSystem.EvaluationMain import Ui_Evaluation
import sys

class LogicEvaluationMain(Ui_Evaluation,QDialog):
    def __init__(self,MySQL):
        super().__init__()
        self.setupUi(self)
        self.MySQL = MySQL
        self.stu_infodata = None
        self.coa_infodata = None


        self.type2card = {
            0:'轮滑',
            1:'滑步车',
            2:'体适能'
        }

        self.init()

        self.slot_init()

    def init(self):
        self.listFunc.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)

        #列表初始化
        self.setTaleInit()
        self.listFunc.itemClicked.connect(self.refreshstu)


        self.initUpdateForm()

        # self.MyClear()

        # self.stu_eval_select()

    def slot_init(self):
        #列表点击
        self.tv_list_stu.selectionModel().selectionChanged.connect(self.tv_stu_row_sel_change)
        self.tv_list_coa.selectionModel().selectionChanged.connect(self.tv_coa_row_sel_change)
        self.tv_classlist.selectionModel().selectionChanged.connect(self.tv_lesson_row_sel_change)

        self.bt_search_stu.clicked.connect(self.SearchStuSpecific)

        self.bt_search_coa.clicked.connect(self.SearchCoaSpecific)

        self.check_stu_openall.stateChanged.connect(self.check_stu)
        self.check_coa_openall.stateChanged.connect(self.check_coa)


        #更改时间，刷新列表
        self.cb_year.currentIndexChanged.connect(self.refresh_lesson_table)
        self.cb_weekday.currentIndexChanged.connect(self.refresh_lesson_table)
        self.cb_weekj.currentIndexChanged.connect(self.refresh_lesson_table)

        self.bt_confrim.clicked.connect(self.UpdateEval)
        self.bt_clear.clicked.connect(self.clearEvalInfo)


    #初始化更新界面
    def initUpdateForm(self):

        #信息展示不可见修改
        self.et_coaname.setEnabled(False)
        self.et_classdate.setEnabled(False)
        self.et_stuname.setEnabled(False)
        self.et_stuphone.setEnabled(False)
        self.et_classtime.setEnabled(False)
        self.et_stuclasstype.setEnabled(False)
        #初始化
        weekday = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
        year,mon,day =  weekfun.getCurrentYMD()
        self.cb_year.addItems([str(year-1),str(year)])
        self.cb_weekday.addItems(weekday)
        for i in range(53):
            self.cb_weekj.addItem('第{}周'.format(i+1))

        #选定当前日期
        self.cb_year.setCurrentIndex(1)
        week, weekday = weekfun.FromDatetoWeek(year=year,month=mon,day=day)
        self.cb_weekj.setCurrentIndex(int(week)-1)
        self.cb_weekday.setCurrentIndex(int(weekday)-1)
        self.lb_date.setText('{}年{}月{}日 周{}'.format(year,mon,day,weekday))

        #初始化今天的任务


        #课程列表表头初始化
        self.headers_StudentList = ['姓名', '科目种类', '上课时间', '教练', '是否签到','是否评价']
        self.class_data_model = QStandardItemModel()
        # 学生表初始化
        self.class_data_model.setHorizontalHeaderLabels(self.headers_StudentList)
        self.tv_classlist.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        self.tv_classlist.setSelectionBehavior(QTableView.SelectRows)  # 选中行
        self.tv_classlist.setModel(self.class_data_model)
        self.tv_classlist.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)



    def MyClear(self):
        # 查询刷新所有学生列表
        self.SearchStuList(flag=True, info=None)
        # 查询刷新所有教练列表
        self.SearchCoaList(flag=True, info=None)

        self.check_coa_openall.setEnabled(False)
        self.check_stu_openall.setEnabled(False)

        self.te_eval_stu.clear()
        self.tv_eval_stu.clear()
        self.te_eval_coa.clear()
        self.tv_eval_coa.clear()

        self.clearinsertinfo()
        #当前课表时间刷新
        # year, mon, day = weekfun.getCurrentYMD()
        # week, weekday = weekfun.FromDatetoWeek(year=year, month=mon, day=day)
        # self.cb_weekj.setCurrentIndex(int(week) - 1)
        # self.cb_weekday.setCurrentIndex(int(weekday) - 1)
        # self.lb_date.setText('{}年{}月{}日 周{}'.format(year, mon, day, weekday))
        # self.lb_date.setText('{}年{}月{}日 周{}'.format(year, mon, day, weekday))


    def clearinsertinfo(self):
        self.et_stuname.clear()
        self.et_stuphone.clear()
        self.et_stuclasstype.clear()
        self.et_classdate.clear()
        self.et_classtime.clear()
        self.et_coaname.clear()
        self.et_eval_insert.clear()

    def refreshstu(self,item):
        self.clearinsertinfo()
        try:
            self.lb_stu_eval_num.setText('暂无评价信息')
            self.lb_stu_eval_num.setText('暂无评价信息')
            self.check_coa_openall.setEnabled(False)
            self.check_stu_openall.setEnabled(False)
            if(item.text()=='评价展示和查询(学生)'):
                self.te_eval_stu.clear()
                self.tv_eval_stu.clear()

            elif (item.text() == '评价展示和查询(教练)'):
                self.te_eval_coa.clear()
                self.tv_eval_coa.clear()

            if not self.et_search_coa.text() == '' or not self.et_search_stu.text()=='':
                self.et_search_coa.clear()
                self.et_search_stu.clear()
                self.SearchCoaList(flag=True, info=None)
                self.SearchStuList(flag=True, info=None)

        except Exception as e:
            print(e)

    #初始化表格
    def setTaleInit(self):
        # 学生列表初始化
        self.headers_stu = ['联系方式', '姓名','办卡种类']
        self.data_model_stu = QStandardItemModel()
        self.data_model_stu.setHorizontalHeaderLabels(self.headers_stu)
        self.tv_list_stu.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        self.tv_list_stu.setSelectionBehavior(QTableView.SelectRows)  # 选中行
        self.tv_list_stu.setModel(self.data_model_stu)
        self.tv_list_stu.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 教练表初始化
        self.headers_coa = ['联系方式', '姓名', '教练职称']
        self.data_model_coa = QStandardItemModel()
        self.data_model_coa.setHorizontalHeaderLabels(self.headers_coa)
        self.tv_list_coa.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        self.tv_list_coa.setSelectionBehavior(QTableView.SelectRows)  # 选中行
        self.tv_list_coa.setModel(self.data_model_coa)
        self.tv_list_coa.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        #学生评价树表的构造
        self.headers_stu_eval = ['时间', '学生','教练','是否签到', '评价']
        self.tv_eval_stu.setColumnCount(5)
        self.tv_eval_stu.setHeaderLabels(self.headers_stu_eval)
        self.tv_eval_stu.setColumnWidth(0,130)
        self.tv_eval_stu.setColumnWidth(1, 100)
        self.tv_eval_stu.setColumnWidth(2, 100)
        self.tv_eval_stu.setColumnWidth(3, 100)
        self.tv_eval_stu.setColumnWidth(4, 100)
        self.tv_eval_stu.clicked.connect(self.stu_eval_tree_click)

        #教练评价树表的构造
        self.headers_stu_eval =['时间', '学生','教练','是否签到', '评价']
        self.tv_eval_coa.setColumnCount(5)
        self.tv_eval_coa.setHeaderLabels(self.headers_stu_eval)
        self.tv_eval_coa.setColumnWidth(0, 130)
        self.tv_eval_coa.setColumnWidth(1, 100)
        self.tv_eval_coa.setColumnWidth(2, 100)
        self.tv_eval_coa.setColumnWidth(3, 100)
        self.tv_eval_coa.setColumnWidth(4, 100)
        self.tv_eval_coa.clicked.connect(self.coa_eval_tree_click)

    # 查询刷新学生列表
    def SearchStuList(self,flag,info):
        try:
            if(flag):
                sql = '''SELECT mem_phone, mem_name, mem_type FROM mem_info'''
            else:
                sql = '''SELECT mem_phone, mem_name, mem_type FROM mem_info WHERE  
                (mem_phone like '%{}%' OR mem_name like '%{}%')'''.format(info, info)
            print(sql)
            flag, self.stu_infodata = self.MySQL.SelectFromDataBse(sql)
            if (flag):
                if (len(self.stu_infodata) > 0):
                    self.add_stu_list()
                # else:
                    # QMessageBox.information(self, '提示', '未查询到有关学员！', QMessageBox.Ok, QMessageBox.Ok)
            else:
                QMessageBox.information(self, '提示', '查询失败！', QMessageBox.Ok, QMessageBox.Ok)
        except Exception as e:
            print(e)

    # 查询刷新教练列表
    def SearchCoaList(self,flag,info):
        try:
            if(flag):
                sql = '''SELECT coa_phone, coa_name, coa_rank FROM coach'''
            else:
                sql = '''SELECT coa_phone, coa_name, coa_rank FROM coach WHERE  
                (coa_phone like '%{}%' OR coa_name like '%{}%')'''.format(info, info)
            print(sql)
            flag, self.coa_infodata = self.MySQL.SelectFromDataBse(sql)
            if (flag):
                if (len(self.coa_infodata) > 0):
                    self.add_coa_list()

                # else:
                    # QMessageBox.information(self, '提示', '未查询到有关教练！', QMessageBox.Ok, QMessageBox.Ok)
            else:
                QMessageBox.information(self, '提示', '查询失败！', QMessageBox.Ok, QMessageBox.Ok)
        except Exception as e:
            print(e)

    # 学生界面查询
    def SearchStuSpecific(self):
        if(self.et_search_stu.text()==''):
            QMessageBox.information(self, '提示', '请输入内容！', QMessageBox.Ok, QMessageBox.Ok)
        self.SearchStuList(flag=False, info=self.et_search_stu.text())

    def SearchCoaSpecific(self):
        if(self.et_search_coa.text()==''):
            QMessageBox.information(self, '提示', '请输入内容！', QMessageBox.Ok, QMessageBox.Ok)
        self.SearchCoaList(flag=False, info=self.et_search_coa.text())

    #刷新学生表格
    def add_stu_list(self):
        self.data_model_stu.clear()
        self.data_model_stu.setHorizontalHeaderLabels(self.headers_stu)
        for i, (mem_phone, mem_name, mem_type) in enumerate(self.stu_infodata):
            self.data_model_stu.appendRow([
                QStandardItem(mem_phone),
                QStandardItem(mem_name),
                QStandardItem(self.type2card[mem_type]),
            ])

    #刷新教练表格
    def add_coa_list(self):
        self.data_model_coa.clear()
        self.data_model_coa.setHorizontalHeaderLabels(self.headers_coa)
        for i, (coa_phone, coa_name, coa_type) in enumerate(self.coa_infodata):
            self.data_model_coa.appendRow([
                QStandardItem(coa_phone),
                QStandardItem(coa_name),
                QStandardItem(coa_type),
            ])

    #点击学生，显示评价列表
    def tv_stu_row_sel_change(self):
        self.tv_eval_stu.clear()
        self.check_stu_openall.setChecked(False)
        try:
            current_row = self.tv_list_stu.currentIndex().row()
            if current_row < len(self.stu_infodata):
                result = self.stu_infodata[current_row]
                sql = 'select * from mem_class where mem_phone=\'{}\' and mem_name = \'{}\' and mem_type = {}'\
                    .format(result[0],result[1],result[2])
                print(sql)
                flag, self.stu_class_item = self.MySQL.SelectFromDataBse(sql)
                if(flag and len(self.stu_class_item)>0):
                    self.lb_stu_eval_num.setText('一共找到{}条评价信息'.format(len(self.stu_class_item)))
                    self.stu_eval_select()
                    self.check_stu_openall.setEnabled(True)
        except Exception as e:
            print(e)

    def tv_coa_row_sel_change(self):
        self.tv_eval_coa.clear()
        self.check_coa_openall.setChecked(False)
        try:
            current_row = self.tv_list_coa.currentIndex().row()
            if current_row < len(self.coa_infodata):
                result = self.coa_infodata[current_row]
                sql = 'select * from mem_class where mem_coa_name=\'{}\''.format(result[1])
                print(sql)
                flag, self.coa_class_item = self.MySQL.SelectFromDataBse(sql)
                if(flag and len(self.coa_class_item)>0):
                    self.lb_coa_eval_num_2.setText('一共找到{}条评价信息'.format(len(self.coa_class_item)))
                    self.coa_eval_select()
                    self.check_coa_openall.setEnabled(True)
        except Exception as e:
            print(e)

    #展示数据
    #学生界面
    def stu_eval_select(self):
        #规则化数据
        stu_eval_info = self.redata(self.stu_class_item)
        year_list = sorted(stu_eval_info, reverse=True)
        for item in year_list:
            #第一层
            root = QTreeWidgetItem(self.tv_eval_stu)
            year_mon = item.split('-')
            root.setText(0,'{}年{}月'.format(year_mon[0],year_mon[1]))

            #第二层
            dianlist = sorted(stu_eval_info[item], reverse=True)
            for item2 in dianlist:
                root2 = QTreeWidgetItem(root)
                day_weekday = item2.split('-')
                root2.setText(0,'{}日 周{}'.format(day_weekday[0],day_weekday[1]))
            #第三层
                sp_info = stu_eval_info[item][item2]
                sp_info = sorted(sp_info, key=lambda sp_info: sp_info[0])
                for item3 in sp_info:
                    child = QTreeWidgetItem(root2)
                    child.setText(0, '{}点'.format(item3[0]))
                    child.setText(1, str(item3[1]))
                    child.setText(2, str(item3[2]))
                    if (item3[3] == 0):
                        child.setText(3, '否')
                    else:
                        child.setText(3, '是')
                    if(item3[4] == None):
                        child.setText(4, '暂无评价')
                    else:
                        child.setText(4, item3[4])

    #教练界面
    def coa_eval_select(self):
        # 规则化数据
        coa_eval_info = self.redata(self.coa_class_item)
        year_list = sorted(coa_eval_info, reverse=True)
        for item in year_list:
            # 第一层
            root = QTreeWidgetItem(self.tv_eval_coa)
            year_mon = item.split('-')
            root.setText(0, '{}年{}月'.format(year_mon[0], year_mon[1]))

            # 第二层
            dianlist = sorted(coa_eval_info[item], reverse=True)
            for item2 in dianlist:
                root2 = QTreeWidgetItem(root)
                day_weekday = item2.split('-')
                root2.setText(0, '{}日 周{}'.format(day_weekday[0], day_weekday[1]))
                # 第三层
                sp_info = coa_eval_info[item][item2]
                sp_info = sorted(sp_info, key=lambda sp_info: sp_info[0])
                for item3 in sp_info:
                    child = QTreeWidgetItem(root2)
                    child.setText(0, str(item3[0]))
                    child.setText(1, str(item3[1]))
                    child.setText(2, str(item3[2]))
                    if (item3[3] == 0):
                        child.setText(3, '否')
                    else:
                        child.setText(3, '是')
                    if (item3[4] == None):
                        child.setText(4, '暂无评价')
                    else:
                        child.setText(4, item3[4])

    #规则化数据
    def redata(self,data):
        first = {}
        for i, (phone, name, type, coach, year, week, weekday, dian, evaluation, signed) in enumerate(data):
            _, mon, day = weekfun.FromWeektoDate(year, week - 1, weekday)

            # 第一层：年月
            if (mon < 10):
                mon = '0{}'.format(mon)
            if (day < 10):
                day = '0{}'.format(day)
            yearandmon = '{}-{}'.format(year, mon)
            if not yearandmon in first:
                first.update({yearandmon: {}})

            # 第二层 日期和周数
            dayandweekday = '{}-{}'.format(day, weekday)
            second = first[yearandmon]
            if not dayandweekday in second:
                second.update({dayandweekday: []})

            # 第三层，具体数据
            info = second[dayandweekday]
            data = [dian, name, coach, signed, evaluation]
            info.append(data)
            second.update({dayandweekday: info})
            first.update({yearandmon: second})
        return first

    #显示评价
    def stu_eval_tree_click(self):
        item = self.tv_eval_stu.currentItem()
        self.te_eval_stu.setText(item.text(4))

    def coa_eval_tree_click(self):
        item = self.tv_eval_coa.currentItem()
        self.te_eval_coa.setText(item.text(4))


    #全部展示or not
    def check_stu(self):
        if(self.check_stu_openall.isChecked()):
            self.tv_eval_stu.expandAll()
        else:
            self.tv_eval_stu.collapseAll()

    def check_coa(self):
        if (self.check_coa_openall.isChecked()):
            self.tv_eval_coa.expandAll()
        else:
            self.tv_eval_coa.collapseAll()


    #录入评价的界面
    def refresh_lesson_table(self):

        self.class_data_model.clear()
        self.class_data_model.setHorizontalHeaderLabels(self.headers_StudentList)

        year = self.cb_year.currentText()
        week = self.cb_weekj.currentIndex()+1
        weekday = self.cb_weekday.currentIndex()+1
        _,mon,day = weekfun.FromWeektoDate(year,week-1,weekday)
        self.lb_date.setText('{}年{}月{}日 周{}'.format(year, mon, day, weekday))
        try:
            sql = 'select * from mem_class where year={} and week = {} and cday = {}'\
                                .format(year,week,weekday)
            print(sql)
            flag, self.lesson_item = self.MySQL.SelectFromDataBse(sql)
            if (flag):
                if (len(self.lesson_item) > 0):
                    self.add_lesson()
                # else:
                #     print(None)
        except Exception as e:
            print(e)

    # self.headers_StudentList = ['姓名', '科目种类', '上课时间', '教练', '是否签到']
    def add_lesson(self):
        for i, (_, mem_name, mem_type,mem_coa_name,_,_,_,ctime,eval, mem_signed) in enumerate(self.lesson_item):
            #是否签到
            if mem_signed == 0:
                signed = '否'
            else:
                signed = '是'


            #有评价
            if eval == None:
                e = '否'
            else:
                e = '是'


            self.class_data_model.appendRow([
                QStandardItem(mem_name),
                QStandardItem(self.type2card[mem_type]),
                QStandardItem('{}点'.format(ctime)),
                QStandardItem(mem_coa_name),
                QStandardItem(signed),
                QStandardItem(e),
            ])


    def tv_lesson_row_sel_change(self):
        try:
            current_row = self.tv_classlist.currentIndex().row()
            if current_row < len(self.lesson_item):
                self.current_lesson = self.lesson_item[current_row]
                self.et_stuname.setText(self.current_lesson[1])
                self.et_stuphone.setText(self.current_lesson[0])
                self.et_stuclasstype.setText(self.type2card[self.current_lesson[2]])
                self.et_classdate.setText(self.lb_date.text())
                self.et_classtime.setText('{}点'.format(self.current_lesson[7]))
                self.et_coaname.setText(self.current_lesson[3])
                #添加评价信息
                if not self.current_lesson[8] == None:
                    self.et_eval_insert.setPlainText(self.current_lesson[8])
        except Exception as e:
            print(e)

    #评价录入按钮
    def UpdateEval(self):
        if(self.et_stuname.text()==''):
            QMessageBox.information(self, '提示', '请选择学生！', QMessageBox.Ok, QMessageBox.Ok)
        elif(self.et_eval_insert.toPlainText()==''):
            QMessageBox.information(self, '提示', '请输入具体评价内容！', QMessageBox.Ok, QMessageBox.Ok)
        else:
            if(self.current_lesson[9]==1):
                self.InsetEval()
            else:
                reply = QMessageBox.warning(self, '提示', '该课程显示未签到\n，是否继续录入?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                if reply == QMessageBox.Yes:
                    self.InsetEval()



    def InsetEval(self):
        hint = '学生姓名：{}\n联系方式：{}\n课程种类：{}\n上课时间：{}'.format(
            self.current_lesson[1],
            self.current_lesson[0],
            self.type2card[self.current_lesson[2]],
            '{} {}'.format(self.et_classdate.text(), self.et_classtime.text())
        )
        reply = QMessageBox.warning(self, '确认信息', hint, QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            try:
                sql = 'UPDATE  mem_class  SET coa_eval=\'{}\' WHERE ' \
                      'mem_phone=\'{}\' ' \
                      'and mem_name=\'{}\' ' \
                      'and mem_type={} ' \
                      'and mem_coa_name=\'{}\' ' \
                      'and year={} ' \
                      'and week={} ' \
                      'and cday={} ' \
                      'and ctime={}'.format(
                    self.et_eval_insert.toPlainText(),
                    self.current_lesson[0],
                    self.current_lesson[1],
                    self.current_lesson[2],
                    self.current_lesson[3],
                    self.current_lesson[4],
                    self.current_lesson[5],
                    self.current_lesson[6],
                    self.current_lesson[7],
                )
                print(sql)
                flag1 = self.MySQL.UpdateFromDataBse(sql)
                if(flag1):
                    self.clearinsertinfo()
                    self.refresh_lesson_table()
                    QMessageBox.information(self, '提示', '录入成功！', QMessageBox.Ok, QMessageBox.Ok)
                else:
                    QMessageBox.information(self, '提示', '录入失败！', QMessageBox.Ok, QMessageBox.Ok)
            except Exception as e:
                print(e)



    def clearEvalInfo(self):
        self.et_eval_insert.clear()

if __name__ == '__main__':
    import Login.CheckDBandFace as ckdf
    f1, MySQL = ckdf.CheckDB()
    MySQL.ConnectMySQL()
    app = QApplication(sys.argv)
    login = LogicEvaluationMain(MySQL=MySQL)
    login.show()
    sys.exit(app.exec_())