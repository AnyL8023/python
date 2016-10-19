# -*- coding:utf-8 -*-
import requests
import json
import config

class Crawler(object):

    url = 'http://www.lagou.com/jobs/positionAjax.json'
    data = {'px':'new','pn':1}
    proxies = {}
    headers = {}

    items = []

    def run(self):

        while True:
            response = requests.post(self.url,self.data,proxies=self.proxies,headers=self.headers)
            print  response.url,self.data

            if response.status_code != 200:
                continue

            isSuccess = True

            try:
                jdict = json.loads(response.content)
            except ValueError:
                isSuccess = False

            if isSuccess == True:
                jcontent = jdict["content"]
                jposresult = jcontent["positionResult"]
                jresult = jposresult["result"];
                for each in jresult:
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
                    print item['companyFullName'],item['createTime']
                    self.items.append(item)
            self.data['pn'] += 1
            break