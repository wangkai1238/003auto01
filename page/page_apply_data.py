import time
from time import sleep

import page
from base.web_base import WebBase


class PageApplyData(WebBase):
    #点击导航栏中的API
    def page_click_nav(self):
        self.base_click(page.nav)
        sleep(1)

    #点击导航栏中的应用开发
    def page_click_nav_application(self):
        self.base_click(page.nav_application)
        sleep(1)

    #点击 使用按钮
    def page_click_nav_application_use_btn(self):
        self.base_click(page.nav_application_use_btn)
        sleep(1)

    # 新打开窗口时切换为新窗口句柄并截图
    def base_switch_to_newopen_handle(self):
        # 获取所有窗口句柄
        handles = self.driver.window_handles
        # 获取主窗口句柄
        main_handle = self.driver.current_window_handle
        # 切换为新打开的窗口句柄
        for newopen in handles:
            if newopen != main_handle:
                # 切换为新打开的的窗口句柄
                self.driver.switch_to.window(newopen)
                self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y-%m-%d %H-%M-%S")))

    def page_click_check_box(self):
        self.base_click(page.readed_check_box)

    def page_click_apply_btn(self):
        self.base_click(page.immediately_apply_btn)

    def page_get_autonym_dialog(self):
        return self.base_get_text(page.autonym_dialog_text)

    # 6. 点击查询按钮
    def page_click_find(self):
        # 1. 点击查询按钮
        self.base_click(page.nav)
        return self.web_base_is_exist(page.nav)
        # 2. 暂停时间
        sleep(2)

    def page_apply_data(self):

        self.page_click_nav()
        self.page_click_nav_application()
        self.page_click_nav_application_use_btn()
        self.page_click_check_box()
        self.page_click_apply_btn()

if __name__ == "__main__":
    print(page.nav)
