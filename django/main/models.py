from django.db import models


class HeroClass(models.Model):
    name = models.TextField(max_length=20, blank=False)

    def __str__(self):
        return self.name


class Actor(models.Model):
    """
    A simple model class for an actor
    """
    # Fields
    name = models.TextField(max_length=20, blank=False)
    surname = models.TextField(max_length=20, blank=False)
    age = models.IntegerField()
    height = models.IntegerField()

    heroClass = models.ForeignKey(HeroClass, on_delete=models.SET_NULL, blank=True, null=True)

    # Metadata
    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name + ' ' + self.surname


