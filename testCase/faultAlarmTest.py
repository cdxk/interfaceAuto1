'''
故障告警工单
'''

from common import configHttp
from common.log import logs
from modelMethod import carDispatch
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
class TestFaultAlarm(unittest.TestCase):
    def setUp(self):
        print("故障告警工单测试开始。。。")
        self.dispatch=carDispatch.CarDispatch('故障')
        logs.info("故障告警工单测试开始。。。")
    def tearDown(self):
        print("故障告警工单测试结束。。。")
        logs.info("故障告警工单测试结束。。。")

    #工单全部通过流程（需领导审核流程）
    # def test_allagree(self):
    #     try:
    #         self.dispatch.addAndCommit('创建提交领导审核')
    #         self.dispatch.approve('作业区值班领导同意')
    #         self.dispatch.approve('厂调审核需领导审核')
    #         self.dispatch.approve('生产运行科同意且需领导')
    #         self.dispatch.approve('厂级领导发表意见')
    #         self.dispatch.approve('录入处理意见')
    #         logs.info("===故障工单流程全部通过处理完毕===")
    #     except Exception:
    #         print('流程出错')
    #         logs.error("===故障工单流程全部通过处理出错===")
    #         raise

    #不需厂领导录意见
    def test_allagree(self):
        try:
            self.dispatch.addAndCommit('创建提交领导审核')
            self.dispatch.approve('作业区值班领导同意')
            # self.dispatch.approve('厂调审核需领导审核')
            # self.dispatch.approve('生产运行科同意无需领导')
            # self.dispatch.approve('录入处理意见')
            logs.info("===故障工单流程全部通过处理完毕===")
        except Exception:
            print('流程出错')
            logs.error("===故障工单流程全部通过处理出错===")
            raise

    # 创建人-厂调-结束
    # def test_short(self):
    #     try:
    #         self.dispatch.addAndCommit('创建提交厂调审核')
    #         self.dispatch.approve('厂调审核无需领导审核')
    #         logs.info("===创建人-厂调-结束流程全部通过处理完毕===")
    #     except Exception:
    #         logs.error("===创建人-厂调-结束流程全部通过处理报错===")
    #         raise

    #作业区领导驳回
    # def test_applyLeader_refused(self):
    #     try:
    #         self.dispatch.addAndCommit('创建提交领导审核')
    #         self.dispatch.approve('作业区值班领导驳回')
    #         logs.info("===故障工单作业区领导驳回完成===")
    #     except Exception:
    #         logs.error("===故障工单作业区领导驳回完出错==")
    #         raise

    #生产运行科驳回
    # def test_productionLeader_refused(self):
    #     try:
    #         self.dispatch.addAndCommit('创建提交领导审核')
    #         self.dispatch.approve('作业区值班领导同意')
    #         self.dispatch.approve('厂调审核需领导审核')
    #         self.dispatch.approve('生产运行科驳回')
    #         logs.info("===生产运行科驳回处理完毕===")
    #     except Exception:
    #         logs.error("===生产运行科驳回处理报错===")
    #         raise

    #驳回关闭
    # def test_factoryLeader_refused(self):
    #     try:
    #         self.dispatch.addAndCommit('创建提交领导审核')
    #         self.dispatch.approve('作业区值班领导驳回')
    #         self.dispatch.closedata('关闭')
    #         logs.info("===关闭故障工单完毕===")
    #     except Exception:
    #         logs.error("===关闭故障工单报错===")
    #         raise

    # def test_addDraft(self):
    #     try:
    #         self.dispatch.addAndCommit('创建草稿')
    #     except Exception:
    #         print('流程出错')
    #         raise




if __name__=='__main__':
   unittest.main()

