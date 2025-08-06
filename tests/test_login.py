import pytest
from page_objects.login_page import LoginPage
from utils.add_cookies import addCookies

# 测试数据
TEST_USERNAME = "18786262123"  # 替换为实际测试账号
TEST_PASSWORD = "ZY314510829903"  # 替换为实际测试密码




def test_douyin_login(driver):
    """测试抖音登录流程"""
    # 初始化登录页面
    login_page = LoginPage(driver)
    
    # 打开抖音页面
    login_page.open_page()
    
    # 添加cookies
    addCookies()

    #打开抖音登录界面
    login_page.click_login_page()

    # 点击密码登录
    login_page.click_password_login()
    
    # 输入账号和密码
    login_page.enter_username(TEST_USERNAME)
    login_page.enter_password(TEST_PASSWORD)
    
    # 点击登录按钮
    login_page.click_login()
    
    # 这里可以添加登录成功的验证逻辑
    # 例如验证页面跳转、用户名显示等
    # 示例：验证页面标题是否包含预期内容
    # assert "抖音" in login_page.get_title()
    
    # 为了演示，这里添加一个短暂的等待，实际测试中可以去掉
    import time
    time.sleep(5)
