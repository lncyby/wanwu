#coding=utf-8
"""booksite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,patterns,include
from django.contrib import admin
#from booksite.views import hello,nihao

urlpatterns = patterns('booksite.views',
    url(r'^admin/', admin.site.urls),
    url('^hello/$','hello',name = "h" ),
    ('^nihao/$','nihao'),
)

urlpatterns += patterns('booksite.views',
            ('^time/$','current_datetime'),
            ('^template/$','template_test'),
            url('^time/plus/(?P<offset>\d{1,2})/$','hours_ahead',{'d':"url test"})
        )

urlpatterns += patterns('',
        (r'^',include('myapp.urls')),
        (r'^form/',include('formapp.urls')),
        )

