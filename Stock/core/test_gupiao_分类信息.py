import urllib.request
import os
import csv
from time import sleep
import requests
'''
加上下面的语句表示从头开始更新（不是从末尾再添加）
'''
headers = ['代码','股票','分类']
with open('classification.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)

k=0
i=0
codes = [] #股票代码
shares = [] #股票名称
classifications = []#分类
while True:
    k+=1
    # url_1="http://data.eastmoney.com/report/hyyl,"
    # str_k=str(k)
    # url_code=str_k.zfill(6)
    # url_2="_1.html"
    # url=url_1+url_code+url_2
    import requests

    url = """http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=0000352&sty=DCRRB&st=z&sr=&p=&ps=&cb=&js=var%20zjlx_hq%20=%20{%22quotation%22:[(x)]}&token=3a965a43f705cf1d9ad7e1a3e429d622&rt=51034666"""

    url="http://data.eastmoney.com/report/hyyl,%s_1.html"%(str(k).zfill(6))
    print(url)
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    req = urllib.request.Request(url=url, headers=headers)  
    response=urllib.request.urlopen(req)
    html=response.read().decode('gbk')

    codes_f=html.find('<li style="width: 170px;">',1)
    codes_t=html.find('研报明细',codes_f)
    print (html[codes_f+26:codes_t-8])
    shares.append(html[codes_f+26:codes_t-8])
    print (html[codes_t-7:codes_t-1])
    codes.append(html[codes_t-7:codes_t-1].zfill(6))
    
    
    classifications_f=html.find('<li style="width: 130px;">',1)
    classifications_t=html.find('研报</li>',classifications_f)      
    print (html[classifications_f+26:classifications_t])
    classifications.append(html[classifications_f+26:classifications_t])
    
    
    row = ['*'+codes[i],shares[i],classifications[i]]

    with open('classification.csv','a',newline = "") as f:
        f_csv = csv.writer(f)
        f_csv.writerow(row)

    i+=1
