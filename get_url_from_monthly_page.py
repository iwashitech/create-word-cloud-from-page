# -*- coding: utf-8 -*-
"""
"""

import time
import requests
import bs4
import os
import re

user_name = os.environ['USERPROFILE'].replace('\\', '/')
page_list = []

END_MONTH = 12
list_month = []
for y in [2022]:
    for m in range(1, END_MONTH + 1):
        list_month.append(str(y) + str(m).rjust(2, '0'))

for month in list_month:
    time.sleep(3)
    url = 'https://www.example.jp/?month=' + month
    get_url_info = requests.get(url)
    #文字化け対策
    get_url_info.encoding = get_url_info.apparent_encoding
    soup = bs4.BeautifulSoup(get_url_info.text, 'lxml')
    pagination_next = soup.select('.pagination_next')[0].find_previous_sibling('a')
    num_end_page = re.search(r'href=".+page=(.+?)"', str(pagination_next)).group(1)
    
    for page in range(1, int(num_end_page) + 1):
        url = 'https://www.example.jp/?month=' + month + '&page=' + str(page)
        get_url_info = requests.get(url)
        #文字化け対策
        get_url_info.encoding = get_url_info.apparent_encoding
        soup = bs4.BeautifulSoup(get_url_info.text, 'lxml')
        
        tag_list = soup.select('.title')
        for tag in tag_list:
            page_list.append(tag.get('href'))

with open(user_name + '/Desktop/url_list.txt', mode='w') as f:
    f.write('\n'.join(page_list))