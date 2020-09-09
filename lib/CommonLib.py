#-*-coding:utf-8-*-
__author__ = 'SanQuan'
__date__ = '2020/9/9'

import os
import datetime
from SeleniumLibrary.base import keyword

class CommonLib(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        pass
    @keyword("获取失败用例截图路径")
    def get_fail_case_screenshot_dir(self, log_dir):
        screenshot = os.path.join(os.path.split(log_dir)[0], "screenshot",
                                  datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S'))
        os.makedirs(screenshot)
        return screenshot

    def hello(self, name):
        welocome = "Hello {}".format(name)
        print(welocome)
        return welocome