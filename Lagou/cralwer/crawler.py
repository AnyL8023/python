# -*- coding:utf-8 -*-
import requests
import json
import datetime
import time
import config
import headers
from proxies import random_proxies
from proxies import remove_proxy
from proxies import check_proxy

import logging

class Crawler(object):

    url = 'http://www.lagou.com/jobs/positionAjax.json'
    data = {'px':'new','pn':1}
    # proxies = { "http": "http://124.88.67.17:843" }
    proxies = {}
    headers = {}

    ISOTIMEFORMAT = "%Y-%m-%d %H:%M:%S"
    isEnd = False

    items = {}
    result_count = {}

    def run(self,run_time):
        self.clear()

        while self.isEnd == False:
            #headers
            self.headers = headers.random_headers()
            #proxies
            ipProxy = random_proxies()
            http = "http://%s:%d"%(ipProxy['ip'],ipProxy['port'])
            self.proxies = {"http": http}

            response = None
            try:
                response = requests.post(self.url,self.data,proxies=self.proxies,headers=self.headers,timeout=config.TIME_OUT)

                # print self.proxies
                # print self.headers
                # print  response.url,self.data,response.status_code,self.headers['User-Agent']
                logging.info("crawler : url=%s page=%d http_code=%d agent=%s",response.url,self.data['pn'],response.status_code,self.headers['User-Agent'])

                if response.status_code != 200:
                    check_proxy(ipProxy)
                    continue
            except requests.exceptions.Timeout:
                check_proxy(ipProxy)
                continue
            except requests.exceptions.ProxyError:
                remove_proxy(ipProxy)
                continue
            except requests.exceptions.ConnectionError:
                check_proxy(ipProxy)
                continue
            except Exception,e:
                isSuccess = False
                check_proxy(ipProxy)
                logging.error(e)
                continue
            # except Exception :
            #     print Exception
            #     check_proxy(ipProxy)
            #     continue

            #标记返回是否成功
            isSuccess = True

            try:
                jdict = json.loads(response.content)
            except ValueError:
                isSuccess = False
                check_proxy(ipProxy)
                continue
            except Exception,e:
                isSuccess = False
                check_proxy(ipProxy)
                logging.error(e)
                continue

            if isSuccess == True:
                jcontent = jdict["content"]
                jposresult = jcontent["positionResult"]
                # jresult = jposresult["result"];

                items_size = len(self.items)

                for each in jposresult:
                    item = self.get_item(each['position'])

                    if self.format_time(item['createTime']) < self.format_time(run_time):
                        logging.warning("crawler stop : time=%s",self.format_time(item['createTime']))
                        self.isEnd = True
                        break
                    # print item['publisherId'],item['companyFullName'],self.format_time(item['createTime'])
                    # self.items.append(item)

                    if self.result_count.has_key(item['positionId']) and self.items.has_key(item['positionId']):
                        self.result_count[item['positionId']] += 1
                        pass
                    else:
                        self.items[item['positionId']] = item
                        self.result_count[item['positionId']] = 1

                self.data['pn'] += 1
            # print len(self.items)
            if items_size<len(self.items):
                logging.info("crawler : count=%d",len(self.items))
            else:
                self.isEnd = True
        return self.items


    def format_time(self,str_time):
        t = time.strptime(str_time, self.ISOTIMEFORMAT)
        return datetime.datetime(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min)

    def get_item(self,each):
        item = {}
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
        logging.info("current data createTime : %s",item['createTime'])
        return item

    def clear(self):
        self.data = {'px': 'new', 'pn': 1}
        self.isEnd = False
        self.items = {}
        self.result_count = {}