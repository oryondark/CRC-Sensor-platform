# Usage ElasticSearch

### What is ElasticSearch?
**ElasticSearch** is an Open-Source based storage service to retrieve data from.<br>
This service consisted of REST API such as PUT, POST, GET, DELETE.<br>

### Simple Usage using cURL
```shell
curl -X GET 'https://search-crc-es-awscloud-wft3afe5m7g2wcw2jmwk5.ap-northeast-2.es.amazonaws.com/climate/_search' -H 'Content-Type: application/json' -d
'{"query":
  {"range":
    {"date":
      {"gte":"now-3d/d", "lt":"now/d"}
    }
  }
}'
```

### Make json form to request in python runtime
In this example, I will represent how a query use in ElasticSearch.
```python
import requests as rq
import json

ES_ENDPOINT = 'ENDPOINT' # Your Endpoint of ElasticSearch service

headers = {'Content-Type': 'application/json'}
query = {
    "size" : 1, # how to get an amount of data ?
    "query":{
        "range":{
            "date":{
                    "gte":"2015-12-01 06:00:00", # greater for
                    "lt":"2020-01-01 06:00:00", # less than for
                    "format": "yyyy-MM-dd HH:mm:ss", # data string format
                    "time_zone": "+09:00" # UTC to Korea TimeZone
                   }
        },
    }
}

res = rq.get(url, data=json.dumps(query), headers=headers)
```
