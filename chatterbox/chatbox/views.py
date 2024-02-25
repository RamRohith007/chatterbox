from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Box,Messages

# Create your views here.

@login_required
def chatboxlist(request):
    chatboxes = Box.objects.all()
    formvalue = {'chatboxes':chatboxes}
    return render(request,'chatbox/chatboxes.html',context=formvalue)

@login_required
def chatbox(request,slug):
    chatbox = Box.objects.get(slug=slug)
    messages = Messages.objects.filter(chatbox=chatbox)[0:25]
    formvalue = {'chatbox':chatbox,'messages':messages}
    return render(request,'chatbox/chatbox.html',context=formvalue)
