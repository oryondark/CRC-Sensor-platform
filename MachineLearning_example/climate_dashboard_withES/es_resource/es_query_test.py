
'''
검색 날짜를 기준으로
엘라스틱서치에서 gte는 크거나 같은 날
lt는 그보다 낮은 날을 기준으로 검색함.
타임존은 한국 시간에 맞춰야하므로 UTC +9
'''
def query_date_range_test(start_d, end_d):
    cmd = "_search"
    url = ES_ENDPOINT + cmd
    print(url)
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
    content = res.content

'''
엘라스틱 서치 결과를 Json형태로 반환하고 읽기를 위한 검토 함수
'''
def read_json_from_ES(resp_content):
    '''
    import requests as rq
    rs = rq.get('endpoint')
    read_json_from_ES(rs)
    '''
    res = json.loads(jsonObj.content) # read cotent from responsed object
    res = res['hits']['hits'][0]['_source'] # Default parsing form to read ES real data.
    for k in res:
        key = k
        print(res[k])

'''
Class bon
'''
class es_template_test():
    def __init__(self):
        self.ES_ENDPOINT = 'ElasticSearch ENDPOINT'

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
