import os
import sys
from testSuite.testSuite import TestSuite
from testCase.faultAlarm import TestFaultAlarm
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
PathProject = os.path.split(rootPath)[0]
sys.path.append(rootPath)
sys.path.append(PathProject)


if __name__=='__main__':
    print("=====构建===开始====")
    TestFaultAlarm.run()
    print("=====构建===结束====")

