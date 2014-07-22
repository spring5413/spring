#-*- coding:utf-8 -*-
'''
Created on 2014-6-23
@author: spring
'''
from piston.handler import BaseHandler
from django.contrib.auth.models import User
from piston.utils import validate, rc, FormValidationError
from django.contrib.auth import login as auth_login, logout as auth_logout
from imspring.user.user_forms import IAPIAuthenticationForm,MyUserCreationForm
from imspring.accounts.models import UserProfile
from django.conf import settings
import logging
import traceback

log = logging.getLogger('wangchunpeng')

class UserLoginHandler(BaseHandler):
    allowed_methods = ('GET', 'POST')
    model = User
    fields = ('username','first_name','last_name',)
    def read(self, request, *args, **kwargs):
        '''
            登录状态验证
            URL:user/login/ 
            描述:验证用户cookie是否为登录状态
        '''
        if request.user.is_authenticated():
            return request.user
        else:
            return rc.FORBIDDEN
    
    
    def create(self,request,*args,**kwargs):
        f = IAPIAuthenticationForm(data=request.POST)
        if f.is_valid():
            auth_login(request, f.get_user())
            log.debug('f.is_valid true')
        else:
            log.debug('f.is_valid false,%s' % f)
            raise FormValidationError(f)
        log.debug('request.user:%s' % request.user)
        request.META['slogin']=True
        return request.user

class UserLogoutHandler(BaseHandler):
    '''用户注销'''
    allowed_methods = ('GET',)
    
    def read(self, request, *args, **kwargs): 
        '''
        注销处理
            URL:user/logout/
            描述:用户注销，清除cookie
        '''
        
        auth_logout(request)
        return rc.ALL_OK
    
class UserRegisterHandler(BaseHandler):
    allowed_methods = ('POST',)
    model = User
    fields = ('username','first_name','last_name',)
    
    def create(self, request, *args, **kwargs):
        '''
        新用户注册
            URL:user/register/
            描述:新用户注册
            参数:
            username:用户名
            password1:密码
            password2:密码确认
            agreement:用户协议
        '''
        f = MyUserCreationForm(request.POST)     
        if f.is_valid():
            instance = f.save()
#             p = instance.get_profile()
            p = UserProfile(user = instance)
            p.save()
        else:
            raise FormValidationError(f)
        return instance