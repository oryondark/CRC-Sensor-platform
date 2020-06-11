import requests as rq
import json
import os

OPENAPI_FORECAST = 'http://api.openweathermap.org/data/2.5/forecast?'
OPENAPI_KEY = os.environ['OPENAPI_KEY']
METEOSTAT_KEY = os.environ['METEO_KEY']

#0 is default
api_type = {
    0 : 'https://api.openweathermap.org/data/2.5/onecall?',
}

def request_forecast(lat, lon, type=0):

    OPENAPI_FORECAST = api_type[type]

    lat = "lat={}".format(lat)
    lon = "&lon={}".format(lon)
    exec = "&exclude=hourly,daily,current"
    appid = "&appid={}".format(OPENAPI_KEY)

    # join the request path
    join = OPENAPI_FORECAST + lat + lon + appid

    res = rq.post(join)
    content = res.content
    return content


'''
Meteostate API proivded free.
our last project that we implemente forecast analytics using OpenWeather API, It is not suitable for recommended system.
As well, openweather api isn't free about past. In this reason, we chose to use meteostat.
'''

def meteostate_search_state(lat, lon):
    url = 'https://api.meteostat.net/v1/stations/nearby?lat={}&lon={}&limit=100&key={}'.format(lat, lon, METEOSTAT_KEY)
    res = rq.post(url)
    json_meta = json.loads(res.content)

    #most nearly
    state = json_meta['data'][0]['id']
    return state

def request_historical(lat, lon, start, end):
    station = meteostate_search_state(lat, lon)
    url = 'https://api.meteostat.net/v1/history/daily?station={}&start={}&end={}&key={}'.format(station, start, end, METEOSTAT_KEY)
    res = rq.post(url)
    return res.content
