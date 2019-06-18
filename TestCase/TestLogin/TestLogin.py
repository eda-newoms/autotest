import os
import time

from selenium import webdriver
import Common.Login;
import unittest;
import Common.HTMLTestRunner;
import  fileinput;
#from unittest
import io;
class TestDict(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("*******start test case*******");

    @classmethod
    def tearDownClass(cls):
        print("*******finish test case*******");

    def test_login(self):
        driver = webdriver.Chrome();
        Common.Login.Login(driver);
        
        print(driver.current_url);
        driver.close();

if __name__ == '__main__':
    suit=unittest.TestSuite();
    testCase = os.path.basename(__file__);

    testCaseList = [TestDict(testCase)];
    suit.addTests(testCaseList);

    #find Log folder path, to save test reports
    dir=os.path.abspath('..')
    path=os.path.dirname(dir)
    file=os.path.join(path,'Log')

    now= time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
    filename = now+"_testReport.html"  # 定义个报告存放路径，支持相对路径
    report=os.path.join(file,filename)
    f = open(report, 'wb')  # 结果写入HTML 文件

    runner=Common.HTMLTestRunner.HTMLTestRunner(stream=f,verbosity=2, title='EDA Newoms Auto Test Report', description=u'自动化测试报告汇总:')
    runner.run(suit)
    f.close();
