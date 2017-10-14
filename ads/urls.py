from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('friendsId.urls')),
    url(r'^', include('campagians.urls')),
    url(r'^', include('user_info.urls')),
    url(r'^', include('get_token.urls')),
]
