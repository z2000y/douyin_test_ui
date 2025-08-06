from selenium import webdriver
import time
import json
from .log_utils import logUtils

# 初始化日志
logger = logUtils.get_logger(__name__)

# 填写webdriver的保存目录
driver = webdriver.Edge()

try:
    # 记得写完整的url 包括http和https
    driver.get('https://www.douyin.com')
    logger.info("已打开抖音首页，请在60秒内完成手动登录")

    # 程序打开网页后60秒内 “手动登陆账户”
    time.sleep(60)

    # 获取并保存cookies
    cookies = driver.get_cookies()
    with open('cookies.txt','w') as f:
        f.write(json.dumps(cookies))
    logger.info(f"成功保存{len(cookies)}条cookies到文件")

except Exception as e:
    logger.error(f"获取cookies时发生错误: {str(e)}")
finally:
    driver.close()
    logger.info("浏览器已关闭")