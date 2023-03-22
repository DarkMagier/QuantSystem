from django.contrib import admin
from django.conf.urls import url
from Stock import views

urlpatterns = [
    url(r'^$',views.Stock_index),
    url(r'^getStockReport',views.getStockReport),
    url(r'^getStockHists',views.getStockHists),

]