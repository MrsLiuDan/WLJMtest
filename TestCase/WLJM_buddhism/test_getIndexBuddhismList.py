

##########佛缘大厅，善言列表##########
###接口名称：http://192.168.1.40:8002/api/temple/buddhism/getIndexBuddhismList   佛缘大厅全部善言
###接口名称：http://192.168.1.40:8002/api/temple/buddhism/getUserBuddhismList    个人主页全部善言
###编写人员：刘丹
###编写日期：2019-09-24

# coding:utf-8
import unittest
import requests
from conf.buddhismUrl import *  #在conf.buddhismUrl中导入所有接口的入参信息

class getIndexBuddhismList(unittest.TestCase):
    def setUp(self) -> None:
        pass

    '''测试佛缘大厅-善言列表:全部善言接口'''
    def test_getIndexBuddhismList(self):
        #测试流程：1、善言列表
        getIndexBuddhismList_data={
            'userId':10000,
              'type' : 1 ,  #1全部善言  2关注善言
            'pageSize':10,
            'pageIndex':1
        }
        ref=requests.post(url=host+getIndexBuddhismList_url,data=getIndexBuddhismList_data)
        #获取返回的code
        ref_code=ref.json()['code']
        print (ref.json())
        #断言code返回0表示获取全部善言成功
        self.assertEqual(ref_code,0)
        '''个人主页善言列表'''
    def test_getUserBuddhismList(self):
        getUserBuddhismList_data={
            'userId':10003,
            'pageSize':10,
            'pageIndex':1
        }
        ref=requests.post(url=host+getUserBuddhismList_url,data=getUserBuddhismList_data)
        res=ref.json()
        res_code=res['code']
        #断言返回code为0,接口调用成功
        self.assertEqual(res_code,0)

    def tearDown(self) -> None:
        pass

if '__name__'=='__main__':
    unittest.main()