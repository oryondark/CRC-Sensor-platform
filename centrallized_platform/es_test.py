import os, sys
import serial
import json
import requests
import time
import datetime

serial_path = 'USB_SerialPort'
groupID = "crc_device_com"

#in this example, will not increased index number.
ES_ENDPOINT_TEST = 'ElasticSearch Endpoint' #POST
headers = {'Content-Type': 'application/json'}

# Just one time run.
while 1:
    sensing_data = serial.Serial(serial_path)
    print(sensing_data)
    string_form_sensing_data = sensing_data.readline().decode()
    sensing_data = json.loads(string_form_sensing_data)
    print(sensing_data)

    sensing_data['groupID'] = groupID
    date = datetime.datetime.now().isoformat()
    sensing_data['timestamp'] = date.split('.')[0]
    print(sensing_data)

    #request_test = requests.put(ES_ENDPOINT_TEST, headers=headers, json=sensing_data)
    request_test = requests.post(ES_ENDPOINT_TEST, headers=headers, json=sensing_data)

    del sensing_data
