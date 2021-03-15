from selenium import webdriver

class GetDriver:
    # 1.声明Driver
    __web_driver = None

    # 2.获取driver
    @classmethod
    def get_web_driver(cls, url):
        # 如果后台有未停止的webdiver先退出置空
        if  cls.__web_driver is None:
            cls.__web_driver = webdriver.Chrome()
            cls.__web_driver.maximize_window()
            cls.__web_driver.get(url)
        return cls.__web_driver

    @classmethod
    def quit_web_driver(cls):
        if cls.__web_driver:
            cls.__web_driver.quit()
            cls.__web_driver = None
