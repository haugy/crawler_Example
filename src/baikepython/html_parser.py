# -*- coding: utf-8 -*-
'''
Created on 2017-9-9

@author: yang
'''
from bs4 import BeautifulSoup
import re
import urlparse


class HtmlParser(object):
    
    
    def parse_new_url(self, page_url, soup):
        '''
        输入：网页url地址，soup对象
        功能：解析出新的url
        返回值：新网页urls(set类型)
        百度百科url格式：<a target="_blank" href="/item/GPL">GPL</a>
        '''
        new_urls = set()
        links_url = soup.find_all('a', href = re.compile(r'/item/'))
#         print '匹配成功'
        for link in links_url:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
#             print new_full_url
            new_urls.add(new_full_url)
#         print 'url解析成功'
        return new_urls
    
    def parse_new_data(self, page_url, soup):
        '''
        输入：网页url地址，soup对象
        功能：解析出新的网页数据
        返回值：新的数据值new_data
        title格式：
            <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
            <div class="lemma-summary" label-module="lemmaSummary">
        
        '''
        res_data = {}
        res_data['url'] = page_url
        title_node = soup.find('dd', class_ = 'lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()
#         print res_data['title']
        
        summary_node = soup.find('div', class_ = 'lemma-summary')
        res_data['summary'] = summary_node.get_text()
#         print res_data['summary']
#         print '数据解析成功'
        return res_data
    
    
    def parse(self, page_url, html_cont):
        '''
        网页解析器
        输入：网页url，网页文档字符串
        功能：从html_cont中解析新的url列表和数据
        返回值：（new_urls, new_data）
        '''
        if page_url is None or html_cont is None:
            return
#         print 'parse start'
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self.parse_new_url(page_url, soup)
        new_data = self.parse_new_data(page_url, soup)
#         print 'parse finish'
        return new_urls, new_data
    
    



