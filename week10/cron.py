import os
import schedule

def job():
    d = os.path.dirname(__file__)
    abspath = os.path.abspath(d)
    scrapy_path = abspath+'/myspiders'
    os.system('cd %s && scrapy crawl smzdm '% (scrapy_path) )

if __name__ == '__main__':
    schedule.every().day.at('02:00').do(job)
    while True:
        schedule.run_pending()