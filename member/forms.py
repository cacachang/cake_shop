from django import forms

class UserForm(forms.Form):
  name = forms.CharField(label="姓名", max_length=30)
  age = forms.IntegerField(label="年齡")
  email = forms.CharField(label="信箱")
  address = forms.CharField(label="地址")
  phone = forms.CharField(label="電話")