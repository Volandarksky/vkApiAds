# coding: utf8
from django.shortcuts import render
from .forms import *

# Create your views here.
def get_token(request):

    form = DataForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data['api_id'])

        api_id = data['api_id']


    return render(request, 'get_token/get_token.html', locals())
