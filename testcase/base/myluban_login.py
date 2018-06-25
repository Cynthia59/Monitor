#encoding: utf-8
"""
@project = Monitor
@file = mylyban_login
@function = myluban(web)相关监控测试
@author = Cindy
@create_time = 2018/6/25 13:14
@python_version = 3.x
"""
from . import myUnit
import time, unittest

class MylubanTest(myUnit.MyTest):

    def test_login(self):
        self.url = 'http://www.myluban.com/#/login'
        self.driver.get(self.url)
        try:
            self.driver.find_element_by_xpath('//*[@placeholder="请输入鲁班通行证账号或手机号"]').send_keys(self.username)
            self.driver.find_element_by_xpath('//*[@placeholder="请输入密码"]').send_keys(self.password)
            self.driver.find_element_by_xpath('//*[@id="loginPer"]').click()
            time.sleep(1)
        except Exception as e:
            print(e)
        finally:
            if self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/a/img').is_displayed():
                assert True
            else:
                assert False


if __name__ == '__main__':
    unittest.main()