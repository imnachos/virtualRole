from django.shortcuts import render
from django.views import generic

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from main.forms import ActorEditForm

from .models import Actor, Object, Location, Event, Group, Campaign, Quest


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


def actor_edit_view(request, pk):
    actor_instance = get_object_or_404(Actor, pk=pk)

    if request.method == 'POST':

        form = ActorEditForm(request.POST)

        if form.is_valid():
            actor_instance.name = form.cleaned_data['name']
            actor_instance.surname = form.cleaned_data['surname']
            actor_instance.description = form.cleaned_data['description']
            actor_instance.save()

            return HttpResponseRedirect(reverse('actors'))

    else:
        form = ActorEditForm(initial={'name': actor_instance.name, "surname" : actor_instance.surname, "description" : actor_instance.description})

    context = {
        'form': form,
        'actor_instance': actor_instance,
    }

    return render(request, 'main/actor_edit.html', context)


# Location

class LocationListView(generic.ListView):
    model = Location

    def get_queryset(self):
        return Location.objects.filter(campaign__owner=self.request.user).order_by('name')


class LocationDetailView(generic.DetailView):
    model = Location


# Objects


class ObjectListView(generic.ListView):
    model = Object

    def get_queryset(self):
        return Object.objects.filter(campaign__owner=self.request.user).order_by('name')


class ObjectDetailView(generic.DetailView):
    model = Object


# Event

class EventListView(generic.ListView):
    model = Event

    def get_queryset(self):
        return Event.objects.filter(campaign__owner=self.request.user).order_by('name')


class EventDetailView(generic.DetailView):
    model = Event


# Group

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
