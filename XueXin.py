# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

#账号
username = "账号"
#密码
password = "密码"

#登录链接
loginUrl = "https://account.chsi.com.cn/passport/login"

#请求的头部
headers = {
    'Host':'account.chsi.com.cn',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Referer':'https://account.chsi.com.cn/passport/login',
    'Connection':'keep-alive'
}

#session
session = requests.session()

#登录页面获取相关信息
loginContet =  session.get(loginUrl)
loginHtml = loginContet.content
loginSoup = BeautifulSoup(loginHtml,'html.parser')
lt =  loginSoup.find("input",{"name":"lt"})['value']
_eventId =  loginSoup.find("input",{"name":"_eventId"})['value']
submit =  loginSoup.find("input",{"name":"submit"})['value']

#登录的数据
loginData = {
    'username':username,
    'password':password,
    'lt':lt,
    '_eventId':_eventId,
    'submit':submit
}

#发送登录请求
session.post(loginUrl,loginData,headers)

#学籍信息(图像校对)
studentInfoUrl = "http://my.chsi.com.cn/archive/xjarchive.action"

studentInfoContent = session.get(studentInfoUrl)
studentInfoHtml = studentInfoContent.content

studentInfoSoup = BeautifulSoup(studentInfoHtml,'html.parser')

studentInfo = studentInfoSoup.find("div",{"id":"resultTable"})

studentInfoRegex = 'initDataInfo\(\".*?\", \"(.*?)\"\);'
studentInfoPattern = re.compile(studentInfoRegex, re.S)
items = re.findall(studentInfoPattern, studentInfoHtml)

print

#院校名称
school = items[0].strip()
#专业名称
major = items[1].strip()
#考生号
examNum = items[2].strip()
#学号
schoolNum = items[3].strip()
#层次
level = items[4].strip()
#学历类别
classify = items[5].strip()
#学习形式
modality = items[6].strip()
#   身份证号码
idCard = items[7].strip()

print school
print major
print examNum
print schoolNum
print level
print classify
print modality
print idCard

studentInfoRegex = '<th>(.*?)</th>\s*?<td.*?>(.*?)</td>'
studentInfoPattern = re.compile(studentInfoRegex, re.S)
items = re.findall(studentInfoPattern, studentInfoHtml)

#姓名
name = items[0][1].strip()
#性别
gender = items[1][1].strip()
#民族
nation = items[2][1].strip()
#出生日期
birthday = items[3][1].strip()
#学院
college = items[8][1].strip()
#班级
clazz = items[11][1].strip()
#入学日期
startSchoolDate = items[16][1].strip()
#学籍状态
schoolStatus = items[17][1].strip()
#预计毕业日期
endSchoolDate = items[18][1].strip()


print name
print gender
print nation
print birthday
print college
print clazz
print startSchoolDate
print schoolStatus
print endSchoolDate