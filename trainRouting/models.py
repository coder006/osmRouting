from django.db import models

class City(models.Model):
    city_name = models.CharField(max_length=200)
    state_name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.city_name

class Station(models.Model):
    station_name = models.CharField(max_length=200)
    city_name = models.ForeignKey(City)

    '''
    train_name = models.CharField(max_length=100)
    train_number = models.IntegerField()
    destination_station_name = models.CharField(max_length=100)
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    travel_time = arrival_time - 
    '''
# class StationLucknowNR(Stations):
