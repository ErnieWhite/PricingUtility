import tkinter as tk
from tkinter import ttk


class UnitFormulaFrame(tk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)
        self._create_controls()
        self._place_controls()
        self.master = container

    def _create_controls(self):
        self.unit_price_label = ttk.Label(self, text='Unit Price')
        self.formula_label = ttk.Label(self, text='Formula')
        self.basis_value_label = ttk.Label(self, text='Basis Value')

        self.unit_price_entry = ttk.Entry(self)
        self.formula_entry = ttk.Entry(self)
        self.basis_value_entry = ttk.Entry(self, state=tk.DISABLED)

        self.basis_value_button = ttk.Button(self, text='Copy', command=lambda: self.copy(self.basis_value_entry))

    def _place_controls(self):
        self.unit_price_label.grid(row=0, column=0)
        self.unit_price_entry.grid(row=0, column=1)

        self.formula_label.grid(row=1, column=0)
        self.formula_entry.grid(row=1, column=1)

        self.basis_value_label.grid(row=2, column=0)
        self.basis_value_entry.grid(row=2, column=1)
        self.basis_value_button.grid(row=2, column=2)

    def copy(self, control):
        pass



