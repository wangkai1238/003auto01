import allure
import pytest
import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()
class Severity(object):
    Blocker="blocker"
    CRITICAL="critical"
    NORMAL="normal"
    MINOR="minor"
    TRIVIAL="trivial"
@allure.epic("定义项目、当有多个项目是使用。往下是feature")
@allure.feature("TestLpLogin登陆测试模块")
class TestLpLogin:
    @allure.testcase("禅道用例连接地址")
    @allure.issue("对应禅道缺陷管理系统里边的bug地址")
    @allure.title("正常账户和密码测试")
    @allure.story("账户为admin,密码root")
    @allure.description("上面的代码会捕获一个类型为 ExceptionName 的异常。如果您想让 "
                        "catch 块能够处理 try 块抛出的任何类型的异常，则必须在异常声明的括号内使用省略号 .")
    @allure.severity("优先级为：critical")
    @allure.severity(severity_level=Severity.NORMAL)

    # 开始初始化测试环境
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_web_driver(page.url_lp)
        # 通过统一页面对象入口类获取登陆页面对象
        self.lp = PageIn(driver).page_get_PageLpLogin()

    # 结束关闭浏览器驱动对象
    def teardown_class(self):
        # 调用GetDriver,关闭webdriver
        GetDriver.quit_web_driver()

    # 测试业务方法
    @pytest.mark.parametrize("username,password,expect", read_yaml("lp_login.yaml"))
    def test_lp_login(self, username, password, expect):
        # 调用登陆页面组合方法
        self.lp.page_lp_login(username, password)
        try:
            # 断言
            assert expect == self.lp.page_get_nickname()
        except Exception as e:
            log.error("断言出错，错误原因是:{}".format(e))
            print("错误原因是", e)
            # 截图
            self.lp.base_get_img()
            # 抛异常
            raise
