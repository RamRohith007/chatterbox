from django.urls import path
from .views import home, CbSignUpView, CbLoginView, LogoutView

##
urlpatterns = [
    path('',home,name="home"),
    path('signup/',CbSignUpView.as_view(),name='signup'),
    path('login/',CbLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page ="login"),name='logout'),
]
