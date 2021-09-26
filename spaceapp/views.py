from django.shortcuts import render
from django.http import HttpResponse
import time
from threading import Timer
# from rest_framework import viewsets
# import requests

from skyfield.api import load, wgs84
from skyfield.api import EarthSatellite
import json

def satelite_data(stations_url):
    # textfile = requests.get(stations_url)
    satellites = load.tle_file(stations_url)

    ts = load.timescale()
    t = ts.now()

    # i = 0
    sat_data = {}
    longitude = []
    latitude = []
    altitude = []
    name = ""
    # epoch = []
    for sat in satellites:
        geocentric = sat.at(t)
        subpoint = wgs84.subpoint(geocentric)
        latitude.append(subpoint.latitude.degrees)
        longitude.append(subpoint.longitude.degrees)
        name = sat.name
        temp = str(sat).split(' ')
        # epoch.append(str(temp[6] + " " + temp[7]))
        altitude.append(format(subpoint.elevation.km))


    sat_data["latitude"] = latitude
    sat_data["longitude"] = longitude
    sat_data["name"] = name
    sat_data["altitude"] = altitude

    # sat_data["epoch"] = epoch
    # print(sat_data["latitude"][0])
    return sat_data

# Create your views here.
url_1 = 'https://celestrak.com/NORAD/elements/1999-025.txt'
url_2 = 'https://celestrak.com/NORAD/elements/2019-006.txt'
url_3 = 'https://celestrak.com/NORAD/elements/iridium-33-debris.txt'
url_4 = 'https://celestrak.com/NORAD/elements/cosmos-2251-debris.txt'


def debri_1(request):
    data = json.dumps(satelite_data(url_1))
    return HttpResponse(data)


def debri_2(request):
    data = json.dumps(satelite_data(url_2))
    return HttpResponse(data)


def debri_3(request):
    data = json.dumps(satelite_data(url_3))
    return HttpResponse(data)


def debri_4(request):
    data = json.dumps(satelite_data(url_4))
    return HttpResponse(data)


