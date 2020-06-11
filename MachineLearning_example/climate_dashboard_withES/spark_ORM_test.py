'''
In this example, the ORM the sparksession read a qeury from json.
'''
from pyspark.conf import SparkConf
from pyspark.sql import SparkSession

#Initate SparkSession Environments and Context
conf = SparkConf().setMaster("local[*]").setAll([
                         ('spark.executor.memory', '4g'),
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

class SparkORM_SetupTest():
    def __init__(self):
        self.appName = ('spark.app.name', 'setup_test')
        self.executorMem = ('spark.executor.memory', '1g')
        self.executorCore = ('spark.executor.cores', '1')
        self.excutorCoreMax = ('spark.cores.max', '2')
        self.driverMem = ('spark.driver.memory', '1g')
        self.in_memory_compressed = ('spark.sql.inMemoryColumnarStorage.compressed', 'true')

        self._spark_conf = self._configure()

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

    def getContext(self):
        return self._spark_conf

    def inner_function(self):
        def _inner_test_1():
            print('hahahahah')
        def _inner_test_2():
            print('hjkim is a man of handsome.')
        _inner_test_1()
        _inner_test_2()


def spark_orm_domestic_temp_test():
    # get data from open URL
    res = rq.post('https://www.weather.go.kr/cgi-bin/aws/nph-aws_txt_min_guide_test?202005221058&0&MINDB_1M&108&a&K')
    content = res.content
    print(content)

    #create table data from HTML ( crawling )
    table_data = [[cell.text for cell in row("td")] for row in BeautifulSoup(content)("tr")]
    for td in table_data[1:]:
        print(td)

    weather_td = table_data[1:]
    keys = weather_td[0]
    datas = weather_td[1:]

    weather_db = []
    for data in datas:
        i = 0
        weather_res = {}
        for key in keys:
            if (i == 9) or (i == 11):
                weather_res[key] = [data[i] , data[i+1]]
                i += 1
            else:
                if data[i] == '시:분':
                    weather_res[key] =
                weather_res[key] = data[i]
            weather_db.append(weather_res)
            i += 1
    print(len(weather_db))
    print(json.dumps(weather_db))

    # Submission job to spark SQL, then read using rdd
    weather_df = sc.parallelize(weather_db).map(lambda x : json.dumps(x))
    print(weather_df.select(weather_df['기온']).collect())


def spark_orm_test():
    import json
    from spark_ORM import *

    weather_json = json.load(open("weather.json",'r'))
    spark_setup = SparkORM('setup_test', '1g', '2', '1g', 'true')

    spark = spark_setup.getSpark()
    spark_ctx = spark_setup.getContext()

    dt = read_RDD(weather_json, spark, spark_ctx)
    '''
    output:
    DataFrame[]
    '''
