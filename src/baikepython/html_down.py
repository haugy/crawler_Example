# -*- coding: utf-8 -*-
'''
Created on 2017-9-9
提供网页下载方法download()
@author: yang
'''
import urllib2


class HtmlDownload(object):
    
    
    def download(self, url):
        '''
        输入：url
        功能：下载url的网页html
        返回值：下载的html字符串
        '''
        if url is None:
            return None
        
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            print url,'下载失败'
            return None
#         print '下载完成'
        return response.read()
        
    
    



