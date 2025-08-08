from selenium.webdriver.common.by import By
from .base_page import BasePage
from utils.log_utils import logUtils


class HomePage(BasePage):
    # 初始化日志
    logger = logUtils.get_logger(__name__)

    # 页面URL
    URL = "https://www.douyin.com/"

    # 页面元素定位器
    SEARCH_BOX = (By.XPATH, '//*[@id="douyin-header"]/div[1]/header/div/div/div[1]/div/div[2]/div/div[1]/input')  # 搜索框
    RECOMMEND_TAB = (By.XPATH, '//*[@id="douyin-navigation"]/div/div[2]/div/div[1]/div/div/div[2]/div/div/a/div[2]/span')  # 推荐标签
    FOLLOW_TAB = (By.XPATH, '//*[@id="douyin-navigation"]/div/div[2]/div/div[1]/div/div/div[5]/div/div/a/div[2]/span')  # 关注标签
    VIDEO_CONTAINER = (By.CSS_SELECTOR, "#sliderVideo > div.E7R0E__S.playerContainer.hide-animation-if-not-suport-gpu.TkocvtkE > div > div.vqN35AZ4.basePlayerContainer.xg5nzy2Q.chapterPlayerStyle.MediaNotSupportStyle.lowPopup > div.vK1R_RFC > div > xg-video-container > video")  # 视频容器
    SEARCH_SUBMIT = (By.CSS_SELECTOR, '//*[@id="douyin-header"]/div[1]/header/div/div/div[1]/div/div[2]/div/button/span')  # 搜索提交按钮

    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        """打开抖音首页"""
        self.logger.info(f"打开抖音首页: {self.URL}")
        self.open(self.URL)

    def is_search_box_displayed(self):
        """判断搜索框是否显示"""
        return self.find_element(self.SEARCH_BOX).is_displayed()

    def is_recommend_tab_displayed(self):
        """判断推荐标签是否显示"""
        return self.find_element(self.RECOMMEND_TAB).is_displayed()

    def is_follow_tab_displayed(self):
        """判断关注标签是否显示"""
        return self.find_element(self.FOLLOW_TAB).is_displayed()

    def is_video_loaded(self):
        """判断视频是否加载"""
        return self.find_element(self.VIDEO_CONTAINER).is_displayed()

    def click_search_box(self):
        """点击搜索框"""
        self.logger.info("点击搜索框")
        self.click(self.SEARCH_BOX)

    def enter_search_keyword(self, keyword):
        """输入搜索关键词"""
        self.logger.info(f"输入搜索关键词: {keyword}")
        self.send_keys(self.SEARCH_BOX, keyword)

    def submit_search(self):
        """提交搜索"""
        self.logger.info("提交搜索")
        self.click(self.SEARCH_SUBMIT)