#encoding: utf-8
"""
@project = Monitor
@file = myUnit
@function = 
@author = Cindy
@create_time = 2018/6/25 11:12
@python_version = 3.x
"""

from selenium import webdriver
import unittest

class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.username = 'cynthia'
        self.password = 'cynthia123456'

    def tearDown(self):
        self.driver.quit()