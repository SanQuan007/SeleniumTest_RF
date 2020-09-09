#-*-coding:utf-8-*-
__author__ = 'SanQuan'
__date__ = '2020/9/7'

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

def get_locator_value(locator_key):
    from variables import locator
    locator_variables = locator.PROJECT_LOCATOR
    class_name = locator_key.split("_")[0]
    class_variables = locator_variables[class_name]
    locator_value = class_variables[locator_key]
    logging.info("Locato is {}:{}".format(locator_key, locator_value))
    return locator_value


if __name__ == '__main__':
    get_locator_value("通用_首页_BUTTON_登录")