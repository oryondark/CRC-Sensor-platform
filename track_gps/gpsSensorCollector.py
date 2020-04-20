from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient, AWSIoTMQTTClient
from GpggaConvert import *
import numpy as np
import time

clientid = 'basicPubSub'
#HOST = 'arpzdkw2j3op9-ats.iot.ap-northeast-2.amazonaws.com'
HOST = 'iotcore.iot.ap-northeast-2.amazonaws.com'
CA = 'root-CA.crt'
PRI_KEY = 'private.key'
CERT_KEY = 'cert.pem'

HANDELR = 'iotcore'

#the print of state result after the method of shadowUpdate.
def shadow_update_Callback_test(payload, response_status, token):
	print("Callback Test Init")
	print("Object Action Named Rule")
	print("$aws/things/crc-hj-rasp/shadow/update/#")
	print("payload = {}".format(payload))
	print("response_status = {}".format(response_status))
	#print("token = {}".format(token))


#Device connect to AWS IoT Core applicatioin
myShadowClient = AWSIoTMQTTShadowClient(clientid, useWebsocket=True)
print('set client id')
myShadowClient.configureEndpoint(HOST, 443)
print('set configuration endpoint')
myShadowClient.configureCredentials(CA, PRI_KEY, CERT_KEY)
print('done certificatation')
myShadowClient.configureAutoReconnectBackoffTime(1, 32, 20)
myShadowClient.configureConnectDisconnectTimeout(10)
myShadowClient.configureMQTTOperationTimeout(5)
myShadowClient.connect()
print('connected!!')
testDevice_shadow = myShadowClient.createShadowHandlerWithName( HANDELR, True )

# parsing gps-log data
g = GpggaGenerator() #GpggaConvert.GpggaEngerator()
t_attr = None
while True:
	payload = next(g)

	if payload == None:
		print(payload)
		pass

	elif (len(payload) == 2) and (payload[0] == 'zu_t'):
		t_attr = str(payload[1])
		print(t_attr)
		pass

	elif payload[2] == '...':
		print(payload)
		pass

	else:
		gps = payload[0]
		utc = payload[1]
		lat_0 = payload[2][0]
		lat_1 = payload[2][1]
		latitude = "{}.{}".format(str(lat_0), str(lat_1))
		lon_0 = payload[3][0]
		lon_1 = payload[3][1]
		longitude = "{}.{}".format(str(lon_0), str(lon_1))

		print('{"state"' + ':{"reported":' + '{"data":{"gps": "' + gps + '", "latitude": "' + latitude + '", "longitude": "' + longitude + '", "zu_t": "' + t_attr + '"}}}}')
		testDevice_shadow.shadowUpdate(
			'{"state"' + ':{"reported":' + '{"data":{"gps": "' + gps + '", "latitude": "' + latitude + '", "longitude": "' + longitude + '", "zu_t": "' + t_attr + '", "user": "hjkim"' + '}}}}',
			shadow_update_Callback_test, 5)
		print("gps uploaded!")

	time.sleep(1)
