import uuid

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


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
    surname = models.TextField(max_length=20, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)

    campaign = models.ForeignKey(Campaign, on_delete=models.SET_NULL, blank=False, null=True)

    class Meta:
        ordering = ["-name"]

    def get_absolute_url(self):
        return reverse('actor-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.TextField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    members = models.ManyToManyField(Actor, symmetrical=False)

    campaign = models.ForeignKey(Campaign, on_delete=models.SET_NULL, blank=False, null=True)

    class Meta:
        ordering = ["-name"]

    def get_absolute_url(self):
        return reverse('group-detail', args=[str(self.id)])

    def __str__(self):
        return self.name + " (" + self.type.name + ")"


class Location(models.Model):
    name = models.TextField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    locations = models.ManyToManyField("self", symmetrical=False, blank=True)

    campaign = models.ForeignKey(Campaign, on_delete=models.SET_NULL, blank=False, null=True)

    class Meta:
        ordering = ["-name"]

    def get_absolute_url(self):
        return reverse('location-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.TextField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, blank=False, null=True)
    groups = models.ManyToManyField(Group, symmetrical=False, blank=True)
    actors = models.ManyToManyField(Actor, symmetrical=False, blank=True)
    date = models.TimeField(blank=True, null=True)

    campaign = models.ForeignKey(Campaign, on_delete=models.SET_NULL, blank=False, null=True)

    class Meta:
        ordering = ["-name"]

    def get_absolute_url(self):
        return reverse('event-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Object(models.Model):
    name = models.TextField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    currentOwner = models.ForeignKey(Actor, on_delete=models.SET_NULL, blank=False, null=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.SET_NULL, blank=False, null=True)

    class Meta:
        ordering = ["-name"]

    def get_absolute_url(self):
        return reverse('item-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Quest(models.Model):
    name = models.TextField(blank=False, null=False, unique=True)
    description = models.TextField(blank=True, null=True)

    givers = models.ManyToManyField(Actor, symmetrical=False, related_name='givers', blank=True)
    participants = models.ManyToManyField(Actor, symmetrical=False, related_name='participants', blank=True)
    events = models.ManyToManyField(Event, symmetrical=False, blank=True)

    campaign = models.ForeignKey(Campaign, on_delete=models.SET_NULL, blank=False, null=True)

    class Meta:
        ordering = ["-name"]

    def get_absolute_url(self):
        return reverse('quest-detail', args=[str(self.id)])

    def __str__(self):
        return self.name
