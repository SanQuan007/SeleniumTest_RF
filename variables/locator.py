#-*-coding:utf-8-*-
__author__ = 'SanQuan'
__date__ = '2020/9/7'

PROJECT_LOCATOR = {
    "通用": {
        "通用_首页_BUTTON_登录": "xpath=//a[text()='登录']",
        "通用_首页_TEXT_你好": "xpath=//a[contains(text(),'你好')]",
        "通用_首页_BUTTON_主题": "xpath=//a[text()='主题']",
    },
    "登录": {
        "登录_首页_TITLE_输入账号": "xpath=//*[text()='Log in to your account.']",
        "登录_首页_INPUT_用户名": "id=id_username",
        "登录_首页_INPUT_密码": "id=id_password",
        "登录_首页_BUTTON_登录": "name=submit",
    },
    "主题": {
        "主题_首页_TITLE_主题": "xpath=//h1[text()='主题']",
        "主题_首页_BUTTON_新建主题": "xpath=//a[text()='新建主题']",
        "主题_新建_TITLE_新主题": "xpath=//h2[text()='添加一个新主题：']",
        "主题_新建_INPUT_主题名称": "id=id_text",
        "主题_新建_BUTTON_添加": "name=submit",
    },
}