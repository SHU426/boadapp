# from ast import Delete
# from dataclasses import field
# from tempfile import template
# from winreg import DeleteValue
from gc import get_objects
import http
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.db import IntegrityError 
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .models import SredModel,Sred_msg_post
from django.views.generic import CreateView,DeleteView,DetailView
from .forms import MsgForm
from django.urls import reverse
from django.shortcuts import get_object_or_404
# Create your views here.
def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            login(request, user)
            return redirect('sred')
        except IntegrityError:
            return render(request,'signup.html',{'error':' このユーザーはすでに登録されています。'})
    return render(request,'signup.html')

def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('sred')
        else:
            return render(request,'login.html',{'context':'ユーザーネーム又はパスワードを正しく入力してください'})
    return render(request,'login.html')

@login_required
def sredfunc(request):
    object_list = SredModel.objects.all()
    return render(request,'sred.html',{'object_list':object_list})


def boardfunc(request):
    return render(request,'board.html',{})




class BoardCreate(CreateView):
    template_name = 'create.html'
    model = SredModel
    fields = ('title','memo','author')
    success_url = reverse_lazy('sred')

class BoardDelete(DeleteView):
    template_name = 'delete.html'
    model = SredModel
    fields = ('title','memo','author')
    success_url = reverse_lazy('sred')

def logoutfunc(request):
    logout(request)
    return redirect('login')

class MsgCreate(CreateView):
    model = Sred_msg_post
    # user = User
    template_name = 'msg_create.html'
    fields = ('sred','msg_detail','msg_author')
    
    def get_form(self):
        user = self.request.user
        pk = self.kwargs.get('pk')
        print(pk)
        form = super(MsgCreate, self).get_form()
        form.fields['sred'].label = '送信先:'
        form.initial['sred'] = self.model.objects.filter(sred_id=pk)
        form.fields['msg_detail'].label = 'Message'
        form.initial['msg_detail'] = ''
        form.fields['msg_author'].label = 'メッセージ作成者'
        form.initial['msg_author'] = user
        return form
    def get_success_url(self):
        return reverse('detail',kwargs={'pk':self.object.sred.pk})
    
    
class MsgDelete(DeleteView):
    model = Sred_msg_post
    template_name ='msg_delete.html'
    fields = ('sred','msg_detail','msg_author')
   
    def get_success_url(self):
        return reverse('detail',kwargs={'pk':self.object.sred.pk})
class MsgDetailfunc(DetailView):
    template_name = 'msg.html'
    model = SredModel
#     # object_list = model.objects.all()
#     # return render(request,'msg.html',{{'object_list':object_list}})

# def MsgDetailfunc(request,name,pk):
#     model = SredModel
#     sred = get_object_or_404(model,name=name)
#     sred_pk = get_object_404(model,pk=pk,sred=sred)
#     template_name = 'sred/sred_pk/msgdetail.html'
#     context = {'sred':sred,'sred_pk':sred_pk,'model':model}
#     return render(request,template_name,context)
    

