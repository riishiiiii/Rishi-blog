from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from .models import profileModel
class SignupForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    mobile = forms.CharField(max_length=10)
    class Meta:
        model = User
        fields =['username','email','mobile']

    # def __init__(self, *args, **kwargs):
    #     super(SignupForm,self).__init__(*args, **kwargs) 

    #     for fieldname in ['username','email']:
    #         self.fields[fieldname].help_text= None


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm,self).__init__(*args, **kwargs) 

        for fieldname in ['username','email']:
            self.fields[fieldname].help_text= None
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = profileModel
        fields = ['image']

