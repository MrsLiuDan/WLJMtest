
##########善言详情##########
###接口名称：http://192.168.1.40:8002/api/temple/buddhism/buddhismDetail
###编写人员：刘丹
###编写日期：2019-09-25

import requests,unittest
from conf.buddhismUrl import *
from conf.user_conf import *
from common.comm_method import *

class buddhismDetail(unittest.TestCase):
    def setUp(self) -> None:
        pass
    '''查看善言详情'''
    def test_buddhismDetail(self):

        # 测试流程1、获取善言文章ID  2、传入善言文章ID，查看善言详情
        buddhismId=get_AllbuddhismId(url=host+getIndexBuddhismList_url)
        paydata={
            'userId':10000,
            'articleId':buddhismId
        }
        ref=requests.post(url=host+buddhismDetail_url,data=paydata)
        res=ref.json()
        print (res)
        #断言code为0，查看善言详情成功
        res_code=res['code']
        self.assertEqual(res_code,0)


    def tearDown(self) -> None:
        pass
if '__name__'=='__main__':
    unittest.main()







