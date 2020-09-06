# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class MyspidersPipeline:
#     def process_item(self, item, spider):
#         return item
import pymysql
from .settings import *


class MyspidersPipeline(object):
    def __init__(self):
        # 爬虫程序启动时，只执行一次，一般用于建立数据库连接
        self.connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='uiop7890',
            database='smzdm1',
            charset='utf8mb4'
        )
        # 数据库游标，用于操作数据库
        self.cursor = self.connection.cursor()
        print('Successfully launched the connection with the database.')
    def process_item(self, item, spider):
        try:
            # 将信息写入数据库
            sql_command = '''INSERT INTO smzdm1(comments,sentiments,username,comment_time) VALUES (%s,%s,%s,%s);'''
            print(sql_command),'sqlsqlsqlsql'
            self.cursor.execute(sql_command, ( item['comments'],item['sentiments'],item['username'],item['comment_time']))

            # 提交信息
            self.connection.commit()
            print('Successfully inserted', self.cursor.rowcount, 'rows of data')

        except Exception as e:
            # 输出错误信息
            print(e)
            self.connection.rollback()
            print('The transcation is rolled back due to the exception error.')
        # 必须写，此函数返回值会交给下一个管道处理item数据
        return item

    def close_spider(self, spider):
        # 爬虫程序结束时，只执行一次，一般用于断开数据库连接
        self.cursor.close()
        self.connection.close()
        print('Successfully shut down the connection with the database')
