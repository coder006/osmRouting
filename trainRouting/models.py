from django.db import models

class City(models.Model):
    city_name = models.CharField(max_length=200)
    state_name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.city_name

class Station(models.Model):
    station_name = models.CharField(max_length=200)
    city_name = models.ForeignKey(City)

    def __unicode__(self):
        return self.station_name + "_" + self.city_name

class GeneralStation(models.Model):
    train_name = 
