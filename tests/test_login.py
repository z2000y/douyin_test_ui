import pytest
import time
from page_objects.login_page import LoginPage
from utils.add_cookies import addCookies
from utils.log_utils import logUtils

# 初始化日志
logger = logUtils.get_logger(__name__)

# 测试数据
TEST_USERNAME = "18786262123"  # 替换为实际测试账号
TEST_PASSWORD = "ZY314510829903"  # 替换为实际测试密码


def test_douyin_login(driver):
    """测试抖音登录流程"""
    logger.info("开始执行抖音登录测试")

    # 初始化登录页面
    login_page = LoginPage(driver)

    # 打开抖音页面
    login_page.open_page()

    # 添加cookies
    logger.info("开始添加cookies")
    addCookies(driver)
    logger.info("cookies添加完成")

    # 打开抖音登录界面
    login_page.click_login_page()

    # 点击密码登录
    login_page.click_password_login()

    # 输入账号和密码
    login_page.enter_username(TEST_USERNAME)
    login_page.enter_password(TEST_PASSWORD)

    # 点击登录按钮
    login_page.click_login()

    # 等待登录完成
    time.sleep(5)
    logger.info("登录操作完成，等待页面加载")

    # 登录验证
    # try:
    #     # 可以根据实际登录后显示的元素进行验证
    #     current_title = login_page.get_title()
    #     assert "抖音" in current_title
    #     logger.info("登录验证成功")
    # except AssertionError:
    #     logger.error("登录验证失败，页面标题不符合预期")
    #     raise
    # finally:
    #     logger.info("抖音登录测试执行完毕")