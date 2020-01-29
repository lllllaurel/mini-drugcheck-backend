#数据库类
from flask import Flask
import sqlite3 

app = Flask(__name__)

class DB():
    def __init__(self):
        self.db_path = 'drugcheck'
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self.c = self.conn.cursor()

    def is_registed(self, openid):
        if openid is None or len(openid) < 1:
            return None 
        sql = 'select * from drugs where openid="%s"'%openid
        row = None
        try:
            cur = self.c.execute(sql)
            self.conn.commit()
            row = cur.fetchone()
        except Exception as err:
            raise Exception(err)
        return None if row is None else tuple(row)[2]

    def regist(self, openid, phone):
        if openid is None or phone is None:
            raise Exception('Invalid Params')
        sql = "insert into drugs(openid, phone) values('%s', '%s')"%(openid, phone)
        try:
            cur = self.c.execute(sql)
            self.conn.commit()
        except Exception as err:
            raise Exception(err)
        return '200'


        

    def __del__(self):
        self.conn.close()