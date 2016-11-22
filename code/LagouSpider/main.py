#-*- coding: utf-8 -*-
import scrapy.cmdline as cmd
import time
import datetime

HOUR = 16
MIN = 30

ISOTIMEFORMAT='%Y-%m-%d %H:%M:%S'

# while True:
#     current_time = time.localtime(time.time())
#     print "Sytem Wait Time %d:%d , Current Time %s"%(HOUR,MIN,time.strftime( ISOTIMEFORMAT, time.localtime( time.time())))
#     # if((current_time.tm_hour == HOUR) and (current_time.tm_min == MIN)):
#     #     cmd.execute('scrapy crawl LagouPositon'.split())
#     cmd.execute('scrapy crawl LagouPositon'.split())
#     time.sleep(60)
#     break
cmd.execute('scrapy crawl LagouPositon'.split())
