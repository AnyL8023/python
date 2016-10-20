from cralwer.crawler import Crawler
import datetime
import time
from cralwer.proxies import random_proxies
from cralwer.proxies import remove_proxy

ISOTIMEFORMAT = "%Y-%m-%d %H:%M:%S"
run_time =  ((datetime.datetime.now()-datetime.timedelta(hours=1)).strftime(ISOTIMEFORMAT))

crawler = Crawler()
crawler.run(run_time)
time.sleep(60)
crawler.run(run_time)


# print time.localtime()
# print (time.localtime().tm_hour+23)%24
# print (0+23)%24

# for i in range(1,100):
#     ipProxy =  random_proxies()
#     print ipProxy
#     if i%10 == 0:
#         remove_proxy(ipProxy)
# remove_proxy(ipProxy)