# -*- coding: utf-8 -*-
import re
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
from taobaoconfig import *
import pymongo

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]




browser = webdriver.Chrome()
wait = WebDriverWait(browser, 20)


def search():#搜索
    try:
        browser.get('https://taobao.com')
        login = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_SiteNavLogin > div.site-nav-menu-hd > div.site-nav-sign > a.h'))
        )
        login.click()
        time.sleep(20)#由于淘宝验证码难以解决 采用手动扫描二维码暂时处理
        #等待  元素是否存在
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#q"))
        )
        #等待   按钮是否可以点击
        submit = wait.until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="J_TSearchForm"]/div[1]/button'))
        )
        #输入信息
        input.send_keys(KEYWORDS)
        #点击搜索
        submit.click()

        #页数
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.total')))
        get_products()
        return total.text
    except TimeoutException:
        return search()

def next_page(page_number):
    try:
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > input"))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit"))
        )
        input.clear()
        input.send_keys(page_number)
        submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span' ), str(page_number)))
        get_products()
    except TimeoutException:
        next_page(page_number)

def get_products():#获取商品信息
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('src'),
            'price': item.find('.price').text().replace(r'\n', ''),
            'deal': item.find('.deal-cnt').text()[:-3],
            'title': item.find('.title').text().replace(r'\n', ''),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
            }
        print(product)
        save_to_mongo(product)

def save_to_mongo(result):
    try:
        if db[MONGO_TABLE].insert(result):
            print('存储到MONGODB成功',result)
    except Exception:
        print('存储到MONGODB失败',result)

def main():
    try:
        # search()
        total = search()
        total = int(re.compile('(\d+)').search(total).group(1))#提取页数
        # print(total)
        for i in range(2,total + 1):
            next_page(i)
    except Exception:
        print('出错了')
    finally:
        browser.close()

if __name__ == '__main__':
    main()