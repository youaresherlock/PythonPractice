#!usr/bin/python
# -*- coding:utf8 -*-
from selenium import webdriver
import time
c = webdriver.Chrome('./chromedriver')

url = 'http://www.baidu.com'

c.get(url)

c.find_element_by_partial_link_text('hao').click()
time.sleep(3)
c.back()
time.sleep(3)
c.forward()



time.sleep(3)
c.quit()















