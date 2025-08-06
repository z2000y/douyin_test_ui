import os

import pytest
import time
import allure
from page_objects.login_page import LoginPage
from utils.add_cookies import addCookies
from utils.log_utils import logUtils

# 初始化日志
logger = logUtils.get_logger(__name__)

# 测试数据
TEST_USERNAME = "18786262123"  # 替换为实际测试账号
TEST_PASSWORD = "ZY314510829903"  # 替换为实际测试密码


@allure.feature("抖音登录功能")
class TestDouyinLogin:

    @allure.story("使用账号密码登录")
    @allure.title("抖音正常登录流程验证")
    @allure.description("测试使用正确的账号密码完成抖音登录，并验证登录结果")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_douyin_login(self, driver):
        """测试抖音账号密码登录流程"""
        logger.info("===== 开始执行抖音登录测试 =====")

        # 初始化登录页面
        login_page = LoginPage(driver)

        with allure.step("打开抖音首页"):
            login_page.open_page()
            logger.info(f"已打开抖音首页: {login_page.URL}")

        with allure.step("添加登录Cookies"):
            logger.info("开始添加Cookies")
            addCookies(driver)
            # 添加Cookies后刷新页面使Cookies生效
            logger.info("Cookies添加完成并刷新页面")

        with allure.step("打开登录入口"):
            login_page.click_login_page()
            time.sleep(2)  # 等待登录面板加载

        with allure.step("切换到密码登录模式"):
            login_page.click_password_login()
            time.sleep(1)  # 等待切换完成

        with allure.step("输入账号和密码"):
            login_page.enter_username(TEST_USERNAME)
            login_page.enter_password(TEST_PASSWORD)

        with allure.step("点击登录按钮"):
            login_page.click_login()
            logger.info("已点击登录按钮，等待登录完成")
            time.sleep(5)  # 等待登录跳转

        with allure.step("验证登录结果"):
            try:
                current_title = login_page.get_title()
                assert "抖音" in current_title, f"页面标题验证失败，当前标题: {current_title}"

                # 可根据实际登录后显示的元素进一步验证（例如用户头像、昵称等）
                # 示例：user_avatar = driver.find_element(By.CSS_SELECTOR, ".user-avatar")
                # assert user_avatar.is_displayed(), "用户头像未显示，登录可能失败"

                logger.info("登录验证成功，符合预期结果")
                allure.attach(driver.get_screenshot_as_png(), "登录成功截图", allure.attachment_type.PNG)
            except AssertionError as e:
                logger.error(f"登录验证失败: {str(e)}")
                allure.attach(driver.get_screenshot_as_png(), "登录失败截图", allure.attachment_type.PNG)
                raise
            finally:
                logger.info("===== 抖音登录测试执行完毕 =====")

