# -*- coding: utf-8 -*-
import json
import requests
from requests.exceptions import RequestException
import re
from multiprocessing import Pool

def get_one_page(url, headers):
    try:
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
     pattern = re.compile('<dd>.*? <i class="board-index.*?">(.*?)</i>.*?'
                          '<img data-src="(.*?)".*?<p class="name">.*?">(.*?)</a>'
                          '</p>.*?<p class="star">(.*?).*?</p>.*?<p class="releasetime">(.*?)</p>.*?'
                          '<i class="integer">(.*?)</i><i class="fraction">(.*?)</i></p>', re.S)
     items = re.findall(pattern, html)
     for item in items:
         yield {
             '排名：': item[0],
             '图片：': item[1],
             '电影名：': item[2],
             '上映时间：': item[4][5:],
             '评分：': item[5]+item[6]
         }
     # print(items)

def write_to_file(content):
    with open(r'C:\Users\Administrator\Desktop\新建文件夹\top榜.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')



def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                             ' Chrome/69.0.3497.100 Safari/537.36'}
    html = get_one_page(url,  headers)
    # print(html)
    for item in parse_one_page(html):
        write_to_file(item)
        print(item)

if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i*10 for i in range(10)])

