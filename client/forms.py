# form for log in
# form for creating pitch
# form for creating pitch image
# form for creating report
# form for creating report image

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), label='Password', max_length=100)