# -*- coding: utf-8 -*-
"""
"""

import requests
import bs4
import os
import pandas as pd
import re

user_name = os.environ['USERPROFILE'].replace('\\', '/')

with open(user_name + '/Desktop/url_list.txt') as f:
    url_list = f.readlines()

add_row = []

for url in url_list:
    url = url.strip()
    get_url_info = requests.get(url)
    #文字化け対策
    get_url_info.encoding = get_url_info.apparent_encoding
    soup = bs4.BeautifulSoup(get_url_info.content, 'lxml')
    [s.extract() for s in soup('style')]
    if(soup.find('section', {'class':'unnecessary'})!=None):
        soup.find('section', {'class':'unnecessary'}).decompose()
    tag_list = soup.select('.block p')
    tag_list2 = soup.select('.block div')
    tag_list3 = soup.select('.block section')
    text = ''
    for tag in tag_list:
        try:
            text += tag.text
        except:
            text += ''
    for tag in tag_list2:
        try:
            text += tag.text
        except:
            text += ''
    for tag in tag_list3:
        try:
            text += tag.text
        except:
            text += ''
    text_list = text.splitlines()
    sentence = ''
    for text in text_list:
        if text != '':
            sentence += text
    
    page = []
    page.append(url.replace('https://www.example.jp/?page=', ''))
    page.append(sentence)
    add_row.append(page)

df = pd.DataFrame(add_row, columns=['id','text'])
df.to_excel(user_name + '/Desktop/page_text.xlsx', index=None)
page_text = ''
for text in df['text']:
    page_text = page_text + text

with open(user_name + '/Desktop/page_text.txt', encoding='utf-8' ,mode='w') as f:
    f.write(page_text)