from django import forms


class TipsName(forms.Form):
    tips_name = forms.CharField(label="Tips name", max_length=20)


class UserName(forms.Form):
    user_name = forms.CharField(label="User name", max_length=15)
