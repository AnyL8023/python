# -*- coding: utf-8 -*-
import re
import random
import base64
import logging
import requests

log = logging.getLogger('middlewares.RandomProxyMiddleware')


class Mode:
    RANDOMIZE_PROXY_EVERY_REQUESTS, RANDOMIZE_PROXY_ONCE, SET_CUSTOM_PROXY = range(3)


class RandomProxy(object):
    def __init__(self, settings):
        # 随机代理模式
        self.mode = settings.get('PROXY_MODE')
        # IP代理列表
        self.proxy_list = settings.get('PROXY_LIST')
        # 单次代理IP
        self.chosen_proxy = ''
        self.custom_proxy = settings.get('CUSTOM_PROXY')
        #添加IP请求连接
        self.ip_proxy_url = settings.get('IP_PROXY_URL')
        #http code
        self.http_error_code = settings.get('RETRY_HTTP_CODES')
        # IP Proxy Pool Size
        self.ip_proxy_pool_size = settings.get('IP_PROXY_POOL_SIZE')


        self.read_ip_proxy_file()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def process_request(self, request, spider):
        # Don't overwrite with a random one (server-side state for IP)
        #判断是否向池中添加IP
        if len(self.proxies)<self.ip_proxy_pool_size:
            self.add_ip()
            self.read_ip_proxy_file()

        if 'proxy' in request.meta:
            if request.meta["exception"] is False:
                return
        request.meta["exception"] = False
        if len(self.proxies) == 0:
            raise ValueError('All proxies are unusable, cannot proceed')

        if self.mode == Mode.RANDOMIZE_PROXY_EVERY_REQUESTS:
            proxy_address = random.choice(list(self.proxies.keys()))
        else:
            proxy_address = self.chosen_proxy

        proxy_user_pass = self.proxies[proxy_address]

        print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
        print "proxy_address:\t",proxy_address
        print "proxy_user_pass:\t",proxy_user_pass
        print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"

        if proxy_user_pass:
            request.meta['proxy'] = proxy_address
            basic_auth = 'Basic ' + base64.b64encode(proxy_user_pass.encode()).decode()
            request.headers['Proxy-Authorization'] = basic_auth
        else:
            request.meta['proxy'] = proxy_address
            log.debug('Proxy user pass not found')
        log.debug('Using proxy <%s>, %d proxies left' % (proxy_address, len(self.proxies)))

    def process_exception(self, request, exception, spider):
        if 'proxy' not in request.meta:
            return
        if self.mode == Mode.RANDOMIZE_PROXY_EVERY_REQUESTS or self.mode == Mode.RANDOMIZE_PROXY_ONCE:
            proxy = request.meta['proxy']
            try:
                del self.proxies[proxy]
                #删除没有用的IP
                self.remove_ip()
            except KeyError:
                pass
            request.meta["exception"] = True
            if self.mode == Mode.RANDOMIZE_PROXY_ONCE:
                self.chosen_proxy = random.choice(list(self.proxies.keys()))
            log.info('Removing failed proxy <%s>, %d proxies left' % (proxy, len(self.proxies)))


    def read_ip_proxy_file(self):

        if self.proxy_list is None:
            raise KeyError('PROXY_LIST setting is missing')

        if self.mode == Mode.RANDOMIZE_PROXY_EVERY_REQUESTS or self.mode == Mode.RANDOMIZE_PROXY_ONCE:
            fin = open(self.proxy_list)
            self.proxies = {}
            print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
            for line in fin.readlines():
                parts = re.match('(\w+://)(\w+:\w+@)?(.+)', line.strip())
                if not parts:
                    continue

                # Cut trailing @
                if parts.group(2):
                    user_pass = parts.group(2)[:-1]
                else:
                    user_pass = ''

                self.proxies[parts.group(1) + parts.group(3)] = user_pass
                print parts.group(1) + parts.group(3), "\t", user_pass
            print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
            fin.close()
            if self.mode == Mode.RANDOMIZE_PROXY_ONCE:
                self.chosen_proxy = random.choice(list(self.proxies.keys()))
        elif self.mode == Mode.SET_CUSTOM_PROXY:
            self.proxies = {}
            parts = re.match('(\w+://)(\w+:\w+@)?(.+)', self.custom_proxy.strip())
            if not parts:
                raise ValueError('CUSTOM_PROXY is not well formatted')

            if parts.group(2):
                user_pass = parts.group(2)[:-1]
            else:
                user_pass = ''

            self.proxies[parts.group(1) + parts.group(3)] = user_pass
            self.chosen_proxy = parts.group(1) + parts.group(3)

    def process_response(self, request, response, spider):
        if response.status in self.http_error_code:
            if 'proxy' not in request.meta:
                return
            if self.mode == Mode.RANDOMIZE_PROXY_EVERY_REQUESTS or self.mode == Mode.RANDOMIZE_PROXY_ONCE:
                proxy = request.meta['proxy']
                try:
                    del self.proxies[proxy]
                    # 删除没有用的IP
                    self.remove_ip()
                except KeyError:
                    pass
                request.meta["exception"] = True
                if self.mode == Mode.RANDOMIZE_PROXY_ONCE:
                    self.chosen_proxy = random.choice(list(self.proxies.keys()))
                log.info('Removing failed proxy <%s>, %d proxies left' % (proxy, len(self.proxies)))
        return response

    def add_ip(self):
        fin = open(self.proxy_list, 'a')
        response = requests.get(self.ip_proxy_url)
        log.info("------------------------------------------------------------")
        log.info("add ip to pool :{\n%s\n}",response.text)
        log.info("------------------------------------------------------------")
        for line in response.text.split("\n"):
            fin.write("http://%s\n" % (line))
        fin.close()

    def remove_ip(self):
        fin = open(self.proxy_list, 'w')
        for (proxy_ip, proxy_user_pass) in self.proxies.items():
            if proxy_user_pass:
                parts = re.match('(\w+://)(\w+:\w+@)?(.+)', proxy_ip.strip())
                if not parts:
                    continue
                fin.write(parts.group(1) + proxy_user_pass + "@" + parts.group(3))
            else:
                fin.write(proxy_ip)
            fin.write('\n')
        fin.close()