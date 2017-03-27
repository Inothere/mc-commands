# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import json

def get_html():
    r = requests.get('http://www.zyyapp.com/mcid.html')
    if r.status_code == 200:
        return r.content
    return ''

def parse_html(content):
    if not content:
        return [], []
    items = []
    err_items = []
    soup = BeautifulSoup(content)
    tbody = soup.tbody
    for tr in tbody:
        try:
            item = {'zh_name': '', 'id': ''}
            item['zh_name'] = tr.find(class_='name').text.encode('utf-8')
            item['id'] = tr.find(class_='id').text
            items.append(item)
        except Exception as ex:
            err_items.append(tr)
    return items, err_items

def items():
    content = get_html()
    items, err_items = parse_html(content)
    return items

if __name__ == '__main__':
    items = items()
    with open('items.txt', 'w') as out:
        json.dump(items, out, ensure_ascii=False)