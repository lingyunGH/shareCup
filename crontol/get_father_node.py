from mysql_model.mysql_model import Mysql


def get_father_node(query_father_node_sql):
    mysql = Mysql()

    found_res = mysql.find_data(query_father_node_sql)
    # print(found_res)
    # print(type(found_res))
    # for item in found_res:
    #     print(item)
    #     print(type(item))
    return found_res

if __name__ == "__main__":
    get_father_node()
