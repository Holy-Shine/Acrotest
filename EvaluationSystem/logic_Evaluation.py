from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QMessageBox, QLineEdit, QApplication, QTableView, QHeaderView
from qtpy import QtCore


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

    def init(self):
        self.listFunc.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)

        #列表初始化
        self.setTaleInit()


        self.listFunc.itemClicked.connect(self.refreshstu)

    def refreshstu(self,item):
        try:
            if(item.text()=='评价展示和查询(学生)'):
                self.SearchStuList(flag=True, info=None)
            elif (item.text() == '评价展示和查询(教练)'):
                self.SearchCoaList(flag=True, info=None)
        except Exception as e:
            print(e)

    #初始化表格
    def setTaleInit(self):
        # 学生列表初始化
        self.headers_stu = ['姓名', '联系方式','办卡种类']
        self.data_model_stu = QStandardItemModel()
        self.data_model_stu.setHorizontalHeaderLabels(self.headers_stu)
        self.tv_list_stu.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        self.tv_list_stu.setSelectionBehavior(QTableView.SelectRows)  # 选中行
        self.tv_list_stu.setModel(self.data_model_stu)
        self.tv_list_stu.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 教练表初始化
        self.headers_coa = ['姓名', '联系方式', '教练职称']
        self.data_model_coa = QStandardItemModel()
        self.data_model_coa.setHorizontalHeaderLabels(self.headers_coa)
        self.tv_list_coa.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        self.tv_list_coa.setSelectionBehavior(QTableView.SelectRows)  # 选中行
        self.tv_list_coa.setModel(self.data_model_coa)
        self.tv_list_coa.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        #查询刷新所有学生列表
        self.SearchStuList(flag= True,info = None)
        #查询刷新所有教练列表
        self.SearchCoaList(flag= True,info = None)

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
                (mem_phone like '%{}%' OR mem_name like '%{}%')'''.format(info, info)
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

if __name__ == '__main__':
    import Login.CheckDBandFace as ckdf
    f1, MySQL = ckdf.CheckDB()
    MySQL.ConnectMySQL()
    app = QApplication(sys.argv)
    login = LogicEvaluationMain(MySQL=MySQL)
    login.show()
    sys.exit(app.exec_())