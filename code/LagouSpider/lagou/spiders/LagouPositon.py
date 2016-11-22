# -*- coding: utf-8 -*-
import scrapy
import json
from lagou.items import LagouItem
import logging
import time
import datetime
from scrapy.utils.project import get_project_settings

log = logging.getLogger('middlewares.RandomProxyMiddleware')

class LagoupositonSpider(scrapy.Spider):

    name = "LagouPositon"

    #allowed_domains = ["lagou.com/zhaopin/"]

    # start_urls = (
    #     'http://www.lagou.com/zhaopin/'
    # )

    # totalPageCount = 0
    curpage = 1
    # cur = 0
    crawl_url = 'http://www.lagou.com/jobs/positionAjax.json?'

    #运行的时间
    run_time = None
    #是否继续运行
    isBreak = False

    # city = u'北京'
    #kds = [u'java','python','PHP','.NET','JavaScript','C#','C++','C','VB','Dephi','Perl','Ruby','Go','ASP','Shell']
    # kds = [u'大数据',u'云计算',u'docker',u'中间件','Node.js',u'数据挖掘',u'自然语言处理',u'搜索算法',u'精准推荐',u'全栈工程师',u'图像处理',u'机器学习',u'语音识别']
    #kds = ['HTML5','Android','iOS',u'web前端','Flash','U3D','COCOS2D-X']
    #kds = [u'spark','MySQL','SQLServer','Oracle','DB2','MongoDB' 'ETL','Hive',u'数据仓库','Hadoop']
    #kds = [u'大数据',u'云计算',u'docker',u'中间件']
    # kd = kds[0]

    def __init__(self):
        self.run_time = datetime.datetime.now() - datetime.timedelta(hours=1)

    def start_requests(self):
        # for self.kd in self.kds:
        #
        #     scrapy.http.FormRequest(self.myurl,
        #                                 formdata={'pn':str(self.curpage),'kd':self.kd},callback=self.parse)

         #查询特定关键词的内容，通过request
         # return [scrapy.http.FormRequest(self.myurl,
         #                                formdata={'pn':str(self.curpage),'kd':self.kd},callback=self.parse)]
        return [scrapy.http.FormRequest(self.crawl_url,
                                        formdata={'pn': str(self.curpage),'px':'new'}, callback=self.parse)]

    def parse(self, response):
        item = LagouItem()
        jdict = None
        isSuccess = True

        try:
            jdict = json.loads(response.body)
        except ValueError:
            log.error('Json parsing exception : json=%s',response.body)
            isSuccess = False

        if isSuccess == True:
            jcontent = jdict["content"]
            jposresult = jcontent["positionResult"]
            jresult = jposresult["result"]
            #计算总页数，取消30页的限制
            # self.totalPageCount = jposresult['totalCount'] /15 + 1;
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
                if self.format_time(each['createTime'])>self.run_time:
                    print "==================================="
                    print "createTime : ",self.format_time(each['createTime'])
                    print "==================================="
                    yield item
                else:
                    print "==================================="
                    print self.format_time(each['createTime'])
                    print "==================================="
                    self.isBreak = True

        if self.isBreak==False:
            self.curpage += 1
            print "===================================="
            print  "run_time : ",self.run_time
            print "===================================="
            yield scrapy.http.FormRequest(self.crawl_url, formdata={'pn': str(self.curpage), 'px': 'new'},
                                          callback=self.parse)


        # if self.curpage <= self.totalPageCount:
        #      self.curpage += 1
        #      # yield scrapy.http.FormRequest(self.myurl,formdata = {'pn': str(self.curpage), 'kd': self.kd},callback=self.parse)
        #      yield scrapy.http.FormRequest(self.myurl, formdata={'pn': str(self.curpage),'px':'new' },callback=self.parse)
        # elif self.cur < len(self.kds)-1:
        #     self.curpage = 1
        #     self.totalPageCount = 0
        #     self.cur += 1
        #     # self.kd = self.kds[self.cur]
        #     # yield scrapy.http.FormRequest(self.myurl,formdata = {'pn': str(self.curpage), 'kd': self.kd},callback=self.parse)
        #     yield scrapy.http.FormRequest(self.myurl, formdata={'pn': str(self.curpage),},callback=self.parse)


    def format_time(self,str_time):
        t = time.strptime(str_time, get_project_settings().get('ISOTIMEFORMAT'))
        return datetime.datetime(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min)
