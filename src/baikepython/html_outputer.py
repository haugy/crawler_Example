# -*- coding: utf-8 -*-
'''
Created on 2017-9-9
collect_data方法收集数据
output_html发给法将数据输出到html文件
@author: yang
'''


class HtmlOutput(object):
    
    def __init__(self):
        #构建列表维护收集的数据
        self.datas = []
    
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    
    def output_html(self):
        '''
        功能：将数据用列表形式写在html中
        '''
        fout = open('output.html', 'w')
        
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')
        
        #ascii 改为utf-8编码 encode('utf-8')
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>'%data['url'])
            fout.write('<td>%s</td>'%data['title'].encode('utf-8'))
            fout.write('<td>%s</td>'%data['summary'].encode('utf-8'))
            fout.write('</tr>\n')
        
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        
        fout.close()
    
    
    
    



