#!/usr/bin/python 
#coding=utf-8

from django.http import HttpResponse,Http404
from django.template import loader
from django.shortcuts import render,render_to_response
import datetime

class A(object):
    a = "nihao cainiao"

    def fun(self):
        return "hello world"

def hello(request):
    return HttpResponse("Hello World!!")

def nihao(request):
    return HttpResponse("nihao world!!")

def current_datetime(request):
    now = datetime.datetime.now()
#    html = "<html><body>It is now %s.</body></html>"%now
    t = loader.get_template('current_datetime.html')
    html = t.render({'current_date':now})
    return HttpResponse(html)

def template_test(request):
    l = ('hello','nihao','hi')
    d = {'a':1,'b':2,'c':3}
    c = A()
    message = "hello world nihao hahhah" 

#1    t = loader.get_template('template1.html')
#    html = t.render({'list':l,'dict':d,'class':c,'value':1,"message":message})
#    return HttpResponse(html)
#2    return render_to_response('template1.html',{'list':l,'dict':d,'class':c,'value':1,"message":message})
#3    return render_to_response('template1.html',locals())
    return render(request,'template1.html',locals())
def hours_ahead(request,offset,d):
    print "+++++",d
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    html = "<html><body>In %s hours,It will be  %s.</body></html>"%(offset,dt)
    return  HttpResponse(html)
