from selenium import webdriver
import subprocess
import pytest
import allure_pytest
import allure
from utils.log_utils import logUtils

@pytest.fixture(scope="function")
def driver():
    # 初始化浏览器
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    # 测试结束后关闭浏览器
    driver.quit()



