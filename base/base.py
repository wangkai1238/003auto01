import os
import time
import allure
from selenium.webdriver.support.wait import WebDriverWait
from config import BASE_PATH
from tools.get_log import GetLog

log = GetLog.get_logger()

class Base:
    def __init__(self, driver):
        log.info("正在初始化driver: {}".format(driver))
        """定义driver,下面查找元素中要传入"""
        self.driver = driver

    def base_find(self, loc, timeout=10, poll=0.5):
        """
        :param loc: 格式为列表或元祖，内容：元素定位信息使用By类
        :param timeout: 查找元素超时时间，默认 30秒
        :param poll: 查找元素频率 默认为0.5
        :return: 元素
        """
        log.info("正在查找元素：{}".format(loc))
        return (WebDriverWait(self.driver,
                              timeout=timeout,
                              poll_frequency=poll)
                .until(lambda x: x.find_element(*loc)))

    def base_input(self, loc, value):
        """
        :param loc: 元素的定位信息
        :param value: 要输入的值
        """
        # 1. 获取元素
        el = self.base_find(loc)
        # 2. 清空操作
        log.info("正在对：{} 元素执行清空操作！".format(loc))
        el.clear()
        # 3. 输入操作
        log.info("正在对：{} 元素执行输入:{} 操作！".format(loc, value))
        el.send_keys(value)

    def base_click(self, loc):
        """
        :param loc: 元素定位信息
        """
        log.info("正在对：{} 元素执行点击操作！".format(loc))
        # 获取元素并点击
        self.base_find(loc).click()

    def base_get_text(self, loc):
        """
        :param loc: 元素定位信息
        :return: 返回元素的文本值
        """
        log.info("正在对：{} 元素获取文本操作！，获取的文本值：{}".format(
            loc, self.base_find(loc).text))
        return self.base_find(loc).text

    file_name = BASE_PATH + os.sep + "image" + os.sep + "err.png"
    def base_get_img(self):
        log.error("断言出错，正在执行截图操作")
        # 1. 调用截图方法
        self.driver.get_screenshot_as_file(self.file_name)
        log.error("断言出错，正在将错误截图写入allure报告")
        # 2. 调用图片写入报告方法
        self.__base_write_img()

    def __base_write_img(self):
        # 1. 获取图片文件流
        with open(self.file_name, "rb") as f:
            # 2. 调用allure.attach附加方法
            allure.attach("错误原因：", f.read(), allure.attach_type.PNG)

if __name__ == "__main__":
    print(BASE_PATH)
    file_name = BASE_PATH + os.sep + "image" + os.sep + "{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S"))
    print(file_name)
