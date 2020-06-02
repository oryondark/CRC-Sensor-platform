import requests as rq
from bs4 import BeautifulSoup
import json
'''
crawling weather data from domestic climate center
'''
class DomestiClimate(object):
    def __init__(self):
        self.data = None

    def get(self, date, term, location_code):
        #'https://www.weather.go.kr/cgi-bin/aws/nph-aws_txt_min_guide_test?202005221058&0&MINDB_1M&108&a&K'
        endpoint = 'https://www.weather.go.kr/cgi-bin/aws/nph-aws_txt_min_guide_test?{}&0&MINDB_{}M&{}&a&K'.format(date, term, location_code)
        req = rq.post(endpoint)

        table_data = [[cell.text for cell in row("td")] for row in BeautifulSoup(req.content)("tr")]

        weather_td = table_data[1:]
        keys = weather_td[0]
        climate_set = weather_td[1:]

        weather_dict = []
        for data in climate_set:
            i = 0
            weather_res = {}
            for key in keys:
                if (i == 9) or (i == 11):
                    # if a key has two values,
                    weather_res[key] = [data[i] , data[i+1]]
                    i += 1
                else:
                    weather_res[key] = data[i]
                weather_dict.append(weather_res)
                i += 1

        return weather_dict
