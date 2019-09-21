
# coding:utf-8
import unittest
'''测试祭拜功能'''
class Test_Kuaidi(unittest.TestCase):
    def setUp(self):
       pass    #前置条件

    def test_test1(self):   #测试用例1 请佛
       print ('test1')    #脚本

    def test_test2(self):   #测试用例2
       print ('test2')

    def teardowm(self):    #后置条件  ()
        pass



if __name__ == "__main__":
    unittest.main()