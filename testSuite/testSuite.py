import os
import unittest
from util import readExcel,get_path
from common import HTMLTestRunner#,SendEmail


readExcel=readExcel.ReadExcel().read_excel(get_path.getPath()+'data/interfaces.xlsx','bi')
getpath=get_path.getPath()
resultHtml=os.path.join(getpath+'result')

class TestSuite():

    def __init__(self):
        print("=========testsuite开始")
        global resultPath
        resultPath=os.path.join(resultHtml+'/report.html')
        print(resultPath)
        self.testcase=os.path.join(getpath+'testCase')
        self.casefile=os.path.join(getpath+'util/caselist.txt')
        self.caselists=[]

    def set_case_list(self):
        print(self.casefile)
        fb=open(self.casefile)
        for value in fb.readlines():
            print(value)
            data=str(value)
            if data !='' and not data.startswith('#'):
                self.caselists.append(data.replace('\n',''))
        fb.close()

    def set_case_suite(self):
        test_suite=unittest.TestSuite()
        test_module=[]
        self.set_case_list()
        for case in self.caselists:
            print(self.testcase+case+'.py')
            discover=unittest.defaultTestLoader.discover(self.testcase,pattern=case+'.py',top_level_dir=None)
            test_module.append(discover)
            print('test_module:'+str(test_module))
        if len(test_module) > 0:
            for suite in test_module:
                print('suite:' + str(suite))
                test_suite.addTest(suite)
                # for test_name in suite:
                #     print("******"+str(test_name))
                #     test_suite.addTest(test_name)

        else:
            return None
        return test_suite

    def run(self):
        fp = open(resultPath, 'wb')
        try:
            suite=self.set_case_suite()
            print(str(suite))
            if suite is not None:
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
                runner.run(suite)
                #发送邮件这里加
            else:
                print('suite is None')
        except Exception as e:
            print(str(e))
        finally:
            fp.close()

if __name__=='__main__':
    TestSuite().run()










