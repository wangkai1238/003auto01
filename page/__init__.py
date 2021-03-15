""" 以下放页面的元素配置信息 页面数据 """
from selenium.webdriver.common.by import By

"""以下数据为登陆、leadpage、servepage页面对象的url"""

# 前端页面url
url_lp = "https://passport.juhe.cn/cas/login?service=https%3A%2F%2Fwww.juhe.cn%2Flogin%2Fcas%2Fauth%2Fucenter%3FsourceChannel%3DjHwww-juhe-cn&from=pc"
# 后台管理url
url_sp = "http://"

"""登陆页面元素配置信息"""
# 用户名
lp_username = (By.CSS_SELECTOR, "#username")
# 密码
lp_password = (By.CSS_SELECTOR, "#password-o")
# 登陆按钮
lp_login_btn = (By.CSS_SELECTOR, "#loginBtn")
# 用户昵称
lp_nickname = (By.CSS_SELECTOR, '.header-status>a[href="https://dashboard.juhe.cn/home"]')

# 导航栏-API
nav = (By.XPATH,"/html/body/header/div/div[2]/div[2]")
# 导航栏-应用开发
nav_application = (By.CSS_SELECTOR,'[href="/docs/index/cid/6"]')
# 导航栏-应用开发-使用 按钮
nav_application_use_btn = (By.CSS_SELECTOR,'a[did="58"]')
# 已经阅读复选框 按钮
readed_check_box = (By.CSS_SELECTOR,'.el-checkbox__input')
# 立即申请 按钮
immediately_apply_btn = (By.CSS_SELECTOR,'.save-button')
# 提示实名 文本
autonym_dialog_text = (By.CSS_SELECTOR,'.dialog-body>p')
# 提示实名 按钮
autonym_dialog_btn = (By.CSS_SELECTOR,'.dialog-footer button')


