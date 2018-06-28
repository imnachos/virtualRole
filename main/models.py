from django.db import models
from django.urls import reverse


class Race(models.Model):
    name = models.TextField(max_length=20, blank=False)

    class Meta:
        ordering = ["-name"]

    def get_absolute_url(self):
        return reverse('race-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class HeroClass(models.Model):
    name = models.TextField(max_length=20, blank=False)

    class Meta:
        ordering = ["-name"]

    def get_absolute_url(self):
        return reverse('heroClass-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Actor(models.Model):

    name = models.TextField(max_length=20, blank=False)
    surname = models.TextField(max_length=20, blank=True)
    age = models.IntegerField(blank=True)
    height = models.IntegerField(blank=True)
    race = models.ForeignKey(Race, on_delete=models.SET_NULL, blank=False, null=True)
    heroClass = models.ForeignKey(HeroClass, on_delete=models.SET_NULL, blank=True, null=True)
    level = models.IntegerField(blank=False, null=False, default=1)

    class Meta:
        ordering = ["-name"]

    def get_absolute_url(self):
        return reverse('actor-detail', args=[str(self.id)])

    def __str__(self):
        return self.name + ' ' + self.surname


