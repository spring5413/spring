# -*- coding:UTF-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from piston.doc import documentation_view

urlpatterns = patterns('',
    url(r'^iapi/user/', include('imspring.user.urls')),
    url(r'^doc/',documentation_view),
    url(r'^$',TemplateView.as_view(template_name="index.html"),name="index"),
     
)
