import pymongo
from random import randint


def save_results(identifier, clusters, set_to_plot, alive_indexes, samples_to_analyze, pids_array):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = myclient["results"]
    mycol = mydb["elements"]

    element_to_insert = {"ident":identifier, "clusters": clusters.tolist(), "set_to_plot": set_to_plot.tolist(), "alive_indexes": alive_indexes.tolist(),
                         "samples_to_analyze": samples_to_analyze.tolist(), "pids_array": pids_array}
    x = mycol.insert_one(element_to_insert)

def load_results(identifier):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = myclient["results"]
    mycol = mydb["elements"]

    myquery = {"ident": identifier}

    mydoc = mycol.find(myquery)

    for x in mydoc:
        return (x)

