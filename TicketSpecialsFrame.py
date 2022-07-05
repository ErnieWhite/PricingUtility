import tkinter as tk
from tkinter import ttk


class TicketSpecialsFrame(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        self.header_row = ['Product #',
                           'Basis',
                           'Formula',
                           'Type',
                           'Decimals',
                           'Description',
                           'Per U/M'
                           'Unit Price',
                           'LIST',
                           'Ord Comm',
                           'AVG-COST',
                           'Pice line',
                           ]

        self.header_frame = ttk.Frame(self)
        self.detail_frame = ttk.Frame(self)

        self.order_num_label = tk.Label(self.header_frame, text='Order Number')
        self.order_number = tk.Label(self.header_frame, text='S111222333')

        self.ship_to_label = tk.Label(self.header_frame, text='Ship-To')
        self.ship_to_name = tk.Label(self.header_frame, text='ALLEN LEEK AIR CONDITIONING SHOP')

        self.vertical_scrollbar = ttk.Scrollbar(self.detail_frame, orient=tk.VERTICAL)
        self.horizontal_scrollbar = ttk.Scrollbar(self.detail_frame, orient=tk.HORIZONTAL)

        self.canvas = tk.Canvas(
            self.detail_frame,
            bg='blue',
            yscrollcommand=self.vertical_scrollbar.set,
            xscrollcommand=self.horizontal_scrollbar.set,
        )
        self.vertical_scrollbar.config(command=self.canvas.yview)
        self.horizontal_scrollbar.config(command=self.canvas.xview)

        self.detail_lines_frame = ttk.Frame(self.canvas)

        # place detail frame widgets
        self.canvas.grid(row=0, column=0, sticky='nsew')
        self.vertical_scrollbar.grid(row=0, column=1, sticky='nse')
        self.horizontal_scrollbar.grid(row=1, column=0, sticky='ews')

        self.detail_frame.rowconfigure(2, weight=2)
        self.detail_frame.columnconfigure(2, weight=2)

        # place header frame widgets
        self.order_num_label.grid(row=0, column=0, sticky='w')
        self.order_number.grid(row=0, column=1, sticky='w')

        self.ship_to_label.grid(row=1, column=0, sticky='w')
        self.ship_to_name.grid(row=1, column=1, sticky='w')

        # place the header and detail frames
        self.header_frame.grid(row=0, column=0, sticky='w')
        self.detail_frame.grid(row=1, column=0, sticky='nsew')

