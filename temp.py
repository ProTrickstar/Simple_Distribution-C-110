from os import name
import statistics
import pandas as pd
import plotly.figure_factory as ff
import csv
import random
import plotly.graph_objects as go

df = pd.read_csv("newdata.csv")
data = df["temp"].tolist()
population_mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print("Population mean: ",population_mean)
print("Standard Deviation:",std_deviation)

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],"temp",show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
    fig.show()