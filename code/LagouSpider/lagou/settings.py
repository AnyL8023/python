# -*- coding: utf-8 -*-

# Scrapy settings for lagou project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import time

ISOTIMEFORMAT='%Y-%m-%d-part-%H'

BOT_NAME = 'lagou'

SPIDER_MODULES = ['lagou.spiders']
NEWSPIDER_MODULE = 'lagou.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0'
FEED_URI = 'data/part-'+time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )+'.csv'
FEED_FORMAT = 'csv'

COOKIES_ENABLED = True

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_NAME = 'Lagou'
MONGODB_TABLE = 'position'


# SCHEDULER  = "scrapy_redis.scheduler.Scheduler"
# SCHEDULER_PERSIST= True
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# REDIS_URL = None
# REDIS_HOST = '127.0.0.1'
# REDIS_PORT = 6379
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY=3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
#COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'lagou.middlewares.MyCustomSpiderMiddleware': 543,
#}

RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 403, 404, 407,408]
RETRY_TIMES = 15
DOWNLOAD_DELAY = 0.25
DOWNLOAD_TIMEOUT = 3

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
#    'lagou.middlewares.MyCustomDownloaderMiddleware': 543,
    'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 90,
    'lagou.middlewares.RandomProxyMiddleware.RandomProxy':100,
    'lagou.middlewares.UserAgentsMiddleware.UserAgentsMiddleware':105,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    # 'scrapy.contrib.downloadermiddleware.defaultheaders.DefaultHeadersMiddleware':80,
    # 'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware':80
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
#     'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
    # 'lagou.middlewares.ProxyMiddleware.ProxyMiddleware':100,
}

# DEFAULT_REQUEST_HEADERS = {
# 'Cookie':'_ga=GA1.2.1023838203.1471935310; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1481698814,1481787946,1481866626,1482284031; user_trace_token=20160823145511-cfe5f8f98994464780781c9809eff805; LGUID=20160823145511-89295256-68fe-11e6-b2e4-525400f775ce; index_location_city=%E6%9D%AD%E5%B7%9E; HISTORY_POSITION=2630569%2C6k-12k%2C%E6%9D%AD%E5%B7%9E%E4%B8%89%E6%B1%87%2CJAVA%E8%BD%AF%E4%BB%B6%E5%BC%80%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88-%E4%B8%8B%E6%B2%99%E5%8A%9E%E4%BA%8B%E5%A4%84%7C1956629%2C10k-15k%2C%E6%B7%98%E7%B2%89%E5%90%A7%2CJava%7C2661279%2C15k-30k%2C%E5%90%8C%E8%8A%B1%E9%A1%BA%2C%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0---%E5%8D%9A%E5%A3%AB%E7%A0%94%E7%A9%B6%E5%91%98%7C1941795%2C15k-20k%2C%E5%AE%B8%E8%B1%AA%2C%E5%88%86%E5%85%AC%E5%8F%B8%E7%BB%8F%E7%90%86%E8%A1%A2%E5%B7%9E%EF%BC%88%EF%BC%89%7C1691660%2C15k-20k%2C%E5%8D%9A%E7%99%BB%E4%BF%A1%E6%81%AF%E7%A7%91%E6%8A%80%2CJava%E7%A0%94%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88%7C; LGMOID=20161212101409-0EE5240CE8A9A77DDB99F05C44777B02; JSESSIONID=689FFB41D3A6EF36E41589DD9CC75F00; LGRID=20161221093351-87247d98-c71d-11e6-bf8e-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1482284031',
# }

# COOKIES_ENABLED = True
# COOKIES_DEBUG = False

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'lagou.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'

# Proxy list containing entries like
# http://host1:port
# http://username:password@host2:port
# http://host3:port
# ...
# PROXY_LIST = 'H:/Python/LagouSpider/ip.txt'
# USER_AGENTS_LIST_FILE = 'H:/Python/LagouSpider/user-agents.txt'
PROXY_LIST = 'ip.txt'
USER_AGENTS_LIST_FILE = 'user-agents.txt'
# Proxy mode
# 0 = Every requests have different proxy
# 1 = Take only one proxy from the list and assign it to every requests
# 2 = Put a custom proxy to use in the settings
PROXY_MODE = 0

# If proxy mode is 2 uncomment this sentence :
#CUSTOM_PROXY = "http://host1:port"

#订单号
IP_PROXY_TID = "556134901906794"
#提取数量
IP_PROXY_NUM = 20
#IP代理网站
IP_PROXY_URL = "http://tpv.daxiangdaili.com/ip/?tid=%s&num=%d&delay=1&category=2&foreign=none&filter=on"%(IP_PROXY_TID,IP_PROXY_NUM)
#ip代理池大小设置
IP_PROXY_POOL_SIZE = 10

ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S'
