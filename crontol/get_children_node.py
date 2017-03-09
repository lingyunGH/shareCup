# -*- coding: UTF-8 -*-
from mysql_model.mysql_model import Mysql


def get_children_node(query_children_node_sql):
    #连接数据库
    mysql = Mysql()
    #寻找孩子节点
    found_res = mysql.find_data(query_children_node_sql)

    # for item in found_res:
    #     print(item)

    return found_res

if __name__ == "__main__":
    query_children_node_sql = "select * from Sheet3 where code like 'A%' and father_id='A79'"
    print (get_children_node(query_children_node_sql))
