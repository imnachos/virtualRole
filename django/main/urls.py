from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('actors/', views.ActorListView.as_view(), name='actors'),
    path('actors/<int:pk>', views.ActorDetailView.as_view(), name='actor-detail'),

    path('races/', views.RaceListView.as_view(), name='races'),
    path('races/<int:pk>', views.RaceDetailView.as_view(), name='race-detail'),

    path('heroClasses/', views.HeroClassListView.as_view(), name='heroClasses'),
    path('heroClasses/<int:pk>', views.HeroClassDetailView.as_view(), name='heroClass-detail'),
]
