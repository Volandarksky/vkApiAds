from django.conf.urls import include, url
from django.contrib import admin
from user_info import views

urlpatterns = [
    url(r'^$', views.user_info, name='user_info'),
    # url(r'^user_info/$', views.user_info, name="user_info"),
]
