import os
import time

from selenium import webdriver
import Common.Login;
import unittest;
import Common.HTMLTestRunner;
import Common.RmaOder


class TestDict(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("*******start test case*******");

    @classmethod
    def tearDownClass(cls):
        print("*******finish test case*******");

    def test_login(self):
        # 1. 登录系统
        driver = webdriver.Chrome();
        Common.Login.Login(driver);

        # 2.进入入库单界面，创建入库单
        RMA = Common.RmaOder.RMA();
        RMA.openRmaPage(driver);
        Rev = RMA.createRMA(driver);

        #3.断言，步骤二新建的入库单存在
        result = RMA.searchRev(driver,Rev);
        self.assertTrue(result,"没找到入库单："+Rev);
        if(result):
            print("新建入库单成功: "+Rev);

if __name__ == '__main__':
    suit = unittest.TestSuite();
    testCase = os.path.basename(__file__);

    testCaseList = [TestDict(testCase)];
    suit.addTests(testCaseList);

    # find Log folder path, to save test reports
    dir = os.path.abspath('..')
    path = os.path.dirname(dir)
    file = os.path.join(path, 'Log')

    now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    filename = now + "_testReport.html"  # 定义个报告存放路径，支持相对路径
    report = os.path.join(file, filename)
    f = open(report, 'wb')  # 结果写入HTML 文件

    runner = Common.HTMLTestRunner.HTMLTestRunner(stream=f, verbosity=2, title='EDA Newoms Auto Test Report',
                                                  description=u'自动化测试报告汇总:')
    runner.run(suit)
    f.close();
