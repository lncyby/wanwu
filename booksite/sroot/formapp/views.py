from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
#from django.template import RequestContext
from formapp.forms import *
from formapp.models import *


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
