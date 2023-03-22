import urllib.request
import os
import csv
from time import sleep


'''
第三页
http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=GGSR&js=var%20GIfmZeyC={%22data%22:[(x)],%22pages%22:%22(pc)%22,%22update%22:%22(ud)%22,%22count%22:%22(count)%22}&ps=25&p=3&code=000001&rt=50721427
第四页
http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=GGSR&js=var%20kpHNbYEU={%22data%22:[(x)],%22pages%22:%22(pc)%22,%22update%22:%22(ud)%22,%22count%22:%22(count)%22}&ps=25&p=4&code=000001&rt=50721431
50714374 50714400  50714403  50718698
http://data.eastmoney.com/report/000001.html
50718478 
'''

'''
url_first="http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=GGSR&js=var%20tUwqJDeL={%22data%22:[(x)],%22pages%22:%22(pc)%22,%22update%22:%22(ud)%22,%22count%22:%22(count)%22}&ps=25&p=2&code=000001&rt="
url=url_first+'50714300'


page1:
http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=GGSR&js=var%20tUwqJDeL={%22data%22:[(x)],%22pages%22:%22(pc)%22,%22update%22:%22(ud)%22,%22count%22:%22(count)%22}&ps=25&p=2&code="
page2:
http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=GGSR&js=var%20SKDTXIZg={%22data%22:[(x)],%22pages%22:%22(pc)%22,%22update%22:%22(ud)%22,%22count%22:%22(count)%22}&ps=25&p=3&code=000001&rt=50718704
page2:http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=GGSR&js=var%20mBSLCIIi={%22data%22:[(x)],%22pages%22:%22(pc)%22,%22update%22:%22(ud)%22,%22count%22:%22(count)%22}&ps=25&p=2&code=000001&rt=50718708

page3:http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=GGSR&js=var%20ocBoqPHV={%22data%22:[(x)],%22pages%22:%22(pc)%22,%22update%22:%22(ud)%22,%22count%22:%22(count)%22}&ps=25&p=3&code=000001&rt=50718707
page5:http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=GGSR&js=var%20GYuKXEfU={%22data%22:[(x)],%22pages%22:%22(pc)%22,%22update%22:%22(ud)%22,%22count%22:%22(count)%22}&ps=25&p=5&code=000001&rt=50718712
'''

'''
3:http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=GGSR&js=var%20EQhJvOQw={%22data%22:[(x)],%22pages%22:%22(pc)%22,%22update%22:%22(ud)%22,%22count%22:%22(count)%22}&ps=25&p=3&code=000001&rt=50727159
4:http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=GGSR&js=var%20BnsqEYbZ={%22data%22:[(x)],%22pages%22:%22(pc)%22,%22update%22:%22(ud)%22,%22count%22:%22(count)%22}&ps=25&p=4&code=000001&rt=50727160
'''


'''
加上下面的语句表示从头开始更新（不是从末尾再添加）

headers = ['代码','股票','卷商','意见','改变','日期']
with open('shares.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
'''

j=300000
k=0



while True:
    
    j+=1
    k=0
    signal_exceed=0 #用来测试是否超页
    data_exceed="" #一个卷商不会在一天发布两个信息
    shares_exceed=""
    signal_exceed_break=0 #跳出信号
    signal_wrong=0#错误信号 该股票不存在
    while True:
        k+=1
        url_1="http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=GGSR&js=var%20VKHGSAnl={%22data%22:[(x)],%22pages%22:%22(pc)%22,%22update%22:%22(ud)%22,%22count%22:%22(count)%22}&ps=25&p="
        url_page=str(k)
        url_2="&code="
        
        str_j=str(j)
        url_code=str_j.zfill(6) #satisfy share's code rules
        url_3="&rt="
        url_final="50727159"
        url=url_1+url_page+url_2+url_code+url_3+url_final
        
        print(url)
        print(url_code)
        print(url_page)
        
        #sleep(3)

        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        req = urllib.request.Request(url=url, headers=headers)  
        response=urllib.request.urlopen(req)
        html=response.read().decode('utf-8')
        codes = [] #股票代码
        shares = [] #股票名称
        name = []  #卷商名称
        change = [] #改变意见
        rate = [] #评级
        data = [] #日期
        i=0

        '''
        print("现在的j与k:")
        print(j)
        print(k)
        print(data_exceed)
        print(shares_exceed)
        sleep(1)
        '''
                
        location=0
        while True:
            name_f=html.find('insName',location)
            name_t=html.find('",',name_f)
            if name_f == -1:#two conditions:one is the page ends, the other is that the url wrong
                if k==1:
                    if signal_wrong==0:
                        signal_exceed_break=1
                break
            signal_wrong=1
            print (html[name_f+10:name_t])
            name.append (html[name_f+10:name_t])

            change_f=html.find('"change":"',location)
            change_t=html.find('",',change_f)      
            print (html[change_f+10:change_t])
            change.append(html[change_f+10:change_t])

            rate_f=html.find('rate":"',location)
            rate_t=html.find('",',rate_f)      
            print (html[rate_f+7:rate_t])
            rate.append(html[rate_f+7:rate_t])

            data_f=html.find('datetime":',location)
            data_t=html.find('",',data_f)  
            print (html[data_f+11:data_t-9])
            data.append(html[data_f+11:data_t-9])

            shares_f=html.find('secuName":',location)
            shares_t=html.find('",',shares_f)  
            print (html[shares_f+11:shares_t])
            shares.append(html[shares_f+11:shares_t])

            codes_f=html.find('secuFullCode":',location)
            codes_t=html.find('",',codes_f)  
            print (html[codes_f+15:codes_t-3])
            codes.append(html[codes_f+15:codes_t-3].zfill(6))
            
            if signal_exceed == 0:
                '''
                print(data[i])
                print(shares[i])
                print("data_exceed")
                print(data_exceed)
                print("share_exceed")
                print(shares_exceed)
                print("data[i]")
                print(data[i])
                print("name[i]")
                print(name[i])
                sleep(5)
                '''
                if str(data_exceed) == str(data[i]):
                    if str(shares_exceed) == str(name[i]):
                        signal_exceed_break=1
                        signal_exceed=1
                        break
                data_exceed=html[data_f+11:data_t-9]
                shares_exceed=html[name_f+10:name_t]
                signal_exceed=1
            

            
            print ()
            row = ['*'+codes[i],shares[i],name[i], rate[i],change[i],data[i]]

            
            with open('shares.csv','a',newline = "") as f:
                f_csv = csv.writer(f)
                f_csv.writerow(row)
            
                
            i+=1
            location=rate_t+2
        if signal_exceed_break==1:
            signal_exceed=0
            break
        signal_exceed=0
        
    


'''

print(html)
'''

