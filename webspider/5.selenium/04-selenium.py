#!usr/bin/python
# -*- coding:utf8 -*-
from selenium import webdriver


driver = webdriver.Chrome('./chromedriver.exe')

driver.get('https://www.baidu.com')
# driver.save_screenshot('baidu.png')

# print(driver.page_source)
print(driver.current_url)
driver.quit()
