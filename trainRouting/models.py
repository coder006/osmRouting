from django.db import models

class Cities(models.Model):
    city_name = models.CharField(max_length=200)
    state_name = models.CharField(max_length=100)

class Stations(models.Model):
    station_name = models.CharField(max_length=200)
    city_name = models.ForeignKey(Cities)

