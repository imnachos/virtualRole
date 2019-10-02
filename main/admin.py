from django.contrib import admin

from .models import Actor, Event, Location, Object, Group, Campaign, Quest

admin.site.register(Campaign)

admin.site.register(Actor)

admin.site.register(Event)

admin.site.register(Location)

admin.site.register(Object)

admin.site.register(Group)

admin.site.register(Quest)
