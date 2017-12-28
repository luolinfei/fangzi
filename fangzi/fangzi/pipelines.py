# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from openpyxl import Workbook
import re
from pymongo import MongoClient
client = MongoClient(host="127.0.0.1",port=27017)

collection = client["fangzi999"]["lianjia"]
class FangziPipeline(object,):
    # wb = Workbook() #class实例化
    # ws = wb.active  #激活工作表
    # ws.append(['房子标题','房子总价','房子单价','小区名称'])#设置表头
    def process_item(self, item, spider):  # 工序具体内容
        print(item)
        # item["content_text"] = [i.replace("\n\t", "") for i in item["content_text"] if len(i.replace("\n\t", "")) > 0]
        # item["content_text"] = [re.sub(r"\xa0|s+|\u3000","",i,re.S) for i in item["content_text"]]
        # item["content_text"] = [i for i in item["content_text"] if len(i)>0]
        # line = [item['house_title'],item['house_price'],item['house_price1'],item['xiaoqu_name']]#把数据中的每一项整理出来
        # self.ws.append(line) # 将数据以行的形式添加到xlsx中
        # self.wb.save('/home/data/lianjia.xlsx')  #保存xlsx文件
        collection.insert(dict(item))
        return item
