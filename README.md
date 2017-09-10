# crawler_Example
## 网络爬虫
##### 简介：
![简介1](/home/yang/pylab/WebCrawler/web1.jpg)
- - -
###### 价值：
1. 爬虫的价值：爬取互联网数据，为我所用！（本质是数据的整合、处理与展示。）
2. 这里列举的如聚合等服务是为用户更方便地提供垂直领域的深度信息（数据分析，基于数据做出相关主题的产品）。
![简介2](/home/yang/pylab/WebCrawler/web2.jpg)
- - -
###### 架构：
![简介3](/home/yang/pylab/WebCrawler/web3.jpg)
1. 爬虫调度端：启动爬虫，停止爬虫，监视爬虫运行情况
2. URL管理器：对将要爬取的和已经爬取过的URL进行管理；可取出带爬取的URL，将其传送给“网页下载器”
3. 网页下载器：将URL指定的网页下载，存储成一个字符串，在传送给“网页解析器”
4. 网页解析器：解析网页可解析出①有价值的数据②另一方面，每个网页都包含有指向其他网页的URL，解析出来后可补充进“URL管理器”
- - -
###### 流程：
*爬虫架构运行流程：*
调度器询问url是否有待爬取的url，如果有，则取出一个url传送给下载器，下载器下载完成后，返回给调度器，调度器将内容传送给解析器，解析器分析出有用数据及关联url，返回给调度器，调度器一方面将有价值数据传送给应用进行存储及分析，另一方面将新的url传送给url管理器。如此循环
![简介4](/home/yang/pylab/WebCrawler/web4.jpg)
- - -
**url管理器**
- url管理器中的业务逻辑(核心防止重复,循环抓取)
![简介5](/home/yang/pylab/WebCrawler/web5.jpg)
- 实现方式：
![简介6](/home/yang/pylab/WebCrawler/web6.jpg)
URL管理器实现方式：
大型公司使用缓存数据库
小型公司或个人使用内存，需要再大一点的数据库或者永久存储使用关系数据库
使用set因为可以去重
- - -
**网页下载器**
![简介7](/home/yang/pylab/WebCrawler/web7.jpg)
![简介8](/home/yang/pylab/WebCrawler/web8.jpg)
*urllib2和urllib的区别：*
- urllib2可以接受一个Request类的实例来设置URL请求的headers，urllib仅可以接受URL。这意味着，你不可以伪装你的User Agent字符串等。
- urllib提供urlencode方法用来GET查询字符串的产生，而urllib2没有。这是为何urllib常和urllib2一起使用的原因。
- - -
++最简洁网页下载方法：++
```
# -*- coding: utf-8 -*-
#网络爬虫测试
import urllib2
#直接请求
response = urllib2.urlopen('http://www.baidu.com')
#获取状态码
print response.getcode()
cont = response.read()
print cont
```
++网页下载方法2：++
![简介9](/home/yang/pylab/WebCrawler/web9.jpg)
```
import urllib2
#下载器2：添加data，http header
#创建request对象：
request = urllib2.Request('http://www.baidu.com')
print request
#添加数据
# request.add_data('w')
print request.data
request.add_header('User-Agent', 'Mozilla/5.0')
response = urllib2.urlopen(request)
```
++网页下载方法3：++
![简介10](/home/yang/pylab/WebCrawler/web10.jpg)
```
import urllib2,cookielib
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
print cj
print response3.read()
```
- - -
**网页解析器**
![简介11](web11.jpg)
![简介12](web12.jpg)
++结构化解析：++
![简介13](web13.jpg)
*beautifulsoup模块：*
安装：`pip install beautifulsoup4`
语法：
![简介14](web14.jpg)
![简介15](web15.jpg)
```
from bs4 import BeautifulSoup
html_doc = open('../C++简历.html') #下载htnl文件或本地html文件，并将其赋给html_doc
# print html_doc
#根据html网页字符串创建beautifulsoup对象
soup = BeautifulSoup(
                     html_doc,#html文档字符串
                     'html.parser',#指定html文档解析器
                     from_encoding = 'utf8'#指定html文档编码
                     )
#搜索节点findall/find方法。参数包含节点名称，属性，字符串
#查找标签为‘xxx’的节点，传入‘xxx’名称
print soup.find_all(re.compile(r'.*img'))
link_node = soup.find_all('td',)
for links in link_node:
    print links.name,links.get_text()
```
- - -
##### 实例
> 爬取百度百科python词条相关1000个页面数据
* * *

###### 步骤
1、确定目标：确定抓取哪个网站的哪些网页的哪部分数据。本实例确定抓取百度百科python词条页面以及它相关的词条页面的标题和简介。
2、分析目标：确定抓取数据的策略。一是分析要抓取的目标页面的URL格式，用来限定要抓取的页面的范围；二是分析要抓取的数据的格式，在本实例中就是要分析每一个词条页面中标题和简介所在的标签的格式；三是分析页面的编码，在网页解析器中指定网页编码，才能正确解析。
3、编写代码：在解析器中会使用到分析目标步骤所得到的抓取策略的结果。
4、执行爬虫
- - -
###### 分析
![简介16](web16.jpg)
分析目标:
入口页面 ； URL 格式  ； 数据格式 ； 页面编码
![简介17](web17.jpg)
[代码入口](https://github.com/haugy/crawler_Example.git)
