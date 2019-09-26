

##########举报文章##########
###接口名称：http://192.168.1.40:8002/api/temple/buddhism/report
###编写人员：刘丹
###编写日期：2019-09-25

import requests,unittest
from conf.buddhismUrl import *
from common.comm_method import *
import warnings



class reportBuddhism(unittest.TestCase):
    def setUp(self) -> None:
        warnings.simplefilter('ignore',ResourceWarning)     #忽略提示信息
    '''举报善言文章+2张图片'''
    def test_reportBuddhism(self):
        #测试流程 1、从全部善言一条善言文章ID,  2、举报该善言文章
        buddhismId=get_AllbuddhismId(url=host+getIndexBuddhismList_url)
        data_json={'userId': 10001,
                   'articleId':buddhismId,
                   'reportContent':'举报文章举报文章',
                   'reportReason':'举报原因'
                    }
        #发善言上传图片
        multiple_files = [('file', ('buddhism_imag.jpg', open('../../files/buddhism_imag.jpg', 'rb'), 'image/jpg')),
            ('file', ('multiple_files.png', open('../../files/multiple_files.png', 'rb'), 'image/png'))]

        ref=requests.post(url=host+report_url,data=data_json,files=multiple_files)
        res=ref.json()
        #断言code返回0表示成功
        res_code=res['code']
        self.assertEqual(res_code,0)
        print (res)

    def tearDown(self) -> None:
        pass



if '__name__' == '__main__':
    unittest.main()