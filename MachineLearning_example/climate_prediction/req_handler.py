from openweather_apiservice import *
from domestic_climate_api import DomestiClimate
import json
from spark_ORM import *
import time, datetime

#initiate for spark ORM
spark_setup = SparkORM('setup_test', '1g', '2', '1g', 'true')
spark = spark_setup.getSpark()
spark_ctx = spark_setup.getContext()

domestic_climate = DomestiClimate()

def kelvin_to_celsius(temp):
    return float(temp) - 273.15

def make_dataframe(res):
    '''
    using spark
    '''
    dtTemperatures = {}

    weather_dt = read_RDD(res, spark, spark_ctx)
    return weather_dt

def to_datetime(col, date):
    for idx, time in enumerate(times):
        day = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')
        times[idx] = day + " " + timeobj["시:분"]
    return times

def to_daily_temp(col, temperature_list):
    for temp in col:
        temperature_list.append(kelvin_to_celsius(temp[0])) # index numer 0 is a daily temperature
    return temperature_list

def handler(lat, lon, start_date, end_date):
    #res = request_forecast(lat, lon)
    #res = request_historical(lat, lon, )
    date = '202005221058'
    location_code = '108'
    term = '1'
    res = domestic_climate.get(date, term, location_code)
    res = json.loads(res)

    weather_df = make_dataframe(res)
    temp_col = spark_orm_domestic_temp(weather_df)
    time_col = spark_orm_domestic_date(weather_df)

    temp_col, date_set = standardize(temp_col, time_col)

    return {"temp_date": to_datetime(date_set, date),
            "temp_plot": temp_col}
