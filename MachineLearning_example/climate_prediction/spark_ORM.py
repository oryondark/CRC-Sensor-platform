import pyspark
from pyspark.conf import SparkConf
from pyspark.sql import SparkSession
from datetime import datetime
import json
import os, sys

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
        
        self.spark = configure()

    def configure(self):
        conf = SparkConf().setMaster("local[*]").setAll([
            self.appName,
            self.executorMem,
            self.executorCore,
            self.executorCoreMax,
            self.driverMem,
            self.in_memory_compressed
        ])
        return SparkSession.builder.config(conf=conf).getOrCreate()
