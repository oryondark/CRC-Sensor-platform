import boto3
import numpy as np
from req_handler import req

class StaticChartData_Test(BaseLineChartView):
    def __init__(self):
        res = handler(35, 139)
        self.dates = list(res['temp_date'])
        self.random_temp = list(np.random.randint(0,40,int(len(self.dates))))
        self.openweather_temp = list(res['temp_plot'])

    def get_labels(self):
        return self.dates

    def get_providers(self):
        # label of per data
        return ["openweather", "our sensorplatform"]

    def get_data(self):
        # plot
        return [self.openweather_temp, self.random_temp]
