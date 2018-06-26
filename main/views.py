from django.shortcuts import render
from django.http import HttpResponse
from .models import HeroClass, Actor, Race
from django.views import generic

def index(request):

    countActors = Actor.objects.all().count()
    countHeroClasses = Actor.objects.all().count()
    countFighters = Actor.objects.filter(heroClass__name='Fighter').count()

    return render(
        request,
        'index.html',
        context={'countActors': countActors, 'countHeroClasses': countHeroClasses, 'countFighters': countFighters},
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


