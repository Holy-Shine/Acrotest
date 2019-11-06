import json


def dict_to_json():

    dic = {
        'save_code':True,
        'name':'admin',
        'pwd':'123'
    }
    json.dump(dic,open('./user_params.json','w'))


def connect_db():
    import pymysql

    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='1230456',
        database = 'user_info_db',
        charset='utf8'
    )

    cursor = conn.cursor()

    sql = 'SELECT * FROM mem_info WHERE mem_name=\'胡图图\''

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            name = row[0]
            gender = row[1]
            parent = row[2]
            phone = row[3]
            type = row[4]
            print('name:\t{}\ngender:\t{}\nparent:\t{}\nphone:\t{}\ntype:\t{}'.format(name, gender, parent, phone, type))
    except:
        print('Error: unable to fetch data')
    
    cursor.close()

    conn.close()


'''
    学员信息表
    CREATE TABLE mem_info
        (mem_phone INT PRIMARY KEY     NOT NULL,
        mem_name   TEXT NOT NULL,
        mem_parent TEXT,
        mem_gender TEXT NOT NULL,
        mem_type INT NOT NULL);

    上课时间表
    每个同学7条记录，day为0表示当天无课！
        CREATE TABLE mem_classtime
        (
        mem_phone INT NOT NULL,
        mem_name TEXT NOT NULL,
        mem_day INT NOT NULL,
        mem_time INT NOT NULL,
        PRIMARY KEY(mem_phone,mem_name, mem_day));
'''
def sqlite_test():
    import sqlite3
    conn = sqlite3.connect('meminfo.db')
    print("Opened database successfully");
    c = conn.cursor()
    sql = '''
        SELECT mem_phone, mem_name FROM mem_info mi WHERE NOT EXISTS(
            SELECT * FROM mem_class  mc WHERE week=9
        )
    '''
    c.execute(sql)

    rst = c.fetchall()
    for i,(mem_phone, mem_name) in enumerate(rst):
        print(i, mem_phone, mem_phone)
    print("Table created successfully")
    conn.commit()
    conn.close()


sqlite_test()
