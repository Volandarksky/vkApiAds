# coding: utf8
from django.shortcuts import render
from .forms import *

from .script import create_campagian_unixTime

# Create your views here.
def campagians(request):

    form = DataForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data)

        account_id = data['account_id']
        cam_type = data['cam_type']
        name = data['name']
        day_limit = data['day_limit']
        all_limit = data['all_limit']
        start_time = data['start_time']
        stop_time = data['stop_time']
        status = data['status']
        token = data['token']

        print(account_id)
        print(start_time)

        campagian_id = create_campagian_unixTime(account_id, cam_type, name, day_limit, all_limit, start_time, stop_time, status, token)

    return render(request, 'campagians/campagians.html', locals())
