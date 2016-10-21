# coding: utf-8

import csv
import config
import logging
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class DB_CSV(object):

    csvfile = None

    def __init__(self,fileName):
        filePath = config.SAVE_FILE_PATH+fileName+".csv"
        print "save data to : ",filePath
        self.csvfile = file(filePath, 'wb')

    def save(self,object):
        writer = csv.writer(self.csvfile)

        data = []
        data.append(object['companyId'])
        data.append(object['workYear'])
        data.append(object['education'])
        data.append(object['jobNature'])
        data.append(object['positionName'])
        data.append(object['positionId'])
        data.append(object['createTime'])
        data.append(object['city'])
        data.append(object['companyLogo'])
        data.append(self.getString(object['industryField']))
        data.append(object['positionAdvantage'])
        data.append(object['salary'])
        data.append(object['companySize'])
        data.append(object['approve'])
        data.append(object['financeStage'])
        data.append(self.getString(object['companyLabelList']))
        data.append(object['district'])
        data.append(object['companyShortName'])
        data.append(object['score'])
        data.append(object['publisherId'])
        data.append(object['explain'])
        data.append(object['plus'])
        data.append(object['pcShow'])
        data.append(object['appShow'])
        data.append(object['deliver'])
        data.append(object['gradeDescription'])
        data.append(object['promotionScoreExplain'])
        data.append(self.getString(object['businessZones']))
        data.append(object['imState'])
        data.append(object['lastLogin'])
        data.append(object['formatCreateTime'])
        data.append(object['adWord'])
        data.append(object['companyFullName'])

        # print "write : ",object
        logging.info("write : publisherId=%d companyFullName=%s",object['positionId'],object['companyFullName'])
        writer.writerow(data)

    def close(self):
        self.csvfile.close()

    def getString(self,object):
        result = ""
        if type(object) == None:
            return None
        elif type(object) == list:
            result = "".join(x + "|" for x in object)
            result = result[:-1]
        elif type(object) == str:
            result = object
        elif type(object) == unicode:
            result = object
        return result