from django.contrib import admin
from django.conf.urls import url,include
from Search import views

urlpatterns = [
    url(r'^$',views.Search_index),
    url(r'^search', views.Search_index)

]