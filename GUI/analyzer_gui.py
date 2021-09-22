import tkinter as tk
from tkinter import filedialog as fd

import numpy as np

from fields_analyzer.json_reader import read_json_file
from fields_analyzer.fields_analyzer import select_fields_to_analyze
from algorithm.K_Means import K_Means
from sklearn.datasets import make_blobs
from results_and_plotter.results_output import plotter


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('Data Clustering Analyzer')
        self.geometry('500x100')

        # label
        self.label = tk.Label(self, text='Please select the JSON file where the data to analyze is')
        self.label.pack()

        # button
        self.button = tk.Button(self, text='Browse..', command=self.browse_data)
        self.button.pack()

    # here we browse the json file and then call the json reader.
    def browse_data(self):
        filetypes = (
            ('text files', '*.json'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open JSON file',
            initialdir='/home/dnavarro/PycharmProjects/k_means_clustering/data',
            filetypes=filetypes)
        json_data = read_json_file(filename)
        samples_to_analyze = select_fields_to_analyze(json_data)
        K_Means_ = K_Means(K=4,max_iterations=150)
        pred = K_Means_.predict(samples_to_analyze)
        plotter(pred.astype(int),samples_to_analyze)





