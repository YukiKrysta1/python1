# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
browser.get('http://www.taobao.com')

input = browser.find_element_by_class_name('h')
input.click()
input = browser.find_element_by_id('J_Quick2Static')
input.click()
input = browser.find_element_by_id('TPL_username_1')
input.send_keys('杨科80741104')
input = browser.find_element_by_id('TPL_password_1')
input.send_keys('sxwoxifuer.....')
tuo1 = browser.find_element_by_id('nc_1_n1z')
tuo2 = browser.find_element_by_class_name('nc-lang-cnt')
act = ActionChains(browser)
act.drag_and_drop_by_offset(tuo1, 298, 38)
act.perform()
input =browser.find_element_by_id('J_SubmitStatic')
input.click()
# input = browser.find_element_by_id('q')
# input.send_keys('小米6')
# button = browser.find_element_by_class_name('btn-search.tb-bg')
# button.click()
