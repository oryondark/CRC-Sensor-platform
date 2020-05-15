import requests as rq
import os

OPENAPI_FORECAST = 'http://api.openweathermap.org/data/2.5/forecast?'
OPENAPI_KEY = os.environ['OPENAPI_KEY']

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
