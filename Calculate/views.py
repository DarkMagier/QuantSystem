from django.shortcuts import render,HttpResponse
from Calculate.core import exchang_rate
import json
# Create your views here.

def index(request):

    return render(request,"calculate_index.html")

def get_exchange_rate(request):
    ex_rate = exchang_rate.get_exchange_rate()
    # print(ex_rate)
    # resp=ex_rate[13:-1]
    return HttpResponse(json.dumps(ex_rate))