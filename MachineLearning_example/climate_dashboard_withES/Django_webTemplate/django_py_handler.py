from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse as httpJson# no refreshed
import time, datetime, json
from es_search import esSearch

#Abstract Class
# need to be loaded esSearch Class.
class BasicHandlerForm(esSearch):
    def read_es_tmpr(self, res, type):
        res = json.loads(res.content)
        values = []
        times = []
        for i in range(len(res['hits']['hits'])):
            try:
                data = res['hits']['hits'][i]['_source']
                values.append(data[type]['Value'])
                times.append(data[type]['createdTime'])
            except:
                pass

        return values, times

    def event_handler(self, requests):
        raise NotImplementedError

    def event_response(self, data):
        '''
        data == json object to sending client.
        '''
        raise NotImplementedError

#Humidity Class
class HandleClass(BasicHandlerForm):
    def __init__(self, cls_name):
        self._class_name = cls_name
        self._esSearch = esSearch()

    def __str__(self):
        return "It is a class to parse {} temperatures".format(self._class_name)

    def __repr__(self):
        return {"class_role", self._class_name}

    '''
    TODO: Handler 통합 필요.
    '''
    def event_handler(self, request):
        #query_date_range ( end_date, start_date)

        ## Test function
        #res_json = test_request_data_read(requests.GET)
        user_range_dict = requests.GET.dict()
        es_res = self._esSearch.query_date_range(user_range_dict['end_date'], user_range_dict['start_date'], type=user_range_dict['type'])
        values, times = self.read_es_tmpr(es_res, type)

        color_coding = ['rgba(255, 99, 132, 0.2)', 'rgba(153, 102, 255, 0.2)']
        edge_coding = ['rgba(255, 99, 132, 1)', 'rgba(153, 102, 255, 1)']
        sensorplt_form = {
         'data': values,
         'label':'sensorplatform',
         'name' :'sensorplatform',
         'backgroundColor': 'rgba(202, 201, 197, 0.5)',
         'borderColor': 'rgba(202, 201, 197, 1)',
         'pointBackgroundColor': 'rgba(202, 201, 197, 1)',
         'pointBorderColor': '#fff'
        }

        res_json = {
            'labels':times,
            'datasets':[
                sensorplt_form,
            ]
        }

        return httpJson(res_json)
