# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SpidersPipeline:
    def process_item(self, item, spider):
        link = item['link']
        film_category = item['film_category']
        plan_date = item['plan_date']
        output = f'|{link}\n|{plan_date}\n|{film_category}\n\n'
        with open('./maoyan_movie.txt', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item
