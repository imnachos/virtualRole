from django.shortcuts import render
from django.http import HttpResponse
from .models import HeroClass, Actor, Race, Item, ItemProperty, Location, LocationType, Event
from django.views import generic


def index(request):

    return render(
        request,
        'index.html',
        context={},
    )


def portal(request):

    return render(
        request,
        'portal.html',
        context={},
    )


# Actor

class ActorListView(generic.ListView):
    model = Actor


class ActorDetailView(generic.DetailView):
    model = Actor


# Class

class HeroClassListView(generic.ListView):
    model = HeroClass


class HeroClassDetailView(generic.DetailView):
    model = HeroClass


# Race

class RaceListView(generic.ListView):
    model = Race


class RaceDetailView(generic.DetailView):
    model = Race


# Location

class LocationTypeListView(generic.ListView):
    model = LocationType


class LocationTypeDetailView(generic.DetailView):
    model = LocationType


class LocationListView(generic.ListView):
    model = Location


class LocationDetailView(generic.DetailView):
    model = Location


# Items

class ItemPropertyListView(generic.ListView):
    model = ItemProperty


class ItemPropertyDetailView(generic.DetailView):
    model = ItemProperty


class ItemListView(generic.ListView):
    model = Item


class ItemDetailView(generic.DetailView):
    model = Item


# Event

class EventListView(generic.ListView):
    model = Event


class EventDetailView(generic.DetailView):
    model = Event
