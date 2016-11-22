import requests

url = "http://tpv.daxiangdaili.com/ip/?tid=557214252373001&num=5&delay=1&category=2&foreign=none&filter=on"
response = requests.get(url)
print response.text
# text = u"""182.37.5.12:8888
# 183.129.151.130:80
# 144.12.222.42:8998
# 122.96.59.105:843
# 113.105.186.142:8080
# 125.42.71.195:80"""
for line in response.text.split("\n"):
    print "http://%s"%(line)