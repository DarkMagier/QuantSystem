from django.conf.urls import url
from Core import views

urlpatterns={
    url(r'^{index.html\w+}|$', views.index),
}