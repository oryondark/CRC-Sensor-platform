import os, sys
import time
import json, requests
from payloads import *
from GprmcConvert import *

'''
Development by Hjkim
This application parses GPGGA in gpsmon and uploads to elasticsearch on AWS.

Note that a user using this application have to do that the the gpsmon runs by the logcat-mode to save in local.
The app will parse for your local logdata periodically and insert to elasticsearch-store on AWS.
If you want save for this local log to backup, you can upload to s3 using trigger option.

E-mail : 4u_olion @ naver.com
Create by Bigdata KOOKMIN University Students.
'''

#Note that Test function don't use!!.

#latitude and longitutde decode
def decode_latitude(lat, printLog=False):
	lat = lat.split('.')

	if len(lat[0]) > 3 :
		if (len(lat[0]) / 2) != 2:
			# This loop round up if the lenth data has the half.
			r = 3
		else :
			r = 2

		lat_p = lat[0][:r]
		lat_g = round(int(lat[0][-2:] + lat[1]) / 60)

		if printLog == True :
			print('got a line in logdata')
			print('latitude position : {} // gradient : {}'.format(lat_p, lat_g))

		return (lat_p, lat_g)
	return (".", ".")

def decode_longitude(lon, printLog=False):
	lon = lon.split('.')

	if len(lon[0]) > 3 :
		if (len(lon[0]) / 2) != 2:
			# This loop round up if the lenth data has the half.
			r = 3
		else :
			r = 2

		lon_p = lon[0][:r]
		lon_g = round(int(lon[0][-2:] + lon[1]) / 60)

		if printLog == True :
			print('longitude position : {} // gradient : {}'.format(lon_p, lon_g))

		return (lon_p, lon_g)
	return (".", ".")

def convert_gpgga(logLine):
	# the GPGGA data looks like "$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47"
	splited_data = logLine.split(',')
	if splited_data[0] == "$GPRMC":
		# generates time-point to get the unit of time.
		# This conditional result will be returned list packed with "zu_t".
		zulu_time = decode_time(splited_data[1])
		return ["zu_t", zulu_time]

	elif splited_data[0] == "$GPGGA":
		lat = str(splited_data[2])
		lon = str(splited_data[4])
		lat = decode_latitude(lat)
		lon = decode_longitude(lon)

		return [splited_data[0], splited_data[1].split('.')[0], lat, lon]
		#convert_gpgga_payload
		#return convert_gpgga_payload(splited_data[0], splited_data[1].split('.')[0], lat, lon)
	else:
		pass

def convert_gpgga_test(logLine):
	# the GPGGA data looks like "$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47"
	splited_data = logLine.split(',')
	if splited_data[0] != "$GPGGA":
		return 0
	else:
		lat = str(splited_data[2])
		lon = str(splited_data[4])
		lat = decode_latitude(lat,True)
		lon = decode_longitude(lon, True)

		payload = convert_gpgga_payload(splited_data[0], splited_data[1].split('.')[0], lat, lon)
		payload = json.loads(json.dumps(payload))
		print(payload['data']['latitude'])
		return True

'''
assume that the sensor platform has low-power and low-resources.
So, i think that the application will be parsed the large data,
and then need to generative model.
'''
def generate_log(localPath):
	raise

def generate_log_test(localPath):
	# Logdata consisted of lineable data.
	# and row information, which involved coordinates, UTC etc, can be splited commba(= ',')
	# resamble to csv format.
	print('start parsing logdata')
	f = open(localPath, 'r')
	for perLine in f.readlines():
		# generative model
		yield perLine

def upload_to_S3():
	raise

def upload_to_dynamo():
	raise

def main():
	raise

ELASTIC_SEARCH_ENDPOINT = 'ELASTIC_SEARCH_ENDPOINT'
def upload_es(data_payload, indexing, svtype):
	'''
	payload = uploads information for saving data using REST API, which be made json.
	indexing = For searching key
	type = type of saving
	'''
	if (data_payload == None) or (json.loads(json.dumps(payload))['data']['latitude'] == '...'):
		print(payload)
		return

	index_payload = {
		"index": {"_index" : indexing, "_type" : svtype}
	}
	print(data_payload)
	r = requests.post(ELASTIC_SEARCH_ENDPOINT, json=data_payload)
	print(r.text)

#the entrypoint
def GpggaGenerator():
	#hard-cording path to test
	path = "./hjkim_gpsmon.log"
	test_logg_gen = generate_log_test(path)
	_ = next(test_logg_gen) # gpsmon would be got a column line at first. so and I need throw-out for this information.
	for gen in test_logg_gen:
		payload = convert_gpgga(gen)
		yield payload

#if you run by interprited script?
'''
if __name__ == "__main__":
	#hard-cording path to test
	path = "./hjkim_gpsmon.log"
	test_logg_gen = generate_log_test(path)
	_ = next(test_logg_gen) # gpsmon would be got a column line at first. so and I need throw-out for this information.
	count = 0
	for gen in test_logg_gen:
		# TODO: add to read data line
		#a = convert_gpgga_test(gen)
		#count += a
		payload = convert_gpgga(gen)
		rq_endpoint = upload_es(payload, "sencrc", "_doc")

		time.sleep(1)
		#TODO: add to remove logdata line
		#os.remove('')

	print("totally gps data : {}".format(count))

'''
