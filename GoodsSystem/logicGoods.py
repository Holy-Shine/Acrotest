import os,json
from PyQt5.QtWidgets import QDialog,QMessageBox,QTableView,QHeaderView, QListWidget, QStackedWidget
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from PyQt5.Qt import QIntValidator

from datetime import datetime as dt
from GoodsSystem.Ui_sysgoods import Ui_sysGoods
from ConnecMySQL.MySQLBase import MySQLBaseFunction

class logicGoods(Ui_sysGoods, QDialog):
    def __init__(self,MySQL):
        super().__init__()
        self.setupUi(self)  
        self.MySQL = MySQL
        self.listFunc.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)   # list和右边窗口index绑定
        self.listFunc.currentRowChanged.connect(self.myclear)
        
        # 货物增删查
        self.headers = ['货物名','货物简介','数目']
        self.data_model = QStandardItemModel()
        self.data_model.setHorizontalHeaderLabels(self.headers)
        self.data = []
        self.tv_goods.setModel(self.data_model)
        
        self.tv_goods.selectionModel().selectionChanged.connect(self.row_sel_change) # 选中事件
        self.tv_goods.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tv_goods.setEditTriggers(QTableView.NoEditTriggers) # 不可编辑
        self.tv_goods.setSelectionBehavior(QTableView.SelectRows) # 选中行

        self.onlyInt = QIntValidator()
        self.le_inout_price.setValidator(self.onlyInt)  # 限制只能为int
        self.le_inout_num.setValidator(self.onlyInt)
       
        self.listFunc.setCurrentRow(0)
        #self.myclear()



        self.le_filter.textChanged.connect(self.on_le_filter_textChange)
        self.cb_inout_year.currentIndexChanged.connect(self.inout_day_parser)
        self.cb_inout_month.currentIndexChanged.connect(self.inout_day_parser)
        ################################# 按钮事件 #############################################
        self.btn_flush.clicked.connect(self.on_btn_connect_db)
        self.btn_confirm_add.clicked.connect(self.on_btn_add_goods)
        self.btn_remove_select.clicked.connect(self.on_btn_remove_goods)
        self.btn_inout_confirm.clicked.connect(self.on_btn_inout_confirm)

    def row_sel_change(self):
        pass

    
    def inout_day_parser(self):
        self.cb_inout_day.clear()
        year = self.cb_inout_year.currentText()
        month = self.cb_inout_month.currentText()
        if year!='' and month!= '':
            year = int(year)
            month = int(month)
            days = [31,28,31,30,31,30,31,31,30,31,30,31]
            # 闰年逻辑
            if year%400==0 or year%100!=0 and year%4==0:
                days[1]=29
            self.cb_inout_day.addItems([str(i) for i in range(1, days[month-1]+1)])
        

    def inout_date_clear(self):
        self.cb_inout_year.clear()
        self.cb_inout_month.clear()
        self.cb_inout_day.clear()
        year = dt.now().year
        month = dt.now().month
        day = dt.now().day
        self.cb_inout_year.addItems([str(year-1),str(year), str(year+1)])
        self.cb_inout_year.setCurrentIndex(1)

        self.cb_inout_month.addItems([str(i) for i in range(1,13)])
        self.cb_inout_month.setCurrentIndex(month-1)

        self.inout_day_parser()
        self.cb_inout_day.setCurrentIndex(day-1)

        
        
    def myclear(self):
        self.btn_remove_select.setEnabled(False)
        self.le_filter.setText('')
        self.btn_flush.setEnabled(True)
        self.btn_flush.setText('连接数据库获取仓库货物信息')


        # 表刷新/后台缓存数据刷新
        self.data_model.clear()
        self.data_model.setHorizontalHeaderLabels(self.headers)
        self.data = []


        # 添加货物刷新
        self.le_goods_name.setText('')
        self.te_goods_info.setText('')
        self.btn_confirm_add.setEnabled(False)


        # 进/出库登记刷新
        self.le_inout_name.clear()
        self.le_inout_num.clear()
        self.le_inout_price.clear()
        self.inout_date_clear()







    #### 按钮/输入事件
    def on_btn_inout_confirm(self):
        # 校验
        if self.le_inout_name.text()=='':
            QMessageBox.critical(self, '错误', '货物名不能为空！', QMessageBox.Ok, QMessageBox.Ok)
        elif self.le_inout_price.text()=='':
            QMessageBox.critical(self, '错误', '货物价格不能为空！', QMessageBox.Ok, QMessageBox.Ok)
        elif self.le_inout_num.text()=='':
            QMessageBox.critical(self, '错误', '货物数目不能为空！', QMessageBox.Ok, QMessageBox.Ok)    

        else:
            goods_name = self.le_inout_name.text()
            goods_price = self.le_inout_price.text()
            goods_num = self.le_inout_num.text()
            year = int(self.cb_inout_year.currentText())
            month = int(self.cb_inout_month.currentText())
            day = int(self.cb_inout_day.currentText())
            inout = 1-self.cb_inout.currentIndex()
            try:
                sql = '''INSERT INTO goods_inout VALUES(
                    '{}',{},{},'{}-{}-{}',{}
                )'''.format(goods_name, goods_price, inout, year, month,day, goods_num)
                print(sql)

                str_confirm='''  操作类型：\t{}\t\n  货物名：\t{}\t\n  货物价格：\t{}\t\n  货物数目：\t{}\t\n  操作日期：\t{}-{}-{}\t
                '''.format(self.cb_inout.currentText(), goods_name, goods_price, goods_num, year, month,day)

                reply = QMessageBox.question(self, '操作确认',str_confirm, QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)

                # 插入数据库
                if reply == QMessageBox.Yes:   
                    veriSQL = '''SELECT goods_num FROM goods WHERE goods_name='{}' '''.format(goods_name)
                    flag1, result1 = self.MySQL.SelectFromDataBse(veriSQL)

                    if flag1 == True:
                        if len(result1) == 0:
                            QMessageBox.critical(self,'错误','仓库中未存在名为“{}”的货物！'.format(goods_name),QMessageBox.Ok, QMessageBox.Ok)
                        
                        elif self.cb_inout.currentIndex()==1 and int(result1[0][0])<int(goods_num):
                            QMessageBox.critical(self,'错误','当前仓库的“{}”的库存不足！\n当前库存：{}'.format(goods_name, result1[0][0]),QMessageBox.Ok, QMessageBox.Ok)
                        
                        else:
                            flag = self.MySQL.InsertFromDataBse(sql)
                            if (flag == True):
                                QMessageBox.information(self,'提示','{}成功'.format(self.cb_inout.currentText()),QMessageBox.Ok, QMessageBox.Ok)
                            else:
                                QMessageBox.critical(self, '错误', '连接数据库失败！\n考虑是否是以下原因引起：\n (1)网络连接出现问题', QMessageBox.Ok, QMessageBox.Ok)
                    else:
                        QMessageBox.critical(self, '错误', '连接数据库失败！\n考虑是否是以下原因引起：\n (1)网络连接出现问题', QMessageBox.Ok, QMessageBox.Ok)                    
            except Exception as e:
                print(e)
    

    def on_btn_remove_goods(self):
        row = self.tv_goods.currentIndex().row()
        
        if row == -1:
            QMessageBox.critical(self, '错误', '未选中任何货物', QMessageBox.Ok, QMessageBox.Ok)
        else:
            name = self.data_model.index(row, 0)
            info = self.data_model.index(row, 1)
            num = self.data_model.index(row, 2)
            dl_goods_name = str(self.data_model.data(name))
            dl_goods_info = str(self.data_model.data(info))
            dl_goods_num = str(self.data_model.data(num))

            try:
                str_confirm = '''是否删除下列货物：\n  货物名：\t{}\n  货物简介：\t{}\n  货物余量：\t{}'''.format(dl_goods_name,dl_goods_info, dl_goods_num)
                reply = QMessageBox.question(self, '确认信息',str_confirm, QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)

                # 插入数据库
                if reply == QMessageBox.Yes:
                    sql = '''DELETE FROM goods WHERE goods_name='{}' '''.format(dl_goods_name)
                    flag = self.MySQL.DeleteFromDataBse(sql)
                    if (flag == True):
                        # 从缓存数据中删除数据
                        for i, (goods_name, goods_info, goods_num) in enumerate(self.data):
                            if dl_goods_name == goods_name:
                                self.data.pop(i)
                                break
                        # 从数据模型中删除
                        self.data_model.removeRow(row)
                        QMessageBox.information(self,'提示','删除货物成功',QMessageBox.Ok, QMessageBox.Ok)
                        
                    else:
                        QMessageBox.critical(self, '错误', '删除货物失败！\n考虑是否是以下原因引起：\n (1)网络连接出现问题', QMessageBox.Ok, QMessageBox.Ok)
            except Exception as e:
                print(e)


    def on_le_filter_textChange(self):
        term = self.le_filter.text().strip()

        # 清空数据模型
        self.data_model.clear()
        self.data_model.setHorizontalHeaderLabels(self.headers)  
        # 备份缓存数据
        if term == '':
            for i, (goods_name, goods_info, goods_num) in enumerate(self.data):
                self.data_model.appendRow([
                    QStandardItem(goods_name),
                    QStandardItem(goods_info),
                    QStandardItem(str(goods_num))
                ])
        else:
            for i, (goods_name, goods_info, goods_num) in enumerate(self.data):
                if term in goods_name:
                    self.data_model.appendRow([
                        QStandardItem(goods_name),
                        QStandardItem(goods_info),
                        QStandardItem(str(goods_num))
                    ])
        
    def on_btn_connect_db(self):
        self.data_model.clear()
        self.data_model.setHorizontalHeaderLabels(self.headers)
        try:
            sql = '''SELECT * FROM goods'''
            flag, result = self.MySQL.SelectFromDataBse(sql)
            if (flag == True):
                self.data = list(result)
                for i, (goods_name, goods_info, goods_num) in enumerate(self.data):
                    self.data_model.appendRow([
                        QStandardItem(goods_name),
                        QStandardItem(goods_info),
                        QStandardItem(str(goods_num))
                    ])
                
                self.btn_flush.setText('刷新仓库货物信息')
                self.btn_remove_select.setEnabled(True)
                self.btn_confirm_add.setEnabled(True)
                self.le_filter.clear()
            else:
                QMessageBox.critical(self, '错误', '连接货物数据库失败', QMessageBox.Ok, QMessageBox.Ok)
                self.btn_remove_select.setEnabled(False)
                self.btn_confirm_add.setEnabled(False)
        except Exception as e:
            print(e)

    def on_btn_add_goods(self):
        # 有效性检查
        if self.le_goods_name.text()=='':
            QMessageBox.critical(self, '错误', '货物名不能为空！', QMessageBox.Ok, QMessageBox.Ok)
        
        else:
            goods_name = self.le_goods_name.text()
            goods_info = self.te_goods_info.toPlainText()
            sql = '''
            INSERT INTO goods (goods_name, goods_info) VALUES ('{}','{}')
            '''.format(goods_name,goods_info)

            try:
                str_confirm = '''插入信息如下：\n  货物名：\t{}\n  货物简介：\t{}'''.format(goods_name,goods_info)
                reply = QMessageBox.question(self, '确认信息',str_confirm, QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)

                # 插入数据库
                if reply == QMessageBox.Yes:
                    flag = self.MySQL.InsertFromDataBse(sql)
                    if not flag:
                        QMessageBox.critical(self, '错误', '插入数据库失败！\n考虑是否是以下原因引起：\n (1)数据库存在同名的货物\n (2)网络连接出现问题', QMessageBox.Ok, QMessageBox.Ok)
                    else:
                        QMessageBox.information(self,'提示','添加货物成功',QMessageBox.Ok, QMessageBox.Ok)
                        
                        # 更新缓存
                        self.data.append((goods_name, goods_info, 0))

                        self.data_model.appendRow([
                            QStandardItem(goods_name),
                            QStandardItem(goods_info),
                            QStandardItem(str(0))
                        ])

                        # 清空输入
                        self.le_goods_name.clear()
                        self.te_goods_info.clear()
            except Exception as e:
                print(e)
            
            