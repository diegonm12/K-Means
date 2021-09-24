import numpy as np
import matplotlib.pyplot as plt


## This function calculates the euclidean distance **********SHOULD BE THE SAME AS THE DISTANCE USED IN THE DOCUMENT***************
def euclidean_dist(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))


class K_Means:

    def __init__(self, K, max_iterations=100):  ##this this the initialization
        self.K = K
        self.max_iterations = max_iterations

        # This is a list of list of indices, where the final cluster will be. It is created empty and the "columns" len should be the same as the K clusters to be created.
        self.clusters = [[] for _ in
                         range(self.K)]  ## here we are creating an empty array for every cluster to be created.
        self.centroids = []  ##this will store actual samples or points of the data, which are the centers of the clusters.

    def predict(self, X):
        self.X = X
        self.rows, self.columns = X.shape

        # First, creating the centroids. Randomly pick some samples
        # random.choice Generates a random sample from a given 1-D array
        random_sample_index = np.random.choice(self.rows, self.K,
                                               replace=False)  # Here we use replace to avoid index duplicated. for example this line return: [0 2 1]
        self.centroids = [self.X[index] for index in
                          random_sample_index]  # ****************CHECK THIS***********************++
        # print(random_sample_index)
        # print(self.centroids)

        # this is the process to update clusters, centroids, check convergence.

        for _ in range(self.max_iterations):
            print("running")
            # update the clusters
            self.clusters = self.create_clusters(self.centroids)

            # now we need to update the centroids.
            previous_centroids = self.centroids  # the previous centroids are stored to use them to check the convergence
            self.centroids = self.get_centroids(
                self.clusters)  # we are calling this function to get the mean of the cluster

            # check if the centroids are converging
            if self.converge_centroids(previous_centroids, self.centroids):
                print("exit")
                break

        # now here we have the clusters labeled.
        return self.get_clusters_labeled(self.clusters)

    # This function creates the clusters using the closest_centroids function
    def create_clusters(self, centroids):
        clusters = [[] for _ in range(self.K)]  # cleaning data
        for index, point in enumerate(self.X):  # here we have the current index for the point
            centroid_index = self.closest_centroid(point,
                                                   centroids)  # this function find the closest centroid for every point
            clusters[centroid_index].append(
                index)  # here we are creating the clusters, using the index from the data set
        return clusters

    # This function find the closest centroid for every point using the euclidean distance
    def closest_centroid(self, point, centroids):
        distances = [euclidean_dist(point, centroids_point) for centroids_point in
                     centroids]  # we have here all the distances of every point to the centroid, we want the min
        closest = np.argmin(distances)
        return closest

    # This function is to get the mean of a cluster to update the centroid
    def get_centroids(self, clusters):
        centroids = np.zeros((self.K, self.columns))
        for cluster_index, cluster in enumerate(clusters):
            cluster_mean = np.mean(self.X[cluster],
                                   axis=0)  # remember that cluster are the indices, so that's why we are using "cluster" to get the mean
            centroids[cluster_index] = cluster_mean
        return centroids

    # this function returns true if the centroids converge, else false
    def converge_centroids(self, previous_centroids, centroids):
        distances = [euclidean_dist(previous_centroids[element], centroids[element]) for element in
                     range(self.K)]  # checking the distances between the old and current centroids
        converge = (sum(distances) == 0)  # if zero , the iteration converges
        return converge

    # this function return for each sample the cluster assigned
    def get_clusters_labeled(self, clusters):
        labeled = np.empty(
            self.rows)  # this is a empty array, labeled is the index of cluster the sample was assigned to
        for cluster_index, cluster in enumerate(clusters):
            for point_index in cluster:
                labeled[point_index] = cluster_index
        return labeled
