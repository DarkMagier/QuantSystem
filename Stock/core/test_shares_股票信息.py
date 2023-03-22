import urllib.request
import os
import csv
from time import sleep

'''
加上下面的语句表示从头开始更新（不是从末尾再添加）
'''
'''
日：http://pdfm2.eastmoney.com/EM_UBG_PDTI_Fast/api/js?id=0000012&TYPE=k&js=fsData1521813934561((x))&rtntype=5&isCR=false&fsData1521813934561=fsData1521813934561
周：http://pdfm2.eastmoney.com/EM_UBG_PDTI_Fast/api/js?id=0000012&TYPE=wk&js=fsData1521813884903((x))&rtntype=5&isCR=false&fsData1521813884903=fsData1521813884903
月：http://pdfm2.eastmoney.com/EM_UBG_PDTI_Fast/api/js?id=0000012&TYPE=mk&js=fsData1521813903987((x))&rtntype=5&isCR=false&fsData1521813903987=fsData1521813903987

headers = ['代码','股票','价格','振幅','日期']
with open('rates.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
'''



codes = []
shares = []
time=[]
prices=[]
rate=[]

'''
日：http://pdfm.eastmoney.com/EM_UBG_PDTI_Fast/api/js?rtntype=5&cb=jQuery172011421335433425495_1521623465806&id=0000022&type=k&_=1521623526194
'''

k=1695 #code ++

while True:
    k+=1
    sleep(1)
    print(k)
    signal_break=0
    url_1="http://pdfm2.eastmoney.com/EM_UBG_PDTI_Fast/api/js?id="
    str_k=str(k)
    url_code=str_k.zfill(6) #satisfy share's code rules
    url_2="2&TYPE=k&js=fsData1521814275942((x))&rtntype=5&isCR=false&fsData1521814275942=fsData1521814275942"
    url=url_1+url_code+url_2
    
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    req = urllib.request.Request(url=url, headers=headers)  
    response=urllib.request.urlopen(req)
    html=response.read().decode('utf-8')
    


    shares_f=html.find('name":"')
    shares_t=html.find('",',shares_f)  
    print (html[shares_f+7:shares_t])
    shares.insert(k,html[shares_f+7:shares_t])
    share=html[shares_f+7:shares_t]

    
    codes_f=html.find('code":')
    codes_t=html.find('",',codes_f)  
    print (html[codes_f+7:codes_t])
    codes.insert(k,html[codes_f+7:codes_t].zfill(6))
    code=html[codes_f+7:codes_t].zfill(6)
    
    time_f=html.find('2015-',0)
    time_t=html.find(',',time_f)      

    if time_f==-1:
        time_f=html.find('2016-',0)
        time_t=html.find(',',time_f)

    if time_f==-1:
        time_f=html.find('2017-',0)
        time_t=html.find(',',time_f)
        
    if time_f==-1:
        time_f=html.find('2018-',0)
        time_t=html.find(',',time_f)  
    
    location=time_f
    j=0 #to make the all arrays have the write codes and share's name 


    while True:

        if shares_f==-1:
            break
        if time_f==-1:
            break
        i=0
        
        time_f=html.find('"',location-1)
        time_t=html.find(',',time_f)      
        #print (html[time_f+1:time_t])
        time.append(html[time_f+1:time_t])

        location=html.find(",",location+1)

        price_f=html.find(',',location+1)
        price_t=html.find(',',price_f+1)      
        #print (html[price_f+1:price_t])
        prices.append(html[price_f+1:price_t])
        
        location=price_t+2
        
        
        
        for i in range(4):
            location=html.find(",",location+1)
            i+=1;
        location=location-1

        rate_f=html.find(',',location)
        rate_t=html.find(',',rate_f+1)      
        #print (html[rate_f+1:rate_t-2])
        rate.append(html[rate_f+1:rate_t-2])

        
        location=rate_t+2

        '''
        if j!=0:
            if prices[j]<prices[j-1]:
                rate[j]=float(rate[j])-2*float(rate[j])
        '''
        


        row = ['*'+code,share,prices[j],rate[j],time[j]]


        if time[j]=="2018-04-12":
            break
        
        with open('rates.csv','a',newline = "") as f:
            f_csv = csv.writer(f)
            f_csv.writerow(row)
        
        j+=1
        







    
        

 

    















        
