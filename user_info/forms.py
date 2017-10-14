from django import forms

class IdForm(forms.Form):
    user_id = forms.IntegerField(label='User Id')
