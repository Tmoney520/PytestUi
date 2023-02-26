# -*- coding: utf-8 -*- 
"""          
# @Time   : 2023/2/24 22:20
#  :TGW
"""
from time import sleep
from selenium.webdriver import ActionChains


class Keys:

    #初始话浏览器
    def __init__(self,driver):
        self.driver = driver

    # 获取地址
    def get_url(self, url):
        self.driver.get(url)

    # 获取元素
    def locate(self, by, value):
        return self.driver.find_element(by, value)

    # 输入内容
    def send_keys(self, by, value, text):
        self.locate(by, value).send_keys(text)

    # 点击
    def click(self, by, value):
        self.locate(by, value).click()

    # 退出
    def quite(self):
        self.driver.quit()

    #等待
    def sleep_(self,text):
        sleep(text)

    # 获取文本
    def get_text(self, by, value):
        return self.locate(by, value).text

    #获取页面标题
    def get_title(self):
        return self.driver.title

    # 断言
    def assert_text(self, by, value):
        return  self.locate(by, value).text

    # 句柄的切换（考虑不同场景的不同切换）
    def swith_handle(self,text=1,close=True,):
        handles = self.driver.window_handles
        if close:
            self.driver.close()
        self.driver.switch_to.window(handles[text])

    #鼠标悬停
    def move_to(self,by,value):
        ActionChains(self.driver).move_to_element(self.locate(by,value)).perform()