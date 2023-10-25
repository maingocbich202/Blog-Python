from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Tài khoản')
    password = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput())