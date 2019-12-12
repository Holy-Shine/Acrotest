#这个文件用于批量插入一些测试数据和清空数据库用


def InsertData(MySQL):
    with open('memdata.utf8','r',encoding='utf-8') as fr:
        for line in fr:
            flag = MySQL.InsertFromDataBse(line.strip())
            if(flag):
                print('插入成功！{}'.format(line.strip()))


def Cleardatabase(MySQL):
    sql1 = 'truncate table mem_info;'
    sql2 = 'truncate table mem_class;'
    sql3 = 'truncate table banka;'
    flag1 = MySQL.InsertFromDataBse(sql1)
    flag2 = MySQL.InsertFromDataBse(sql2)
    flag3 = MySQL.InsertFromDataBse(sql3)
    if(flag1 and flag2 and flag3):
        print("成功清除所有数据！")

if __name__ == '__main__':
    from ConnecMySQL.MySQLBase import MySQLBaseFunction

    host = '121.199.17.205',  # IP
    user = 'Jessie',  # 用户名
    password = 'Jessie.121406',  # 密码
    database = 'meminfo',
    MySQL = MySQLBaseFunction(HostIP=host[0],
                              Username=user[0],
                              Password=password[0],
                              DataBase=database[0])
    MySQL.ConnectMySQL()
    # InsertData(MySQL=MySQL)
    Cleardatabase(MySQL=MySQL)