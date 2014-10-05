from django.contrib import admin
from models import City, Station

class CityAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'state_name')

class StationAdmin(admin.ModelAdmin):
    list_display = ('station_name', 'city_name')

admin.site.register(City, CityAdmin)
admin.site.register(Station, StationAdmin)
