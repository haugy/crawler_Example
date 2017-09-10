# -*- coding: utf-8 -*-
'''
Created on 2017-9-9
提供url管理器两种存储网页的属性self.new_urls,self.old_urls
提供网页管理方法：add_new_url，add_new_urls,has_new_url,get_new_url
@author: yang
'''


class UrlManager(object):
    
    def __init__(self):
        '''
        类属性初始化
        将new_urls,old_urls属性设置为set()表，set不存在重复元素，元素无序
        '''
        self.new_urls = set()
        self.old_urls = set()
    
    def add_new_url(self, url):
        '''
        输入：root_url
        功能:向url管理器中添加新url
        '''
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
        

    def add_new_urls(self, urls):
        '''
        输入：new_urls
        功能:向url管理器中添加批量url
        '''
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)
    
    def has_new_url(self):
        '''
        输入：无
        功能:判断url管理器中是否有新url待爬取
        返回值：bool型
        '''
        return len(self.new_urls) != 0

    
    def get_new_url(self):
        '''
        输入：无
        功能:从url管理器中获取一个待爬取新url
        返回值：new_urls中的一个新的url
        '''
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    

    
    
    
    
    
    
    
    



