import json

#request_forecast()
def req_forecast_test(lat, lon):
    dump = open('./test_dummy.json', 'r')
    dump = dump.read()
    return dump

def handler_test(lat, lon):
    print("get latitude {} / longitude {}".format(lat, lon))
    print(" but this testcode will be used for dump data")
    print("request climate")
    res = req_forecast_test(lat, lon)
    print("responsed\n")
    print(res)

    print("to pretty")
    json_res = json.loads(res)
    print(json.dumps(json_res, indent=4))

    return json_res


def parse_climates_data(res):
    print("parse Keys : {}".format(res.keys()))
    print("so you should be parsed for 'list'.")
    print("type of climate data : {} and length : {}".format(type(res['list']), len(res['list'])))
    print("picked data from listed climate : {} \nand keys : {}".format(res['list'][0], res['list'][0].keys()))

    for i in range(int(res['cnt'])):
        datetime = res['list'][i]['dt']
        temperature = res['list'][i]['main']['temp']
        print('{} : [ date: {} , temperature: {} ]'.format(i, datetime, temperature))
