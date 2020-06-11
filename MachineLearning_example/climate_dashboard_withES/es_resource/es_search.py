import requests as rq
import json
from django.db import models
from django import forms

ES_ENDPOINT = 'HOST' # Your Endpoint of ElasticSearch service
HOUR = [24 - i for i in range(0,24)]
HOUR.sort()
MINUTE = [12 - i for i in range(0,12)]
MINUTE.sort()
SECOND = [60 - i for i in range(0, 60)]
SECOND.sort()

def parse_temp_date(resp):
    es_temp = []
    es_date = []
    for data in content['hits']['hits']:
        try:
            temp = data['_source']['temperature']['Value']
            date = data['_source']['temperature']['createdTime']
            es_temp.append(float(temp))
            es_date.append(date)
            #print("temper : ", temp, " date : ", date)
        except:
            print("occurs key error : ", data)
    return es_temp, es_date

def query_date_range(end, start=None):
    if start == None:
        ymd, hms = end.split(" ")
        hms = hms.split(":")

        hour_idx = HOUR.index(int(hms[0]))
        hour_idx = hour_idx - 1
        hour_idx = hour_idx%24

        hms[0] = str(HOUR[hour_idx])
        start_hms = "{}:{}:{}".format(hms[0], hms[1], hms[2])
        start = ymd + " " + start_hms
    cmd = "_search"
    url = ES_ENDPOINT + cmd
    print(url)
    headers = {'Content-Type': 'application/json'}
    query = {
        "size" : 100,
        "query":{
            "range":{
                "date":{"gte":start,
                        "lt":end,
                        "format": "yyyy-MM-dd HH:mm:ss",
                        "time_zone": "+09:00" # UTC to Korea TimeZone
                       }
            },
        },
        "_source":"temperature"
    }

    res = rq.get(url, data=json.dumps(query), headers=headers)
    return res
