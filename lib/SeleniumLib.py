#-*-coding:utf-8-*-
__author__ = 'SanQuan'
__date__ = '2020/9/5'

from lib import SysLib
from SeleniumLibrary import SeleniumLibrary
from SeleniumLibrary.base import keyword
from SeleniumLibrary.keywords import (AlertKeywords,
                                      BrowserManagementKeywords,
                                      CookieKeywords,
                                      ElementKeywords,
                                      FormElementKeywords,
                                      FrameKeywords,
                                      JavaScriptKeywords,
                                      RunOnFailureKeywords,
                                      ScreenshotKeywords,
                                      SelectElementKeywords,
                                      TableElementKeywords,
                                      WaitingKeywords,
                                      WebDriverCache,
                                      WindowKeywords)

class SeleniumLib(SeleniumLibrary):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, *args, **kwargs):
        super(SeleniumLib,self).__init__(*args, **kwargs)

    def find_element(self, locator, parent=None):
        if "="not in locator:
            locator = SysLib.get_locator_value(locator)
        return super(SeleniumLib, self).find_element(locator, parent=parent)

    @keyword("点击")
    def click_element(self, locator):
        locator = self.find_element(locator)
        return ElementKeywords(self).click_element(locator=locator)

    @keyword("检查元素")
    def wait_until_page_contains_element(self, locator):
        locator = self.find_element(locator)
        return WaitingKeywords(self).wait_until_page_contains_element(locator=locator)

    @keyword("检查元素不存在")
    def wait_until_page_does_not_contain_element(self, locator):
        locator = self.find_element(locator)
        return WaitingKeywords(self).wait_until_page_does_not_contain_element(locator=locator)

    @keyword("检查文本")
    def wait_until_page_contains(self, text):
        return WaitingKeywords(self).wait_until_page_contains(text=text)

    @keyword("检查文本不存在")
    def wait_until_page_does_not_contain(self, text):
        return WaitingKeywords(self).wait_until_page_does_not_contain(text=text)

    @keyword("输入文本")
    def input_text(self, locator, text):
        locator = self.find_element(locator)
        return FormElementKeywords(self).input_text(locator=locator, text=text)


if __name__ == '__main__':
    print(SeleniumLib().find_element("通用_首页_BUTTON_登录"))