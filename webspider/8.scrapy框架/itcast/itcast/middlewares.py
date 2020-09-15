import random
from itcast.settings import USER_AGENTS_LIST


class UserAgentMiddleware(object):

    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENTS_LIST)
        request.headers["User-Agent"] = user_agent


class Check_UA(object):
    def process_response(self, request, response, spider):
        print(request.headers["User-Agent"])
        return response


class ProxyMiddlewares(object):

    def process_request(self, request, spider):
        # 准备好代理ＩＰ
        proxy = "https://116.196.85.150:3128"
        request.meta["proxy"] = proxy
        return None

from selenium import webdriver
import time
def get_cookies():
    # 使用selenium登录github 拿到登陆之后的cookie
    login_url = "https://github.com/login"
    username = "ZuoAndroid"
    password = "lyp82nlf@.."
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(login_url)
    time.sleep(3)
    driver.find_element_by_xpath("//input[@id='login_field']").send_keys(username)
    driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
    driver.find_element_by_xpath("//input[@class='btn btn-primary btn-block']").click()
    time.sleep(3)
    # 获取cookie
    cookis_str = driver.get_cookies()
    cookies_dict = {cookie["name"]: cookie["value"] for cookie in cookis_str}
    driver.quit()
    return cookies_dict


class SeleniumMiddlewares(object):

    def process_request(self, request, spider):
        cookie_dict = get_cookies()
        print(cookie_dict)
        request.cookies = cookie_dict