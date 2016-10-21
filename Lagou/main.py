from cralwer.crawler import Crawler
import datetime
import time
from db.save_csv import DB_CSV
from cralwer.proxies import random_proxies
from cralwer.proxies import remove_proxy

ISOTIMEFORMAT = "%Y-%m-%d %H:%M:%S"

crawler = Crawler()

MIN = 27
crawler = Crawler()

while True:
    current_time = time.localtime(time.time())
    print "Current Time %s"%(time.strftime( ISOTIMEFORMAT,current_time))
    if current_time.tm_min == MIN:
        run_time = (datetime.datetime.now() - datetime.timedelta(hours=1))
        run_time_str = ((datetime.datetime.now() - datetime.timedelta(hours=1)).strftime(ISOTIMEFORMAT))
        items = crawler.run(run_time_str)

        fileName = run_time.strftime("%Y-%m-%d-%H")
        db = DB_CSV(fileName)
        if len(items)>0:
            for item in items.values():
                db.save(item)
        db.close()

    time.sleep(60)

# run_time = (datetime.datetime.now() - datetime.timedelta(hours=1))
# fileName = run_time.strftime("%Y-%m-%d-%H")
# db = DB_CSV(fileName)
# db.save(None)
# db.close()