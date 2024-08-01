from selenium_tools import Tool
import time
from selenium import webdriver


# 测试自动化登录百度网盘
def testLogin():
    # 生成edge驱动
    driver = webdriver.Edge()
    # 生成工具类
    client = Tool(driver)
    # 访问网盘官网
    client.driver.get("https://pan.baidu.com")
    # 点击显示登录窗口
    go_login_Btn = ("class", "bd-login-button bd-login-content__login")
    # 单击“去登陆”按钮
    client.click(go_login_Btn)
    # 声明登录框显示对象
    show_login_form = ("id", "TANGRAM__PSP_11__changePwdCodeItem")
    # 单击显示账号登录方式，显示登录输入框
    client.click(show_login_form)
    # 休眠0.5s
    time.sleep(0.5)
    # element = client.find("name","wd")
    # 账号
    account = ("id", "TANGRAM__PSP_11__userName")
    # 密码
    password = ("id", "TANGRAM__PSP_11__password")
    # 设置账号
    client.fill(account, "CSD1216")
    # 休眠2.5s，让操作更真实
    time.sleep(2.5)
    # 填充密码
    client.fill(password, "CSD@1216")
    # 休眠3s，让操作更真实
    time.sleep(3)
    click_obj = ("id", "TANGRAM__PSP_11__submit")
    # 单击登录按钮
    client.click(click_obj)
    # 休眠10s
    time.sleep(10)


if __name__ == '__main__':
    testLogin()
