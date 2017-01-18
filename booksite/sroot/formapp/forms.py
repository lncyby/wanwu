# -*- coding:utf-8 -*-
from django import forms
from formapp.models import *

TOPIC_CHOICES=(
		('leve1','差评'),
		('leve3','中评'),
		('leve2','好评'),
		)

class RemarkForm(forms.Form):
	subject = forms.CharField(max_length=100,label='标题')
	mail = forms.EmailField(label='邮件')
	topic = forms.ChoiceField(choices=TOPIC_CHOICES,label='评分')
	message = forms.CharField(label='内容',widget=forms.Textarea)
	cc_myself = forms.BooleanField(required=False,label='订阅')

        def clean_message(self):
            message = self.cleaned_data['message']
            num = len(message.split())
            if num < 4:
                raise forms.ValidationError('Not enough words!')
            return message

class ContactForm(forms.ModelForm):
    class Meta:
        model = Adver
	fields = ('orderID','title','content')
