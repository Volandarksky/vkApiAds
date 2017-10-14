from django.conf.urls import include, url
from django.contrib import admin
from campagians import views

urlpatterns = [
    url(r'^campagians/$', views.campagians, name="campagians"),
]
