from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [

    url(r'^$', views.index, name='home'),
    path('portal/', views.portal, name='portal'),

    path('actor/', views.ActorListView.as_view(), name='actors'),
    path('actor/<int:pk>', views.ActorDetailView.as_view(), name='actor-detail'),

    path('race/', views.RaceListView.as_view(), name='races'),
    path('race/<int:pk>', views.RaceDetailView.as_view(), name='race-detail'),

    path('heroClass/', views.HeroClassListView.as_view(), name='heroClasses'),
    path('heroClass/<int:pk>', views.HeroClassDetailView.as_view(), name='heroClass-detail'),

    path('location/', views.LocationListView.as_view(), name='locations'),
    path('location/<int:pk>', views.LocationDetailView.as_view(), name='location-detail'),

    path('locationType/', views.LocationTypeListView.as_view(), name='locationTypes'),
    path('locationType/<int:pk>', views.LocationTypeDetailView.as_view(), name='locationType-detail'),

    path('event/', views.EventListView.as_view(), name='events'),
    path('event/<int:pk>', views.EventDetailView.as_view(), name='event-detail'),

    path('item/', views.ItemListView.as_view(), name='items'),
    path('item/<int:pk>', views.ItemDetailView.as_view(), name='item-detail'),

    path('itemProperty/', views.ItemPropertyListView.as_view(), name='itemProperties'),
    path('itemProperty/<int:pk>', views.ItemPropertyDetailView.as_view(), name='itemProperty-detail'),

    path('group/', views.GroupListView.as_view(), name='groups'),
    path('group/<int:pk>', views.GroupDetailView.as_view(), name='group-detail'),

    path('groupType/', views.GroupTypeListView.as_view(), name='groupTypes'),
    path('groupType/<int:pk>', views.GroupTypeDetailView.as_view(), name='groupType-detail'),

    path('campaign/', views.CampaignListView.as_view(), name='campaigns'),
    path('campaign/<uuid:pk>', views.CampaignDetailView.as_view(), name='campaign-detail'),

    path('quest/', views.QuestListView.as_view(), name='quests'),
    path('quest/<int:pk>', views.QuestDetailView.as_view(), name='quest-detail'),
]
