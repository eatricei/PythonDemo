# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem
import cx_Oracle

class DoubanspiderSpider(scrapy.Spider):
    name = 'doubanspider'
    start_urls = ['http://https://book.douban.com/']
    temp = 20180016483
    temp_sort = 21

    def start_requests(self):
        url = "https://book.douban.com/tag/%E4%BA%BA%E9%99%85%E5%85%B3%E7%B3%BB?start=0&type=T"
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        item = DoubanItem()
        info_list = response.xpath('//div[@class="info"]')
        print(info_list)

        for info in info_list:
            item['book_name'] = info.xpath('.//h2/a/@title').extract_first()
            temp_arr = info.xpath('.//div[@class="pub"]/text()').extract_first().split('/')
            temp_len = len(temp_arr)
            if temp_len >= 4:
                item['book_auther'] = temp_arr[0].strip()
                item['book_pub'] = temp_arr[temp_len - 3].strip()
                item['book_publication_date'] = temp_arr[temp_len - 2].strip()
                item['book_price'] = temp_arr[temp_len - 1].strip()
            else:
                break
            item['book_sort'] = self.temp_sort
            item['book_status'] = '100'
            self.temp = self.temp + 1
            item['book_id'] = self.temp
            yield item

        next_temp_url = response.xpath('//span[@class="next"]/a/@href').extract_first()
        print(next_temp_url)
        if next_temp_url is not None:
            next_url = response.urljoin(next_temp_url)
            print(next_url)
            yield scrapy.Request(next_url)
        elif self.temp_sort <= 35:
            cursor = None
            conn = None
            try:
                conn = cx_Oracle.connect('swj', '19961226')
                cursor = conn.cursor()
                self.temp_sort = self.temp_sort + 1
                x = cursor.execute('select * from t_enumvalue where enumvalue=%s' % (self.temp_sort))
                value = x.fetchone()
                next_url = "https://book.douban.com/tag/" + value[2] + "?start=0&type=T"
                print(next_url)
                yield scrapy.Request(next_url)
            finally:
                cursor.close()
                conn.close()
