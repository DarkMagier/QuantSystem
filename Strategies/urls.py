from django.conf.urls import url
from Strategies import views

urlpatterns={
    url(r'^$', views.index),
    url(r'^runSript', views.runSript),
    url(r'^createScript', views.createScript),
    url(r'^getScriptList$', views.getScriptList),
    url(r'^saveStrategy', views.saveStrategy),
    url(r'^getScript$', views.getScript),
    url(r'^deleteScript$', views.deleteScript),
}