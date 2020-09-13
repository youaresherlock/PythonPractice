#!usr/bin/python
# -*- coding:utf8 -*-
import time
from selenium import webdriver


url = 'https://www.baidu.com'

driver = webdriver.Chrome('./chromedriver.exe')
driver.get(url)
# 打开第二个标签页
js = "window.open('http://www.itcast.cn')"
driver.execute_script(js)

# 获取到当前所有的标签页的句柄的列表
current_win = driver.window_handles

print(driver.title)
# 切换标签页
driver.switch_to.window(current_win[1])
print(driver.title)

time.sleep(10)
driver.quit()











