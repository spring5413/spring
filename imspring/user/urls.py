# -*- coding:UTF-8 -*-
'''
Created on 2014-6-23

@author: spring
'''
from django.conf.urls import patterns, include, url
from utils.piston_resource import PistonResource as Resource

from imspring.user.user_views import UserLoginHandler,UserLogoutHandler,UserRegisterHandler

user_login_handler = Resource(UserLoginHandler)
user_logout_handler = Resource(UserLogoutHandler)
user_register_handler = Resource(UserRegisterHandler)

urlpatterns = patterns('',
            url(r'^login/$', user_login_handler),
            url(r'^logout/$', user_logout_handler),
            url(r'^register/$', user_register_handler),            
)
