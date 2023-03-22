from django.shortcuts import render
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from NewsCMS import models
import json
# Create your views here.

def News_index(request):
    return render(request,"news_index.html")

def getLastNews(request):
    page_index=int(request.GET.get('page',None))
    # print(page_index)
    max=5
    l=(page_index-1)*max;
    r=l+max
    print(l,r)
    res = models.lastNews.objects.filter().order_by('-id')[l:r]
    res = [ x.to_dict(150) for x in res]
    return HttpResponse(json.dumps(res))

def read_news(request,name=None):
    print(name)
    news=models.lastNews.objects.filter(id=name).first()
    news=news.to_dict()
    return render(request,'news_read.html',{'news':news})