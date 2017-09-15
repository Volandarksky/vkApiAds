from django.conf.urls import include, url
from django.contrib import admin
from friendsId import views

urlpatterns = [
    url(r'^friendsId/$', views.friendsId, name="friendsId"),
]
