# -*- coding: utf-8 -*-
import scrapy
import json
from lagou.items import LagouItem
#from scrapy_redis.spiders import RedisSpider

class LagoupositonSpider(scrapy.Spider):
    name = "LagouPositon"
    #allowed_domains = ["lagou.com/zhaopin/"]
    start_urls = (
        'http://www.lagou.com/zhaopin/'
    )
    totalPageCount = 0
    curpage = 1
    cur = 0
    myurl = 'http://www.lagou.com/jobs/positionAjax.json?'

    # city = u'北京'
    #kds = [u'java','python','PHP','.NET','JavaScript','C#','C++','C','VB','Dephi','Perl','Ruby','Go','ASP','Shell']
    # kds = [u'大数据',u'云计算',u'docker',u'中间件','Node.js',u'数据挖掘',u'自然语言处理',u'搜索算法',u'精准推荐',u'全栈工程师',u'图像处理',u'机器学习',u'语音识别']
    #kds = ['HTML5','Android','iOS',u'web前端','Flash','U3D','COCOS2D-X']
    #kds = [u'spark','MySQL','SQLServer','Oracle','DB2','MongoDB' 'ETL','Hive',u'数据仓库','Hadoop']
    #kds = [u'大数据',u'云计算',u'docker',u'中间件']
    # kd = kds[0]
    def start_requests(self):
        # for self.kd in self.kds:
        #
        #     scrapy.http.FormRequest(self.myurl,
        #                                 formdata={'pn':str(self.curpage),'kd':self.kd},callback=self.parse)

         #查询特定关键词的内容，通过request
         # return [scrapy.http.FormRequest(self.myurl,
         #                                formdata={'pn':str(self.curpage),'kd':self.kd},callback=self.parse)]
        return [scrapy.http.FormRequest(self.myurl,
                                        formdata={'pn': str(self.curpage),}, callback=self.parse)]

    def parse(self, response):
        # print response.body
        fp = open('1.html','w')
        fp.write(response.body)
        item = LagouItem()
        jdict = None
        isSuccess = True
        try:
            jdict = json.loads(response.body)
        except ValueError:
            isSuccess = False

        if isSuccess == True:
            jcontent = jdict["content"]
            jposresult = jcontent["positionResult"]
            jresult = jposresult["result"]
            #计算总页数，取消30页的限制
            self.totalPageCount = jposresult['totalCount'] /15 + 1;
            # if self.totalPageCount > 30:
            #     self.totalPageCount = 30;
            for each in jresult:
                item['companyId'] = each['companyId']
                item['workYear'] = each['workYear']
                item['education'] = each['education']
                item['jobNature'] = each['jobNature']
                item['positionName'] = each['positionName']
                item['positionId'] = each['positionId']
                item['createTime'] = each['createTime']
                item['city'] = each['city']
                item['companyLogo'] = each['companyLogo']
                item['industryField'] = each['industryField']
                item['positionAdvantage'] = each['positionAdvantage']
                item['salary'] = each['salary']
                item['companySize'] = each['companySize']
                item['approve'] = each['approve']
                item['financeStage'] = each['financeStage']
                item['companyLabelList'] = each['companyLabelList']
                item['district'] = each['district']
                item['companyShortName'] = each['companyShortName']
                item['score'] = each['score']
                item['publisherId'] = each['publisherId']
                item['explain'] = each['explain']
                item['plus'] = each['plus']
                item['pcShow'] = each['pcShow']
                item['appShow'] = each['appShow']
                item['deliver'] = each['deliver']
                item['gradeDescription'] = each['gradeDescription']
                item['promotionScoreExplain'] = each['promotionScoreExplain']
                item['businessZones'] = each['businessZones']
                item['imState'] = each['imState']
                item['lastLogin'] = each['lastLogin']
                item['formatCreateTime'] = each['formatCreateTime']
                item['adWord'] = each['adWord']
                item['companyFullName'] = each['companyFullName']
                yield item


        if self.curpage <= self.totalPageCount:
             self.curpage += 1
             # yield scrapy.http.FormRequest(self.myurl,formdata = {'pn': str(self.curpage), 'kd': self.kd},callback=self.parse)
             yield scrapy.http.FormRequest(self.myurl, formdata={'pn': str(self.curpage), },callback=self.parse)
        elif self.cur < len(self.kds)-1:
            self.curpage = 1
            self.totalPageCount = 0
            self.cur += 1
            # self.kd = self.kds[self.cur]
            # yield scrapy.http.FormRequest(self.myurl,formdata = {'pn': str(self.curpage), 'kd': self.kd},callback=self.parse)
            yield scrapy.http.FormRequest(self.myurl, formdata={'pn': str(self.curpage),},callback=self.parse)

