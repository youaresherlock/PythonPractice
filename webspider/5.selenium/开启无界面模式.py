#!usr/bin/python
# -*- coding:utf8 -*-
import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)
driver.get("http://www.baidu.com/")

print(driver.title)
time.sleep(1)

driver.quit()












