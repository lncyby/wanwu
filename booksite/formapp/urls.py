#coding=utf-8

from django.conf.urls import *
from formapp.views import *

urlpatterns = patterns('',
        ('^search-form/$',search_form),
        ('^search/$',search),
        )

urlpatterns += patterns('',
        ('^contact/$',contact),
        ('^contact/thanks/$',thanks),
        )

urlpatterns += patterns('',
        ('^form/$',formtest),
        ('^form1/$',form1test),
        )
urlpatterns += patterns('',
        url('^reg/$',reg,name='reg'),
        url('^login/$',login,name='login'),
        url('^loginout/$',loginout,name='loginout'),
        )
