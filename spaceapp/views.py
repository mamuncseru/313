from django.shortcuts import render
from django.http import HttpResponse
import time
from threading import Timer
# from rest_framework import viewsets
# import requests

from skyfield.api import load, wgs84
from skyfield.api import EarthSatellite
import json

def satelite_data():
    print("function called....")
    stations_url = 'https://celestrak.com/NORAD/elements/1999-025.txt'
    # textfile = requests.get(stations_url)
    satellites = load.tle_file(stations_url)

    ts = load.timescale()
    t = ts.now()

    # i = 0
    sat_data = {}
    longitude = []
    latitude = []
    name = []
    epoch = []
    for sat in satellites:
        geocentric = sat.at(t)
        subpoint = wgs84.subpoint(geocentric)
        latitude.append(subpoint.latitude.degrees)
        longitude.append(subpoint.longitude.degrees)
        name.append(sat.name)
        temp = str(sat).split(' ')
        epoch.append(str(temp[6] + " " + temp[7]))

    sat_data["latitude"] = latitude
    sat_data["longitude"] = longitude
    sat_data["name"] = name
    sat_data["epoch"] = epoch
    print(sat_data["latitude"][0])
    return sat_data

# Create your views here.
run = True
def index(request):
    data = json.dumps(satelite_data())
    return HttpResponse(data)


