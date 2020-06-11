from spark_ORM import SparkORM

weather_json = json.load(open("weather.json",'r'))
def driver_main_test():
    spark_setup = SparkORM('setup_test', '1g', '2', '1g', 'true')
