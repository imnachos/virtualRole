from django.contrib import admin
from .models import HeroClass, Actor, Race

admin.site.register(HeroClass)
admin.site.register(Race)
admin.site.register(Actor)
