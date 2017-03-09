# -*- coding:utf-8 -*-

from flask import Flask
from flask import render_template
from crontol.get_father_node import get_father_node
from crontol.get_children_node import get_children_node

app = Flask(__name__)


def storage():
    # print(3)
    res = []
    # #选取前四层
    # 查询父节点的sql语句
    query_father_node_sql = "select * from Sheet1  WHERE class<4 GROUP BY parent"
    father_node = get_father_node(query_father_node_sql)
    print(4)
    print(len(father_node))
    father_node_set = set()    # 存储父节点的id
    for father_node_item in father_node:
        if father_node_item:
            father_node_set.add(father_node_item[1])
        else:
            print('root node:%s'%father_node_item[0])
    print(father_node_set)
    # count = 1
    # children_node_set = set()
    #遍历父节点[A01,A02......A99]
    for id_item in father_node_set:
        node_map = {}
        node_map["name"] = id_item
        # print id_item
        query_children_node_sql = "select * from Sheet1 where class<4 and parent='{0}'".format(id_item)

        #获取孩子节点,[]
        children_node = get_children_node(query_children_node_sql)
        # print(children_node)
        node_map["value"] = len(children_node)
        node_map["children"] = []
        #遍历孩子节点
        for children_node_item in children_node:
            # children_node_set.add(children_node_item[1])
            children_node_map = {}
            children_node_map["value"] = 1
            children_node_map["name"] = "{0}({1})".format(children_node_item[1].encode("utf-8"),children_node_item[0])

            # print(children_node_item[1])


            node_map["children"].append(children_node_map)
        # print('===============')

        # if count > 5:
        #     break
        #
        # count += 1

        res.append(node_map)

        # print(6)
        # print(res)

    # mongo.data_insert(res)
    return res


@app.route('/')
def hello_world():

    # mongo = Mongo("lly", "data")
    #
    # query = {"_id":{"$exists": True } }
    # res = mongo.data_find_all(query)
    # print(1)
    res = storage()
    # res =
    print(res)
    return render_template("index.html", data_res=res)


if __name__ == '__main__':
    app.run()
