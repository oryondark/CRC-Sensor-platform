'''
In this example, the ORM the sparksession read a qeury from json.
'''
from pyspark.sql import SparkSession

#Initate SparkSession and Context
conf = SparkConf().setAppName("crc-arduino-temp-rdd").setMaster("local[*]").setAll([('spark.executor.memory', '4g'),
                         ('spark.app.name', 'arduino-climate-rdd'),
                         ('spark.executor.cores', '4'),
                         ('spark.cores.max', '4'),
                         ('spark.driver.memory','4g'),
                         ('spark.sql.inMemoryColumnarStorage.compressed', 'true')])
spark = SparkSession.builder.config(conf=conf).getOrCreate()
sc = spark.sparkContext

def showing_schema(weather_json):
    '''
    json.load from object
    '''
    weather_df = sc.parallelize(weather_json).map(lambda x: json.dumps(weather_json))
    weather_df = spark.read.json(weather_df)
    weather_df.printSchema()

def showing_dataframe(weather_json):
    weather_df = sc.parallelize(weather_json).map(lambda x: json.dumps(weather_json))
    weather_df = spark.read.json(weather_df)
    weather_df.show()

def selecting_query(weather_json, column_name, column_name2, **kargs):
    weather_df = sc.parallelize(weather_json).map(lambda x: json.dumps(weather_json))
    weather_df = spark.read.json(weather_df)

    weather_df.select(weather_df[column_name][column_name2]).show()
    if int(len(kargs)) > 0:
        for key, value in kargs.items():
            weather_df.select(weather_df[key][value]).show()

def convert_to_datetime(weather_json):
    weather_df = sc.parallelize(weather_json).map(lambda x: json.dumps(weather_json))
    dt_test = weather_df.select(weather_df['current']['dt']).collect()[0]['current.dt']
    real_time = datetime.fromtimestamp(int(dt_test)).strftime('%Y-%m-%d %H:%M:%S')
    print(real_time)
