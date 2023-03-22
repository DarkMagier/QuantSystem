
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
import json
from django.http import request
import pandas as pd
# Create your views here.
from Stock import models
def Stock_index(request):
    return render(request,"DashBoard.html")

def getStockReport(request):
    page_index=int(request.GET.get('page',None))
    # print(page_index)
    max=10
    l=(page_index-1)*max;
    r=l+max
    print(l,r)
    res = models.stockReport.objects.filter()[l:r]
    res = [ x.to_dict() for x in res]
    return HttpResponse(json.dumps(res))

def getStockHists(request):
    stockCode=request.GET.get('stockCode',None )
    stockDocName="%s.csv"%(stockCode)
    stockHists=pd.read_csv('./Stock/core/codeHistDatas/%s'%(stockDocName))
    # print(stockHists)
    stockHists=stockHists.to_dict()
    stockInfo=models.stockReport.objects.filter(code=stockCode).values('code','name').first()
    stockHists.update(stockInfo)
    return HttpResponse(json.dumps(stockHists))