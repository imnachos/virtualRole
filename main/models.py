from django.db import models
from django.urls import reverse


class Race(models.Model):
    name = models.TextField(max_length=20, blank=False, null=False)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["-name"]

    def get_absolute_url(self):
        return reverse('race-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class HeroClass(models.Model):
    name = models.TextField(max_length=20, blank=False)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["-name"]

    def get_absolute_url(self):
        return reverse('heroClass-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class ClassProgress(models.Model):
    heroClass = models.ForeignKey(HeroClass, on_delete=models.SET_NULL, blank=True, null=True)
    level = models.IntegerField(blank=False, null=False, default=1)

    def __str__(self):
        return 'Level ' + str(self.level) + self.heroClass.name


class Actor(models.Model):

    name = models.TextField(max_length=20, blank=False)
    surname = models.TextField(max_length=20, blank=True)
    age = models.IntegerField(blank=True)
    height = models.IntegerField(blank=True)
    race = models.ForeignKey(Race, on_delete=models.SET_NULL, blank=False, null=True)
    heroClasses = models.ManyToManyField(ClassProgress, symmetrical=False, blank=False)

    class Meta:
        ordering = ["-name"]

    def get_absolute_url(self):
        return reverse('actor-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class LocationType(models.Model):
    name = models.TextField(max_length=20, blank=False, null=False)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["-name"]

    def get_absolute_url(self):
        return reverse('locationType-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.TextField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    type = models.ForeignKey(LocationType, on_delete=models.SET_NULL, blank=False, null=True)
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
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, blank=False, null=True)

    class Meta:
        ordering = ["-name"]

    def get_absolute_url(self):
        return reverse('event-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class ItemProperty(models.Model):
    name = models.TextField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    value = models.FloatField(blank=False)

    class Meta:
        ordering = ["-name"]

    def get_absolute_url(self):
        return reverse('itemProperty-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.TextField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    properties = models.ManyToManyField(ItemProperty, symmetrical=False)

    class Meta:
        ordering = ["-name"]

    def get_absolute_url(self):
        return reverse('item-detail', args=[str(self.id)])

    def __str__(self):
        return self.name
