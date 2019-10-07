import uuid

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.timezone import deactivate


class Campaign(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True)
    name = models.TextField(max_length=20, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    creation = models.TimeField(auto_now_add=True, blank=False)

    class Meta:
        ordering = ["-name"]

    def get_absolute_url(self):
        return reverse('campaign-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.TextField(max_length=20, blank=False)
    description = models.TextField(blank=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.SET_NULL, blank=False, null=True)

    surname = models.TextField(max_length=20, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)

    profession = models.TextField(blank=True, null=True)
    race = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["-name"]

    def get_absolute_url(self):
        return reverse('actor-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, name, surname, description):
        actor = cls(name=name, surname=surname, description=description)
        return actor


class Group(models.Model):
    name = models.TextField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.SET_NULL, blank=False, null=True)

    members = models.ManyToManyField(Actor, symmetrical=False)

    class Meta:
        ordering = ["-name"]

    def get_absolute_url(self):
        return reverse('group-detail', args=[str(self.id)])

    def __str__(self):
        return self.name + " (" + self.type.name + ")"


class Location(models.Model):
    name = models.TextField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.SET_NULL, blank=False, null=True)

    locations = models.ManyToManyField("self", symmetrical=False, blank=True)

    class Meta:
        ordering = ["-name"]

    def get_absolute_url(self):
        return reverse('location-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.TextField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.SET_NULL, blank=False, null=True)

    location = models.ForeignKey(Location, on_delete=models.SET_NULL, blank=False, null=True)
    groups = models.ManyToManyField(Group, symmetrical=False, blank=True)
    actors = models.ManyToManyField(Actor, symmetrical=False, blank=True)
    date = models.TimeField(blank=True, null=True)

    class Meta:
        ordering = ["-name"]

    def get_absolute_url(self):
        return reverse('event-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Object(models.Model):
    name = models.TextField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.SET_NULL, blank=False, null=True)

    currentOwner = models.ForeignKey(Actor, on_delete=models.SET_NULL, blank=False, null=True)

    class Meta:
        ordering = ["-name"]

    def get_absolute_url(self):
        return reverse('object-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Quest(models.Model):
    name = models.TextField(blank=False, null=False, unique=True)
    description = models.TextField(blank=True, null=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.SET_NULL, blank=False, null=True)

    givers = models.ManyToManyField(Actor, symmetrical=False, related_name='givers', blank=True)
    participants = models.ManyToManyField(Actor, symmetrical=False, related_name='participants', blank=True)
    events = models.ManyToManyField(Event, symmetrical=False, blank=True)
    locations = models.ManyToManyField(Location, symmetrical=False, blank=True)

    class Meta:
        ordering = ["-name"]

    def get_absolute_url(self):
        return reverse('quest-detail', args=[str(self.id)])

    def __str__(self):
        return self.name
