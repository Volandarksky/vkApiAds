from django import forms

class DataForm(forms.Form):
    token = bd_day = forms.CharField(label='token')
    user_name = forms.CharField(label='Users name')
    bd_day = forms.IntegerField(label='Day')
    bd_month = forms.IntegerField(label='Month')
