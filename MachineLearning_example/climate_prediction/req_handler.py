from openweather_apiservice import *
import json

def handler(lat, lon):
    res = request_forecast(lat, lon)
    json.dumps(req, indent=4)
    return "success"
