import requests as rq
import json
from django.db import models
from django import forms

ES_ENDPOINT = 'ENDPOINT' # Your Endpoint of ElasticSearch service

def date_range_search_test(date_range):
    cmd = "_search"
    url = ES_ENDPOINT + cmd
    print(url)
    headers = {'Content-Type': 'application/json'}
    query = {"query":
                {"range":
                    {"date":
                        {"gte":"now-3d/d", "lt":"now/d"}
                    }
                }
            }

    #you should be build json object query.
    res = rq.get(url, data=json.dumps(query), headers=headers)
    print(res.content)


def query_date_range_test(ES_ENDPOINT):
    cmd = "_search"
    url = ES_ENDPOINT + cmd
    print(url)

    HOUR = [24 - i for i in range(0,24)]
    HOUR.sort()

    ## Time Generate
    end = "2020-06-02 15:00:00"

    start = None
    ymd, hms = end.split(" ")
    hms = hms.split(":")

    hour_idx = HOUR.index(int(hms[0]))
    hour_idx = hour_idx - 1
    hour_idx = hour_idx%24

    hms[0] = str(HOUR[hour_idx])
    start_hms = "{}:{}:{}".format(hms[0], hms[1], hms[2])
    start = ymd + " " + start_hms

    ## Header & Parameter
    headers = {'Content-Type': 'application/json'}
    query = {
        "size" : 1, #get only one data
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
    print(res.content)

#Django
class es_template_test(model.Model):
    def __init__(self):
        self.ES_ENDPOINT = 'ENDPOINT'

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
        return query
