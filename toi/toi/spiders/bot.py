# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from scrapy.spiders import BaseSpider
import csv
import re
import datetime
import requests
import traceback
from lxml import html
import os.path

class BotSpider(scrapy.Spider):
    name = 'bot'
    # allowed_domains = ['indiatimes.com']
    # start_urls = ['https://timesofindia.indiatimes.com/2018/5/18/archivelist/year-2018,month-5,starttime-43238.cms']

    custom_settings = {
        'DOWNLOAD_DELAY': 0.5,
        'CONCURRENT_REQUESTS': 5
        }

    def start_requests(self):
        for i in range(0,1):
            url = 'https://timesofindia.indiatimes.com/2018/5/18/archivelist/year-2018,month-5,starttime-43238.cms'
            yield scrapy.Request(url, callback=self.get_article)

    def get_article(self, response):
        articles = response.xpath('//span[contains(@style,"font-family:arial ;font-size:12;color: #006699")]/a/@href').extract()
        for article in articles:
            article_url = "https://timesofindia.indiatimes.com" + article
            yield scrapy.Request(article_url, callback=self.parse)

    def parse(self, response):
        data = {}
        temp2 = response.xpath('//h1[contains(@class,"heading1")]/arttitle/text()').extract_first()
        # import pdb; pdb.set_tradatace()/
        if(str(temp2) == 'None'):
            return
        else:
            data['Article_Name'] = temp2
            temp = response.xpath('//span[contains(@itemprop,"author")]/a/text()').extract_first()
            if(temp == 'None'):
                data['Author'] = ''
            else:
                data['Author'] = temp

            temp1 = response.xpath('//span[contains(@class,"time_cptn")]/span[2]/text()').extract()
            data['DateTime'] = ', '.join(temp1)
            # import pdb; pdb.set_trace()
            
            file_exists = os.path.isfile('/home/deep/Workspace/data_file.csv')
            with open('/home/deep/Workspace/data_file.csv', 'a') as csvfile:
                w = csv.DictWriter(csvfile, data.keys())
                if not file_exists:
                    w.writeheader()
                w.writerow(data)

            