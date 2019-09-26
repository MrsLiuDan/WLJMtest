# coding:utf-8
import unittest
import requests
from conf.buddhismUrl import *  #在conf.user_conf中导入所有接口的入参信息

#获取全部善言列表第一篇善言文章ID
def get_AllbuddhismId(url):
    getIndexBuddhismList_data = {
        'userId': 10000,
        'type': 1,  # 1全部善言  2关注善言
        'pageSize': 10,
        'pageIndex': 1
    }
    ref=requests.post(url=url,data=getIndexBuddhismList_data)
    res=ref.json()
    # 获取善言列表第一条善言文章ID
    buddhismId=res['data']['recordList'][0]['buddhismId']
    return buddhismId

