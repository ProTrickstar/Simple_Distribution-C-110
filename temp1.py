from os import name
import statistics
import pandas as pd
import plotly.figure_factory as ff
import csv
import random
import plotly.graph_objects as go

df = pd.read_csv("newdata.csv")
data = df["temp"].tolist()
dataSet = []

for i in range(0,100):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataSet.append(value)

mean = statistics.mean(dataSet)
std_deviation = statistics.stdev(dataSet)
print("Mean of the sample: ",mean)
print("Standard Deviation of the sample: ",std_deviation)    