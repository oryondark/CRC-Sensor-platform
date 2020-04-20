from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient, AWSIoTMQTTClient
from OxhrmMonitor import OxiHRMonitor
import numpy as np
import time

clientid = 'basicPubSub2'
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

# parsing oximetry-heart-rate-log data
clss = OxiHRMonitor()
ctx = clss.serialContext('/dev/tty.KMU_MSPL-DevB')
g = clss.listen(ctx)
t_attr = None
while True:
	res = next(g)
	print('{"state"' + ':{"reported":' + '{"data": {"rate": "' + res[0] + '", "concen": "' + res[1][0] + '"}, "sensor": "oxhrm"}}}')
	testDevice_shadow.shadowUpdate(
		'{"state"' + ':{"reported":' + '{"data": {"rate": "' + res[0] + '", "concen": "' + res[1][0] + '"}, "sensor": "oxhrm"}}}',
		shadow_update_Callback_test, 5)
	print("hrm uploaded!")

	#time.sleep(1)
