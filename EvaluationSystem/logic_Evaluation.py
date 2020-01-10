from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QMessageBox, QLineEdit, QApplication, QTableView, QHeaderView, QTreeWidgetItem
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


        self.stu_eval_select()

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

        #学生评价树表的构造
        self.headers_stu_eval = ['时间', '学生','教练','是否签到', '评价']
        self.tv_eval_stu.setColumnCount(5)
        self.tv_eval_stu.setHeaderLabels(self.headers_stu_eval)
        self.tv_eval_stu.setColumnWidth(0,120)
        self.tv_eval_stu.setColumnWidth(1, 100)
        self.tv_eval_stu.setColumnWidth(2, 100)
        self.tv_eval_stu.setColumnWidth(3, 100)
        self.tv_eval_stu.setColumnWidth(4, 100)
        self.tv_eval_stu.clicked.connect(self.stu_eval_tree_click)

        #教练评价树表的构造
        self.headers_stu_eval =['时间', '学生','教练','是否签到', '评价']
        self.tv_eval_coa.setColumnCount(5)
        self.tv_eval_coa.setHeaderLabels(self.headers_stu_eval)
        self.tv_eval_coa.setColumnWidth(0, 120)
        self.tv_eval_coa.setColumnWidth(1, 100)
        self.tv_eval_coa.setColumnWidth(2, 100)
        self.tv_eval_coa.setColumnWidth(3, 100)
        self.tv_eval_coa.setColumnWidth(4, 100)


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

    #点击学生，显示评价列表
    def stu_eval_select(self):
        root1 = QTreeWidgetItem(self.tv_eval_stu)
        root1.setText(0, '2020年1月')

        child11 = QTreeWidgetItem(root1)
        child11.setText(0, '9号 周四')
        child12 = QTreeWidgetItem(root1)
        child12.setText(0, '10号 周五')

        child111 = QTreeWidgetItem(child11)
        child111.setText(0,'10点')
        child111.setText(1, '裴正蒙')
        child111.setText(2, '王安')
        child111.setText(3, '是')
        child111.setText(4, '暂无评价')

        child121 = QTreeWidgetItem(child12)
        child121.setText(0, '10点')
        child121.setText(1, '郑波')
        child121.setText(2, '王安')
        child121.setText(3, '是')
        child121.setText(4, '暂无人大大时代阿萨德阿萨德阿萨德若群若啊我去评价')

        root2 = QTreeWidgetItem(self.tv_eval_stu)
        root2.setText(0, '2019年12月')
        child21 = QTreeWidgetItem(root2)
        child21.setText(0, '31号 周二')
        root2.addChild(child21)

    #显示评价
    def stu_eval_tree_click(self):
        try:
            item = self.tv_eval_stu.currentItem()
            self.te_eval_stu.setText(item.text(4))
        except Exception as e:
            print(e)

if __name__ == '__main__':
    import Login.CheckDBandFace as ckdf
    f1, MySQL = ckdf.CheckDB()
    MySQL.ConnectMySQL()
    app = QApplication(sys.argv)
    login = LogicEvaluationMain(MySQL=MySQL)
    login.show()
    sys.exit(app.exec_())