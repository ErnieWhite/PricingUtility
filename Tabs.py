import tkinter as tk
from tkinter import ttk

from UnitBasisTab import UnitBasisTab
from UnitFormulaTab import UnitFormulaTab
from FormulaConverterTab import FormulaConverterTab
from TicketSpecialsTab import TicketSpecialsTab


class Tabs(ttk.Notebook):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        unitbasistab = UnitBasisTab(self)
        unitformulatab = UnitFormulaTab(self)
        formulaconvertertab = FormulaConverterTab(self)
        ticketspecialtab = TicketSpecialsTab(self)

        unitbasistab.grid(sticky='nsew')
        unitformulatab.grid(sticky='nsew')
        formulaconvertertab.grid(sticky='nsew')
        ticketspecialtab.grid(sticky='nsew')

        self.add(unitbasistab, text='Find Formula')
        self.add(unitformulatab, text='Find Basis')
        self.add(formulaconvertertab, text='Formula Converter')
        self.add(ticketspecialtab, text='Ticket to Batch')
