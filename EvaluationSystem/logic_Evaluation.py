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

        self.MyClear()

        # self.stu_eval_select()

    def slot_init(self):
        #列表点击
        self.tv_list_stu.selectionModel().selectionChanged.connect(self.tv_stu_row_sel_change)
        self.tv_list_coa.selectionModel().selectionChanged.connect(self.tv_coa_row_sel_change)

        self.bt_search_stu.clicked.connect(self.SearchStuSpecific)

        self.bt_search_coa.clicked.connect(self.SearchCoaSpecific)

        self.check_stu_openall.stateChanged.connect(self.check_stu)
        self.check_coa_openall.stateChanged.connect(self.check_coa)

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

    def refreshstu(self,item):
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
                else:
                    QMessageBox.information(self, '提示', '未查询到有关学员！', QMessageBox.Ok, QMessageBox.Ok)
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

                else:
                    QMessageBox.information(self, '提示', '未查询到有关教练！', QMessageBox.Ok, QMessageBox.Ok)
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
if __name__ == '__main__':
    import Login.CheckDBandFace as ckdf
    f1, MySQL = ckdf.CheckDB()
    MySQL.ConnectMySQL()
    app = QApplication(sys.argv)
    login = LogicEvaluationMain(MySQL=MySQL)
    login.show()
    sys.exit(app.exec_())