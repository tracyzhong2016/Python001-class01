import requests
from bs4 import BeautifulSoup as bs
import lxml.etree

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'

header = {'User-Agent':user_agent}
myurl='https://maoyan.com/films?showType=3'

response = requests.get(myurl,headers=header)

bs_info = bs(response.text, 'html.parser')
base_link='https://maoyan.com'
mylist=[]

# Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
for tags in bs_info.find_all('div', attrs={'class': 'channel-detail movie-item-title'}):
    for atag in tags.find_all('a'):
       extr_link=(atag.get('href'))
       url=base_link+extr_link
       res = requests.get(url, headers=header)
       selector = lxml.etree.HTML(res.text)

       film_name = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()')
       film_class = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a[1]/text()')
       plan_date = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')
       info=[film_name, film_class, plan_date]

       mylist.append(info)

import pandas as pd

movie1 = pd.DataFrame(data = mylist)

# windows需要使用gbk字符集
movie1.to_csv('./movie.csv', encoding='utf8', index=False, header=False)


