import unittest,requests
from conf.buddhismUrl import *  #在conf.buddhismUrl中导入所有接口的入参信息
from common.comm_method import *

class Comment(unittest.TestCase):
    def setUp(self) -> None:
        pass
    '''评论善言功能'''
    def test_Comment(self):
        #测试流程：1、从全部善言列表获取第一条善言文章ID   2、传入善言文章ID，对该条善言文章进行评论
        #全部善言列表方法封装在common文件夹comm_method中
        buddhismId=get_AllbuddhismId(url=host+getIndexBuddhismList_url)

        #评论文章
        comment_data={
            'userId':10000,
            'articleId':buddhismId,
            'content':'评论文章'
        }
        ref=requests.post(url=host+comment_url,data=comment_data)
        res=ref.json()
        res_code=res['code']
        print (res)
        #code为0 评论成功
        self.assertEqual(res_code,0)

    def tearDown(self) -> None:
        pass
if '__name__'=='__main__':
    unittest.main()
