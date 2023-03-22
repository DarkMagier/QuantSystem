from django.contrib import admin
from django.conf.urls import url
from NewsCMS import views

urlpatterns = [
    url(r'^$',views.News_index),
    url(r'getLastNews',views.getLastNews),
    url(r'([0-9]+).html',views.read_news)

]