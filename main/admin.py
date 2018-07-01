from django.contrib import admin
from .models import HeroClass, Actor, Race, Event, Location, LocationType, Item, ItemProperty, ClassProgress, Group, GroupType

admin.site.register(HeroClass)

admin.site.register(ClassProgress)

admin.site.register(Race)

admin.site.register(Actor)

admin.site.register(Event)

admin.site.register(Location)
admin.site.register(LocationType)

admin.site.register(Item)
admin.site.register(ItemProperty)

admin.site.register(Group)
admin.site.register(GroupType)



