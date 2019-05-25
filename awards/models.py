from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models import Q

import datetime as dt

# Create your models here.
class categories(models.Model):
    categories = models.CharField(max_length = 100)

    def __str__(self):
        return self.categories

    def save_category(self):
        self.save()

    @classmethod
    def delete_category(cls,categories):
        cls.objects.filter(categories=categories).delete()


class technologies(models.Model):
    technologies = models.CharField(max_length = 150)

    def __str__(self):
        return self.technologies

    def save_technology(self):
        self.save()

    @classmethod
    def delete_technology(cls,technologies):
        cls.objects.filter(technologies=technologies).delete()


class colors(models.Model):
    colors = models.CharField(max_length = 100)

    def __str__(self):
        return self.colors

    def save_color(self):
        return self.save()

    @classmethod
    def delete_color(cls,colors):
        cls.objects.filter(colors = colors).delete()

class countries(models.Model):
    countries = models.CharField(max_length = 150)

    def __str__(self):
        return self.countries

    class Meta:
        ordering = ['countries']

    def save_country(self):
        self.save()

    @classmethod
    def delete_country(cls,countries):
        cls.objects.filter(countries = countries).delete()

