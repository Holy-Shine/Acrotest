
from PyQt5.QtWidgets import QDialog, QMessageBox, QLineEdit, QApplication, QTableView, QHeaderView
from qtpy import QtGui

from StudentSystem.BasicInfoModify import Ui_BasicInfoModify
import sys


class LogicModifyInfo(Ui_BasicInfoModify,QDialog):
    def __init__(self,MySQL,BasicInfo):
        super().__init__()
        self.setupUi(self)
        self.MySQL = MySQL
        self.BasicInfo = BasicInfo
        self.init()
        self.slot_init()

    def init(self):
        classitem = ['轮滑','滑步车']
        self.cb_classitem.addItems(classitem)
        self.init_PlaceHoder()
        self.et_name.setEnabled(False)

        self.type2card = {
            0:'轮滑',
            1:'滑步车'
        }

    def slot_init(self):
        # 确认信息和更新数据。
        self.bt_confrim.clicked.connect(self.modify_info)
        # 返回
        self.bt_back.clicked.connect(self.close)

    def init_PlaceHoder(self):
        self.et_age.setValidator(QtGui.QIntValidator())
        self.et_cishu.setValidator(QtGui.QIntValidator())


        self.et_name.setText(self.BasicInfo['学生姓名'])
        self.et_phone.setPlaceholderText(self.BasicInfo['联系方式'])
        self.et_parent.setPlaceholderText(self.BasicInfo['学生家长'])
        self.et_age.setPlaceholderText(str(self.BasicInfo['学生年龄']))
        self.et_cishu.setPlaceholderText(str(self.BasicInfo['课时次数']))

        if (self.BasicInfo['学生性别']=='男'):
            self.rb_man.setChecked(True)
        else:
            self.rb_woman.setChecked(True)


        self.cb_classitem.setCurrentIndex(int(self.BasicInfo['课程种类']))

    #修改学生信息
    def modify_info(self):
        try:
            if not self.et_phone.text() == '' and not self.PhoneCheck(self.et_phone.text()):
                QMessageBox.warning(self, u"温馨提示", u"请输入正确的11位手机号码",
                                    buttons=QMessageBox.Ok, )
            else:
                name = self.et_name.text()

                if (self.et_phone.text() == ''):
                    phone = self.BasicInfo['联系方式']
                else:
                    phone = self.et_phone.text()
                if (self.et_cishu.text() == ''):
                    cishu = self.BasicInfo['课时次数']
                else:
                    cishu = self.et_cishu.text()

                if (self.et_parent.text() == ''):
                    parent = self.BasicInfo['学生家长']
                else:
                    parent = self.et_parent.text()

                if (self.et_age.text() == ''):
                    age = self.BasicInfo['学生年龄']
                else:
                    age = self.et_age.text()

                if(self.rb_woman.isChecked()):
                    gender = '女'
                else:
                    gender = '男'

                type = self.cb_classitem.currentIndex()

                hint = '学生姓名：{}\n学生性别：{}\n学生年龄：{}\n学生家长：{}\n联系方式：{}\n课时次数：{}\n' \
                       '课程种类：{}'.format(
                    name,
                    gender,
                    age,
                    parent,
                    phone,
                    cishu,
                    self.type2card[type]
                )

                reply = QMessageBox.warning(self, '确认信息', hint, QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                if reply == QMessageBox.Yes:
                    sql_update_meminfo = 'UPDATE  mem_info  SET ' \
                                         'mem_phone=\'{}\', ' \
                                         'men_age=' \
                                         '\'{}\',' \
                                         'mem_type={},' \
                                         'mem_parent=\'{}\','\
                                         'mem_gender=\'{}\','\
                                         'mem_cls_left={}' \
                                         ' WHERE mem_phone=\'{}\' and mem_name=\'{}\' and mem_type={};'.format(
                        phone,
                        age,
                        type,
                        parent,
                        gender,
                        cishu,
                        phone,
                        name,
                        self.BasicInfo['课程种类']
                    )
                    print(sql_update_meminfo)
                    flag = self.MySQL.UpdateFromDataBse(sql_update_meminfo)

                    if(flag):
                        QMessageBox.information(self, '提示', '修改成功！', QMessageBox.Ok, QMessageBox.Ok)
                    else:
                        QMessageBox.information(self, '提示', '修改失败！', QMessageBox.Ok, QMessageBox.Ok)
                    self.accept()
        except Exception as e:
            print(e)



    # 确认是电话号码
    def PhoneCheck(self, s):
        # 检测号码是否长度是否合法。
        if len(s) != 11:
            return False
        elif (s.isdigit()):
            return True
        else:
            return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = LogicModifyInfo(MySQL='1',BasicInfo='2')
    login.show()
    sys.exit(app.exec_())