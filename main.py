import os
import sys
from testSuite.testSuite import TestSuite
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
PathProject = os.path.split(rootPath)[0]
sys.path.append(rootPath)
sys.path.append(PathProject)
print("=====构建===开始====")
TestSuite().run()
print("=====构建===结束====")
