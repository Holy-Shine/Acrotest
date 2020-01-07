import pymysql

def insert():
    conn = pymysql.connect(
        host='121.199.17.205',
        user='Jessie',
        password='Jessie.121406',
        database = 'meminfo',
        charset='utf8'
    )

    cursor = conn.cursor()

    sql = ''

    bankas = [10,10,15,20,25,23,40,45,30,36,20,5]
    xukas =  [5,5,7,15,20,10,11,17,8,9,20,5]

    i_name = 0
    try:
        for i in range(1,13,1):
            date = '2019-'+str(i)+'-1'
            
            # 插入当月办卡数据
            for j in range(bankas[i-1]):
                name = '测试-'+str(i_name)
                i_name+=1
                sql = '''
                INSERT INTO banka VALUES(
                    '12312312312',
                    \'{}\',
                    0,
                    1000,
                    \'{}\'
                )
                '''.format(name,date)
                cursor.execute(sql)

            # 插入当月续卡数据
            for j in range(xukas[i-1]):
                name = '测试-'+str(i_name)
                i_name+=1
                sql = '''
                INSERT INTO banka VALUES(
                    '12312312312',
                    \'{}\',
                    1,
                    1000,
                    \'{}\'
                )
                '''.format(name,date)
                cursor.execute(sql)

        # cursor.execute(sql)

    except Exception as e:
        print(e)
        print('Error: unable to fetch data')
    conn.commit()
    cursor.close()
    conn.close()

def search():

    sql = '''
    SELECT COUNT(*) FROM meminfo.banka AS bk where bk.banka_type=1 or bk.banka_date like '%2019-10%'
    '''

    conn = pymysql.connect(
        host='121.199.17.205',
        user='Jessie',
        password='Jessie.121406',
        database = 'meminfo',
        charset='utf8'
    )

    cursor = conn.cursor()
    cursor.execute(sql)
    rst = cursor.fetchall()
    print(rst)
    print(len(rst))
    print(rst[0][0])


# from SummarySystem.myUI import ComboCheckBox
# items = ['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']
# self.cb_fluid_month = ComboCheckBox(items, self.widget)

        from SummarySystem.myUI import ComboCheckBox
        items = ['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']
        self.cb_fluid_month = ComboCheckBox(items, self)

        items = ['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']
        self.cb_fluid_month_2 = ComboCheckBox(items, self)
        self.cb_fluid_month_2.setObjectName("cb_fluid_month_2")
        self.gridLayout_5.addWidget(self.cb_fluid_month_2, 0, 3, 1, 1)


        items = ['出库','入库']
        self.cb_fluid_inout = ComboCheckBox(items, self)