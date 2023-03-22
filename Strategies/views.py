from django.shortcuts import render,HttpResponse
import json
from Strategies.models import userStrategies
import time,random
# Create your views here.
from Strategies.core.ipykernel import exec_script
def index(request):

    return render(request,'strategies_index.html')
def downloadScrip(request):
    pass
def deleteScript(request):
    scriptID = request.GET.get('id', None)
    userStrategies.objects.filter(id=scriptID).delete()
    return HttpResponse("删除成功!")
def getScript(request):
    scriptID=request.GET.get('id',None)
    if scriptID is not None:
        resp=userStrategies.objects.filter(id=scriptID).first()
        return HttpResponse(json.dumps(resp.to_dict()))
def saveStrategy(request):
    strategy=request.GET.dict()
    try:
        print(strategy)
        # del strategy['$$hashKey']
        del strategy['createTime']
        del strategy['lastEditTime']
        strategy_entity=userStrategies.objects.filter(id=strategy['id']).update(**strategy)
        # print(strategy_entity)
        # strategy_entity.update(strategy)
        # strategy_entity.save()

        res="保存成功！"
        print(res)
    except Exception as e:
        print(e)
        res=e

    return HttpResponse(res)
def createScript(request):
    uid=request.session.get('uid',None)
    strategy=userStrategies()
    strategy.id= str(int(time.time() + random.random() * 10000000000))
    strategy.strategyName="策略"+str(userStrategies.objects.filter(userid=uid).count()+1)
    # strategy.createTime=time.time()
    strategy.userid=uid
    # strategy.lastEditTime=strategy.createTime
    strategy.strategyScript="#请输入您的策略\n"

    strategy_dict=strategy.to_dict()
    userStrategies.objects.create(**strategy_dict).save()
    return HttpResponse(json.dumps(strategy_dict))
def getScriptList(request):
    uid=request.session.get('uid', None)
    res=userStrategies.objects.filter(userid=uid)[0:10]
    res_list=[]
    for item in res:
        res_list.append(item.to_dict(haveScript=False))
    return HttpResponse(json.dumps(res_list))
def editScript(request):
    strategy=userStrategies()
    strategy.id= str(int(time.time() + random.random() * 10000000000))
    strategy.strategyName="策略"+str(time.time().hex())
    strategy.createTime=time.time()
    strategy.userid=request.session.get('uid',None)
    strategy.lastEditTime=strategy.createTime
    strategy.strategyScript="#请输入您的策略\n"
    strategy.save()
    pass
def runSript(request):
    scriptOri=request.GET.get('strategyScript',None)
    scope={}
    print('将要运行的策略：',scriptOri)
    # dataDict={'res':'123'}
    # exec(scriptOri)
    res=exec_script(scriptOri)
    print("执行结果>>:",res)
    # print(a)

    # print(scope)

    # return HttpResponse(json.dumps(dataDict))
    return HttpResponse(json.dumps(res))