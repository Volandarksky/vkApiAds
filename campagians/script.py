# coding: utf8
import pickle
import json
import time
import vk

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

def create_campagian_unixTime(_accId, _camType, _camName, _camDayLimit, _camAllLimit, _unixStartTime, _unixStopTime, _camStatus, _token):
    session = vk.Session(access_token=_token)
    vk_api = vk.API(session)
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
