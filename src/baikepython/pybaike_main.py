# -*- coding: utf-8 -*-
'''
Created on 2017-9-9
pybaike_main (爬虫总调度程序) 
url_manager(url管理器)  
html_down(下载器)
html_parser(html解析器)  
html_outputer(将数据处理好的数据写出到 html 的页面)
@author: yang
'''
from baikepython import url_manager, html_down, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        '''
        SpiderMain初始化
        添加self.urls属性，初始化为UrlManager()类
        添加self.downloader属性，初始化为HtmlDownload()类
        添加self.parser属性，初始化为HtmlParser()类
        添加self.outputer属性，初始化为HtmlOutput()类
        '''
        self.urls = url_manager.UrlManager()
        self.downloader = html_down.HtmlDownload()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutput()
    
    def craw(self, root_url):
        '''
        定义craw方法：
        输入：入口url
        过程：
            添加入口url到urls属性
            判断是has_new_url():
            获取新url，get_new_url()方法
            下载new_url到html_cont，download()方法，
            解析出new_urls,new_data,parse()方法
            添加新的url到urls属性中，add_new_urls()方法
            使用outputer.collect_data()方法收集新数据
            try:+except:加入异常处理
            最后循环结束，使用outputer.output_html()方法输出到html
        '''
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' %(count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                
                if count == 1000:
                    break
                count = count + 1
            except:
                print 'craw failed'

        self.outputer.output_html()
            
    
    

if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/Python'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)