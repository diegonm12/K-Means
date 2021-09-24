import numpy as np


def cluster_results(clusters, pids_array):
    clusters_pids = [[] for _ in range(np.amax(clusters) + 1)]  ## here we create the arrays where the pids will be
    ## the index is going to be the number of the cluster
    for element in range(len(clusters)):
        clusters_pids[clusters[element]].append(pids_array[element])  ## add the pids to the clusters_pids

    # here we create it as an dictionary
    print(clusters_pids)
    clusters_dict = {i: clusters_pids[i] for i in range(0, len(clusters_pids))}
    print(clusters_dict)
