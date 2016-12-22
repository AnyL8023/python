import requests
import time
import datetime
import json

# url = "http://tpv.daxiangdaili.com/ip/?tid=556134901906794&num=5&delay=1&category=2&foreign=none&filter=on"
# response = requests.get(url)
# print response.text
# text = u"""182.37.5.12:8888
# 183.129.151.130:80
# 144.12.222.42:8998
# 122.96.59.105:843
# 113.105.186.142:8080
# 125.42.71.195:80"""
# for line in response.text.split("\n"):
#     print "http://%s"%(line)

url = "http://www.lagou.com/jobs/positionAjax.json"
mycookie = {
    #'Cookie':'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1481698814,1481787946,1481866626,1482284031;
    # user_trace_token=20160823145511-cfe5f8f98994464780781c9809eff805;
    # LGUID=20160823145511-89295256-68fe-11e6-b2e4-525400f775ce;
    # HISTORY_POSITION=2630569%2C6k-12k%2C%E6%9D%AD%E5%B7%9E%E4%B8%89%E6%B1%87%2CJAVA%E8%BD%AF%E4%BB%B6%E5%BC%80%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88-%E4%B8%8B%E6%B2%99%E5%8A%9E%E4%BA%8B%E5%A4%84%7C1956629%2C10k-15k%2C%E6%B7%98%E7%B2%89%E5%90%A7%2CJava%7C2661279%2C15k-30k%2C%E5%90%8C%E8%8A%B1%E9%A1%BA%2C%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0---%E5%8D%9A%E5%A3%AB%E7%A0%94%E7%A9%B6%E5%91%98%7C1941795%2C15k-20k%2C%E5%AE%B8%E8%B1%AA%2C%E5%88%86%E5%85%AC%E5%8F%B8%E7%BB%8F%E7%90%86%E8%A1%A2%E5%B7%9E%EF%BC%88%EF%BC%89%7C1691660%2C15k-20k%2C%E5%8D%9A%E7%99%BB%E4%BF%A1%E6%81%AF%E7%A7%91%E6%8A%80%2CJava%E7%A0%94%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88%7C;
    # LGMOID=20161212101409-0EE5240CE8A9A77DDB99F05C44777B02; JSESSIONID=689FFB41D3A6EF36E41589DD9CC75F00;
    # LGRID=20161221093351-87247d98-c71d-11e6-bf8e-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1482284031',

    # 'Cookie':'_ga=GA1.2.1023838203.1471935310; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1481787946,1481866626,1482284031,1482369493; user_trace_token=20160823145511-cfe5f8f98994464780781c9809eff805; LGUID=20160823145511-89295256-68fe-11e6-b2e4-525400f775ce; index_location_city=%E6%9D%AD%E5%B7%9E; LGMOID=20161212101409-0EE5240CE8A9A77DDB99F05C44777B02; SEARCH_ID=c0a173f063d8491cb6177bb1eea1c668; JSESSIONID=D064D3712B3C15EC6A483A1148DF8499',
    # 'Cookie':'user_trace_token=20160823145511-cfe5f8f98994464780781c9809eff805; LGUID=20160823145511-89295256-68fe-11e6-b2e4-525400f775ff;',

    # 'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6':'1481698814,1481787946,1481866626,1482284031',
    # 'user_trace_token':'20160823145511-cfe5f8f98994464780781c9809eff805',
    'user_trace_token':time,
    # 'LGUID':'20160823145511-89295256-68fe-11e6-b2e4-525400f775ce'
    'LGUID':time,
    # 'HISTORY_POSITION':'2630569%2C6k-12k%2C%E6%9D%AD%E5%B7%9E%E4%B8%89%E6%B1%87%2CJAVA%E8%BD%AF%E4%BB%B6%E5%BC%80%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88-%E4%B8%8B%E6%B2%99%E5%8A%9E%E4%BA%8B%E5%A4%84%7C1956629%2C10k-15k%2C%E6%B7%98%E7%B2%89%E5%90%A7%2CJava%7C2661279%2C15k-30k%2C%E5%90%8C%E8%8A%B1%E9%A1%BA%2C%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0---%E5%8D%9A%E5%A3%AB%E7%A0%94%E7%A9%B6%E5%91%98%7C1941795%2C15k-20k%2C%E5%AE%B8%E8%B1%AA%2C%E5%88%86%E5%85%AC%E5%8F%B8%E7%BB%8F%E7%90%86%E8%A1%A2%E5%B7%9E%EF%BC%88%EF%BC%89%7C1691660%2C15k-20k%2C%E5%8D%9A%E7%99%BB%E4%BF%A1%E6%81%AF%E7%A7%91%E6%8A%80%2CJava%E7%A0%94%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88%7C',
    # 'LGMOID':'20161212101409-0EE5240CE8A9A77DDB99F05C44777B02',
    # 'JSESSIONID':'689FFB41D3A6EF36E41589DD9CC75F00',
    # 'LGRID':'0161221093351-87247d98-c71d-11e6-bf8e-5254005c3644',
    # 'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6':'1482284031'
}
i=1
while True:
    if i>200:
        break
    # print "----------------", i, "-----------------------"
    time = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S')
    url = "http://www.lagou.com/jobs/positionAjax.json?px=new&pn="+str(i)
    # print time
    # print url
    # mycookie = {
    #     'user_trace_token': time,
    #     'LGUID': time,
    # }
    # mycookie = {'Cookie':'user_trace_token='+time+'; LGUID='+time+'; '}
    proxie = {
        'http': 'http://124.88.67.18:843',
        'http': 'http://183.66.73.103:8998',
        'http': 'http://60.176.47.40:8998',
        'http': 'http://182.92.103.55:8118',
        'http': 'http://180.107.193.212:8998',
        'http': 'http://60.176.37.125:8998',
        'http': 'http://112.80.89.132:8123',
        'http': 'http://106.89.92.91:8998',
        'http': 'http://115.200.171.155:8998',
        'http': 'http://115.203.9.210:8998',
        'http': 'http://115.200.69.217:8998',
        'http': 'http://114.232.82.180:8088',
        'http': 'http://183.144.53.40:8998',
        'http': 'http://183.144.36.159:8998',
        'http': 'http://125.84.113.197:8998',
        'http': 'http://60.169.54.32:808',
        'http': 'http://118.113.80.51:8998',
        'http': 'http://124.88.67.18:843',

    }
    headers = {
        # 'HOST':'www.lagou.com',
        # 'Cookie':'_ga=GA1.2.1023838203.1471935310; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1481698814,1481787946,1481866626,1482284031; user_trace_token=20160823145511-cfe5f8f98994464780781c9809eff805; LGUID=20160823145511-89295256-68fe-11e6-b2e4-525400f775ce; index_location_city=%E6%9D%AD%E5%B7%9E; HISTORY_POSITION=2630569%2C6k-12k%2C%E6%9D%AD%E5%B7%9E%E4%B8%89%E6%B1%87%2CJAVA%E8%BD%AF%E4%BB%B6%E5%BC%80%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88-%E4%B8%8B%E6%B2%99%E5%8A%9E%E4%BA%8B%E5%A4%84%7C1956629%2C10k-15k%2C%E6%B7%98%E7%B2%89%E5%90%A7%2CJava%7C2661279%2C15k-30k%2C%E5%90%8C%E8%8A%B1%E9%A1%BA%2C%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0---%E5%8D%9A%E5%A3%AB%E7%A0%94%E7%A9%B6%E5%91%98%7C1941795%2C15k-20k%2C%E5%AE%B8%E8%B1%AA%2C%E5%88%86%E5%85%AC%E5%8F%B8%E7%BB%8F%E7%90%86%E8%A1%A2%E5%B7%9E%EF%BC%88%EF%BC%89%7C1691660%2C15k-20k%2C%E5%8D%9A%E7%99%BB%E4%BF%A1%E6%81%AF%E7%A7%91%E6%8A%80%2CJava%E7%A0%94%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88%7C; LGMOID=20161212101409-0EE5240CE8A9A77DDB99F05C44777B02; JSESSIONID=689FFB41D3A6EF36E41589DD9CC75F00; LGRID=20161221093351-87247d98-c71d-11e6-bf8e-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1482284031',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
        'Cookie':'user_trace_token=' + time + '; LGUID=' + time + '; '
    }
    try:
        response = requests.get(url,
                                # cookies = mycookie,
                                proxies = proxie,headers=headers,timeout=3)
        response.encoding='utf8'
        json.loads(response.text)
        print response.text
        # print response.headers
        # print response.encoding
        i+=1
    except Exception:
        continue