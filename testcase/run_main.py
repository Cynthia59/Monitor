#encoding: utf-8
"""
@project = Monitor
@file = run_main
@function = 
@author = Cindy
@create_time = 2018/6/25 12:21
@python_version = 3.x
"""
from base import htmlReport, center_login, myluban_login, shell_login
from HTMLTestRunner import HTMLTestRunner
import time, unittest


suite = unittest.TestSuite()
suite.addTest(center_login.CenterTest('test_login'))
suite.addTest(myluban_login.MylubanTest('test_login'))
suite.addTest(shell_login.ShellTest('test_login_BE'))

if __name__ == '__main__':

    now = time.strftime("%Y-%m-%d %H-%M-%S")
    file_name = './report/' + now + 'result.html'
    fp = open(file_name, 'wb')
    runner = HTMLTestRunner(stream=fp, title='正式外网各系统测试', description='用例执行结果：')
    res = runner.run(suite)
    if res.error_count > 0:
        assert False
    else:
        assert True
    fp.close()
    htmlReport.HtmlReport()