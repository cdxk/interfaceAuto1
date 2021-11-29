'''
百口泉值班车调度-长途-全部同意流程
'''

from common import configHttp
from common.log import logs
from util import readConfig,readExcel,geturl,get_path
import json
import unittest
import datetime


taskId=''
processInstanceId=''
case=None
title=''
res=None

class TestApi(unittest.TestCase):
    def setUp(self):
        print("测试开始。。。")
        global case
        if case==None:
            case = readExcel.ReadExcel().read_excel(get_path.getPath() + 'data/interfaces.xlsx', '值班车')
        logs.info("测试开始。。。")
    def tearDown(self):
        print("测试结束。。。")
        logs.info("测试结束。。。")
    #获取具体的接口用例
    def getInterface(self,name):
        for n in case:
            if n['name']==name:
                return n

    def test_1_add(self):
        interdata=self.getInterface('创建长途')
        param = eval(interdata['param'])
        global title
        title = "长途" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        param['title'] = title
        interdata['param'] = param
        print(interdata['name'])
        self.checkresult(interdata['name'], interdata['interface'], eval(interdata['header']), interdata['method'],
                         interdata['param'], interdata['result'])


        #申请领导审批
    def test_2_approve1(self):
        interdata = self.getInterface('申请领导审批通过')
        self.getDataBytitle('待办工单列表')
        param = eval(interdata['param'])
        param['taskId'] = taskId
        param['processInstanceId'] = processInstanceId
        interdata['param'] = param
        print(interdata['name'])
        self.checkresult(interdata['name'], interdata['interface'], eval(interdata['header']), interdata['method'],
                         interdata['param'], interdata['result'])

    #生产运行科领导审批通过
    def test_3_approve2(self):
        interdata = self.getInterface('生产运行科领导审批通过')
        self.getDataBytitle('待办工单列表')
        param = eval(interdata['param'])
        param['taskId'] = taskId
        param['processInstanceId'] = processInstanceId
        interdata['param'] = param
        print(interdata['name'])
        self.checkresult(interdata['name'], interdata['interface'], eval(interdata['header']), interdata['method'],
                         interdata['param'], interdata['result'])

     # 值班厂领导审批通过
    def test_4_approve3(self):
        interdata = self.getInterface('值班厂领导审批通过')
        self.getDataBytitle('待办工单列表')
        param = eval(interdata['param'])
        param['taskId'] = taskId
        param['processInstanceId'] = processInstanceId
        interdata['param'] = param
        print(interdata['name'])
        self.checkresult(interdata['name'], interdata['interface'], eval(interdata['header']), interdata['method'],
                         interdata['param'], interdata['result'])


    #  # 厂调盖章
    def test_5_approve3(self):
        interdata = self.getInterface('厂调盖章')
        self.getDataBytitle('待办工单列表')
        param = eval(interdata['param'])
        param['taskId'] = taskId
        param['processInstanceId'] = processInstanceId
        interdata['param'] = param
        print(interdata['name'])
        self.checkresult(interdata['name'], interdata['interface'], eval(interdata['header']),
                         interdata['method'],
                         interdata['param'], interdata['result'])


      #检查工单状态
    def test_6_checkStatus(self):
        interdata = self.getInterface('百口泉工单查询')
        interface = interdata['interface'] + '&title' + title
        dataresult = configHttp.ConfigHttp().run_method(interdata['method'], interface, eval(interdata['header']),
                                                        interdata['param'])
        results=json.loads(dataresult)
        print(interdata['name'])
        if results['empty']==False:
            datalist = results['content']
            try:
                for d in datalist:
                    if d['title'] == title:
                        self.assertEqual(d['status'], "success")
                        print("===状态正常===")
                        logs.info('状态验证正常，标题：%s' % title)

            except AssertionError as e:
                print("===状态异常常===")
                logs.error('用例[%s]失败，错误信息：%s' % (interdata['name'], e))
                logs.info('接口返回错误信息：%s' % results)



    #获取待办的工单任务id和数据id
    def getDataBytitle(self,name):
        global res,processInstanceId,taskId
        interdata = self.getInterface(name)
        interface = interdata['interface'] + '&title' + title
        dataresult = configHttp.ConfigHttp().run_method(interdata['method'], interface, eval(interdata['header']),
                                                        interdata['param'])
        # 将json转化为python编码
        res = json.loads(dataresult)

        datalist=res['content']
        for d in datalist:
            if d['title']==title:
                processInstanceId=d['processInstanceId']
                taskId=d['taskId']

    def checkresult(self,name,interface,header,method,param,result):
        results=configHttp.ConfigHttp().run_method(method,interface,header,param)
        # 将json转化为python编码
        res=json.loads(results)
        logs.info('用例名称:%s' % name)
        logs.info('用例body:%s' % param)
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


if __name__=='__main__':
    unittest.main()
