#!usr/bin/python
# -*- coding:utf8 -*-
import time
from selenium import webdriver


driver = webdriver.Chrome('./chromedriver.exe')

driver.get('https://www.baidu.com')

# # 在文本框中输入内容 定位到文本框
# driver.find_element_by_id('kw').send_keys('一拳超人')
#
# # 获取百度一下的按钮,点击
# driver.find_element_by_id('su').click()

# 获取当前页面中所有的a标签
a_list = driver.find_elements_by_xpath('//a')
for a in a_list:
    # 获取标签中的文本内容
    print(a.text)
    # 获取标签中的属性值
    print(a.get_attribute('href'))

time.sleep(5)


driver.quit()










