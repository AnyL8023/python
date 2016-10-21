# -*- coding:utf-8 -*-
import json
import requests
import config
from random import choice
import logging

ip_proxy_pool = []
ip_try_count = {}

def random_proxies():
    global ip_proxy_pool
    while len(ip_proxy_pool)<=10:
        ipProxy = get_proxy()
        ip_proxy_pool.append(ipProxy)

    ipProxy = choice(ip_proxy_pool)
    # print "random : ",ipProxy
    logging.error("random : http://%s:%d",ipProxy['ip'],ipProxy['port'])

    return ipProxy

def get_proxy():
    ipProxy = None
    isSuccess = False
    while isSuccess != True:
        response = requests.get(config.IP_PROXIES_URL,timeout=config.TIME_OUT)
        if response.status_code != 200:
            continue
        content = response.content
        # print "Response content : ", content
        try:
            ipProxy = json.loads(content)
        except ValueError:
            # print "request ip proxy again"
            logging.warning("request ip proxy again")
        isSuccess = True

    # print "request : ",ipProxy
    logging.info("request : http://%s:%d",ipProxy['ip'],ipProxy['port'])

    return ipProxy

def remove_proxy(ipProxy):
    global ip_proxy_pool
    ip_proxy_pool.remove(ipProxy)
    condition = "&ip='%s'&port=%d"%(ipProxy['ip'],ipProxy['port'])
    requests.get(config.IP_DELETE_URL+condition,timeout=config.TIME_OUT)
    # print "remove : ",ipProxy
    logging.info("remove : http://%s:%d",ipProxy['ip'],ipProxy['port'])

def check_proxy(ipProxy):
    global ip_try_count

    if ip_try_count.has_key(ipProxy['ip']):
        ip_try_count[ipProxy['ip']] += 1
    else:
        ip_try_count[ipProxy['ip']] = 1

    # print "check : ", ipProxy['ip'], " ", ip_try_count[ipProxy['ip']]
    logging.info("check : ip=%s\tcount=%d",ipProxy['ip'],ip_try_count[ipProxy['ip']])

    if ip_try_count[ipProxy['ip']] >= config.CHECK_TIME:
        remove_proxy(ipProxy)
