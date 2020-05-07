import boto3
import numpy as np

plots_1 = np.random.randint(1,10,5)
plots_2 = np.random.randint(1,10,5)

class StaticChartData_Test(BaseLineChartView):
    def get_labels(self):
        # setup X-axis
        return ["x1", "x2", "x3", "x4", "x5"]

    def get_providers(self):
        # label of per data
        return ["line_1", "line_2"]

    def get_data(self):
        # plot
        return [list(plots_1),
                list(plots_2)]
