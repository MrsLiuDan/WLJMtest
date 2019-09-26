

##########发布善言##########
###接口名称：http://192.168.1.40:8002/api/temple/buddhism/addbuddhism
###编写人员：刘丹
###编写日期：2019-09-25

import requests,unittest
from conf.buddhismUrl import *
import warnings



class addbuddhism(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore',ResourceWarning)     #忽略提示信息
    '''发布善言+2张图片'''
    def test_addbuddhism(self):
        data_json={'userId': 10005, 'content': '接口测试发布善言'}

        #发善言上传图片
        multiple_files = [
            ('file', ('buddhism_imag.jpg', open('../../files/buddhism_imag.jpg', 'rb'), 'image/jpg')),
            ('file', ('multiple_files.png', open('../../files/multiple_files.png', 'rb'), 'image/png'))]

        ref=requests.post(url=host+addbuddhism_url,data=data_json,files=multiple_files)  #浏览器原生表单提交数据
        res=ref.json()
        #断言code返回0表示成功
        res_code=res['code']
        print (res)
        self.assertEqual(res_code,0)


    def tearDown(self):
        pass



if '__name__' == '__main__':
    unittest.main()