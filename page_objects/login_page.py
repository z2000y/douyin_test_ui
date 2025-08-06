from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    # 页面URL
    URL = "https://www.douyin.com/"
    
    # 页面元素定位器
    LOGIN_PAGE=(By.CSS_SELECTOR,"#RkbQLUok > button > span > p")
    PASSWORD_LOGIN_BUTTON = (By.XPATH, '//*[@id="douyin_login_comp_flat_panel"]/div/div[2]/div/div[2]/div/div/div[1]/span[2]')  # 密码登录按钮
    USERNAME_INPUT = (By.XPATH, '//*[@id="douyin_login_comp_flat_panel"]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/input')  # 账号输入框
    PASSWORD_INPUT = (By.XPATH, '//*[@id="douyin_login_comp_flat_panel"]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/input')  # 密码输入框
    LOGIN_BUTTON = (By.XPATH, '//*[@id="douyin_login_comp_flat_panel"]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[4]/div')  # 登录按钮
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def open_page(self):
        """打开抖音网页"""
        self.open(self.URL)
    def click_login_page(self):
        """打开抖音登录界面"""
        self.click(self.LOGIN_PAGE)
    def click_password_login(self):
        """点击密码登录按钮"""
        self.click(self.PASSWORD_LOGIN_BUTTON)
    
    def enter_username(self, username):
        """输入账号"""
        self.send_keys(self.USERNAME_INPUT, username)
    
    def enter_password(self, password):
        """输入密码"""
        self.send_keys(self.PASSWORD_INPUT, password)
    
    def click_login(self):
        """点击登录按钮"""
        self.click(self.LOGIN_BUTTON)
