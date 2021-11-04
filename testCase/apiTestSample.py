import unittest

class ApiTestSample(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def add(self,input01,input02):
        result=input01+input02
        return result
    def test_add(self):
        testResult=self.add(input01=1,input02=2)
        self.assertEqual(testResult,3)

if __name__=='__main__':
    unittest.main()


