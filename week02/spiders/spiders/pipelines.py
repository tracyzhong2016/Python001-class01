import scrapy
from spiders.items import SpidersItem
from scrapy.selector import Selector


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3&offset=0']

    def start_requests(self):
        url = f'https://maoyan.com/films?showType=3&offset=0'
        yield scrapy.Request(url=url)

    def parse(self, response):
        base_url = 'https://maoyan.com'
        movies = Selector(response=response).xpath('//div[@class="channel-detail movie-item-title"]')
        for movie in movies:
            item = SpidersItem()
            title = movie.xpath('./a/text()')  # 电影名称
            link = movie.xpath('./a/@href')  # 链接
            item['film_name'] = title.extract_first().strip()
            item['link'] = base_url + link.extract_first().strip()  # 拼接完整的 url
            yield scrapy.Request(url=item['link'], meta={'item': item}, callback=self.parse2)

    # 解析具体页面
    def parse2(self, response):

        item = response.meta['item']
        infos = Selector(response=response).xpath('//div[@class="movie-brief-container"]')
        for info in infos:
            film_category = info.xpath('./ul/li/a/text()').extract()
            plan_date = info.xpath('./ul/li[last()]/text()').extract_first().strip()
            item['film_category'] = film_category
            item['plan_date'] = plan_date
        yield item













