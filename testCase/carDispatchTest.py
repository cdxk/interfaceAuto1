'''
百口泉值班车调度-创建并必提交"长途"工单
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
class TestCarDispatch(unittest.TestCase):
    def setUp(self):
        print("百口泉值班车测试开始。。。")
        self.dispatch=carDispatch.CarDispatch('值班车')
        logs.info("百口泉值班车测试开始。。。")
    def tearDown(self):
        print("百口泉值班车测试结束。。。")
        logs.info("百口泉值班车测试结束。。。")

    #长途车全部通过流程
    # def test_long_allagree(self):
    #     try:
    #         self.dispatch.addAndCommit('长途')
    #         self.dispatch.approve('申请领导审批通过')
    #         self.dispatch.approve('长途生产运行科通过')
    #         self.dispatch.approve('值班厂领导审批通过')
    #         self.dispatch.approve('厂调盖章')
    #         logs.info("===长途车流程全部通过处理完毕===")
    #     except Exception:
    #         print('流程出错')
    #         logs.error("===长途车流程全部通过处理出错===")
    #         raise
    # #短途全部通过
    # def test_short_allagree(self):
    #     try:
    #         self.dispatch.addAndCommit('短途')
    #         self.dispatch.approve('申请领导审批通过')
    #         self.dispatch.approve('短途生产运行科通过')
    #         self.dispatch.approve('厂调盖章')
    #         logs.info("===短途车流程全部通过处理完毕===")
    #     except Exception:
    #         logs.info("===短途车流程全部通过处理完毕===")
    #         raise
    # #申请领导拒绝
    # def test_applyLeader_refused(self):
    #     try:
    #         self.dispatch.addAndCommit('短途')
    #         self.dispatch.approve('申请领导审批驳回')
    #     except Exception:
    #         raise

    #
    # #生产运行科拒绝
    # def test_productionLeader_refused(self):
    #     try:
    #         self.dispatch.addAndCommit('短途')
    #         self.dispatch.approve('申请领导审批通过')
    #         self.dispatch.approve('生产运行科驳回')
    #         logs.info("===生产运行科驳回处理完毕===")
    #     except Exception:
    #         logs.error("===生产运行科驳回处理报错===")
    #         raise
    #
    #
    # #厂领导拒绝
    def test_factoryLeader_refused(self):
        try:
            self.dispatch.addAndCommit('长途')
            self.dispatch.approve('申请领导审批通过')
            self.dispatch.approve('长途生产运行科通过')
            self.dispatch.approve('值班厂领导审批驳回')
            logs.info("===厂领导驳回处理完毕===")
        except Exception:
            logs.error("===厂领导驳回处理报错===")
            raise
    # #拒绝关闭
    # def test_factoryLeader_refused(self):
    #     try:
    #         self.dispatch.addAndCommit('短途')
    #         self.dispatch.approve('申请领导审批驳回')
    #         self.dispatch.closedata('关闭')
    #         logs.info("===关闭工单完毕===")
    #     except Exception:
    #         logs.error("===关闭工单报错===")
    #         raise

    # def test_addDraft(self):
    #     try:
    #         self.dispatch.addAndCommit('创建草稿')
    #     except Exception:
    #         print('流程出错')
    #         raise




if __name__=='__main__':
   unittest.main()

