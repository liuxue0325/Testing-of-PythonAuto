import time
from splinter import Browser


def login_mail(url):
    browser = Browser('edge')
    # 登录163邮箱
    browser.visit(url)
    # 设置账号和密码
    browser.find_by_id('account-box').fill('xxxx@163.com')
    browser.find_by_id('auto-id-1722334959338').fill('密码')
    # 模拟单击登录按钮
    browser.find_by_id('dologin').click()
    time.sleep(10)
    # close the window of browser
    browser.quit()


if __name__ == '__main__':
    mail_addr = 'https://mail.163.com/'
    login_mail(mail_addr)
