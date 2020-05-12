import pyspark
from pyspark.conf import SparkConf
from pyspark.sql import SparkSession
from datetime import datetime
import json
import os, sys


# As Spark Session, We choose SQL method to access our solver.
# It's class for Spark SQL to process Json type of climate.
class SparkORM(object):
    def __init__(self, weather_json, appName, exmemSize, excoreNum, driveMem, inmemCompress):
        self.weather_json = weather_json
        self.appName = ('spark.app.name', appName)
        self.executorMem = ('spark.executor.memory', exmemSize)
        if excoreNum > 2:
            raise "It can not set up core Num more : [2]"
        self.executorCore = ('spark.executor.cores', excoreNum)
        self.excutorCoreMax = ('spark.cores.max', '2'),
        self.driverMem = ('spark.driver.memory', driveMem)
        self.in_memory_compressed = ('spark.sql.inMemoryColumnarStorage.compressed', inmemeCompress)

        self._spark_conf = self._configure()
        self._result_obj = None

    def _configure(self):
        conf = SparkConf().setMaster("local[*]").setAll([
            self.appName,
            self.executorMem,
            self.executorCore,
            self.executorCoreMax,
            self.driverMem,
            self.in_memory_compressed
        ])
        return SparkSession.builder.config(conf=conf).getOrCreate()

    def getContext(self):
        '''
        Get Spark Context
        '''
        return self._spark_conf.sparkContext

    def read_RDD():
        '''
        Re construction from Json obejct.
        'parallelize' api is one of the RDD's functions.
        It is reconstruction from your iterable obejct or dictionary.
        And then that makes a collection from your distributed dataset on parallelized computation.
        '''
        df = sc.parallelize(weather_json).map(lambda x: json.dumps(weather_json)) # Transforms
        df = spark.read.json(weather_df) # Read the DataFrame copied form of Json.

        #just return only dataframe
        return df

    def single_query_ORM(self, df, **kargs):
        '''
        kargs type is dictionary.
        This function only return to list( using collect func )
        '''
        def _sequential_iter(key_1, key_2):
            v = df.select(weather_df['current']['dt']).collect()
            return v
        def _query_error():
            return {"state" : "assembled query error"}

        if int(len(kargs)) > 2:
            k_list = list(kargs.keys())
            key_1 = kargs.pop(k_list[0])
            key_2 = kargs.pop(k_list[1])
            del k_list # Remove the overwirting data.
            result = _sequential_iter(key_1, key_2)
        else:
            result = _query_error()

        return result

    def multiply_query_ORM(self):
        raise "no impl."
