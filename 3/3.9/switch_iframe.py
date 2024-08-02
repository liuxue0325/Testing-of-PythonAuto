# -*- coding: utf-8 -*-

from selenium import webdriver
from  selenium.webdriver.common.by import By

import time

import os

driver = webdriver.Edge()

file_path = 'file:///' + os.path.abspath('iframe.html')
driver.get(file_path)

driver.implicitly_wait(30)

# 先找到最外层的iframe(if1)
driver.switch_to.frame("if1")

# 再找到内层的iframe(id=if2)
driver.switch_to.frame("if2")

# 操作元素
driver.find_element(By.ID,"query").send_keys("Python")
driver.find_element(By.ID,"stb").click()

time.sleep(3)
driver.quit()