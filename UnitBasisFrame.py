import tkinter as tk
from tkinter import ttk


class UnitBasisFrame(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        self._create_widgets()
        self._place_widgets()

    def _create_widgets(self):
        self.unit_price_label = ttk.Label(self, text='Unit Price')
        self.unit_price_entry = ttk.Entry(self)

        self.basis_value_label = ttk.Label(self, text='Basis Value')
        self.basis_value_entry = ttk.Entry(self)

        self.decimal_places_label = ttk.Label(self, text='Decimal Places')
        self.decimal_places_entry = ttk.Combobox(self)

        self.multiplier_formula_entry = ttk.Entry(self, state=tk.DISABLED)
        self.discount_formula_entry = ttk.Entry(self, state=tk.DISABLED)
        self.markup_formula_entry = ttk.Entry(self, state=tk.DISABLED)
        self.grossprofit_formula_entry = ttk.Entry(self, state=tk.DISABLED)

        self.multiplier_formula_button = ttk.Button(
            self,
            text='Copy',
            command=lambda: self.copy(self.multiplier_formula_entry)
        )
        self.discount_formula_button = ttk.Button(
            self,
            text='Copy',
            command=lambda: self.copy(self.discount_formula_entry)
        )
        self.markup_formula_button = ttk.Button(
            self,
            text='Copy',
            command=lambda: self.copy(self.markup_formula_entry)
        )
        self.grossprofit_formula_button = ttk.Button(
            self,
            text='Copy',
            command=lambda: self.copy(self.grossprofit_formula_entry)
        )

    def _place_widgets(self):
        #  Row 0
        self.unit_price_label.grid(row=0, column=0, sticky='w')
        self.unit_price_entry.grid(row=0, column=1, sticky='ew')
        self.multiplier_formula_entry.grid(row=0, column=2)
        self.multiplier_formula_button.grid(row=0, column=3)

        #  Row 1
        self.basis_value_label.grid(row=1, column=0, sticky='w')
        self.basis_value_entry.grid(row=1, column=1, sticky='ew')
        self.discount_formula_entry.grid(row=1, column=2)
        self.discount_formula_button.grid(row=1, column=3)

        #  Row 2
        self.decimal_places_label.grid(row=2, column=0, sticky='w')
        self.decimal_places_entry.grid(row=2, column=1, sticky='ew')
        self.markup_formula_entry.grid(row=2, column=2)
        self.markup_formula_button.grid(row=2, column=3)

        #  Row 3
        self.grossprofit_formula_entry.grid(row=3, column=2)
        self.grossprofit_formula_button.grid(row=3, column=3)

    def copy(self, control):
        pass



