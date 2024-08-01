from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


class Tool():
    def __init__(self, driver):
        self.driver = driver

    # 查找指定定位的元素
    def find(self, locator):
        # lambda方式匹配元组
        element = WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element(*locator))
        return element

    # 填充文本到指定的文本元素
    def fill(self, locator, text):
        self.find(locator).send_keys(text)

    # 检查该元素是否存在
    def element_exists(self, locator):
        ones = self.find(locator)
        # 如果存在则返回True
        if len(ones) >= 1:
            return True
        else:
            return False

    # 触发单击事件
    def click(self, locator):
        # 定位元素被点击
        self.find(locator).click()
