import boto3
import numpy as np

from req_handler import req

plots_1 = np.random.randint(1,10,5)
plots_2 = np.random.randint(1,10,5)

class StaticChartData_Test(BaseLineChartView):
    def __init__(self, xs_date, ys_openweather, ys_awses):
        self.xs = xs_date
        if isinstance(self.xs, list) is False:
            self.xs = list(self.xs)

        self.ys_0 = ys_openweather
        if isinstance(self.ys_0, list) is False:
            self.ys_0 = list(self.ys_0)

        self.ys_1 = ys_awses
        if isinstance(self.ys_1, list) is False:
            self.ys_1 = list(self.ys_1)

    def get_labels(self):
        # setup X-axis
        return self.xs

    def get_providers(self):
        # label of per data
        return ["line_{}".format(i) for i in range(int(len(self.xs)))]

    def get_data(self):
        # plot
        return [self.ys_0, self.ys_1]
