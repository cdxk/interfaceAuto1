'''
百口泉值班车调度-流程接口
'''

from common import configHttp
from common.log import logs
from util import readConfig,readExcel,geturl,get_path
from util.editConfig import EditConfig
import json
import unittest
import datetime,os


taskId=''
processInstanceId=''
case=None
title=''
res=None
getpath=get_path.getPath()
class CarDispatch:
    def __init__(self,sheet):
        print("carDispatch开始。。。")
        global case
        if case==None:
            case = readExcel.ReadExcel().read_excel(get_path.getPath() + 'data/interfaces.xlsx', sheet)
        logs.info("carDispatch开始。。。")

    #获取具体的接口用例
    def getInterface(self,name):
        for n in case:
            if n['name']==name:
                return n

    #创建草稿
    def addDraft(self,interfaceName):
        interdata = self.getInterface(interfaceName)
        param = eval(interdata['param'])
        global title
        title = interfaceName + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        param['title'] = title
        interdata['param'] = param
        print(interdata['name'])
        try:
            self.checkresult(interdata['name'], interdata['interface'], eval(interdata['header']), interdata['method'],
                             interdata['param'], interdata['result'], interdata['status'], interdata['statusName'],
                             interdata['processDefinitionId'], interdata['taskNumber'], interdata['assertinterface'])
        except Exception as e:
            print("新增草稿数据失败")
            raise e

    #创建并提交审核工单
    def addAndCommit(self,interfaceName):
        interdata=self.getInterface(interfaceName)
        param = eval(interdata['param'])
        global title
        title = interfaceName + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        param['title'] = title
        interdata['param'] = param
        print(interdata['name'])
        try:
            self.checkresult(interdata['name'], interdata['interface'], eval(interdata['header']), interdata['method'],
                             interdata['param'], interdata['result'],interdata['status'],interdata['statusName'],
                             interdata['processDefinitionId'],interdata['taskNumber'],interdata['assertinterface'])
        except Exception as e:
            print("新增数据失败")
            raise e

    #申请领导审核
    def applyLeader_agree(self):
        interdata = self.getInterface('申请领导审批通过')
        self.getTodoDataBytitle('待办工单列表')
        param = eval(interdata['param'])
        param['taskId'] = readConfig.ReadConfig().get_config("CARDISPATCH", "taskId")
        param['processInstanceId'] = readConfig.ReadConfig().get_config("CARDISPATCH", "processInstanceId")
        interdata['param'] = param
        print(interdata['name'])
        try:
            self.checkresult(interdata['name'], interdata['interface'], eval(interdata['header']), interdata['method'],
                             interdata['param'], interdata['result'],interdata['status'],interdata['statusName'],
                             interdata['processDefinitionId'],interdata['taskNumber'],interdata['assertinterface'])
        except Exception as e:
            raise

    #生产运行科领导审核
    def productionLeader_agree(self):
        interdata = self.getInterface('生产运行科领导审批通过')
        self.getTodoDataBytitle('待办工单列表')
        param = eval(interdata['param'])
        param['taskId'] = readConfig.ReadConfig().get_config("CARDISPATCH", "taskId")
        param['processInstanceId'] = readConfig.ReadConfig().get_config("CARDISPATCH", "processInstanceId")
        interdata['param'] = param
        print(interdata['name'])
        try:
            self.checkresult(interdata['name'], interdata['interface'], eval(interdata['header']), interdata['method'],
                             interdata['param'], interdata['result'],interdata['status'],interdata['statusName'],
                             interdata['processDefinitionId'],interdata['taskNumber'],interdata['assertinterface'])
        except Exception as e:
            raise

    #值班厂级领导审核
    def factoryLeader_agree(self):
        interdata = self.getInterface('值班厂领导审批通过')
        self.getTodoDataBytitle('待办工单列表')
        param = eval(interdata['param'])
        param['taskId'] = readConfig.ReadConfig().get_config("CARDISPATCH", "taskId")
        param['processInstanceId'] = readConfig.ReadConfig().get_config("CARDISPATCH", "processInstanceId")
        interdata['param'] = param
        print(interdata['name'])
        try:
            self.checkresult(interdata['name'], interdata['interface'], eval(interdata['header']), interdata['method'],
                             interdata['param'], interdata['result'],interdata['status'],interdata['statusName'],
                             interdata['processDefinitionId'],interdata['taskNumber'],interdata['assertinterface'])
        except Exception as e:
            raise

    #厂调盖章
    def seal(self):
        interdata = self.getInterface('厂调盖章')
        self.getTodoDataBytitle('待办工单列表')
        param = eval(interdata['param'])
        param['taskId'] = readConfig.ReadConfig().get_config("CARDISPATCH", "taskId")
        param['processInstanceId'] = readConfig.ReadConfig().get_config("CARDISPATCH", "processInstanceId")
        interdata['param'] = param
        print(interdata['name'])
        try:
            self.checkresult(interdata['name'], interdata['interface'], eval(interdata['header']), interdata['method'],
                             interdata['param'], interdata['result'],interdata['status'],interdata['statusName'],
                             interdata['processDefinitionId'],interdata['taskNumber'],interdata['assertinterface'])
        except Exception as e:
            raise

    #审批处理公用方法
    def approve(self,interfaceName):
        interdata = self.getInterface(interfaceName)
        self.getTodoDataBytitle('待办工单列表')
        param = eval(interdata['param'])
        param['taskId'] = readConfig.ReadConfig().get_config("CARDISPATCH", "taskId")
        param['processInstanceId'] = readConfig.ReadConfig().get_config("CARDISPATCH", "processInstanceId")
        interdata['param'] = param
        print(interdata['name'])
        try:
            self.checkresult(interdata['name'], interdata['interface'], eval(interdata['header']), interdata['method'],
                             interdata['param'], interdata['result'],interdata['status'],interdata['statusName'],
                             interdata['processDefinitionId'],interdata['taskNumber'],interdata['assertinterface'])
        except Exception as e:
            raise

     # 关闭工单
    def closedata(self, interfaceName):
        interdata = self.getInterface(interfaceName)
        self.getTodoDataBytitle('待办工单列表')
        interdata['interface'] = interdata[
                                     'interface'] + "&processInstanceId=" + readConfig.ReadConfig().get_config(
            "CARDISPATCH", "processInstanceId")
        print(interdata['name'])
        try:
            self.checkresult(interdata['name'], interdata['interface'], eval(interdata['header']),
                             interdata['method'],
                             interdata['param'], interdata['result'], interdata['status'],
                             interdata['statusName'],
                             interdata['processDefinitionId'], interdata['taskNumber'],
                             interdata['assertinterface'])
        except Exception as e:
            raise

     # 获取待办的工单任务id和数据id
    def getTodoDataBytitle(self, asserinterface):
        global res, processInstanceId, taskId
        interdata = self.getInterface(asserinterface)
        interface = interdata['interface'] + '&title' + title
        dataresult = configHttp.ConfigHttp().run_method(interdata['method'], interface, eval(interdata['header']),
                                                        interdata['param'])
        # 将json转化为python编码
        res = json.loads(dataresult)
        data=None
        if ('content' in res):
            datalist = res['content']
            for d in datalist:
                if d['title'] == title:
                    data = d
                    if asserinterface == '待办工单列表':
                        # 写入待办工单的ID
                        EditConfig().edit_config("CARDISPATCH", "taskId", d['taskId'])
                        EditConfig().edit_config("CARDISPATCH", "processInstanceId", d['processInstanceId'])

        return data


    def checkresult(self,name,interface,header,method,param,result,status,statusName,processDefinitionId,taskNumber,assertinterface):
        results=configHttp.ConfigHttp().run_method(method,interface,header,param)
        # 将json转化为python编码
        res=json.loads(results)
        logs.info('用例名称:%s' % name)
        logs.info('用例body:%s' % param)
        if(result=='true'):
            try:
                if method=='get':
                    assert res['totalElements']!="0"
                else:
                    data=self.getTodoDataBytitle(assertinterface)
                    if not data is None:
                        if assertinterface == '待办工单列表':
                            # 断言流程节点
                            assert data['status'] == status
                            assert data['statusName'] == statusName
                            assert data['processDefinitionId'] == processDefinitionId
                            assert data['taskNumber'] == taskNumber
                            # assert data['processId'] == 249576824003547136

                        else:
                            # 断言已处理状态todo
                            assert data['status'] == status
                            assert data['statusName'] == statusName
                            assert data['isFile'] == taskNumber #是否归档验证
                    else:
                        raise Exception("接口报错")

            except AssertionError as e:
                logs.error('用例[%s]失败，错误信息：%s' % (name, e))
                logs.info('接口返回错误信息：%s' % res)
                raise  e

        elif(result=='false'):
            try:
                assert not res
            except AssertionError as e:
                logs.error('用例[%s]失败，错误信息：%s' %(name,e))
                raise e
        else:
            AssertionError("excel中result值不符合规范！")
            logs.error('用例[%s]失败，错误信息：%s' % (name, res))
            logs.info('用例body:%s' % param)

    #获取管理工单列表数据详情
    def getDetailByid(self,id):
        interdata = self.getInterface("获取工单详情")
        interdata['interface']=interdata['interface']+id
        print(interdata['interface'])
        try:
            results = configHttp.ConfigHttp().run_method(interdata['method'], interdata['interface'], eval(interdata['header']),
                                                        interdata['param'])
            # 将json转化为python编码
            res = json.loads(results)
            logs.info('用例名称:%s' % "获取工单详情")
            logs.info('用例body:%s' % interdata['param'])
            assert res['code']


        except Exception as e:
            raise


if __name__=='__main__':
   CarDispatch

