# -*- coding: UTF-8 -*-
import MySQLdb


class Mysql():
    def __init__(self):

        self.conn = MySQLdb.connect(          
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='xxxxx',
            db='icd',
            charset='utf8'
        )
        #获取游标
        self.cur = self.conn.cursor()

    def find_data(self, query_sql):
        #执行sql语句
        find_data = self.cur.execute(query_sql)
        #返回多条记录
        found_data_res = self.cur.fetchmany(find_data)

        return found_data_res

    def close(self):
        self.cur.close()
        self.conn.commit()
        self.conn.close()

if __name__ == "__main__":

    query = "select * from Sheet1 "

    test = Mysql()

    res = test.find_data(query)

    print (res)
    print (len(res))
