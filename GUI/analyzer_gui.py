import tkinter as tk
from tkinter import filedialog as fd

import numpy as np

from fields_analyzer.json_reader import read_json_file
from fields_analyzer.fields_analyzer import select_fields_to_analyze
from algorithm.K_Means import K_Means
from results_and_plotter.clusters_results import cluster_results
from results_and_plotter.results_output import plotter
from results_and_plotter.save_results import save_results,load_results


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.size = '500x300'
        # configure the root window
        self.title('Data Clustering Analyzer')
        self.geometry(self.size)

        # label
        self.label = tk.Label(self, text='Please select the JSON file where the data to analyze is')
        self.label.pack( padx=10, pady=10)

        # button
        self.button = tk.Button(self, text='Browse..', command=self.browse_data)
        self.button.pack( padx=10, pady=10)

        # label
        self.label = tk.Label(self, text='Or load a previous execution, entering the identifier')
        self.label.pack(padx=10, pady=10)

        self.label = tk.Label(self, text="Identifier")
        self.label.pack()

        self.entry2 = tk.Entry(self, )
        self.entry2.pack()

        # button
        self.button1 = tk.Button(self, text='Load..', command=self.load_data)
        self.button1.pack(padx=10, pady=10)

        # check_box
        self.save_exe = 0
        self.checkbox = tk.Checkbutton(self, text="Save execution", variable=self.save_exe, onvalue=1, offvalue=0,
                                       command=self.isChecked)
        self.checkbox.pack( padx=10, pady=10)

        self.label = tk.Label(self,text = "Identifier")

        self.entry = tk.Entry(self, )

    def isChecked(self):
        if self.save_exe == 1:
            self.save_exe = 0
            self.entry.pack_forget()
            self.label.pack_forget()
        else:
            self.save_exe = 1
            self.entry.pack()
            self.label.pack()

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
        samples_to_analyze, pids_array = select_fields_to_analyze(json_data)
        set_to_plot, alive_indexes = np.unique(samples_to_analyze, axis=0, return_index=True)
        K_Means_ = K_Means(K=7, max_iterations=150)
        pred = K_Means_.predict(samples_to_analyze)

        if self.save_exe == 1:
            save_results(self.entry.get(),pred.astype(int), set_to_plot, alive_indexes, samples_to_analyze, pids_array)
        cluster_results(pred.astype(int), pids_array)
        plotter(pred.astype(int), set_to_plot, alive_indexes)


    def load_data(self):
        if len(self.entry2.get()) > 0:
            dp = load_results(self.entry2.get())
            cluster_results(dp["pred"], dp["pids_array"])
            plotter(dp["clusters"], dp["set_to_plot"], dp["alive_indexes"])





