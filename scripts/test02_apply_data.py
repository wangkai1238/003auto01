import pytest
import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()

class TestApplyData:
    # 1. 初始化
    # @pytest.fixture()
    # print("前置条件，请先登录")
    def setup_class(self):
        # 1. 获取driver
        driver = GetDriver.get_web_driver(page.url_lp)
        # 2. 获取统一入口类对象
        self.page_in = PageIn(driver)
        # 3. 获取PageMpLogin对象并调用成功登录依赖方法
        self.page_in.page_get_PageLpLogin().page_mp_login_success()
        # 4. 获取PageMpArticle页面对象
        self.applydata = self.page_in.page_get_PageApplyData()

    # 2. 结束
    def teardown_class(self):
        GetDriver.quit_web_driver()

    # 3. 测试发布文章方法
    @pytest.mark.parametrize("expect", read_yaml("apply_data.yaml"))
    def test_apply_data(self, expect):

        # 调用发布文章业务方法
        self.applydata.page_apply_data()
        try:
            # 断言
            assert expect == self.applydata.page_get_autonym_dialog()
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.applydata.base_get_img()
            # 抛异常
            raise
