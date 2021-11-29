'''
百口泉值班车调度-申请领导审批"长途"工单-同意
'''
from common import configHttp
from common.log import logs
from util import readConfig,readExcel,geturl,get_path,editConfig
import json
import unittest
import datetime,os

taskId=''
processInstanceId=''
case=None
title=''
res=None
getpath=get_path.getPath()
class TestCarDispatch2(unittest.TestCase):
    def setUp(self):
        print("测试开始。。。")
        self.datafile=os.path.join(getpath+'util/cardispatch.txt')
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

    def test_2_approve1(self):
        interdata = self.getInterface('申请领导审批通过')
        self.getDataBytitle('待办工单列表')
        param = eval(interdata['param'])
        param['taskId'] = readConfig.ReadConfig("CARDISPATCH","taskId")
        param['processInstanceId'] =readConfig.ReadConfig("CARDISPATCH","processInstanceId")
        interdata['param'] = param
        print(interdata['name'])
        self.checkresult(interdata['name'], interdata['interface'], eval(interdata['header']), interdata['method'],
                         interdata['param'], interdata['result'])

     # 获取待办的工单任务id和数据id
    def getDataBytitle(self, name):
        global res, processInstanceId, taskId
        interdata = self.getInterface(name)
        interface = interdata['interface'] + '&title' + title
        dataresult = configHttp.ConfigHttp().run_method(interdata['method'], interface, eval(interdata['header']),
                                                        interdata['param'])
        # 将json转化为python编码
        res = json.loads(dataresult)
        data=None
        datalist = res['content']
        for d in datalist:
            if d['title'] == title:
                data=d
                #写入待办工单的ID
                editConfig.EditConfig("CARDISPATCH","taskId",d['taskId'])
                editConfig.EditConfig("CARDISPATCH", "processInstanceId", d['processInstanceId'])
        return data




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
                    data=self.getDataBytitle('待办工单列表')
                    self.assertEqual(data['status'], 'handle')
                    self.assertEqual(data['statusName'], '处理中')
                    self.assertEqual(data['processDefinitionId'], '1651f255-3eb3-11ec-a43f-fecb102cf6d9')
                    # self.assertEqual(data['processId'], '249684946491723776')
                    self.assertEqual(data['taskNumber'], 'T3')
            except AssertionError as e:
                logs.error('用例[%s]失败，错误信息：%s' % (name, e))
                logs.info('接口返回错误信息：%s' % res)
                raise

        elif(result=='false'):
            try:
                self.assertEqual(res, False)
            except AssertionError as e:
                logs.error('用例[%s]失败，错误信息：%s' %(name,e))
                raise
        else:
            logs.error('用例[%s]失败，错误信息：%s' % (name, res))
            logs.info('用例body:%s' % param)


if __name__=='__main__':
   unittest.main()

