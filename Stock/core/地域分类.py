import tushare as ts
import pandas as pd
import numpy as np
def getBusinessClassify():
    BusinessClassify=ts.get_area_classified()
    BusinessClassify.to_csv('地域分类.csv',encoding='utf-8')
    return BusinessClassify

def loadBusinessClassify():
    f=open('地域分类.csv','r',encoding='utf-8')
    BusinessClassify=pd.read_csv(f,header=0,encoding='utf-8')
    return BusinessClassify
def uniqueClassify(BusinessClassify):
    classify=np.array(BusinessClassify['area']).tolist()
    classified=list(set(classify))
    print(classify)
    return classified

def updateClass(classified):
    import os, django

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "QuantSystem.settings")
    django.setup()
    from Stock.models import areaClass
    obj_list=[]
    for item in classified:

        obj=areaClass(className=item)
        obj_list.append(obj)
    areaClass.objects.bulk_create(obj_list)
    # print(obj)


if __name__=='__main__':
    # pd=getBusinessClassify()
    # print(pd)
    BusinessClassify=loadBusinessClassify()
    print(BusinessClassify)
    classified=uniqueClassify(BusinessClassify)
    print(classified)
    updateClass(classified)