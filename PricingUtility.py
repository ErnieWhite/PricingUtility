import tkinter as tk
from tkinter import ttk

from FormulaConverterFrame import FormulaConverterFrame
from TicketSpecialsFrame import TicketSpecialsFrame
from UnitBasisFrame import UnitBasisFrame
from UnitFormulaFrame import UnitFormulaFrame


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.current_frame = None

        menubar = tk.Menu(self, tearoff=False)
        self.config(menu=menubar)

        file_menu = tk.Menu(menubar)

        file_menu.add_command(
            label='Exit',
            command=self.destroy,
        )

        view_menu = tk.Menu(menubar)
        view_menu.add_command(label='Unit/Basis', command=lambda: self.change_frame('unitbasis'))
        view_menu.add_command(label='Unit/Formula', command=lambda: self.change_frame('unitformula'))
        view_menu.add_command(label='Formula Converter', command=lambda: self.change_frame('formulaconverter'))
        view_menu.add_command(label='Ticket Special', command=lambda: self.change_frame('ticketspecial'))

        menubar.add_cascade(
            label='File',
            menu=file_menu,
        )
        menubar.add_cascade(
            label='View',
            menu=view_menu,
        )

        self.unitbasisframe = UnitBasisFrame(self)
        self.unitformulaframe = UnitFormulaFrame(self)
        self.formulaconverterframe = FormulaConverterFrame(self)
        self.ticketspecialframe = TicketSpecialsFrame(self)

        self.frames = {
            'unitbasis': self.unitbasisframe,
            'unitformula': self.unitformulaframe,
            'formulaconverter': self.formulaconverterframe,
            'ticketspecial': self.ticketspecialframe,
        }

        self.change_frame('unitbasis')

    def change_frame(self, frame_name):
        if self.current_frame:
            self.current_frame.grid_forget()
        self.current_frame = self.frames[frame_name]
        self.current_frame.grid(row=0, column=0, sticky='nsew')


if __name__ == '__main__':
    app = App()

    app.mainloop()


