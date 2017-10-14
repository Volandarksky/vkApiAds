# coding: utf8
import pickle
import json
import time
import vk
from django.shortcuts import render
from .forms import *

# from .script import getting_usersId

def friendsId(request):

    form = DataForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        # print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        token = data["token"]
        name = data["user_name"]
        day = data["bd_day"]
        month = data["bd_month"]
        print(token)

        result = getting_usersId(name, day, month, token)
        users_id = result['bd_id']
        friends_id = result['friends_id']
        # users_id = []
        # for i in range(4):
        #     users_id.append(result[i+1]['uid'])

        # result = data

    return render(request, 'friendsId/friendsId.html', locals())


def getting_usersId (_name, _day, _month, _token):
    session = vk.Session(access_token=_token)
    vk_api = vk.API(session)

    bd_list = vk_api.users.search(q=_name, count=100, city=123, age_from=15, age_to=40, birth_day=_day, birth_month=_month)

    # массив со всеми id именинников
    i=1
    friends_id = []
    bd_id = []
    while i<len(bd_list):
        # print bd_list[i]['uid']
        fr_list = vk_api.friends.get(user_id=bd_list[i]['uid'])
        friends_id.extend(fr_list)
        bd_id.append(bd_list[i]['uid'])
        i+=1
        time.sleep(0.33)

    data = {'name': _name,'bd_id': bd_id, 'friends_id': friends_id}
    dataJson = json.dumps(data, separators=(',',':'))
    # fileName = 'data'+_name+'.json'
    # file = open(fileName, 'w')
    # file.write(dataJson)
    # file.close()
    # print data
    return data
