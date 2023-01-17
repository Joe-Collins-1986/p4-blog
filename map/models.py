from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True, default=None)
    code = models.CharField(max_length=5, unique=True, default=None)
    capital = models.CharField(max_length=100, unique=True, default=None)
    region = models.CharField(max_length=100, default=None)
    currency = models.CharField(max_length=100, default=None)
    language = models.CharField(max_length=100, default=None)
    about = models.CharField(max_length=500, default=None)
    population = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.name


class Visit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="users_map")
    country = models.ForeignKey(Country, on_delete=models.CASCADE,
                                related_name="country_map")
    status = models.CharField(max_length=50, default="not_visited")

    def __str__(self):
        return self.status

