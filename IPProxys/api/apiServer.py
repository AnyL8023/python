#coding:utf-8
'''
定义几个关键字，count type,protocol,country,area,
'''
import urllib
from config import API_PORT
from db.SQLiteHelper import SqliteHelper
from validator.Validator import Validator

__author__ = 'Xaxdus'

import BaseHTTPServer
import json
import urlparse
import random
import copy

# keylist=['count', 'types','protocol','country','area']
class WebRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_GET(self):
        """
        """
        dict={}

        parsed_path = urlparse.urlparse(self.path)
        try:
            query = urllib.unquote(parsed_path.query)
            print query
            if query.find('&')!=-1:
                params = query.split('&')
                for param in params:
                    dict[param.split('=')[0]]=param.split('=')[1]
            else:
                    dict[query.split('=')[0]]=query.split('=')[1]

            str_count=''
            conditions=[]
            sqlHelper = SqliteHelper()
            validator = Validator(sqlHelper)

            method = dict['method']

            if method == 'get':
                for key in dict:
                    if key =='count':
                        str_count = 'lIMIT 0,%s'% dict[key]
                    if key =='country' or key =='area':
                        conditions .append(key+" LIKE '"+dict[key]+"%'")
                    elif key =='types' or key =='protocol' or key =='country' or key =='area':
                        conditions .append(key+"="+dict[key])
                    if key == 'speed':
                        conditions.append(key + "<=" + dict[key])
                if len(conditions)>1:
                    conditions = ' AND '.join(conditions)
                else:
                    conditions =conditions[0]
                result = sqlHelper.select(sqlHelper.tableName,conditions,str_count)
                results = copy.copy(result)
                if dict.has_key("random"):
                    result = random.choice(results)
                    while True:
                        proxy = {}
                        proxy['ip'] = result[0]
                        proxy['port'] = result[1]

                        result = validator.detect_list(proxy)
                        if result == None or result['speed'] >= 2:
                            _conditions = []
                            for key in proxy:
                                if key == 'ip':
                                    _conditions.append(key + "=" + dict[key])
                                if key == 'port':
                                    _conditions.append(key + "=" + dict[key])
                            if len(conditions) > 1:
                                _conditions = ' AND '.join(_conditions)
                            else:
                                _conditions = _conditions[0]
                            sqlHelper.delete(sqlHelper.tableName, _conditions)
                            result = random.choice(results)
                        else:
                            break

            elif method == 'random':
                conditions.append("'中国' LIKE '中国%'")
                conditions.append("types = 0")
                conditions.append("speed <= 2")
                if len(conditions) > 1:
                    conditions = ' AND '.join(conditions)
                else:
                    conditions = conditions[0]
                result = sqlHelper.select(sqlHelper.tableName, conditions, str_count)
                results = copy.copy(result)
                result = random.choice(results)

                while True:
                    proxy = {}
                    proxy['ip'] = result[0]
                    proxy['port'] = result[1]

                    result = validator.detect_list(proxy)

                    if result == None or result['speed'] >= 2:
                        _conditions = []
                        for key in proxy:
                            if key == 'ip':
                                _conditions.append(key + "=" + dict[key])
                            if key == 'port':
                                _conditions.append(key + "=" + dict[key])
                        if len(conditions) > 1:
                            _conditions = ' AND '.join(_conditions)
                        else:
                            _conditions = _conditions[0]
                        sqlHelper.delete(sqlHelper.tableName, _conditions)
                        result = random.choice(results)
                    else:
                        break
            elif method == 'remove':
                for key in dict:
                    if key =='ip':
                        conditions.append(key + "=" + dict[key])
                    if key =='port':
                        conditions.append(key + "=" + dict[key])
                if len(conditions)>1:
                    conditions = ' AND '.join(conditions)
                else:
                    conditions =conditions[0]
                sqlHelper.delete(sqlHelper.tableName,conditions)
            # print type(result)
            # for r in  result:
            #     print r
            print result
            data = json.dumps(result)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(data)
            sqlHelper.close()
        except Exception,e:
            print e
            self.send_response(404)


if __name__=='__main__':
    server = BaseHTTPServer.HTTPServer(('0.0.0.0',API_PORT), WebRequestHandler)
    server.serve_forever()