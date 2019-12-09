import pymysql.cursors
cnn= pymysql.connect(host='121.199.17.205',     #IP
                             user='Jessie',  #用户名
                             password='Jessie.121406',  #密码
                             port=3306,  #端口号
                             charset='utf8')#注意是utf8不是utf-8
# 使用cursor()方法获取操作游标
cursor = cnn.cursor()
# 使用execute方法执行SQL语句
cursor.execute("use meminfo;")
cursor.execute("show tables;")
result = cursor.fetchall()
print (result)

