#!/usr/bin/python3


import sys
import os
from bs4 import BeautifulSoup
import datetime
import urllib3

def download( url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    #if response.getcode() != 200:
    #    return None
    return response.data


def bs4_paraser(html):
    all_value = []
    value = {}
    soup = BeautifulSoup(html, 'html.parser')
    all_div = soup.find_all('div', attrs={'class': 'content__list--item'})
    for row in all_div:
        #print(row)
        title_div_item = row.find_all('p', attrs={'class': 'content__list--item--title twoline'})
        title_str = title_div_item[0].contents[1].contents[0].strip()
        url_str = title_div_item[0].contents[1].attrs['href'].strip()
        #print(title_str.strip())
        des_div_item = row.find_all('p', attrs={'class': 'content__list--item--des'})
        area_str = des_div_item[0].contents[6].strip() 
        des_str =  des_div_item[0].contents[8].strip() + des_div_item[0].contents[10].strip()
        #print(des_str.strip())
        price_div_item = row.find_all('span', attrs={'class': 'content__list--item-price'})
        price_str = price_div_item[0].contents[0].contents[0].strip()
        last_div_item = row.find_all('p', attrs={'class': 'content__list--item--time oneline'})
        last_str = last_div_item[0].contents[0].strip().replace("发布","")
        #print(area_str, price_str, title_str, des_str)
        all_value += last_str + "|" + area_str + "|" + price_str + "| [" + title_str + "](https://sz.lianjia.com"+url_str+") |" + des_str + '\n'
    return all_value

def cur_file_dir():
     path = sys.path[0]
     if os.path.isdir(path):
         return path + '/'
     elif os.path.isfile(path):
         return os.path.dirname(path)

if __name__ == '__main__':
    #f = open(cur_file_dir() + 'test.html', 'r')
    #html = f.read()
    #print(html)
    now = datetime.datetime.now()
    now_str= now.strftime("%Y.%m.%d")
    title_str = "时间 | 面积 | 价格 | 标题 | 描述 \n ----|----|---|---|----\n"

    f = open(cur_file_dir() +'rent_price.md', 'a+')
    #f.seek(2,0)
    f.write('\n# 祥云天都' + now_str + '\n')
    f.write(title_str)
    html = download('https://sz.lianjia.com/zufang/c2411048614076?sug=%E7%A5%A5%E4%BA%91%E5%A4%A9%E9%83%BD%E4%B8%96%E7%BA%AA%E5%A4%A7%E5%8E%A6')
    f.writelines(bs4_paraser(html))
    f.write('\n# 雍翠华府' +now_str + '\n')
    f.write(title_str)
    html = download('https://sz.lianjia.com/zufang/c2411048903207/?sug=%E9%9B%8D%E7%BF%A0%E5%8D%8E%E5%BA%9C')
    f.writelines(bs4_paraser(html))
    f.write('\n# 保利上城' + now_str+ '\n')
    f.write(title_str)
    html = download('https://sz.lianjia.com/zufang/c2411052622309/?sug=%E4%BF%9D%E5%88%A9%E4%B8%8A%E5%9F%8E')
    f.writelines(bs4_paraser(html))

    f.close()

