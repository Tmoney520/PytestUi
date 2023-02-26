# -*- coding: utf-8 -*- 
"""          
# @Time   : 2023/2/25 19:50
# @Author :TGW
"""
import allure
from VAR.URL import homepage
from base_key.keyword import Keys

@allure.title('教学日历核对流程')
def test_search(browser):
    driver = Keys(browser)
    driver.get_url(homepage)
    driver.move_to('link text', '教学科研')
    driver.click('link text', '教学')
    driver.click('link text', '教学日历')
    driver.swith_handle()
    assert '2022-2023学年校历' == driver.get_title()
