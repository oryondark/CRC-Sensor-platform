import requests
import json
import os, sys
from payloads import *
ELASTIC_SEARCH_ENDPOINT = 'https://elasticsearch_endpoint.ap-northeast-2.es.amazonaws.com/crcgps/'

def all_query(size):
	payloads = read_all(size)
	r = requests.post(ELASTIC_SEARCH_ENDPOINT + "_search", json=payloads)
	print(len(json.loads(json.dumps(r.json()))['hits']['hits']))

def count():
	payloads = count_payload()
	r = requests.get(ELASTIC_SEARCH_ENDPOINT + "_search", json=payloads)
	body = r.json()
	return json.loads(json.dumps(body))['hits']['total']


if __name__ == "__main__":
	cnt = count()
	size = cnt
	all_query(size)
