from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.http import request
from django.contrib.auth import authenticate,login as d_login,logout as d_logout
import json
# Create your views here.
from  UserRegisters.models import User
import time,random
def login(request):
    user=request.POST.get('user',None)
    pwd=request.POST.get('pwd',None)

    user_dict={
        'username':user,
        'password':pwd
    }
    user=authenticate(username=user,password=pwd)
    print(user_dict)
    if user is not None :
        if user.is_active:
            d_login(request, user)
            request.session['uid']=user.uid
            request.session['nickname']=user.nickname
        # print()
            resp={"status":200,"url":"/Core"}
        else:
            resp = {"status": 404, "msg": "用户名或密码错误"}
    else:
        resp={"status":404,"msg":"用户名或密码错误！"}
    return HttpResponse(json.dumps(resp),request)

def Signup(request):
    if request.method=="GET":
        return render(request,"Signup.html")
    if request.method=='POST':
        try:
            user_dict=dict()
            for k,v in request.POST.items():
                print(k, v)
                if k !="csrfmiddlewaretoken":
                    user_dict[k]=v

            random.seed=time.time()
            uid = str(int(time.time() + random.random() * 10000000000))
            user_dict['uid']=uid
            print(user_dict)
            obj=User.objects.create_user(**user_dict)
            resp = {"status": 200, "msg": "注册成功！"}
            obj.save()
        except Exception as e:
            print(e)
            resp = {"status": 404, "msg": "注册失败！"}

    # print(request.POST)


    return HttpResponse(json.dumps(resp))

def Sign(request):
    return render(request,"Sign.html")

def Logout(request):
    d_logout(request)
    return HttpResponseRedirect('/')

def changePassword(request):
    if request.method=='GET':
        return render(request,"ChangePassword.html")
    elif request.method=='POST':

        obj=User.objects.update()
        pass

def changPersonalInfo(request):
    user_id=request.session.get('uid',None)

    if user_id==None:
        return HttpResponse("请先登录!")

    else:
        obj_dict=User.objects.filter(uid=user_id).first().to_dict()
        if request.method=='GET':
            # print(obj_dict)
            return render(request, "changePersonalInfo.html",{'user_dict':obj_dict})

        elif request.method=='POST':
            print("收到信息")
            form_data=request.POST
            form_dict=dict()
            for k,v in form_data.items():
                # print(k,v)
                form_dict[k]=v
            del form_dict['csrfmiddlewaretoken']
            # del form_dict['uid']
            print(form_dict)
            User.objects.filter(uid=user_id).update(**form_dict)
            return HttpResponse("修改成功！")

    # print(username_session)
