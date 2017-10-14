from django.conf.urls import include, url
from django.contrib import admin
from get_token import views

urlpatterns = [
    url(r'^get_token/$', views.get_token, name="get_token"),
]
