from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views

urlpatterns=[
    path('',views.HomeView.as_view(),name="home"),
    path('home',views.HomeView.as_view(),name="home"),
    path('phonelist',views.PhoneListView.as_view(),name="phonelist"),
    path('<int:pk>/phone',views.PhonedetailView.as_view(),name="phone"),
    path('gamelist',views.GameListView.as_view(),name="gamelist"),
    path('<int:pk>/game',views.GamedetailView.as_view(),name="game"),
    path('<int:pk>/review',views.ReviewView.as_view(),name="review"),
    path('createreview',views.CreateReviewView.as_view(),name="createreview"),
    path('<int:pk>/updatereview',views.UpdateReviewView.as_view(),name="updatereview"),
    path('<int:pk>/deletereview',views.DeleteReviewView.as_view(),name="deletereview"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)