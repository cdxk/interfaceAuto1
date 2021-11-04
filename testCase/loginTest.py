from common import configHttp
from util import readConfig,readExcel,geturl
import json
import unittest
import paramunittest

url=geturl.GetUrl().get_url()
data_xls=readExcel.ReadExcel().read_excel('data.xlsx','caselist')
@paramunittest.parametrized(*data_xls)
class TestUserLogin(unittest.TestCase):
    def setParameters(self,case_name,interface,method,param,result):
        self.case_name=case_name
        name=case_name
        self.interface=interface
        self.method=method
        self.param=param
        self.result=result
    def setUp(self):
        print(self.case_name+"测试开始。。。")
    def tearDown(self):
        print(self.case_name+"测试结束。。。")
    def checkresult(self):
        new_url=geturl.GetUrl().get_url()
        result=configHttp.ConfigHttp().run_method(self.method,new_url+self.interface,self.param)
        res=json.loads(result)
        print(res)
        if(self.case_name=='case_ok'):
            self.assertEqual(res['result'],True)
        if(self.case_name=='case_error'):
            self.assertEqual(res['result'],False)

    def test_case(self):
        self.checkresult()

if __name__=='__main__':
    unittest.main()