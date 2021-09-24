import matplotlib.pyplot as plot
import numpy as np
import random


def plotter(clusters, array_to_analyze, valid_index):
    # here we are going to clean the cluster array according to the valid_index array
    cluster_cleaned = np.array(clusters)[valid_index]
    i = 0
    if len(array_to_analyze[0]) == 3:
        fig = plot.figure()
        ax = fig.add_subplot(projection='3d')
        max_cluster = np.amax(cluster_cleaned) + 1
        colormap = []
        for clusters_values in range(max_cluster):
            r = random.random()
            b = random.random()
            g = random.random()
            color = (r, g, b)
            colormap.append(color)
        for row in range(len(array_to_analyze)):
            print(i)
            i = i + 1
            ax.scatter(array_to_analyze[row][0], array_to_analyze[row][1], array_to_analyze[row][2],
                       c=[colormap[cluster_cleaned[row]]])
        plot.show()
    elif len(array_to_analyze[0]) == 2:
        fig = plot.figure()
        ax = fig.add_subplot()
        max_cluster = np.amax(cluster_cleaned) + 1
        colormap = []
        for clusters_values in range(max_cluster):
            r = random.random()
            b = random.random()
            g = random.random()
            color = (r, g, b)
            colormap.append(color)
        for row in range(len(array_to_analyze)):
            print(i)
            i = i + 1
            ax.scatter(array_to_analyze[row][0], array_to_analyze[row][1], c=[colormap[cluster_cleaned[row]]])
        plot.show()
    else:
        print("The result cannot be graphed")
