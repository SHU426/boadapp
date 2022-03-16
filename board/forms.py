from dataclasses import field
from django import forms
from .models import SredModel,Sred_msg_post
from django.contrib.auth.models import User

class MsgForm(forms.ModelForm):
    class Meta:
        model = Sred_msg_post
        fields = ('sred','msg_detail','msg_author')
