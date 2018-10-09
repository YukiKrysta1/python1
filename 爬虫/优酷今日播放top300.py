# -*- coding: utf-8 -*-
import requests
import re
from requests.exceptions import RequestException
import json
from multiprocessing import Pool

def get_one_page(url, headers):
    try:
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            return response
        return None
    except RequestException as e:
        return e

def parse_one_page(html):
    pattern = re.compile('<div class="p-thumb">.*?title="(.*?)".*?<span class="vip-free">(.*?)</span>'
                         '.*?<li class="title">.*?<a href="(.*?)".*?>.*?<li class="actor">.*?title="(.*?)"'
                         '.*?title="(.*?)".*?<li>(.*?)</li>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            '电影名：': item[0],
            'VIP:': item[1],
            '地址：': item[2],
            '主演': item[3]+item[4],
            '播放次数：': item[5]

        }

def write_to_file(content):
    with open(r'优酷top100.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

def main(p):
    url = 'https://list.youku.com/category/show/c_96_s_1_d_1_p_'+str(p)+'.html?spm=a2h1n.8251845.0.0'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    html = get_one_page(url, headers).content.decode('utf-8')
    for item in parse_one_page(html):
        write_to_file(item)
    # print(html)

if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i for i in range(1,11)])


