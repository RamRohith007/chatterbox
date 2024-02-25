from django.forms import BaseModelForm
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request,"chatapp/home.html")

class CbLoginView(LoginView):
    template_name = 'chatapp/cblogin.html'
    fields = "__all__"
    redirect_authenticated_user = True
    context_object_name = 'loginform'
    
    
    def get_success_url(self):
        return reverse_lazy('home')
    
class CbSignUpView(FormView):
    template_name = 'chatapp/cbsignup.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    context_object_name = 'signupform'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(CbSignUpView, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(CbSignUpView, self).get(*args, **kwargs)
