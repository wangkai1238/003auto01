# 创建封装WebBase基类
from time import sleep

from selenium.webdriver.common.by import By

from base.base import Base, log


class WebBase(Base):
    """web项目专属方法"""

    def web_base_click_element(self, placeholder_text, click_text):
        loc = By.CSS_SELECTOR, "[placehoder='{}']".format(placeholder_text)
        self.base_click(loc)

        sleep(1)

        loc = By.XPATH, "[//*[text()='{}']".format(click_text)
        self.base_click(loc)

    def web_base_is_exist(self, text):
        loc = By.XPATH, "//*[text()='{}']".format(text)
        try:
            self.base_find(loc, timeout=3)
            print("找到{}元素了".format(loc))
            return True
        except:
            print("没找到{}元素".format(loc))
            return False

    # 判断页面是否包含指定元素
    # def web_base_is_exist(self, text):
    #     log.info("正在调用查找页面是否存在指定元素：{} 方法".format(text))
    #     # 1. 组装元素配置信息
    #     loc = By.XPATH, "//*[text()='{}']".format(text)
    #     # 2. 找元素
    #     try:
    #         # 1. 找元素 修改查找元素时间 3
    #         self.base_find(loc, timeout=3)
    #         # 2. 输出找到信息
    #         print("找到：{} 元素啦！".format(loc))
    #         # 3. 返回 True
    #         return True
    #     except:
    #         # 1. 输出未找到信息
    #         print("没有找到：{} 元素！".format(loc))
    #         # 2. 返回False
    #         return False
