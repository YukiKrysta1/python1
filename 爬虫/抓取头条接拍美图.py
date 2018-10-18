# -*- coding: utf-8 -*-
import json
import os
from hashlib import md5
import pymongo
import re
from urllib.parse import urlencode
from conFig import *
from multiprocessing import Pool
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import requests

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]



def get_page_index(offset, keywrod):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keywrod,
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1,
        'from': 'search_tab'
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    global headers
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    try:
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException as e:
        return print(e)

def parse_one_page(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
       for i in data.get('data'):
           yield i.get('article_url', 'nofind')

def get_page_detail(url):
    try:
        if url !='nofind':
            response = requests.get(url, headers = headers)
            if response.status_code == 200:
                return response.text
            return None
    except RequestException as e:
        return print(e)


def parse_page_detail(html, url):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select('title')[0].get_text()

    imamg_pattern = re.compile('gallery: JSON.parse\("(.*?)"\),', re.S)
    result = re.search(imamg_pattern, html)

    if result is not None:
        # print(result.group(1))
        newResule = result.group(1).replace(r'\\', '#')
        newResule = newResule.replace('\\', '')
        newResule = newResule.replace('#', r'\\')
        newResule = newResule.replace(r'\/', '/')
        data = json.loads(newResule)
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            for image in images: download_image(image)
            return {
                'title': title,
                'url': url,
                'images': images
            }

def save_to_mongo(resule):
    if db[MONGO_TABLE].insert(resule):
        print('存储到MongoDB成功', resule)
        return True
    return False

def download_image(url):
    try:
        if url != 'nofind':
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                save_image(response.content)
            return None
    except RequestException as e:
        return print(e)

def save_image(content):
    file_path = '{0}/{1}.{2}'.format(r'C:\Users\Administrator\Desktop\yk', md5(content).hexdigest(), 'jpg')
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)


def main(offset):
    html = get_page_index(offset, KEYWORD)
    for url in parse_one_page(html):
        html = get_page_detail(url)
        if html:
            if parse_page_detail(html, url) is not None:
                result = parse_page_detail(html, url)
                save_to_mongo(result)


if __name__ == '__main__':

    groups = [x * 20 for x in range(GROUP_START, GROUP_END + 1)]
    pool = Pool()
    pool.map(main, groups)








