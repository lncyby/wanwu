#coding=utf-8

from django.conf.urls import *
from myapp.views import *
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
        url(r'^models/$',models_fun),
        url(r'^index/$',index,name = "index"),
        url(r'^about/$',TemplateView.as_view(template_name = 'index.html'))
        )

urlpatterns += patterns('',
        (r'^foo/$',foo_bar,{'template_name':'foo.html'}),
        (r'^bar/$',foo_bar,{'template_name':'bar.html'}),
        url(r'^base/$',base,name='base'),
        (r'^email/$',email)
        )
