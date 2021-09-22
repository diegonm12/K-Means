import matplotlib.pyplot as plot
import numpy as np
import random


def plotter (clusters, array_to_analyze):
    print(clusters)
    print(array_to_analyze)
    if len(array_to_analyze[0]) == 3:
        fig = plot.figure()
        ax = fig.add_subplot(projection='3d')
        max_cluster = np.amax(clusters) + 1
        colormap = []
        for clusters_values in range(max_cluster):
            r = random.random()
            b = random.random()
            g = random.random()
            color = (r, g, b)
            colormap.append(color)
            plot.xlim(0, 100)
            plot.ylim(0, 100)
        for row in range(len(array_to_analyze)):
            ax.scatter(array_to_analyze[row][0],array_to_analyze[row][1],array_to_analyze[row][2], c = [colormap[clusters[row]]])
        plot.show()
    elif len(array_to_analyze[0]) == 2:
        fig = plot.figure()
        ax = fig.add_subplot()
        max_cluster = np.amax(clusters) + 1
        colormap = []
        for clusters_values in range(max_cluster):
            r = random.random()
            b = random.random()
            g = random.random()
            color = (r, g, b)
            colormap.append(color)
        for row in range(len(array_to_analyze)):
            ax.scatter(array_to_analyze[row][0],array_to_analyze[row][1], c = [colormap[clusters[row]]])
            plot.xlim(0, 100)
            plot.ylim(0, 100)
            ax.set_aspect('equal', adjustable='box')
        plot.show()
    else:
        print("The result cannot be graphed")

