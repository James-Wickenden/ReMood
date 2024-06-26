import tkinter as tk
from tkinter import ttk
from tkinter import N, E, S, W

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np

# Initiate the window
window = tk.Tk()
window.title = 'ReMood Demo'

# Set up the Window frame structure
mainframe = ttk.Frame(window, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))


def graph_all_days(*args):
    print('graph here')
    fig = Figure(figsize=(5, 4), dpi=100)
    t = np.arange(0, 3, .01)
    fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

    canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


ttk.Button(mainframe, text="Graph All Days", command=graph_all_days).grid(column=1, row=1, sticky=W)



# create window
window.mainloop()
