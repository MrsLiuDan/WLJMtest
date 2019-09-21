# coding:utf-8
import unittest
import requests
from conf.user_conf import *  #在conf.user_conf中导入所有接口的入参信息
#定义一个全局变量
# session = requests.Session()
class Test_Kuaidi(unittest.TestCase):
    def setUp(self):
        pass
        # 登录的入参
    def test_login(self):
        login_data = {
            "username": "13715035908",
            "password": "123456"
        }
        rep = requests.post(url=login_host+login_url, data=login_data)
        # return rep.json()
        log_re = rep.json()
        loginCode = log_re['code'] # json获取字符串data的值
        # userId = a['userId']
        print(login_host+login_url)
        print(log_re)

        #断言返回code=0表示接口调用成功
        self.assertEqual(loginCode,0)

    def tearDown(self):
        pass

if '__name__'=='__main__':
    unittest.main()
