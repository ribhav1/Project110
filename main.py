import csv
import random
import statistics
import pandas as pd
import plotly.figure_factory as ff

file_data = pd.read_csv('medium_data.csv')

data = file_data['reading_time'].tolist()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean


def setup():
    mean_list = []
    for i in range(0, 100):
        set_of_mean = random_set_of_mean(30)
        mean_list.append(set_of_mean)
    
    show_fig(mean_list)


def show_fig(mean_list):
    fd = mean_list
    mean = statistics.mean(mean_list)
    figure = ff.create_distplot([fd], ['reading_time'], show_hist=False)
    figure.show()

setup()