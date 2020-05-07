import requests as rq
import os

OPENAPI_FORECAST = 'http://api.openweathermap.org/data/2.5/forecast?'
OPENAPI_KEY = os.environ['OPENAPI_KEY']

def request_forecast(lat, lon):
    lat = "lat={}".format(lat)
    lon = "&lon={}".format(lon)
    appid = "&appid={}".format(OPENAPI_KEY)
    # join the request path
    join = OPENAPI_FORECAST + lat + lon + appid


    res = rq.post(join)
    content = res.content
    return content
