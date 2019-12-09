from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QMessageBox, QLineEdit, QApplication, QTableView, QHeaderView
from qtpy import QtCore

from StudentSystem.StudentMain import Ui_StudentMain
from CoachSystem.logic_verify import logicVerify
from StudentSystem.Logic_BasicInfoModify import LogicModifyInfo
import sys

class LogicStudentMain(Ui_StudentMain,QDialog):
    def __init__(self,MySQL):
        super().__init__()
        self.setupUi(self)
        self.MySQL = MySQL

        self.init()
        self.slot_init()
        self.frash_studentList()


    def init(self):
        self.headers_StudentList = ['联系方式', '姓名', '科目种类','剩余次数','学生性别','学生年龄','办卡种类','人脸信息']
        self.data_model = QStandardItemModel()
        # 学生表初始化
        self.data_model.setHorizontalHeaderLabels(self.headers_StudentList)
        self.table_studentList.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        self.table_studentList.setSelectionBehavior(QTableView.SelectRows)  # 选中行
        self.table_studentList.setModel(self.data_model)
        self.table_studentList.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 学员查询数据
        self.data_meminfo_search = None

        #设置修改和查询界面不可用
        self.bt_modifyinfo.setEnabled(False)
        self.bt_checkclass.setEnabled(False)


        self.cardtype = {
            '轮滑': 0,
            '平衡车': 1
        }

        self.type2card = {
            0:'轮滑',
            1:'平衡车'
        }

        self.meminfo_data = {
            '学生姓名': '',
            '学生性别': '',
            '学生年龄': '',
            '学生家长': '',
            '联系方式': '',
            '课程种类': '',  # 平衡车or轮滑
            '课时次数': '',
            '办卡种类': '',  # 年卡，月卡，季度卡等等
        }

    #学生数据清空
    def meminfoclear(self):
        self.meminfo_data = {
            '学生姓名': '',
            '学生性别': '',
            '学生年龄': '',
            '学生家长': '',
            '联系方式': '',
            '课程种类': '',  # 平衡车or轮滑
            '课时次数': '',
            '办卡种类': '',  # 年卡，月卡，季度卡等等
        }


    def slot_init(self):
        self.bt_flash.clicked.connect(self.frash_studentList)
        #表内选择
        self.table_studentList.selectionModel().selectionChanged.connect(self.row_sel_change)
        #修改信息，打开二级密码账户
        self.bt_modifyinfo.clicked.connect(self.modify_meminfo)
        #根据电话号码查询
        self.bt_search.clicked.connect(self.search_for_studentinfo)

    #添加表格
    def add_table(self):
        self.data_model.clear()
        self.data_model.setHorizontalHeaderLabels(self.headers_StudentList)
        for i, (mem_phone, mem_name, mem_type, mem_age, mem_parent,
                mem_gender, mem_cls_left, mem_cardtype, mem_face) in enumerate(self.data_meminfo_search):
            if (mem_face == b'NULL'):
                face = '否'
            else:
                face = '是'
            self.data_model.appendRow([
                QStandardItem(mem_phone),
                QStandardItem(mem_name),
                QStandardItem(self.type2card[mem_type]),
                QStandardItem(str(mem_cls_left)),
                QStandardItem(mem_gender),
                QStandardItem(str(mem_age)),
                QStandardItem(mem_cardtype),
                QStandardItem(face),
            ])


    #查询数据库，更新最新的学生列表
    def frash_studentList(self):
        # 设置修改和查询界面不可用
        self.bt_modifyinfo.setEnabled(False)
        self.bt_checkclass.setEnabled(False)
        try:
            sql = 'select * from mem_info'
            flag,self.data_meminfo_search = self.MySQL.SelectFromDataBse(sql)
            if(flag):
                self.add_table()
        except Exception as e:
            print(e)

    #
    def row_sel_change(self):
        try:
            current_row = self.table_studentList.currentIndex().row()
            if current_row < len(self.data_meminfo_search):
                result = self.data_meminfo_search[current_row]
                self.addtomeminfo_data(result)
                self.bt_modifyinfo.setEnabled(True)
                self.bt_checkclass.setEnabled(True)
        except Exception as e:
            print(e)

    def addtomeminfo_data(self,result):
        try:
            self.meminfo_data['联系方式'] = result[0]
            self.meminfo_data['学生姓名'] = result[1]
            self.meminfo_data['课程种类'] = result[2]
            self.meminfo_data['学生年龄'] = result[3]
            self.meminfo_data['学生家长'] = result[4]
            self.meminfo_data['学生性别'] = result[5]
            self.meminfo_data['课时次数'] = result[6]
            self.meminfo_data['办卡种类'] = result[7]
        except Exception as e:
            print(e)

    def modify_meminfo(self):
        try:
            self.FormVerify = logicVerify()
            self.FormVerify.setWindowModality(QtCore.Qt.ApplicationModal)
            self.FormVerify.show()
            if self.FormVerify.exec() == 1:
                self.FormModify = LogicModifyInfo(MySQL=self.MySQL,BasicInfo = self.meminfo_data)
                self.FormModify.setWindowModality(QtCore.Qt.ApplicationModal)
                self.FormModify.show()
                if(self.FormModify.exec() == 1):
                    self.frash_studentList()
        except Exception as e:
            print(e)

    # 根据电话号码查询学生信息列表
    def search_for_studentinfo(self):
        phonenum = self.et_search.text()
        if not (self.PhoneCheck(phonenum)):
            QMessageBox.warning(self, u"Warning", u"请输入正确的11位电话号码格式",
                                buttons=QMessageBox.Ok)
        else:
            sql = 'SELECT * FROM mem_info WHERE  mem_phone=\'{}\''.format(phonenum)
            try:
                flag, self.data_meminfo_search = self.MySQL.SelectFromDataBse(sql)
                if (flag):
                    self.add_table()
                    self.et_search.clear()
                else:
                    QMessageBox.information(self, '提示', '查询失败！', QMessageBox.Ok, QMessageBox.Ok)
            except Exception as e:
                print(e)

    #确认是电话号码
    def PhoneCheck(self,s):
        # 检测号码是否长度是否合法。
        if len(s) != 11:
            return False
        elif(s.isdigit()):
            return True
        else:
            return False




if __name__ == '__main__':
    from ConnecMySQL.MySQLBase import MySQLBaseFunction

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
    login = LogicStudentMain(MySQL=MySQL)
    login.show()
    sys.exit(app.exec_())