# -*- coding: utf-8 -*-
#网络爬虫测试
import urllib2,cookielib
import re
#直接请求
response1 = urllib2.urlopen('http://www.baidu.com')
#获取状态码
print response1.getcode()#,response.info()
cont = response1.read()
print len(cont)
#下载器2：添加data，http header
#创建request对象：
request = urllib2.Request('http://www.baidu.com')
# print request
#添加数据
# request.add_data('w')
# print request.data
request.add_header('User-Agent', 'Mozilla/5.0')
response2 = urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())
#下载器3：
#创建cookie容器
cj = cookielib.CookieJar()
#创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#给urllib2安装一个opener
urllib2.install_opener(opener)
#使用带有cookie的urllib2访问网页
url = 'http://www.baidu.com'
response3 = urllib2.urlopen(url)
print response3.getcode()
print len(response3.read())
# print cj
# print response3.read()
'''beautifulsoup4语法测试'''
from bs4 import BeautifulSoup
html_doc = open('../C++简历.html') #下载htnl文件或本地html文件，并将其赋给html_doc
# print html_doc
#根据html网页字符串创建beautifulsoup对象
soup = BeautifulSoup(
                     html_doc,#html文档字符串
                     'html.parser',#指定html文档解析器
                     from_encoding = 'utf-8'#指定html文档编码
                     )
#搜索节点findall/find方法。参数包含节点名称，属性，字符串
#查找标签为‘xxx’的节点，传入‘xxx’名称
print soup.find_all(re.compile(r'.*img'))
link_node = soup.find_all('img',src = re.compile(r'http.*com'))
for links in link_node:
    print links.name,links.src