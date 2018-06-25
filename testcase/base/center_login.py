#encoding: utf-8
"""
@project = Monitor
@file = center_login
@function = center的相关监控测试
@author = Cindy
@create_time = 2018/6/25 11:05
@python_version = 3.x
"""
from selenium import webdriver
import time, unittest
from . import myUnit


class CenterTest(myUnit.MyTest):

    def test_login(self):
        self.url = 'http://center.lubansoft.com/#/login'
        self.driver.get(self.url)
        try:
            self.driver.find_element_by_xpath('//*[@id="username"]/input').send_keys(self.username)
            self.driver.find_element_by_xpath('//*[@id="password"]/input').send_keys(self.password)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[2]/form/div[4]/button/span/span').click()
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[2]/form/div[4]/button/span/span').click()
            time.sleep(4)
        except Exception as e:
            print(e)
        finally:
            if self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div[2]/div[3]/div/div/div/h3').is_displayed():
                assert True
            else:
                assert False


if __name__ == '__main__':
    unittest.main()
