from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [

    url(r'^$', views.index, name='home'),
    path('portal/', views.portal, name='portal'),

    path('actor/', views.ActorListView.as_view(), name='actors'),
    path('actor/<int:pk>', views.ActorDetailView.as_view(), name='actor-detail'),
    path('actor/<int:pk>/edit', views.actor_edit_view, name='actor-edit'),

    path('location/', views.LocationListView.as_view(), name='locations'),
    path('location/<int:pk>', views.LocationDetailView.as_view(), name='location-detail'),

    path('event/', views.EventListView.as_view(), name='events'),
    path('event/<int:pk>', views.EventDetailView.as_view(), name='event-detail'),

    path('object/', views.ObjectListView.as_view(), name='objects'),
    path('object/<int:pk>', views.ObjectDetailView.as_view(), name='object-detail'),

    path('group/', views.GroupListView.as_view(), name='groups'),
    path('group/<int:pk>', views.GroupDetailView.as_view(), name='group-detail'),

    path('campaign/', views.CampaignListView.as_view(), name='campaigns'),
    path('campaign/<uuid:pk>', views.CampaignDetailView.as_view(), name='campaign-detail'),

    path('quest/', views.QuestListView.as_view(), name='quests'),
    path('quest/<int:pk>', views.QuestDetailView.as_view(), name='quest-detail'),
]
