from django.conf.urls import url
from Calculate import views

urlpatterns={
    url(r'^$', views.index),
    url(r'get_exchange_rate', views.get_exchange_rate),
}