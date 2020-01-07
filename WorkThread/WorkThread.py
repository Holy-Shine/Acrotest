from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import xlwt

class MySQLThread(QThread):
    trigger = pyqtSignal(tuple)

    def __init__(self,MySQL,sql,parent=None):
        super(MySQLThread, self).__init__(parent)
        self.sql = sql
        self.MySQL = MySQL
    
    def run(self):

        # 执行查询
        _, data = self.MySQL.SelectFromDataBse(self.sql)
        self.trigger.emit(data)

class WriteExcelThread(QThread):
    trigger = pyqtSignal()

    def __init__(self, data, filepath, header, labels,label_idx,parent=None):
        super(WriteExcelThread, self).__init__(parent)
        self.data = data
        self.filepath = filepath
        self.header=header
        self.labels = labels
        self.label_idx = label_idx

    def run(self):
        if self.filepath=='':
            pass
        else:
        # 写文件
            wb = xlwt.Workbook()
            sheet = wb.add_sheet('数据')

            # 写表头
            for i in range(len(self.header)):
                sheet.write(0, i, self.header[i])
            
            j=1
            for line in self.data:
                for i in range(len(self.header)):
                    if i==self.label_idx:
                        sheet.write(j, i, self.labels[line[i]])
                    else:
                        sheet.write(j, i, line[i])
                j+=1
            
            wb.save(self.filepath)
            self.trigger.emit()
        


