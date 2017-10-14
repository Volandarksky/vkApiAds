# coding: utf8
from django import forms

class DataForm(forms.Form):
    api_id = forms.CharField(label='API ID Вашего приложения')
