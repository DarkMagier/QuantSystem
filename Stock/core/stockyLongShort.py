import tushare as ts
import os,django
import time
import hashlib
import json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "QuantSystem.settings")
django.setup()
# pd=ts.get_hist_data('sh')
from Stock import models
def getStockCode():
    queryset=models.stockReport.objects.values('code')

    resultList=[x['code'] for x in queryset]

    print(resultList)
    with open('stockCode.json','w')as f:

        json.dump(resultList,f)

def getStockHist():
    with open('stockCode.json','r')as f:
        stockCodes=json.load(f)
    stockHistData_dicts=dict()
    for stockCode in stockCodes:
        stockHistData_pd=ts.get_hist_data(stockCode)
        print(stockHistData_pd)
        stockHistData_pd.to_csv('.\codeHistDatas\%s.csv'%(stockCode),encoding='utf-8')
if __name__=='__main__':
    # getStockCode()
    # pd=ts.get_hists()
    # pd.to_csv('stockHist.csv',encoding='utf-8')
    getStockHist()