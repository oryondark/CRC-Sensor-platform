import pyspark
from pyspark.conf import SparkConf
from pyspark.sql import SparkSession
from datetime import datetime
import json
import os, sys
import numpy as np


# As Spark Session, We choose SQL method to access our solver.
# It's class for Spark SQL to process Json type of climate.
class SparkORM(object):
    #Usage:
    #spark = sparkORM.getSpark()
    #spark_ctx = sparkORM.getContext()
    def __init__(self, appName, exmemSize, excoreNum, driveMem, inmemCompress):
        self.appName = ('spark.app.name', appName)
        self.executorMem = ('spark.executor.memory', exmemSize)
        if int(excoreNum) > 2:
            raise "It can not set up core Num more : [2]"
        self.executorCore = ('spark.executor.cores', excoreNum)
        self.excutorCoreMax = ('spark.cores.max', '2')
        self.driverMem = ('spark.driver.memory', driveMem)
        self.in_memory_compressed = ('spark.sql.inMemoryColumnarStorage.compressed', inmemCompress)

        self._spark = self._configure()
        self._result_obj = None

    def _configure(self):
        conf = SparkConf().setMaster("local[*]").setAll([
            self.appName,
            self.executorMem,
            self.executorCore,
            self.excutorCoreMax,
            self.driverMem,
            self.in_memory_compressed
        ])
        return SparkSession.builder.config(conf=conf).getOrCreate()
    def getSpark(self):
        return self._spark

    def getContext(self):
        '''
        Get Spark Context
        '''
        return self._spark.sparkContext

def read_RDD(jsonObj, spark, context):
    '''
    Re construction from Json obejct.
    'parallelize' api is one of the RDD's functions.
    It is reconstruction from your iterable obejct or dictionary.
    And then that makes a collection from your distributed dataset on parallelized computation.
    '''
    df = context.parallelize(jsonObj).map(lambda x: json.dumps(jsonObj)) # Transforms
    df = spark.read.json(df) # Read the DataFrame copied form of Json.
    #just return only dataframe
    return df

def spark_orm_domestic_temp(df):
    temp_objs = df.select(df['기온']).collect()
    for idx, obj in enumerate(temp_objs):
        temp_objs[idx] = obj['기온']
    return temp_objs

def spark_orm_domestic_date(df):
    time_objs = df.select(df['시:분']).collect()
    for idx, obj in enumerate(time_objs):
        time_objs[idx] = obj['시:분']
    return time_objs

def standardize(temps, times):
    pivot = 0
    date_set = []
    temp_set = []

    stack = []

    time_cache = None
    while temps:
        time = times.pop(0)
        temp = temps.pop(0)
        if time_cache == None:
            time_cache = time

        if temp == ".":
            continue

        if time_cache != time:
            if len(stack) != 0:
                date_set.append(time)
                temp_set.append(np.mean(stack, dtype=np.float16))
                del stack
                stack = []

        time_cache = time
        stack.append(float(temp))

    return date_set, temp_set


def single_query_ORM(df, **kargs):
    '''
    kargs type is dictionary.
    This function only return to list( using collect func )
    '''
    result = None
    def _sequential_iter(key_1, key_2):
        v = df.select(df[key_1][key_2]).collect()[0]["{}.{}".format(key_1, key_2)]
        return v
    def _query_error():
        return {"state" : "assembled query error"}
    if int(len(kargs)) >= 2:
        k_list = list(kargs.keys())
        key_1 = kargs.pop(k_list[0])
        key_2 = kargs.pop(k_list[1])
        del k_list # Remove the overwirting data.
        result = _sequential_iter(key_1, key_2)
    elif int(len(kargs)) < 2:
        result = _query_error()
    return result

def multiply_query_ORM():
    raise "no impl."
