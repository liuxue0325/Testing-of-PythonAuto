##使用tag-name进行定位
# # -*- coding: utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# # 引入系统os模块，方便操作文件
# import os
# import time
#
# driver = webdriver.Chrome()
# file_path = 'file://' + os.path.abspath('textinput.html')
# driver.get(file_path)
#
# # 选择页面上所有的input tag对象
# input_objs = driver.find_elements(By.TAG_NAME, 'input')
# add_texts = ['auto', 'test', 'python']
# # 从中筛选出type为text的元素并分别赋值
# index = 0
# for input in input_objs:
#     if input.get_attribute('type') == 'text':
#         input.send_keys(add_texts[index])
#         index += 1
#         time.sleep(3)
#
# time.sleep(10)
# driver.quit()

# 使用CSS-selector进行定位
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
driver = webdriver.Chrome()
file_path = 'file://' + os.path.abspath('textinput.html')
driver.get(file_path)

# 直接选择所有type为text的元素并给文本框赋值
text_inputs =  driver.find_elements(By.CSS_SELECTOR,'input[type=text]')

add_texts = ['auto', 'test', 'python']
# 从中筛选出type为text的元素并分别赋值
index = 0
for input in text_inputs:
    input.send_keys(add_texts[index])
    index += 1

time.sleep(3)
driver.quit()