from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse,HttpResponseRedirect
#from django.template import RequestContext
from formapp.forms import *
from formapp.models import *
from myapp.models import *
import logging
from django.contrib.auth.hashers import make_password
from django.contrib import auth
from django.contrib.auth.decorators import login_required,permission_required

logger = logging.getLogger('formapp.views')

# Create your views here.

def search_form(request):
    return render(request,'search_form.html',{})

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        print "++++++++++++++++",q
        return HttpResponse("Thanks")
    else:
        return render(request,'search_form.html',{'error':True})

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject',''):
            errors.append('Enter a subject')

        if not request.POST.get('message',''):
            errors.append('Enter a message')

        if not request.POST.get('email',''):
            errors.append('Enter a email address')

        if not errors:
            return HttpResponseRedirect('/form/contact/thanks')

    return render(request,'contact_form.html',{'errors':errors,'subject':request.POST.get('subject',''),\
            'message':request.POST.get('message',''),
            'email':request.POST.get('email',''),})
def thanks(request):
    return HttpResponse("Thanks!!!")

def formtest(request):
    if request.method == 'POST':
        form = RemarkForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print cd['subject']
            print cd['mail']
            print cd['topic']
            print cd['message']
            print cd['cc_myself']
            return HttpResponseRedirect('/form/form/')
    else:
        form = RemarkForm()

    return render(request,'formtest.html',{'form':form})

def form1test(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd  = form.cleaned_data
            dic = {'orderID':cd['orderID'],'title':cd['title'],'content':cd['content']}
            Adver.objects.create(**dic)
            return HttpResponseRedirect('/form/form1/')
    else:
        form = ContactForm()
    return render(request,'form1test.html',{'form':form})
@permission_required('polls.can_vote',login_url = '/form/contact/thanks/')
def reg(request):
    try:
        if request.method == 'POST':
            reg_form = RegForm(request.POST)
            if reg_form.is_valid():
                cd = reg_form.cleaned_data
                User.objects.create(username=cd['username'],password=make_password(cd['password']),email=cd['email'],mobile=cd['tel'])
                
                return HttpResponseRedirect("/form/login/")
            else:
                return render(request,'failure.html',{'reason':reg_form.errors})
        else:
            reg_form = RegForm()
    except Exception as e:
        logger.error(e)
    return render(request,'reg.html',locals())

def vote(request):
    return False


@login_required(login_url = '/form/reg/')
def login(request):
    errors=[]
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if not request.POST.get('username',''):
            errors.append('Enter a username.')
        if not request.POST.get('password',''):
            errors.append('Enter a password.')
        if not errors:
#            if not request.user.is_authenticated():
            user = auth.authenticate(username=username,password=password)
            if user is not None and user.is_active:
                auth.login(request,user)
                return HttpResponse('You have logged in.')
            else:
                return HttpResponse('usrname or password invalid.')
#            else:
#                return HttpResponse("You have already login")
    return render(request,'user_login.html',{'errors':errors,})

def loginout(request):
    auth.logout(request)
    return HttpResponseRedirect("/form/login/")
