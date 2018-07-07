from django.shortcuts import render
from django.http import HttpResponse
from .models import HeroClass, Actor, Race, Item, ItemProperty, Location, LocationType, Event, Group, GroupType, Campaign, Quest
from django.views import generic


def index(request):
    context = {}

    context['campaigns'] = Campaign.objects.filter(owner=request.user).order_by('name')

    return render(
        request,
        'index.html',
        context,
    )


def portal(request):

    return render(
        request,
        'portal.html',
        context={},
    )

# Campaign

class CampaignListView(generic.ListView):
    model = Campaign

    def get_queryset(self):
        return Campaign.objects.filter(owner=self.request.user).order_by('name')


class CampaignDetailView(generic.DetailView):
    model = Campaign


# Actor


class ActorListView(generic.ListView):
    model = Actor

    def get_queryset(self):
        return Actor.objects.filter(campaign__owner=self.request.user).order_by('name')


class ActorDetailView(generic.DetailView):
    model = Actor


# Class

class HeroClassListView(generic.ListView):
    model = HeroClass

    def get_queryset(self):
        return HeroClass.objects.filter(campaign__owner=self.request.user).order_by('name')


class HeroClassDetailView(generic.DetailView):
    model = HeroClass


# Race

class RaceListView(generic.ListView):
    model = Race

    def get_queryset(self):
        return Race.objects.filter(campaign__owner=self.request.user).order_by('name')


class RaceDetailView(generic.DetailView):
    model = Race


# Location

class LocationTypeListView(generic.ListView):
    model = LocationType

    def get_queryset(self):
        return LocationType.objects.filter(campaign__owner=self.request.user).order_by('name')


class LocationTypeDetailView(generic.DetailView):
    model = LocationType


class LocationListView(generic.ListView):
    model = Location

    def get_queryset(self):
        return Location.objects.filter(campaign__owner=self.request.user).order_by('name')


class LocationDetailView(generic.DetailView):
    model = Location


# Items

class ItemPropertyListView(generic.ListView):
    model = ItemProperty

    def get_queryset(self):
        return ItemProperty.objects.filter(campaign__owner=self.request.user).order_by('name')


class ItemPropertyDetailView(generic.DetailView):
    model = ItemProperty


class ItemListView(generic.ListView):
    model = Item

    def get_queryset(self):
        return Item.objects.filter(campaign__owner=self.request.user).order_by('name')


class ItemDetailView(generic.DetailView):
    model = Item


# Event

class EventListView(generic.ListView):
    model = Event

    def get_queryset(self):
        return Event.objects.filter(campaign__owner=self.request.user).order_by('name')


class EventDetailView(generic.DetailView):
    model = Event


# Group

class GroupTypeListView(generic.ListView):
    model = GroupType

    def get_queryset(self):
        return GroupType.objects.filter(campaign__owner=self.request.user).order_by('name')


class GroupTypeDetailView(generic.DetailView):
    model = GroupType


class GroupListView(generic.ListView):
    model = Group

    def get_queryset(self):
        return Group.objects.filter(campaign__owner=self.request.user).order_by('name')


class GroupDetailView(generic.DetailView):
    model = Group


# Quest

class QuestListView(generic.ListView):
    model = Quest

    def get_queryset(self):
        return Quest.objects.filter(campaign__owner=self.request.user).order_by('name')


class QuestDetailView(generic.DetailView):
    model = Quest
