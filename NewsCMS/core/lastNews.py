import tushare as ts
import os,django
import time
import hashlib
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "QuantSystem.settings")
django.setup()
from NewsCMS import models
# from Search.inverted_index.inverted_index import Inverted_Index
def updateNews():
    last_news_pandas=ts.get_latest_news(top=21,show_content=True)
    year = time.strftime('%Y')
    print(type(last_news_pandas))
    for index,row in last_news_pandas.iterrows():
        news_update_dict=dict(row)
        # hashid=hashlib.md5(news_update_dict['title'].encode()).hexdigest()
        news_update_dict['hashid']=hashlib.md5(news_update_dict['title'].encode()).hexdigest()
        news_update_dict['time']=year+'-'+news_update_dict['time']
        # print(type(hashid),hashid)
        try:
            obj=models.lastNews.objects.create(**news_update_dict)
        except Exception as e:
            print(e)

            # print(year,news_update_dict['time'])
    # obj.save()

def getNews():
    res = models.lastNews.objects.filter().order_by('-id')[0:10]
    res = [x.to_json() for x in res]
    print(res)

def saveNews():
    last_news_pandas = ts.get_latest_news(top=10, show_content=True)
    last_news_pandas.to_csv('News.csv', encoding='utf-8')
def marked():
    l=models.lastNews.objects.first()
    # print(l.mark())




if __name__=='__main__':
    # marked()
    updateNews()
    # getNews()
    # saveNews()