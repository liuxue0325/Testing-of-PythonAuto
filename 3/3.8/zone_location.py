# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

import time
import os

driver = webdriver.Edge()
file_path = 'file:///' + os.path.abspath('dropList.html')
driver.get(file_path)

# 单击button下拉按钮，弹出下拉列表框
driver.find_element(By.LINK_TEXT,'Event1').click()

# 在父元素下找到链接为Event3的子元素

targets = driver.find_element(By.ID,'super1').find_element(By.LINK_TEXT,"Event3")

# 将光标移动到该子元素上
ActionChains(driver).move_to_element(menu).perform()
time.sleep(4)

driver.quit()