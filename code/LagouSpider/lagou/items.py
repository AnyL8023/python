# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # city = scrapy.Field()
    # companyName = scrapy.Field()
    # companySize = scrapy.Field()
    # positionName = scrapy.Field()
    # salaryMax = scrapy.Field()
    # salaryMin = scrapy.Field()
    # salaryAvg = scrapy.Field()
    # positionType = scrapy.Field()
    # positionAdvantage = scrapy.Field()
    # companyLabelList = scrapy.Field()
    # keyword = scrapy.Field()

    companyId = scrapy.Field()
    workYear = scrapy.Field()
    education = scrapy.Field()
    jobNature = scrapy.Field()
    positionName = scrapy.Field()
    positionId = scrapy.Field()
    createTime = scrapy.Field()
    city = scrapy.Field()
    companyLogo = scrapy.Field()
    industryField = scrapy.Field()
    positionAdvantage = scrapy.Field()
    salary = scrapy.Field()
    companySize = scrapy.Field()
    approve = scrapy.Field()
    financeStage = scrapy.Field()
    companyLabelList = scrapy.Field()
    district = scrapy.Field()
    companyShortName = scrapy.Field()
    score = scrapy.Field()
    publisherId = scrapy.Field()
    explain = scrapy.Field()
    plus = scrapy.Field()
    pcShow = scrapy.Field()
    appShow = scrapy.Field()
    deliver = scrapy.Field()
    gradeDescription = scrapy.Field()
    promotionScoreExplain = scrapy.Field()
    businessZones = scrapy.Field()
    imState = scrapy.Field()
    lastLogin = scrapy.Field()
    formatCreateTime = scrapy.Field()
    adWord = scrapy.Field()
    companyFullName = scrapy.Field()

class JobItem(scrapy.Item):
    positionId = scrapy.Field()
    metaKeywords = scrapy.Field()
    metaDescription = scrapy.Field()
    advantage = scrapy.Field()
    description = scrapy.Field()
    address = scrapy.Field()