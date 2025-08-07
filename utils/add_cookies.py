from selenium import webdriver
import json
import time
import pytest
import os
from .log_utils import logUtils

# 初始化日志
logger = logUtils.get_logger(__name__)

def addCookies(driver):
    try:
        # 首先清除由于浏览器打开已有的cookies
        driver.delete_all_cookies()
        logger.info("已清除浏览器现有cookies")

        with open('./utils/cookies.txt', 'r') as f:
            # 使用json读取cookies
            cookies_list = json.load(f)
            logger.info(f"成功加载{len(cookies_list)}条cookies")

            # 处理并添加cookies
            for cookie in cookies_list:
                if isinstance(cookie.get('expiry'), float):
                    cookie['expiry'] = int(cookie['expiry'])
                driver.add_cookie(cookie)
            logger.info("cookies已成功添加到浏览器")
    except FileNotFoundError:
        logger.error("cookies文件不存在，请先获取cookies")
        raise
    except Exception as e:
        logger.error(f"添加cookies时发生错误: {str(e)}")
        raise

