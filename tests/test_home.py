import time
import allure
import pytest
from page_objects.home_page import HomePage
from utils.log_utils import logUtils
from utils.add_cookies import addCookies

# 初始化日志
logger = logUtils.get_logger(__name__)


@allure.feature("抖音首页功能")
class TestDouyinHomePage:

    @allure.story("首页元素验证")
    @allure.title("验证抖音首页关键元素是否正常显示")
    @allure.description("测试抖音首页加载后，关键功能元素是否正常显示")
    @allure.severity(allure.severity_level.NORMAL)
    def test_home_page_elements(self, driver):
        """验证抖音首页关键元素是否正常显示"""
        logger.info("===== 开始执行抖音首页元素验证测试 =====")

        # 初始化首页对象
        home_page = HomePage(driver)

        with allure.step("打开抖音首页"):
            home_page.open_page()
            logger.info(f"已打开抖音首页: {home_page.URL}")
            time.sleep(3)  # 等待页面加载
        with allure.step("添加登录Cookies"):
            logger.info("开始添加Cookies")
            addCookies(driver)
            driver.refresh()
            logger.info("Cookies添加完成,并刷新了页面")
        with allure.step("验证首页标题"):
            title = home_page.get_title()
            if "验证码" in title:
                time.sleep(10)
            assert "抖音" in title, f"首页标题验证失败，当前标题: {title}"
            logger.info(f"首页标题验证成功: {title}")

        with allure.step("验证搜索框是否显示"):
            assert home_page.is_search_box_displayed(), "搜索框未显示"
            logger.info("搜索框显示正常")

        with allure.step("验证推荐标签是否显示"):
            assert home_page.is_recommend_tab_displayed(), "推荐标签未显示"
            logger.info("推荐标签显示正常")

        with allure.step("验证关注标签是否显示"):
            assert home_page.is_follow_tab_displayed(), "关注标签未显示"
            logger.info("关注标签显示正常")

        with allure.step("验证首页视频是否加载"):
            assert home_page.is_video_loaded(), "首页视频未加载"
            logger.info("首页视频加载正常")

        with allure.step("截取首页截图"):
            allure.attach(driver.get_screenshot_as_png(), "抖音首页截图", allure.attachment_type.PNG)

        logger.info("===== 抖音首页元素验证测试执行完毕 =====")

    @allure.story("首页搜索功能")
    @allure.title("测试抖音首页搜索功能")
    @allure.description("测试在抖音首页使用搜索框进行搜索的功能")
    @allure.severity(allure.severity_level.NORMAL)
    def test_home_page_search(self, driver):
        """测试抖音首页搜索功能"""
        logger.info("===== 开始执行抖音首页搜索功能测试 =====")

        # 初始化首页对象
        home_page = HomePage(driver)

        with allure.step("打开抖音首页"):
            home_page.open_page()
            time.sleep(3)  # 等待页面加载
        with allure.step("添加登录Cookies"):
            logger.info("开始添加Cookies")
            addCookies(driver)
            driver.refresh()
            logger.info("Cookies添加完成，并刷新了页面")
        with allure.step("验证首页标题"):
            title = home_page.get_title()
            if "验证码" in title:
                time.sleep(10)
            assert "抖音" in title, f"首页标题验证失败，当前标题: {title}"
            logger.info(f"首页标题验证成功: {title}")
        # with allure.step("点击搜索框"):
        #     home_page.click_search_box()
        #     time.sleep(1)

        with allure.step("输入搜索关键词"):
            search_keyword = "热门音乐"
            home_page.enter_search_keyword(search_keyword)
            logger.info(f"已输入搜索关键词: {search_keyword}")

        with allure.step("提交搜索"):
            home_page.submit_search()
            time.sleep(3)  # 等待搜索结果加载

        with allure.step("验证搜索结果"):
            assert search_keyword in home_page.get_url(), f"搜索结果页面验证失败，当前标题: {home_page.get_url()}"
            logger.info("搜索功能验证成功")

        with allure.step("截取搜索结果截图"):
            allure.attach(driver.get_screenshot_as_png(), "搜索结果截图", allure.attachment_type.PNG)

        logger.info("===== 抖音首页搜索功能测试执行完毕 =====")