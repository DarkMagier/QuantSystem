from django.contrib import admin
from django.conf.urls import url
from UserRegisters import views

urlpatterns = [
    url(r'Login',views.login),
    url(r'Signup',views.Signup),
    url(r'^$',views.Sign),
    url(r'^Logout',views.Logout),
    url(r'^ChangePassword',views.changePassword),
    url(r'^ChangePersonalInfo',views.changPersonalInfo),
]