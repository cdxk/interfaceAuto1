from common.log import logs
import unittest
class LogsTestSample(unittest.TestCase):
    def setUp(self):
        print("测试开始。。。")
    def tearDown(self):
        print("测试结束。。。")
    def logstest(self):
        print(111)
        try:
            self.assertEqual(u"name", u"name1")
        except AssertionError as e:
            logs.error('用例1:%s' % e)



if __name__=='__main__':
    LogsTestSample().logstest()