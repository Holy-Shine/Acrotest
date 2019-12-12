import os,json
from PyQt5.QtWidgets import QDialog,QMessageBox,QTableView,QHeaderView, QListWidget, QStackedWidget
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from PyQt5.QtCore import *
from PyQt5.QtGui import  *


from CoachSystem.Ui_syscoach import Ui_sysCoach
from CoachSystem.logic_verify import logicVerify

class logicSysCoach(Ui_sysCoach, QDialog):
    def __init__(self,MySQL):
        super().__init__()
        self.setupUi(self)  
        self.MySQL = MySQL
        self.listFunc.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)   # list和右边窗口index绑定 
        self.listFunc.currentRowChanged.connect(self.init_upcoach)

        self.btn_confirm.clicked.connect(self.on_button_add_coach)
        self.btn_clear.clicked.connect(self.clear_add)

        self.tv_search_coach.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        self.tv_search_coach.setSelectionBehavior(QTableView.SelectRows) # 选中行

        # self.verify = False  # 默认未验证
        self.headers = ['联系方式','姓名','职级','类别']
        self.data_model = QStandardItemModel()
        self.data_model.setHorizontalHeaderLabels(self.headers)
        self.data = []
        self.tv_search_coach.setModel(self.data_model)
        self.tv_search_coach.selectionModel().selectionChanged.connect(self.row_sel_change) # 选中事件

        self.tv_search_coach.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        self.btn_search.clicked.connect(self.on_button_search)

        self.btn_confirm_2.clicked.connect(self.on_button_update)

        self.btn_remove.clicked.connect(self.on_button_remove)
    
        self.btn_verify.clicked.connect(self.on_button_verify)

        self.btn_search.setShortcut(Qt.Key_Return)
        self.listFunc.setCurrentRow(0)

    def init_upcoach(self):
        self.btn_remove.setEnabled(False)
        self.btn_confirm_2.setEnabled(False)
        self.lb_status.setText('当前状态：未认证')
        self.btn_verify.setEnabled(True)

    def on_button_verify(self):
        # 二级密码验证
        veriWin = logicVerify()
        veriWin.myshow()
        if veriWin.exec() == 1:
            self.btn_remove.setEnabled(True)
            self.btn_confirm_2.setEnabled(True)
            self.lb_status.setText('当前状态：已认证')
            self.btn_verify.setEnabled(False)
        


    def on_button_remove(self):
        crow = self.tv_search_coach.currentIndex().row()
        if crow == -1:
            QMessageBox.warning(self, '提示','未选中任何教练！', QMessageBox.Yes, QMessageBox.Yes)    

        else:

            sql = '''
            DELETE FROM coach WHERE coa_phone=\"{}\"
            '''.format(self.data[crow][0])

            types = ['轮滑','平衡车','均可']
            hint = '教练姓名：{}\n性别：{}\n联系方式：{}\n职级：{}\n类别：{}'.format(
                                                    self.data[crow][1], 
                                                    self.data[crow][2], 
                                                    self.data[crow][0], 
                                                    self.data[crow][3],
                                                    types[int(self.data[crow][4])]
                                                )

            reply = QMessageBox.warning(self, '确认删除下列教练？',hint, QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)
            print(sql)
            if reply == QMessageBox.Yes:
                try:
                    # conn = pymysql.connect(
                    #     host='121.199.17.205',
                    #     user='Jessie',
                    #     password='Jessie.121406',
                    #     database = 'meminfo',
                    #     port = 3306,
                    #     charset='utf8'
                    # )
                    # cursor = conn.cursor()
                    # cursor.execute(sql)
                    # conn.commit()
                    # conn.close()
                    flag= self.MySQL.DeleteFromDataBse(sql)
                    if(flag ==True):
                        self.data.remove(self.data[self.tv_search_coach.currentIndex().row()])
                        self.data_model.removeRow(self.tv_search_coach.currentIndex().row())
                        

                        QMessageBox.information(self, '提示', '删除成功！',QMessageBox.Ok,QMessageBox.Ok)
                        
                    else:
                        QMessageBox.information(self, '提示', '删除失败！', QMessageBox.Ok, QMessageBox.Ok)
                except Exception as e:
                    print(e)
                    QMessageBox.critical(self,'错误','数据库异常！',QMessageBox.Ok,QMessageBox.Ok)     

    def on_button_update(self):
        crow = self.tv_search_coach.currentIndex().row()
        if crow == -1:
            QMessageBox.warning(self, '提示','未选中任何教练！', QMessageBox.Yes, QMessageBox.Yes)
        

        else:
            types= ['轮滑','平衡车','均可']
            n_phone = self.le_c_phone_3.text()
            n_name = self.le_c_name_3.text()    
            n_gender = self.cb_c_gender_3.currentText()
            n_rank = self.comboBox_4.currentText()
            n_type =self.comboBox_3.currentIndex()     
            n_info = self.te_cmsg_2.toPlainText()   



            sql = '''
                UPDATE  coach  SET
                    coa_phone = \'{}\',
                    coa_name = \'{}\',
                    coa_gender = \'{}\',
                    coa_rank = \'{}\',
                    coa_type = {},
                    coa_info = \'{}\' 
                WHERE
                    coa_phone = \'{}\';
                    
                '''.format(
                                    n_phone, 
                                    n_name, 
                                    n_gender, 
                                    n_rank,
                                    n_type,
                                    n_info, self.data[crow][0])

            hint = '教练姓名：{}\n性别：{}\n联系方式：{}\n职级：{}\n类别：{}'.format(
                                                    n_name, 
                                                    n_gender, 
                                                    n_phone, 
                                                    n_rank,
                                                    types[int(n_type)]
                                                )

            print(sql)
            reply = QMessageBox.warning(self, '更新确认信息',hint, QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)
            print(sql)
            if reply == QMessageBox.Yes:
                try:
                    # conn = pymysql.connect(
                    #     host='121.199.17.205',
                    #     user='Jessie',
                    #     password='Jessie.121406',
                    #     database = 'meminfo',
                    #     port = 3306,
                    #     charset='utf8'
                    # )
                    # cursor = conn.cursor()
                    # cursor.execute(sql)
                    # conn.commit()
                    # conn.close()
                    # QMessageBox.information(self, '提示', '更新成功！',QMessageBox.Ok,QMessageBox.Ok)
                    flag = self.MySQL.UpdateFromDataBse(sql)
                    if (flag == True):
                        QMessageBox.information(self, '提示', '更新成功！', QMessageBox.Ok, QMessageBox.Ok)
                    else:
                        QMessageBox.information(self, '提示', '更新失败！', QMessageBox.Ok, QMessageBox.Ok)
                except Exception as e:
                    print(e)
                    QMessageBox.critical(self,'错误','数据库异常！',QMessageBox.Ok,QMessageBox.Ok)     

    def row_sel_change(self):
        current_row = self.tv_search_coach.currentIndex().row()
        print(current_row)
        ranks = ['助教','初级','中级','高级']
        
        if  current_row < len(self.data):
            phone = self.data[current_row][0]
            name = self.data[current_row][1]
            rank = ranks.index(self.data[current_row][3])
            ctype = int(self.data[current_row][4])
            info = self.data[current_row][-1]



            self.le_c_phone_3.setText(phone)
            self.le_c_name_3.setText(name)
            self.comboBox_4.setCurrentIndex(rank)
            self.comboBox_3.setCurrentIndex(ctype)
            self.te_cmsg_2.setText(info)
        # else:
        #     self.le_choose_name.setText('')
        #     self.le_choose_phone.setText('')


        
        
    def clear_add(self):
        '''清空添加教练内容
        '''
        self.le_c_phone.setText('')
        self.le_c_name.setText('')
        self.te_cmsg.setText('')
    
    def on_button_search(self):

        # 检查有效性
        if self.le_search_term.text()=='':
            QMessageBox.warning(self, '提示','搜索关键字不能为空！', QMessageBox.Yes, QMessageBox.Yes)
    
        else:
            # 清空表
            self.data_model.clear()
            self.data_model.setHorizontalHeaderLabels(self.headers)    
            if self.le_search_term.text()=='*':
                sql = '''
                SELECT * FROM coach
                ''' 
            else:
                sql = '''
                    SELECT * FROM coach WHERE coa_name like \"%{}%\" or coa_phone like  \"%{}%\" or coa_rank like \"%{}%\"
                '''.format(self.le_search_term.text(),self.le_search_term.text(),self.le_search_term.text())
            try:
                flag,result = self.MySQL.SelectFromDataBse(sql)
                if (flag == True):
                    self.data = list(result)
                    self.lb_result.setText('共搜索到 {} 条记录'.format(len(self.data)))
                    types = ['轮滑', '平衡车', '均可']
                    for i, (coa_phone, coa_name, coa_gender, coa_rank, coa_type, coa_info) in enumerate(self.data):
                        self.data_model.appendRow([
                            QStandardItem(coa_phone),
                            QStandardItem(coa_name),
                            QStandardItem(coa_rank),
                            QStandardItem(types[int(coa_type)])
                        ])
                else:
                    QMessageBox.information(self, '提示', '查询失败！', QMessageBox.Ok, QMessageBox.Ok)
            except Exception as e:
                print(e)
                QMessageBox.critical(self,'错误','数据库异常！',QMessageBox.Ok,QMessageBox.Ok)            

    def on_button_add_coach(self):
        
        # 检查有效性
        if self.le_c_name.text()=='':
            QMessageBox.warning(self, '提示','教练名字不能为空！', QMessageBox.Yes, QMessageBox.Yes)

        elif self.le_c_phone.text()=='':
            QMessageBox.warning(self, '提示','教练联系方式不能为空！', QMessageBox.Yes, QMessageBox.Yes)


        else:
            types = ['轮滑','平衡车','均可']
            sql = 'INSERT INTO coach  VALUES(\'{}\', \'{}\',\'{}\',\'{}\',{},\'{}\')'.format(
                                    self.le_c_phone.text(), 
                                    self.le_c_name.text(), 
                                    self.cb_c_gender.currentText(), 
                                    self.cb_a_rank.currentText(),
                                    self.cb_a_type.currentIndex(),
                                    self.te_cmsg.toPlainText()
                                )

            hint = '教练姓名：{}\n性别：{}\n联系方式：{}\n职级：{}\n类别：{}'.format(
                                                    self.le_c_name.text(), 
                                                    self.cb_c_gender.currentText(), 
                                                    self.le_c_phone.text(), 
                                                    self.cb_a_rank.currentText(),
                                                    types[self.cb_a_type.currentIndex()]
                                                )

            reply = QMessageBox.warning(self, '确认信息',hint, QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)
            print(sql)
            if reply == QMessageBox.Yes:
                try:
                    # conn = pymysql.connect(
                    #     host='121.199.17.205',
                    #     user='Jessie',
                    #     password='Jessie.121406',
                    #     database = 'meminfo',
                    #     port = 3306,
                    #     charset='utf8'
                    # )
                    # cursor = conn.cursor()
                    # cursor.execute(sql)
                    # conn.commit()
                    # QMessageBox.information(self, '提示', '录入成功！',QMessageBox.Ok,QMessageBox.Ok)
                    #
                    # conn.close()
                        flag = self.MySQL.InsertFromDataBse(sql)
                        if (flag == True):
                            QMessageBox.information(self, '提示', '录入成功！', QMessageBox.Ok, QMessageBox.Ok)
                        else:
                            QMessageBox.information(self, '提示', '录入失败！', QMessageBox.Ok, QMessageBox.Ok)
                except:
                    QMessageBox.critical(self,'错误','数据库异常！',QMessageBox.Ok,QMessageBox.Ok)

        


        
    def myclear(self):
        self.data_model.clear()
        self.data_model.setHorizontalHeaderLabels(self.headers)
        self.data = []  

        self.le_search_term.clear()
        self.le_c_name.clear()
        self.le_c_phone.clear()
        self.cb_a_rank.setCurrentIndex(0)
        self.cb_a_type.setCurrentIndex(0)
        self.te_cmsg.clear()

        self.le_c_name_3.clear()
        self.le_c_phone_3.clear()
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_4.setCurrentIndex(0)

        self.te_cmsg_2.clear()

        self.listFunc.setCurrentRow(0)


