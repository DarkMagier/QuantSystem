from django.contrib import admin
from django.conf.urls import url
from Index import views
urlpatterns={
    url(r'^{index.html\w+}|$',views.index),

}