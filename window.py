import tkinter as tk
from tkinter import ttk
from tkinter import N, E, S, W

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np

import os
import json
from datetime import datetime

# Initiate the window
window = tk.Tk()
window.title('ReMood Demo')
window.state('zoomed')

# Set up the Window frame structure
mainframe = ttk.Frame(window, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))


def parse_days_data():
    filename = 'days_remood.json'
    if os.path.exists(filename):
        with open(filename) as f:
            days_json = json.loads(f.read())
        datetime_days_json = dict(((datetime.strptime(k, '%d/%m/%Y'), float(v))
                                   for (k, v) in days_json.items()))

        return datetime_days_json
    else:
        # todo: message in status box alerting days file does not exist!
        pass


def graph_all_days(*args):
    print('graph here')

    # fetch the days data
    days_json = parse_days_data()
    x, y = zip(*sorted(days_json.items()))
    print(days_json)

    # set up the figure with key days data
    fig = Figure(figsize=(16,8), dpi=100)
    fig.add_subplot(111).plot(x, y)

    # add a medium line
    fig.axes[0].axhline(5.0, color='black', ls='--')
    fig.axes[0].fill_between(x, y, alpha=0.5)

    # create the canvas
    canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
    canvas.get_tk_widget().grid(row=2, column=1)
    canvas.draw()

    # add the toolbar to the tkinter grid on the row below the canvas
    toolbar = NavigationToolbar2Tk(canvas, window, pack_toolbar=False)
    toolbar.grid(row=3, column=1)
    toolbar.update()


ttk.Button(mainframe, text="Graph All Days", command=graph_all_days).grid(column=1, row=1, sticky=W)



# create window
window.mainloop()
