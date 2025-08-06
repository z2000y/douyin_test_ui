from selenium import webdriver
import json
import time

# 填写webdriver的保存目录
driver = webdriver.Edge()

# 记得写完整的url 包括http和https
driver.get('https://www.douyin.com')

def addCookies():
    # 首先清除由于浏览器打开已有的cookies
    driver.delete_all_cookies()

    with open('cookies.txt', 'r') as f:
        # 使用json读取cookies 注意读取的是文件 所以用load而不是loads
        cookies_list = json.load(f)

        # 方法1 将expiry类型变为int
        for cookie in cookies_list:
            # 并不是所有cookie都含有expiry 所以要用dict的get方法来获取
            if isinstance(cookie.get('expiry'), float):
                cookie['expiry'] = int(cookie['expiry'])
            driver.add_cookie(cookie)
