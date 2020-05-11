from openweather_apiservice import *
import json

def kelvin_to_celsius(temp):
    return float(temperature) - 273.15

def parse_climate(res):
    '''
    using spark
    '''
    dtTemperatures = {}
    state = res['cod']
    if state != 200:
        return "Failure read climate data from openweather platform... let is check your api state"

    length = res['cnt']
    location = res['city']


    return dtTemperatures

'''
This handler should be imported to django module.
Openweather API can request using http endpoint, however you must need for api-key from generated there.
Note that the responsed temperature data is "Kelvin temperature".
so if you want to explain Celsius temperature, must change to celsius format.
principal = 286.37K − 273.15 = 13.22°C
'''
def handler(lat, lon):
    res = request_forecast(lat, lon)
    res = json.loads(res)

    pairs = parse_climate(res)

    return pairs
