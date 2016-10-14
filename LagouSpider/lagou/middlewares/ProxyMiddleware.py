# Importing base64 library because we'll need it ONLY in case if the proxy we are going to use requires authentication
import base64
import requests
import json

# Start your middleware class
class ProxyMiddleware(object):

    IPProxyUrl = u"http://best8023.com:8000/?types=0&country=%E4%B8%AD%E5%9B%BD&random=1"

    # overwrite process request
    def process_request(self, request, spider):
        ipProxy = None
        isSuccess = False
        while isSuccess!=True:
            response = requests.get(self.IPProxyUrl)
            if  response.status_code != 200:
                continue
            content = response.content
            print "Response content : ",content
            try:
                ipProxy = json.loads(content)
            except ValueError:
                print "request ip proxy again"
            isSuccess = True

        # Set the location of the proxy
        request.meta['proxy'] = "http://%s:%d"%(ipProxy[0],ipProxy[1])

        print "IP Proxy : ",request.meta['proxy']

        # Use the following lines if your proxy requires authentication
        # proxy_user_pass = "USERNAME:PASSWORD"
        # setup basic authentication for the proxy
        # encoded_user_pass = base64.encodestring(proxy_user_pass)
        # request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass