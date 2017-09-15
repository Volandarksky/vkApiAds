# coding: utf8
import pickle
import json
import time
import vk

session = vk.Session(access_token='ad37dfae6dbdc3302e4732e')
vk_api = vk.API(session)

def getId (_name, _day, _month):
    bdList = vk_api.users.search(q=_name, count=100, city=123, age_from=15, age_to=40, birth_day=_day, birth_month=_month)

    # массив со всеми id именинников
    i=1
    fr_id = []
    bd_id = []
    while i<len(bdList):
        # print bdList[i]['uid']
        fr_list = vk_api.friends.get(user_id=bdList[i]['uid'])
        fr_id.extend(fr_list)
        bd_id.append(bdList[i]['uid'])
        i+=1
        time.sleep(0.33)

    data = {'name': _name,'bd_id': bd_id, 'fr_id': fr_id}
    dataJson = json.dumps(data, separators=(',',':'))
    fileName = 'data'+_name+'.json'
    file = open(fileName, 'w')
    file.write(dataJson)
    file.close()
    # print data

names = ['Vladimir', 'Dmitry', 'Alexander', 'Viktor', 'Evgeny', 'Elena', 'Ekaterina', 'Natalya', 'Anna', 'Svetlana']

try:
    for i in range(len(names)):
        getId(names[i], 12, 8)

        print('uids:'+names[i]+' created')
        time.sleep(1)
        i+=1
except RuntimeError:
    print('Ой! Надо подождать несколько секунд, скоро продолжим')
    for t in range(11):
        print(i)
        time.sleep(1)
        i+=1
    print('Продолжаем')

# for i in range(len(names)):
#     getId(names[i], 12, 8)
#
#     print('uids:'+names[i]+' created')
#     time.sleep(1)
#     i+=1
