# coding: utf8
from django.shortcuts import render
from .forms import *

from .script import getting_userInfo

def user_info(request):

    form = IdForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["user_id"])

        user_information = getting_userInfo(data["user_id"])
        # user_info = repr(user_info1).decode("unicode_escape")
        user_name = user_information[0][u'first_name']
        user_lastName = user_information[0][u'last_name']
        # print(user_information)

    return render(request, 'user_info/user_info.html', locals())
