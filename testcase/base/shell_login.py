#encoding: utf-8
"""
@project = Monitor
@file = shell
@function = 
@author = Cindy
@create_time = 2018/6/25 14:21
@python_version = 3.x
"""
import subprocess
import unittest
import autoit, time

class ShellTest(unittest.TestCase):

    def test_login_BE(self):
        self.path = r'D:\Luban PDS\Luban Explorer\shell\PDSShell.exe'
        self.username = 'cynthia'
        self.password = 'd76bf909a7646e788a1fcbdefb0ddfe1'
        self.ip = 'pds.lubansoft.com'
        self.epid = '1'
        self.pros = 'Luban Explorer.exe'
        try:
            subprocess.Popen(self.path + ' ' + self.username + '$$' + self.password + '$$' + self.ip + '$$' + self.epid)
            time.sleep(10)
        except Exception as e:
            print(e)
        finally:
            if autoit.process_exists(self.pros):
                autoit.process_close(self.pros)
                assert True
            else:
                autoit.process_close('PDSShell.exe')
                assert False

if __name__ == '__main__':
    unittest.main()

