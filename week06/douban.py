# coding: utf-8
import lxml.etree
import requests

import pymysql
url='https://movie.douban.com/subject/33446524/comments?status=P'
header={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
response=requests.get(url,headers=header)

# print(response.text)

print(response.status_code)

selector = lxml.etree.HTML(response.text)


rate =selector.xpath('/html/body/div[3]/div[1]/div/div[1]/div[4]/div[5]/div[2]/h3/span[2]/span[2]/title')

short_comments=selector.xpath('//div[@class="comment-item"]')

connect=pymysql.connect(host='127.0.0.1',user='root',password='uiop7890',port=3306,database='hotmovie')

cur = connect.cursor()
for short in short_comments:
    a = short.xpath('./div[@class="comment"]/p/span/text()')
    sql = 'insert into hotmovie.douban_movie (short) values(\'{}\')'.format(str(a[0]))
    cur.execute(sql)

cur.close()
connect.commit()










