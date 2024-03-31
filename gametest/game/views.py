from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.urls import reverse,reverse_lazy
from django.views.generic import View,ListView,DetailView,CreateView,DeleteView,UpdateView,TemplateView
from .models import Phonedata,Gamedata,Review
from .forms import ReviewForm
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(ListView):
    template_name='game/index.html'
    model=Phonedata

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update({
            'object_list2': Gamedata.objects.all(),
        })
        return context

    def get_queryset(self):
        return Phonedata.objects.all()

class PhoneListView(ListView):
    template_name='game/PhoneList.html'
    model=Phonedata

class PhonedetailView(DetailView):
    template_name='game/Phonedetail.html'
    model=Phonedata
    

    def get_context_data(self, **kwargs):
        context = super(PhonedetailView, self).get_context_data(**kwargs)
        context.update({
            'object_list': Review.objects.all(),
            'object_list2': Gamedata.objects.all(),
            'object_list3': Phonedata.objects.all()
        })
        return context

    def get_queryset(self):
        return Phonedata.objects.all()

    
class GameListView(ListView):
    template_name='game/GameList.html'
    model=Gamedata

class GamedetailView(DetailView):
    template_name='game/Gamedetail.html'
    model=Gamedata

    def get_context_data(self, **kwargs):
        context = super(GamedetailView, self).get_context_data(**kwargs)
        context.update({
            'object_list': Review.objects.all(),
            'object_list2': Gamedata.objects.all(),
            'object_list3': Phonedata.objects.all()
        })
        return context

    def get_queryset(self):
        return Gamedata.objects.all()

class ReviewView(DetailView):
    template_name='game/Reviewview.html'
    model=Review
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 現在ログインしているユーザーの情報を取得
        current_user = self.request.user
        context['current_user'] = current_user
        return context

class CreateReviewView(LoginRequiredMixin,CreateView):
    template_name='game/Createreview.html'
    model=Review
    form_class = ReviewForm
    
    def form_valid(self, form):
        form.instance.user=self.request.user
        form.instance.image = self.request.FILES.get('image', None) 
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')
    
class UpdateReviewView(UpdateView):
    template_name='game/updateview.html'
    model=Review
    form_class = ReviewForm

    def get_success_url(self):
        return reverse('home')
    
    def get_object(self, queryset=None):
        obj=super().get_object(queryset)

        if obj.user !=self.request.user:
            raise PermissionDenied
        
        return obj
    
class DeleteReviewView(DeleteView):
    template_name="game/deleteview.html"
    model=Review
    
    def get_success_url(self):
        return reverse('home')
    
    def get_object(self, queryset=None):
        obj=super().get_object(queryset)

        if obj.user !=self.request.user:
            raise PermissionDenied
        
        return obj