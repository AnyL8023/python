# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

#处理页面标签类
class Tool:
    # #去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    # #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    # #把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # #将表格制表<td>替换为\t
    replaceTD= re.compile('<td>')
    # #把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    # #将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    # #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    def replaceBlank(self,x):
        # x = re.sub(self.removeImg,"",x)
        # x = re.sub(self.removeAddr,"",x)
        # x = re.sub(self.replaceLine,"\n",x)
        # x = re.sub(self.replaceTD,"\t",x)
        # x = re.sub(self.replacePara,"\n    ",x)
        # x = re.sub(self.replaceBR,"\n",x)
        # x = re.sub(self.removeExtraTag,"",x)
        x = re.sub(re.compile("[\t\r\n\f\v]"), "", x)
        #strip()将前后多余内容删除
        return x.strip()

    def replaceTag(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePara,"\n    ",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        # strip()将前后多余内容删除
        return x.strip()

tool = Tool()
page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    content = tool.replaceBlank(content)
    print content
    # pattern = re.compile('<div class="content">(.*?)</div>', re.S)
    pattern = re.compile('<div class="author clearfix"><a.*?<img src="(.*?)".*?>.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>.*?<i class="number">(.*?)</i>', re.S)
    items = re.findall(pattern, content)

    print
    print

    for item in items:
        # haveImg = re.search("img", item[3])
        # if not haveImg:
            # print item[0], item[1], item[2], item[4]
        # print tool.replaceTag(item)
        print tool.replaceTag(item[0])
        print tool.replaceTag(item[1])
        print tool.replaceTag(item[2])
        print tool.replaceTag(item[3])
        print "---------------------------------------"
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason