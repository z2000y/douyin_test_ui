from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open(self, url):
        """打开指定URL"""
        self.driver.get(url)
    
    def find_element(self, locator):
        """查找单个元素"""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click(self, locator):
        """点击元素"""
        self.wait.until(EC.element_to_be_clickable(locator)).click()
    
    def send_keys(self, locator, text):
        """向输入框发送文本"""
        self.find_element(locator).clear()
        self.find_element(locator).send_keys(text)
    
    def get_url(self):
        """获取页面网址"""
        return self.driver.url
    def get_title(self):
        """获取页面标题"""
        return self.driver.title
