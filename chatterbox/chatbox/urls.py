from django.urls import path
from . import views

##
urlpatterns = [
    path('chatboxes/',views.chatboxlist,name='chatboxes'),
    path('<slug:slug>/',views.chatbox,name='chatbox'),
]
