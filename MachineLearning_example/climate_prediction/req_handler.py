from openweather_apiservice import *
import json
from spark_ORM import *

#initiate for spark ORM
spark_setup = SparkORM('setup_test', '1g', '2', '1g', 'true')
spark = spark_setup.getSpark()
spark_ctx = spark_setup.getContext()

def kelvin_to_celsius(temp):
    return float(temp) - 273.15

def make_dataframe(res):
    '''
    using spark
    '''
    dtTemperatures = {}
    state = res['cod']
    if state != 200:
        return "Failure read climate data from openweather platform... let is check your api state"

    weather_dt = read_RDD(res, spark, spark_ctx)
    return weather_dt

def to_datetime(col, datetime_list):
    for dt in col:
        datetime_list.append(datetime.fromtimestamp(int(dt)).strftime('%Y-%m-%d %H:%M:%S'))
    return datetime_list

def to_daily_temp(col, temperature_list):
    for temp in col:
        temperature_list.append(kelvin_to_celsius(temp[0])) # index numer 0 is a daily temperature
    return temperature_list

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

    weather_dt = make_dataframe(res)
    col_datetime = single_query_ORM(weather_dt, key_1='daily', key_2='dt')
    col_temperature = single_query_ORM(weather_dt, key_1='daily', key_2='temp')
    datetime_list = []
    temperature_time = []
    return {"temp_date": to_datetime(col_datetime, datetime_list),
            "temp_plot": to_daily_temp(col_temperature, temperature_time)}
