# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from snownlp import SnowNLP
from myspiders.items import MyspidersItem


class SmzdmSpider(scrapy.Spider):
    name = 'smzdm'
    allowed_domains = ['smzdm.com']
    start_urls = ['https://www.smzdm.com/fenlei/zhinengshouji/']

    # 解析函数
    def parse(self, response):
        urLList = response.xpath('//ul[@id="feed-main-list"]/li[position()<=5]//h5/a/@href').extract()
        for urL in urLList:
            yield scrapy.Request(url=urL, callback=self.checkpage, meta={'url': urL})



    def checkpage(self, response):
        pageList = response.xpath(
            '//*[@id="comment"]/div[1]/ul[@class="pagination"]/li[position()<last()-2]/a/@href').extract()
        if len(pageList) != 0:
            for page in pageList:
                yield scrapy.Request(url=page, callback=self.getinfor)
        else:
            # dont_filter跳过判断是否重复请求
            yield scrapy.Request(url=response.meta['url'], callback=self.getinfor, dont_filter=True)

    def getinfor(self,response):
        # comment_time = pinglun.xpath('.//div[@class="time"]/meta/@content').extract()[0]
        comments = Selector(response=response).xpath('//div[@class="comment_con"]')
        for comment in comments:
            # item = response.meta['item']
            item=MyspidersItem()
            comment_contents = comment.xpath('./p/span/text()')
            comment_time = comment.xpath('.//div[@class="time"]/meta/@content').extract()[0]
            username = comment.xpath('.//a[@class="a_underline user_name"]/span/text()').extract()[0]
            comment_content=comment_contents.extract_first().strip()

            s = SnowNLP(comment_content)
            sentiments=s.sentiments
            item['sentiments']=sentiments
            item['comments']=comment_content
            item['username']=username
            item['comment_time']=comment_time
            yield item