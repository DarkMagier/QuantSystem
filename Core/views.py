from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from QuantSystem.settings import URL_LOGIN
# Create your views here.

def index(request):
    nickname=request.session.get('nickname')

    return render(request, "core.html", {'nickname':nickname})
