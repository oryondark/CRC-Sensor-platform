import os, sys
import serial
import json
import requests
import time
import datetime

serial_path = 'USB serial port'
groupID = "crc_device_com"
ES_ENDPOINT = 'ElasticSearch Endpoint'
headers = {'Content-Type': 'application/json'}

while 1:
    sensing_data = serial.Serial(serial_path)
    string_form_sensing_data = sensing_data.readline().decode()
    sensing_data = json.loads(string_form_sensing_data)
    #print(sensing_data)

    sensing_data['groupID'] = groupID
    date = datetime.datetime.now().isoformat()
    sensing_data['date'] = date.split('.')[0]
    print(sensing_data)
    request = requests.post(ES_ENDPOINT, headers=headers, json=sensing_data)

    del sensing_data
