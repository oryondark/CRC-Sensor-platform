import requests as rq
import json
from django.db import models
from django import forms

class esSearch(object):
    def __init__(self):
        self.ES_ENDPOINT = 'Your ES ENDPOINT PATH'

        self.HOUR = [24 - i for i in range(0,24)]
        self.HOUR.sort()

        self.MINUTE = [12 - i for i in range(0,12)]
        self.MINUTE.sort()

        self.SECOND = [60 - i for i in range(0, 60)]
        self.SECOND.sort()

    def parse_temp_date(self, resp):
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

    def get_specify(self, now_date):
        cmd = "_search"
        url = self.ES_ENDPOINT + cmd
        headers = {'Content-Type': 'application/json'}
        query = {
            "size" : 100,
            "query":{
                "range":{
                    "date":{"gte":"2020-06-02 14:00:00",
                        "lt":"2020-06-02 15:00:00",
                        "format": "yyyy-MM-dd HH:mm:ss",
                        "time_zone": "+09:00"
                    }
                },
            },
            "_source":"temperature"
        }
        res = rq.get(url, data=json.dumps(query), headers=headers)
        return res

    def get_range(self, dates):
        cmd = "_search"
        url = self.ES_ENDPOINT + cmd
        headers = {'Content-Type': 'application/json'}
        query = {
            "query":{
                "range":{
                    "date":{
                        "gte": dates[0],
                        "lt" : dates[1]
                    }
                }
            }
        }

    def query_date_range(self, end, start=None, type='temperature'):
        if start == None:
            ymd, hms = end.split(" ")
            hms = hms.split(":")

            hour_idx = self.HOUR.index(int(hms[0]))
            hour_idx = hour_idx - 1
            hour_idx = hour_idx % 24

            #hms[0] = str(HOUR[hour_idx])
            start_hms = "{}:{}:{}".format(hms[0], hms[1], hms[2])
            start = ymd + " " + start_hms
        cmd = "_search"
        url = self.ES_ENDPOINT + cmd
        #print(url)
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
            "_source":type
        }
        print(url, start, end)

        res = rq.get(url, data=json.dumps(query), headers=headers)
        return res
