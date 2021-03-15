# 创建page目录 封装登陆页面类 整理登录顺序方法
import allure
from base.base import Base
import page
from time import sleep
from tools.get_log import GetLog
log = GetLog.get_logger()


class PageLpLogin(Base):

    @allure.step("第一步:输入用户名")
    def page_input_username(self, username):
        self.base_input(page.lp_username, username)

    @allure.step("第二步：输入密码")
    def page_input_password(self, password):
        self.base_input(page.lp_password, password)

    @allure.step("第三步：点击登陆按钮")
    def page_click_login_btn(self):
        self.base_click(page.lp_login_btn)
        sleep(1)

    @allure.step("第四步：获取用户登录昵称")
    # 获取用户昵称字段 业务层断言使用
    def page_get_nickname(self):
        return self.base_get_text(page.lp_nickname)

    @allure.step("第五步：组合操作方法")
    # 登陆页面操作组合方法 业务层调用

    def page_lp_login(self, username, password):
        log.info("正在调用前台页面登录业务方法，用户名：{} 密码：{}".format(username, password))
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_btn()

    @allure.title("登陆成功测试")
    @allure.story("账户为admin,密码root")
    @allure.description("申请应用数据前的登陆成功测试")
    # 组合业务方法 ->发布文章依赖使用
    def page_mp_login_success(self, username="15628866863", password="8866863"):
        log.info("正在调用自媒体登录业务方法，用户名：{} 密码：{}".format(username, password))
        """提示：调用相同页面操作步骤，跨页面暂时不考虑"""
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_btn()

if __name__ == "__main__":
    print(PageLpLogin)
