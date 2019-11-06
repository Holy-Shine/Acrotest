import sqlite3


def createTable():
    conn = sqlite3.connect('meminfo.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE mem_info_v3
    (mem_phone INTEGER PRIMARY KEY NOT NULL,
     mem_name TEXT NOT NULL,
     mem_parent,
     mem_gender TEXT NOT NULL,
     mem_type INTEGER NOT NULL,
     mon INTEGER NOT NULL,
     tues INTEGER NOT NULL,
     wed INTEGER NOT NULL,
     thur NUMINTEGERERIC NOT NULL,
     fri INTEGER NOT NULL,
     sat INTEGER NOT NULL,
     sun INTEGER NOT NULL)
    ''')
    conn.commit()
    conn.close()

createTable()