import tkinter as tk
from tkinter import ttk


class FormulaConverterTab(tk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)
        self._create_widgets()
        self._place_widgets()

    def _create_widgets(self):
        self.multiplier_label = tk.Label(self, text='Multiplier')
        self.discount_label = tk.Label(self, text='Discount')
        self.markup_label = tk.Label(self, text='Markup')
        self.gross_label = tk.Label(self, text='Gross Profit')

        self.multiplier_field = tk.Entry(self)
        self.discount_field = tk.Entry(self)
        self.markup_field = tk.Entry(self)
        self.gross_field = tk.Entry(self)

        self.multiplier_button = tk.Button(self, text='Copy', command=lambda: self.copy(self.multiplier_field))
        self.discount_button = tk.Button(self, text='Copy', command=lambda: self.copy(self.discount_field))
        self.markup_button = tk.Button(self, text='Copy', command=lambda: self.copy(self.markup_field))
        self.gross_button = tk.Button(self, text='Copy', command=lambda: self.copy(self.gross_field))

    def _place_widgets(self):
        self.multiplier_label.grid(row=0, column=0)
        self.multiplier_field.grid(row=0, column=1)
        self.multiplier_button.grid(row=0, column=2)
        self.discount_label.grid(row=1, column=0)
        self.discount_field.grid(row=1, column=1)
        self.discount_button.grid(row=1, column=2)
        self.markup_label.grid(row=2, column=0)
        self.markup_field.grid(row=2, column=1)
        self.markup_button.grid(row=2, column=2)
        self.gross_label.grid(row=3, column=0)
        self.gross_field.grid(row=3, column=1)
        self.gross_button.grid(row=3, column=2)

    def copy(self, control):
        pass




