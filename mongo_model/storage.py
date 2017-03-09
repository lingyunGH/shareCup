# -*- coding: UTF-8 -*-
import pymongo

from common.logger import Logger

logger = Logger("storage.py")


class Mongo():
    def __init__(self, db_name, collection_name):
        self.db_nam = db_name
        self.col_nam = collection_name

        self.collection = self.conn()

    # 建立连接
    def conn(self,):
        # 连接本地
        # client = pymongo.MongoClient(host="127.0.0.1", port=27017)
        # client = pymongo.MongoClient(host="127.0.0.1", port=11227)
        # 连接到云服务器上,带上用户名和密码
        # client = pymongo.MongoClient('mongodb://ads_data:kxMfecclMWHKnjs9@192.168.192.27:27017/')

        client = pymongo.MongoClient(host="127.0.0.1", port=27017)
        # 判断是否有错
        if client is None:
            logger.error("mongodb连接失败...")
            # return None

        db = client[self.db_nam]

        collection = db[self.col_nam]

        return collection

    def data_find_one(self, query):
        # 防止出错
        try:
            result = self.collection.find_one(query)
            return result

        except Exception as e:
            logger.error("查询数据时,出错:{}".format(e))

    def data_find_all(self, query):

        # 防止出错
        try:
            result = self.collection.find(query)
            return result

        except Exception as e:
            logger.error("查询数据时,出错:{}".format(e))

    def monitor_find_one(self, query):
        try:
            result = self.collection.find_one(query)
            return result

        except Exception as e:
            logger.error("查询数据时,出错:{}".format(e))

    def monitor_insert(self, data):
        try:
            self.collection.insert(data)
        except:
            pass

    def data_insert(self, data):

        # 防止出错
        try:
            self.collection.insert(data)
        except Exception as e:
            logger.error("插入数据时,出错,执行更新操作...".format(e))
            self.data_update(data)

            # data 是list类型  ,而data_update要求字典类型

        # logger.info("数据存储成功...")

    # 插入失败,执行更新操作
    def data_update(self, data):
        try:
            # 根据id更新
            _id = data['_id']
            try:
                self.collection.update({'_id': _id}, data)

            except Exception as e:
                logger.error("更新数据出错:{}".format(e))

        except Exception as e:
            logger.info("数据解析出错:{}".format(e))

        # logger.info("更新数据,成功...")



