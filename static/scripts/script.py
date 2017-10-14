# coding: utf8
import pickle
import json
import time
import vk

def getting_userInfo(_id):
    session = vk.Session()
    vk_api = vk.API(session)

    user_info = vk_api.users.get(user_id=_id)
    return user_info

def getting_usersId (_name, _day, _month, _token):
    session = vk.Session(access_token=_token)
    vk_api = vk.API(session)

    bdList = vk_api.users.search(q=_name, count=100, city=123, age_from=15, age_to=40, birth_day=_day, birth_month=_month)

    # массив со всеми id именинников
    i=1
    fr_id = []
    bd_id = []
    while i<len(bd_list):
        # print bd_list[i]['uid']
        fr_list = vk_api.friends.get(user_id=bd_list[i]['uid'])
        fr_id.extend(fr_list)
        bd_id.append(bd_list[i]['uid'])
        i+=1
        time.sleep(0.33)

    data = {'name': _name,'bd_id': bd_id, 'fr_id': fr_id}
    dataJson = json.dumps(data, separators=(',',':'))
    # fileName = 'data'+_name+'.json'
    # file = open(fileName, 'w')
    # file.write(dataJson)
    # file.close()
    # print data
    return dataJson

def create_campagian(_accId, _camType, _camName, _camDayLimit, _camAllLimit, _startTimeDay, _startTimeMonth, _startTimeYear, _stopTimeDay, _stopTimeMonth, _stopTimeYear, _camStatus):
    unixStartTime = time.mktime(time.strptime(''+str(_startTimeDay)+'/'+str(_startTimeMonth)+'/'+str(_startTimeYear)+'', "%d/%m/%Y"))

    unixStopTime = time.mktime(time.strptime(''+str(_stopTimeDay)+'/'+str(_stopTimeMonth)+'/'+str(_stopTimeYear)+'', "%d/%m/%Y"))

    _camData = {'type':_camType,
                'name':_camName,
                'day_limit':_camDayLimit,
                'all_limit':_camAllLimit,
                'start_time':unixStartTime,
                'stop_time':unixStopTime,
                'status':_camStatus
                }

    campagianId = vk_api.ads.createCampaigns(account_id=_accId, data=_camData)
    return campagianId

def create_campagian_unixTime(_accId, _camType, _camName, _camDayLimit, _camAllLimit, _unixStartTime, _unixStopTime, _camStatus):
    # unixStartTime = time.mktime(time.strptime(''+str(_startTimeDay)+'/'+str(_startTimeMonth)+'/'+str(_startTimeYear)+'', "%d/%m/%Y"))
    #
    # unixStopTime = time.mktime(time.strptime(''+str(_stopTimeDay)+'/'+str(_stopTimeMonth)+'/'+str(_stopTimeYear)+'', "%d/%m/%Y"))

    _camData = {'type':_camType,
                'name':_camName,
                'day_limit':_camDayLimit,
                'all_limit':_camAllLimit,
                'start_time':_unixStartTime,
                'stop_time':_unixStopTime,
                'status':_camStatus
                }

    campagianId = vk_api.ads.createCampaigns(account_id=_accId, data=_camData)
    return campagianId

def create_ADS (_accId, _camId, _adFormat, _costType, _cpc, _ageR, _status, _title, _sex, _retargeting_groups):

    _adsData = [{'campaign_id':_camId,
                'ad_format':_adFormat,
                'cost_type':_costType,
                'cpc':_cpc,
                'age_restriction':_ageR,
                'status':_status,
                'name':_title + _sex,
                'title':_title,
                'sex':_sex,
                'retargeting_groups':_retargeting_groups}]

    vk_api.users.search(account_id=_accId, data=_adsData)

# names = ['Vladimir', 'Dmitry', 'Alexander', 'Viktor', 'Evgeny', 'Elena', 'Ekaterina', 'Natalya', 'Anna', 'Svetlana']
#
# try:
#     for i in range(len(names)):
#         getId(names[i], 12, 8)
#
#         print('uids:'+names[i]+' created')
#         time.sleep(1)
#         i+=1
# except RuntimeError:
#     print('Ой! Надо подождать несколько секунд, скоро продолжим')
#     for t in range(11):
#         print(i)
#         time.sleep(1)
#         i+=1
#     print('Продолжаем')
