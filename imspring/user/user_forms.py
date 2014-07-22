# -*- coding:UTF-8 -*-
'''
Created on 2014-6-23
@author: spring
'''
from django import forms
from django.contrib.auth.forms import SetPasswordForm, AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User

class IAPIAuthenticationForm(AuthenticationForm):
    ver = forms.IntegerField(required=False)

class MyUserCreationForm(UserCreationForm):
    agreement = forms.BooleanField(required=False,label=u'我已阅读并同意',initial=True)

