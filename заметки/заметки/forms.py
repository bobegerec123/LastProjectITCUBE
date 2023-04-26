from django import forms


class TipsName(forms.Form):
    product_name = forms.CharField(label="Product name", max_length=20)

class UserName(forms.Form):
    user_name = forms.Charfield(label="User name", max_length=15)