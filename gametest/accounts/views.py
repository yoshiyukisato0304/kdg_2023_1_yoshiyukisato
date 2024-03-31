from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView ,ListView
from django.contrib.auth import logout
from .forms import SignupForm
from game.models import Review

class SignupView(CreateView):
    model=User
    form_class=SignupForm
    template_name='accounts/signup.html'
    success_url=reverse_lazy("home")

def logout_view(request):
    logout(request)
    return redirect('home')

class ProfileView(ListView):
    template_name='accounts/profile.html'
    model=Review