from common import configHttp
from common.log import logs
from util import readConfig,readExcel,geturl,get_path
import json
import unittest
import paramunittest
from ddt import ddt,unpack,data

# url=geturl.GetUrl().get_url()
# data_xls=readExcel.ReadExcel().read_excel('data.xlsx','caselist')
# paramunittest开始
# @paramunittest.parametrized(*data_xls)
# class TestUserLogin(unittest.TestCase):
#     def setParameters(self,case_name,interface,method,param,result):
#         self.case_name=case_name
#         name=case_name
#         self.interface=interface
#         self.method=method
#         self.param=param
#         self.result=result
#     def setUp(self):
#         print(self.case_name+"测试开始。。。")
#     def tearDown(self):
#         print(self.case_name+"测试结束。。。")
#     def checkresult(self):
#         new_url=geturl.GetUrl().get_url()
#         result=configHttp.ConfigHttp().run_method(self.method,new_url+self.interface,self.param)
#         res=json.loads(result)
#         print(res)
#         if(self.case_name=='case_ok'):
#             self.assertEqual(res['result'],True)
#         if(self.case_name=='case_error'):
#             self.assertEqual(res['result'],False)
#
#     def test_case(self):
#         self.checkresult()
# paramunittest结束

#ddt开始
#url=geturl.GetUrl().get_url()
case=readExcel.ReadExcel().read_excel(get_path.getPath()+'data/interfaces.xlsx','bi')
@ddt
class TestApi(unittest.TestCase):
    def setUp(self):
        print("测试开始。。。")
        logs.info("测试开始。。。")
    def tearDown(self):
        print("测试结束。。。")
        logs.info("测试结束。。。")
    def checkresult(self,name,interface,header,method,param,result):
        new_url=geturl.GetUrl().get_url()
        results=configHttp.ConfigHttp().run_method(method,new_url+interface,header,param)
        # 将json转化为python编码
        res=json.loads(results)
        logs.info('用例body:%s' % param)
        print('用例body:%s' % param)
        if(result=='true'):
            try:
                if method=='get':
                    self.assertIsNotNone(res['totalElements'])
                else:
                    self.assertEqual(res, True)
            except AssertionError as e:
                logs.error('用例[%s]失败，错误信息：%s' % (name, e))
                logs.info('接口返回错误信息：%s' % res)

        elif(result=='false'):
            try:
                self.assertEqual(res, False)
            except AssertionError as e:
                logs.error('用例[%s]失败，错误信息：%s' %(name,e))
        else:
            logs.error('用例[%s]失败，错误信息：%s' % (name, res))
            logs.info('用例body:%s' % param)
    @data( * case )
    @unpack
    def test_case(self,name,interface,header,method,param,result,isrun):#参数名称必须和case中的key名字一致
        self.checkresult(name, interface, eval(header), method, eval(param), result)


#ddt结束

if __name__=='__main__':
    unittest.main()