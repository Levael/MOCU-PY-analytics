import matplotlib.pyplot as chart


class DataVisualisation:
    def __init__(self, analysis_object, mode='release'):
        self._oculus_trials_total_times = analysis_object.oculus_trials_total_times
        self._moog_trials_total_times = analysis_object.moog_trials_total_times




    def DrawMoogAndOculusTotalTrialsTimes(self):
        chart.figure('Oculus & Moog trials total times')

        # oculus chart
        chart.subplot(2, 1, 1)
        chart.title('Oculus')
        #chart.xlabel('frames')
        #chart.ylabel(y_axis_name)
        x_axis = range(1, len(self._oculus_trials_total_times)+1)
        y_axis = self._oculus_trials_total_times
        chart.scatter(x_axis, y_axis, s=1)

        # moog chart
        chart.subplot(2, 1, 2)
        chart.title('Moog')
        # chart.xlabel('frames')
        # chart.ylabel(y_axis_name)
        x_axis = range(1, len(self._moog_trials_total_times) + 1)
        y_axis = self._moog_trials_total_times
        chart.scatter(x_axis, y_axis, s=1)

        chart.show()








    def MakePointedChart(self, data, number_of_charts = 1, index_in_figure = 1, chart_name = "", y_axis_name = ""):
        chart.subplot(1, number_of_charts, index_in_figure)
        chart.title('Total time: ' + str(round(sum(data), 2)) + 'ms')
        chart.xlabel('frames')
        chart.ylabel(y_axis_name)

        x_axis = range(1, len(data)+1)
        y_axis = data

        print(data)

        chart.scatter(x_axis, y_axis, s=1)

    def DrawChartAsAxes (self, data):
        chart.figure('')
        self.MakeChartAsAxes(data)
        #chart.title('Test')
        chart.xlabel('number of trials')
        chart.ylabel('trial total time')
        chart.show()


    def DrawCharts (self, data):
        list_of_trials = data

        chart.figure('Charts of ' + str(len(list_of_trials)) + ' last trials')

        for sub_chart in list_of_trials:
            self.MakeChartAsAxes(
                sub_chart,
                len(list_of_trials),
                list_of_trials.index(sub_chart)+1,
                '',
                'delay between frames (ms)')

        chart.show()