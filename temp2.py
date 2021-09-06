import statistics
import pandas as pd
import plotly.figure_factory as ff
import csv
import random
import plotly.graph_objects as go

df = pd.read_csv("newdata.csv")
data = df["temp"].tolist()
#counter = 1
#d = 1/10 * std_deviation of population
def random_set_of_mean(counter):

    dataSet = []

    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataSet.append(value)

    mean = statistics.mean(dataSet)
    return mean


def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(mean_list)
    std_deviation = statistics.stdev(mean_list)
    print("Standard Deviation of the data is: ",std_deviation)
    print("Mean of the data is: ", mean)
    fig = ff.create_distplot([df], ["temp"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[
                  0, 1], mode="lines", name="MEAN"))
    fig.show()


def setup():
    mean_list = []
    for i in range(0, 1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)


setup()
