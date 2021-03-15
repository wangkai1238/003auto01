"""统一页面对象入口类"""
from page.page_apply_data import PageApplyData
from page.page_lp_login import PageLpLogin

class PageIn:

    def __init__(self,driver):
        self.driver = driver

    # 返回 登录 页面对象
    def page_get_PageLpLogin(self):
        return PageLpLogin(self.driver)

    # 返回 登录 页面对象
    def page_get_PageApplyData(self):
        return PageApplyData(self.driver)

