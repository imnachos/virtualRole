from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    path('actors/', views.ActorListView.as_view(), name='actors'),
    path('actors/<int:pk>', views.ActorDetailView.as_view(), name='actor-detail'),

    path('races/', views.RaceListView.as_view(), name='races'),
    path('races/<int:pk>', views.RaceDetailView.as_view(), name='race-detail'),

    path('heroClasses/', views.HeroClassListView.as_view(), name='heroClasses'),
    path('heroClasses/<int:pk>', views.HeroClassDetailView.as_view(), name='heroClass-detail'),

    path('locations/', views.LocationListView.as_view(), name='locations'),
    path('locations/<int:pk>', views.LocationDetailView.as_view(), name='location-detail'),

    path('locationTypes/', views.LocationTypeListView.as_view(), name='locationTypes'),
    path('locationType/<int:pk>', views.LocationDetailView.as_view(), name='locationType-detail'),

    path('events/', views.EventListView.as_view(), name='events'),
    path('events/<int:pk>', views.EventDetailView.as_view(), name='event-detail'),

    path('items/', views.ItemListView.as_view(), name='items'),
    path('items/<int:pk>', views.ItemDetailView.as_view(), name='item-detail'),

    path('itemProperty/', views.ItemPropertyListView.as_view(), name='itemProperties'),
    path('itemProperties/<int:pk>', views.ItemPropertyDetailView.as_view(), name='itemProperty-detail'),
]
