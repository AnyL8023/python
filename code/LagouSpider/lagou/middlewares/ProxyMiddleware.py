# Importing base64 library because we'll need it ONLY in case if the proxy we are going to use requires authentication
import base64
import requests
import json

# Start your middleware class
class ProxyMiddleware(object):

    IPProxyUrl = u"http://best8023.com:8000/?method=random"
    IPDeleteUrl = u"http://best8023.com:8000/?method=remove"

    ip = None
    port = None

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
        self.ip = ipProxy['ip']
        self.port = ipProxy['port']
        request.meta['proxy'] = "http://%s:%d"%(ipProxy['ip'],ipProxy['port'])

        print "IP Proxy : ",request.meta['proxy']

        # Use the following lines if your proxy requires authentication
        # proxy_user_pass = "USERNAME:PASSWORD"
        # setup basic authentication for the proxy
        # encoded_user_pass = base64.encodestring(proxy_user_pass)
        # request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass

    # def process_response(self,request, response, spider):
        # if response.status_code == 404:
        #     response = requests.get(self.IPDeleteUrl,data={'ip':self.ip,'port':self.port})
        #     print "Remove IP Proxy : ip = ",self.ip," ;port = ",self.port
        # print request.status_code
        # return response