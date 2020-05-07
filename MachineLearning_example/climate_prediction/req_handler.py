from openweather_apiservice import *
import json

def parse_climate(res):
    state = res['cod']
    if state != 200:
        return "Failure read climate data from openweather platform... let is check your api state"

    length = res['cnt']
    location = res['city']

    for index in range(int(length)):
        
    return



'''
This handler should be imported to django module.
'''
def handler(lat, lon):
    res = request_forecast(lat, lon)
    res = json.loads(req)
    parse_climate(res)

    return
