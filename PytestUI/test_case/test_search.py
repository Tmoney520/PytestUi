# -*- coding: utf-8 -*- 
"""          
# @Time   : 2023/2/25 19:32
# @Author :TGW
"""
import allure
import pytest
from VAR.URL import homepage
from base_key.keyword import Keys
from utils.read_yaml import yaml_data

@allure.title('分数线查询流程')
@pytest.mark.parametrize("data",yaml_data("../test_data/search.yaml"))
def test_search(browser,data):
    with allure.step('启动Chrome浏览器'):
        driver = Keys(browser)
    with allure.step('访问学校页面'):
        driver.get_url(homepage)
    with allure.step('鼠标悬停到招生就业'):
        driver.move_to(**data['move_to'])
    with allure.step('点击招生'):
        driver.click(**data['click'])
    with allure.step('切换句柄'):
        driver.swith_handle()
    with allure.step('鼠标悬停到招生就业'):
        driver.move_to(**data['move_to1'])
    with allure.step('点击历年录取'):
        driver.click(**data['click1'])
    with allure.step('点击16年分数线'):
        driver.click(**data['click2'])
    with allure.step('切换句柄'):
        driver.swith_handle()
    with allure.step('断言其他类分数线'):
        assert '438' in driver.get_text('xpath','//*[@id="maincontent"]/div[3]/div[2]/div[1]/dl/dd/div[3]/div/table/tbody/tr[8]/td[3]')
