##########祈福页面接口##########
###接口名称：
###编写人员：

# coding:utf-8
import unittest
import requests
from conf.user_conf import *  #在conf.user_conf中导入所有接口的入参信息
#定义一个全局变量
# session = requests.Session()
class Bless(unittest.TestCase):
    def setUp(self):
        pass

        # 1.进入祈福页面接口
    def test_bless_url(self):
        #入参信息
        bless_data = {
            "userId":10000 ,
            "pageSize": 1,
            "pageIndex": 1,
            "offerIds": "2"
            }
        #发送post请求测试进入祈福页面接口
        rep = requests.post(url=bless_host+bless_url, data=bless_data)
        #获取接口返回值code
        blessCode = rep.json()['code']
        # buddhald=rep.json()['data']['templeBlessRequestDetailVo']['buddhaId']
        #打印接口UIL和返回信息
        print(bless_host+bless_url)
        print(rep.json())

        # 断言返回code=0表示接口调用成功
        self.assertEqual(blessCode, 0)

    #     #2.添加恭请的佛像
    def test_addSelectBuddha_url(self):
        #入参信息
        addSelectBuddha_data = {
            "userId":10000,
            "buddhaId":132,
        }
        #发送post请求测试添加恭请佛像接口
        rep = requests.post(url=addSelectBuddha_host+addSelectBuddha_url,data=addSelectBuddha_data)
        #获取接口返回值code
        self.addSelectBuddhaCode = rep.json()['code']
        #打印接口ulL和返回信息
        print(addSelectBuddha_host+addSelectBuddha_url)
        print(rep.json())

        # 断言返回code=0表示接口调用成功
        self.assertEqual(self.addSelectBuddhaCode, 0)

        #3.以恭请的佛像列表-分页
    def test_hasSelectBuddhaListPage_url_(self):
        #入参信息
        hasSelectBuddhaListPage_data = {
            "userId":10000,
            "pageSize":212,
            "pageIndex":211,
        }
        #发送post请求测试以恭请佛像列表-分页接口
        rep = requests.post(url=hasSelectBuddhaListPage_host+hasSelectBuddhaListPage_url,data=hasSelectBuddhaListPage_data)
       #获取接口返回值code
        self.hasSelectBuddhaListPageCode = rep.json()['code']
        #打印接口UIL和返回信息
        print(hasSelectBuddhaListPage_host+hasSelectBuddhaListPage_url)
        print(rep.json())

        #断言返回code=0表示接口调用成功
        self.assertEqual(self.hasSelectBuddhaListPageCode,0)

        #4.



















    def tearDown(self):
        pass

if '__name__'=='__main__':
    unittest.main()
