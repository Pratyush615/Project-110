import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
mean = statistics.mean(data)
std_dev = statistics.stdev(data)
print("Population Mean: ",mean)
print("Population Standard Deviation: ",std_dev)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df=mean_list
    mean = statistics.mean(mean_list)
    print("mean of sampling distribution: ",mean)
    fig = ff.create_distplot([df],["reading_time"],show_hist = False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    std_dev = statistics.stdev(mean_list)
    print("standard deviation of sampling distribution: ", std_dev)
    show_fig(mean_list)
setup()