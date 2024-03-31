from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView

from .views import SignupView,ProfileView

app_name ='accounts'

urlpatterns=[
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('signup/',SignupView.as_view(),name='signup'),
    path('profile/',ProfileView.as_view(),name="profile")
]