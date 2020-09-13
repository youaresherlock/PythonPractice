#!usr/bin/python
# -*- coding:utf8 -*-
import time
import requests
from selenium import webdriver


driver = webdriver.Chrome('./chromedriver.exe')

url = 'https://github.com/login'
driver.get(url)
time.sleep(3)

driver.find_element_by_id("//input[@id='login_field']").send_keys('clarence')
driver.find_element_by_id("//input[@id='password']").send_keys('xxxx')

driver.find_element_by_xpath("//input[@name='commit']").click()

cookies = driver.get_cookies()

# 用requests携带cookie
# cookies_dict = {cookie['name']: cookie['value'] for cookie in driver.get_cookies()}
# requests.get(url, cookies=cookies_dict)

driver.quit()








