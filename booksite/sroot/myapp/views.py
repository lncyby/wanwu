from django.shortcuts import render,render_to_response
from django.http import HttpResponse,Http404
from django.template import loader,RequestContext
from myapp.models import *
import datetime
#from django.db import connection
from django.conf import settings
from django.core.mail import send_mail
import logging

# Create your views here.
logger = logging.getLogger('myapp.views')

def global_setting(request):
    site_url = settings.SITE_URL
    site_name = settings.SITE_NAME
    global_message = "This is a global test message"
    return locals()
#    return {'global_test':"hello world"}

def index(request):
#    return render_to_response('index.html',{},context_instance=RequestContext(request))
    return render(request,'index.html',{})

def foo_bar(request,template_name):
    logger.error("foo")
    return render(request,template_name,{})

def base(request):
    return render(request,'time.html',{})

def email(request):
    send_mail("django email","send email test","lvze_work@126.com",["guohao0221@126.com"])
    return HttpResponse("send OK")


def models_fun(request):
#    Publisher.objects.create(name='lvze',address='XiBeiwang',city='Beijing',state_province='Haidian'\
#            ,country='China',website='http://192.168.1.111')
#    
#    dic = {'first_name':'Guo','last_name':'Hao','email':'guohao@126.com'}
#    Author.objects.create(**dic)
#    
#    obj = Book(title = 'Python web',publication_date = datetime.datetime.now())
#    obj.save()

#    Publisher.objects.filter(id=3).delete()

#    Publisher.objects.filter(id=2).update(name='quhe')

#    obj = Book.objects.get(id=2)
#    obj.title = "Html5"
#    obj.save()

    book = Book.objects.all()

    a = Publisher.objects.all().values('name')

    b = Author.objects.get(id = 1)

    c = Publisher.objects.filter(id__gt=0).count()

    return render(request,'models.html',locals())

