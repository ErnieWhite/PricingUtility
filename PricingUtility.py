import tkinter as tk
from tkinter import ttk

from Tabs import Tabs


class MainFrame(tk.Frame):
    def __init__(self, kwargs):
        super().__init__(kwargs)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        tabs = Tabs(self)
        tabs.grid()


if __name__ == '__main__':
    app = App()

    app.mainloop()


