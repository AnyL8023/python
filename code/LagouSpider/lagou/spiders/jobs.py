# -*- coding: utf-8 -*-
import scrapy
from lagou.items import JobItem

class JobsSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["www.lagou.com/gongsi"]
    start_urls = (
        'https://www.lagou.com/jobs/1956629.html',
    )

    def parse(self, response):
        job = JobItem()
        job['metaKeywords'] = response.xpath('//meta[name="keywords"]@content').extract()
        job['metaDescription'] = response.xpath('//meta[name="description"]@content').extract()
        # response.xpath('//*[@id="job_detail"]/dd[1]/p')
        return job