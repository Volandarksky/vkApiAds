# coding: utf8
from django import forms

class DataForm(forms.Form):
    # token = bd_day = forms.CharField(label='token')
    # user_name = forms.CharField(label='User name')
    # bd_day = forms.IntegerField(label='Day')
    # bd_month = forms.IntegerField(label='Month')

    account_id = forms.IntegerField(label='идентификатор рекламного кабинета')


    cam_type = forms.CharField(label='тип кампании')
    # тип кампании:
    # normal — обычная кампания, в которой можно создавать любые объявления, кроме записей в сообществе;
    # promoted_posts — кампания, в которой можно рекламировать только записи в сообществе.

    name = forms.CharField(label='название рекламной кампании')
    # строка длиной от 3 до 60 символов

    day_limit = forms.IntegerField(label='дневной лимит в рублях')
    # дневной лимит в рублях. положительное число

    all_limit = forms.IntegerField(label='общий лимит в рублях')
    # общий лимит в рублях.
    # положительное число

    start_time = forms.IntegerField(label='время запуска кампании')
    # время запуска кампании в формате unixtime.
    # положительное число

    stop_time = forms.IntegerField(label='время остановки кампании')
    # время остановки кампании в формате unixtime. положительное число

    status = forms.IntegerField(label='статус рекламной кампании')
    # статус рекламной кампании (1 — запущена, 0 — остановлена).
    # флаг, может принимать значения 0 или 1

    token = forms.CharField(label='Токен')
