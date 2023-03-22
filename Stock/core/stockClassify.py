import tushare as ts
import os,django
import time
import hashlib
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "QuantSystem.settings")
django.setup()
from Stock import models
# df=ts.get_stock_basics()
# print(df.head())
# print(ts.get_latest_news()) #默认获取最近80条新闻数据，只提供新闻类型、链接和标题
# print(ts.get_latest_news(top=20,show_content=True)) #显示最新5条新闻，并打印出新闻内容
# print(ts.get_notices(code='000001'))
# print(ts.guba_sina())
# print(ts.get_realtime_quotes(df['code'].tail(10)))
# print(ts.get_zz500s())

# print(pd['distrib'])
def spiderNews(year,season):
    pd=ts.get_report_data(year, season)
    print(pd[4])
    pd.to_csv('stockReport.csv', encoding='utf-8')

def updateNews():
    year=2014
    season=2

    # year = time.strftime('%Y')
    # print(type(last_news_pandas))
    data_list=[]
    with open('stockReport.csv','r',encoding='utf-8')as f:

        for lines in f.readlines():
            data_split_ori=lines.split(',')
            data_split=[]
            for item in data_split_ori:
                data_split.append(item.strip())
            del(data_split[0])
            # data_split.remove(data_split.index(0))
            data_list.append(data_split)
            # news_update_dict=dict(row)
            # # hashid=hashlib.md5(news_update_dict['title'].encode()).hexdigest()
            # news_update_dict['season']="%d-%d"%(year,season)
            # # print(type(hashid),hashid)
            # try:
            #     obj=models.stockReport.objects.create(**news_update_dict)
            # except Exception as e:
            #     print(e)

            # print(year,news_update_dict['time'])
    # obj.save()
    # print(len(data_list))
    data_head=data_list[0]
    print(data_head)
    # data_head[data_head.index("eps")]="esp_num"
    print(data_list)
    del(data_list[0])
    # print(data_list)
    data_dict=dict()
    # print(len(data_list))
    print(data_head)
    for item in data_list:
        # print(item)
        # print(len(item))
        for i in range(0,11):
            data_dict[data_head[i]]=item[i]
            data_dict['season'] = "%d-%d" % (year, season)
            # print(data_dict)
        # if data_dict['code']=='600606':
            # print(data_dict)
            # del data_dict['name']
            #
            # # data_dict['code'] = models.stockBasics.objects.filter(code=data_dict['code']).first()
            # data_dict['code'] = models.stockBasics.objects.filter(code=data_dict['code']).first()
            # del data_dict['code']

        try:
            obj=models.stockReport.objects.create(**data_dict)
        except Exception as e:
            print("**********")
            print(data_dict)
            print(e)
            print('\n\n')
    # print(data_list)
def getNews():
    res = models.stockReport.objects.filter().order_by('-id')[0:10]
    # res = [x.to_json() for x in res]
    print(res)
if __name__=='__main__':
    # spiderNews(2014,2)
    updateNews()
    # getNews()