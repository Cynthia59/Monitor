#encoding: utf-8
"""
@project = Monitor
@file = htmlReport
@function = 
@author = Cindy
@create_time = 2018/6/25 11:18
@python_version = 3.x
"""
import os, shutil

class HtmlReport():

    def __init__(self):
        #类初始化时直接调用获取最新报告和复制最新报告方法
        self.base_dir = os.path.dirname(os.path.dirname(__file__))
        self.base_dir = str(self.base_dir).replace('\\', '/')
        self.base = self.base_dir.split('./base')[0]
        self.report_dir = self.base + './report'
        self.latest_report = self.get_latest_report()
        self.copy = self.copy_latest_report()

    def get_latest_report(self):
        lists = os.listdir(self.report_dir)
        lists.sort(key=lambda fn: os.path.getmtime(self.report_dir+'\\'+fn))
        print('最新的文件为：', lists[-1])
        file = os.path.join(self.report_dir, lists[-1]).replace('\\','/')
        return file

    def copy_latest_report(self):
        old = self.latest_report
        new = old.split('/20')[0]+'/new_report.html'
        shutil.copyfile(old, new)

if __name__ == '__main__':

    h = HtmlReport()
