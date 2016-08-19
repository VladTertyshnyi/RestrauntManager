#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

# TOASK: should all widgets be resizable
# TOASK: tooltips for [input] part
# TOASK: Sizegrip(self).grid(column=999, row=999, sticky=S+E)
# TOASK: saveWeb opportunity (if yes -> add more code).
# TOASK: savePDF opportunity (if yes -> add more code)
# TOASK: scrollbar at comment entry.
# TOASK: shortcuts for main program (ctr+q == save+exit)
# TOASK: windows-oriented, linux-oriented, or both?


# Replace treeView with tktable
# TODO: deletion from treeView
# TODO: wrapping lines in treeView
# TODO: validation if [name] exists in autoCompleteBox (here: in [dishes] list).

import re
import tkinter
import json
from tkinter.ttk import Frame, Label, Button, Entry, Scrollbar, Treeview
from tkinter import N, S, W, E, X, RIGHT, CENTER, VERTICAL, Text, END, messagebox, filedialog
from AutoEntry import AutocompleteEntry
 
__license__ = 'MIT'
__version__ = '0.1.2'
__author__ = 'Maxim Gonchar'
__email__ = 'maxgonchar9@gmail.com'
__status__ = 'Development'

DEFAULT_MINSIZE_WIDTH = 800
DEFAULT_MINSIZE_HEIGHT = 750


class Program(Frame):
    """Class to represent a main window"""
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.content = Frame(self, padding=(5, 5, 5, 20))
        # Some variables.
        self.frames = []
        self.entries = {}
        # TODO: This list should be filled with data from json
        self.dishes = []
        self.parent = parent
        # Some top-level settings.
        self.parent.title('Restaurant manager')
        self.parent.minsize(DEFAULT_MINSIZE_WIDTH, DEFAULT_MINSIZE_HEIGHT)
        self.parent.protocol('WM_DELETE_WINDOW', self.onQuit)
        self.initWidgets()
        self.getFromJson()
    
    def getFromJson(self):
        file = open("menu_main.json", "r")
        file_string = file.read()
        json_string = json.loads(file_string)
        for x in json_string:
         self.dishes.append(x['name'])
        print(self.dishes)
        
    def initWidgets(self):
        """
        Initialize widgets here.
        ----------------------------------------------------------
        4 frames are initialized and saved into self.frames[] here:
        1) about_frm - Frame to contain all non-food entries.
        2) newOrder_frm - Frame to contain entries for adding orders to the main table.
        3) ordersTable_frm - Frame to contain table with list of added orders.
        4) saveReport_frm - Frame to contain buttons, which save a report.
        ----------------------------------------------------------
        """
        # Create 5 frames here.
        for i in range(5):
            self.frames.append(
                Frame(self.content)
            )
        # Set the weights of cols and rows in the grid.
        self.configureGrid()
        # Center a window.
        self.centerWindow()

        # Place 4 frames to the window.
        self.frames[0].grid(column=0, row=0, sticky=N+E+W, padx=5, pady=3)
        self.frames[1].grid(column=0, row=1, sticky=N+S+E+W, padx=5, pady=3)
        self.frames[2].grid(column=0, row=2, sticky=N+S+E+W, padx=5, pady=3)
        self.frames[3].grid(column=0, row=3, sticky=N+S+E+W, padx=5, pady=10)
        self.frames[4].grid(column=0, row=4, sticky=S+E+W, padx=5, pady=3)

        # About frame widgets.
        Label(self.frames[0], text='Client').grid(row=0, column=0, sticky=E, padx=3, pady=5)
        Label(self.frames[0], text='Manager').grid(row=1, column=0, sticky=E, padx=3, pady=5)
        Label(self.frames[0], text='Location').grid(row=2, column=0, sticky=E, padx=3, pady=5)
        Label(self.frames[0], text='Date').grid(row=0, column=2, sticky=E, padx=3, pady=5)
        Label(self.frames[0], text='Event type').grid(row=1, column=2, sticky=E, padx=3, pady=5)
        Label(self.frames[0], text='Time').grid(row=2, column=2, sticky=E, padx=3, pady=5)
        Label(self.frames[0], text='Amount of persons',
              justify=RIGHT, wraplength=80).grid(row=1, column=4, sticky=E, padx=3, pady=5)

        self.entries['client'] = Entry(self.frames[0])
        self.entries['manager'] = Entry(self.frames[0])
        self.entries['location'] = Entry(self.frames[0])
        self.entries['date'] = Entry(self.frames[0])
        self.entries['eventtype'] = Entry(self.frames[0])
        self.entries['time'] = Entry(self.frames[0])
        self.entries['personsamount'] = Entry(self.frames[0])

        self.entries['client'].grid(row=0, column=1, sticky=E+W, padx=7, pady=5)
        self.entries['manager'].grid(row=1, column=1, sticky=E+W, padx=7, pady=5)
        self.entries['location'].grid(row=2, column=1, sticky=E+W, padx=7, pady=5)
        self.entries['date'].grid(row=0, column=3, sticky=E+W, padx=7, pady=5)
        self.entries['eventtype'].grid(row=1, column=3, sticky=E+W, padx=7, pady=5)
        self.entries['time'].grid(row=2, column=3, sticky=E+W, padx=7, pady=5)
        self.entries['personsamount'].grid(row=1, column=5, sticky=E+W, padx=7, pady=5)

        # Add a separator between [about] and [new order] frames
        sep1 = Frame(self.frames[1], height=2, borderwidth=1, relief='sunken')
        sep1.pack(fill=X, padx=1, pady=10)

        # New Order frame widgets.
        # Empty labels for grid
        Label(self.frames[2], width=7).grid(row=0, column=0, sticky=W+E)
        Label(self.frames[2], width=15).grid(row=0, column=1, sticky=W+E)
        Label(self.frames[2], width=15).grid(row=0, column=3, sticky=W+E+S)
        Label(self.frames[2], width=15).grid(row=2, column=3, sticky=W+E+S)
        Label(self.frames[2], text='Name', anchor=E).grid(row=1, column=0, sticky=N+S+W+E, padx=5)
        Label(self.frames[2], text='Amount', anchor=E).grid(row=2, column=0, sticky=N+S+W+E, padx=5)
        Label(self.frames[2], text='Comment', anchor=CENTER).grid(row=0, column=2, sticky=N+S+W+E)

        self.entries['name'] = AutocompleteEntry(self.frames[2])
        self.entries['name'].set_completion_list(self.dishes)
        self.entries['amount'] = Entry(self.frames[2])
        self.comment_entry = Text(self.frames[2], height=8, width=45)
        addOrder_btn = Button(self.frames[2], text='Add to the list')

        self.entries['name'].grid(row=1, column=1, sticky=W+E, pady=3)
        self.entries['amount'].grid(row=2, column=1, sticky=W+E, pady=3)
        self.comment_entry.grid(row=1, column=2, rowspan=2, sticky=W+E+S+N, padx=8, pady=3)
        addOrder_btn.grid(row=1, column=3, padx=8, sticky=N+S+W+E)

        # Orders Table frame widgets.
        self.orders_view = Treeview(self.frames[3])
        self.orders_view['columns'] = ('Weight', 'Amount', 'Comment', 'Price', 'Sum')

        self.orders_view.heading('#0', text='Name')
        self.orders_view.column('#0', anchor='w', width=220)
        self.orders_view.heading('Weight', text='Weight')
        self.orders_view.column('Weight', anchor=CENTER, width=60)
        self.orders_view.heading('Amount', text='Amount')
        self.orders_view.column('Amount', anchor=CENTER, width=60)
        self.orders_view.heading('Comment', text='Comment')
        self.orders_view.column('Comment', anchor='w', width=180)
        self.orders_view.heading('Price', text='Price')
        self.orders_view.column('Price', anchor=CENTER, width=60)
        self.orders_view.heading('Sum', text='Sum')
        self.orders_view.column('Sum', anchor=CENTER, width=60)

        self.orders_view.grid(row=0, column=0, sticky=N+S+E+W, padx=3, pady=3)

        orders_scrlbar = Scrollbar(self.frames[3], orient=VERTICAL, command=self.orders_view.yview)
        self.orders_view['yscrollcommand'] = orders_scrlbar.set
        orders_scrlbar.grid(row=0, column=1, sticky=N+S)

        # Save Report frame widgets.
        button_command = [self.savePDF, self.saveWeb, self.saveXLS]
        button_text = ['Save PDF', 'Save Web', 'Save XLS']
        saveReportFrame_widgets = []
        for i in range(3):
            saveReportFrame_widgets.append(
                Button(self.frames[4], text=button_text[i], width=20, command=button_command[i])
            )
            saveReportFrame_widgets[i].pack(side='left', anchor=CENTER, padx=5, pady=3)
        # Configure button, which adds a new entry to TreeView
        addOrder_btn['command'] = lambda: self.addDish()

    def configureGrid(self):
        """Configure weights of grids columns and rows"""
        # Top-level configuration.
        self.grid(sticky=N+S+E+W)
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Configuration of main content frame.
        self.configureFrame(self.content, [1], [0, 0, 0, 3, 0])
        # Configuration of about frame.
        self.configureFrame(self.frames[0], [0, 1, 0, 1, 0, 1], [1, 1, 1])
        # Configuration of new order frame.
        self.configureFrame(self.frames[2], [0, 1, 3, 1], [0, 1, 1])
        # Configuration of orders table frame.
        self.configureFrame(self.frames[3], [1, 0], [1])

    def centerWindow(self):
        """Place the main window in the center of screen"""
        window_w = DEFAULT_MINSIZE_WIDTH
        window_h = DEFAULT_MINSIZE_HEIGHT
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        x = (screen_w - window_w) / 2
        y = (screen_h - window_h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (window_w, window_h, x, y))

    def onQuit(self):
        """Before the program exits, ask user, if he really wants it"""
        if messagebox.askyesno('Quit?', 'Do you really want to quit?'):
            self.quit()

    @staticmethod
    def configureFrame(frame, columns_wght, rows_wght):
        """Function to organize frame configuration routine"""
        frame.grid(column=0, row=0, sticky=N + S + E + W)
        for i, weight in enumerate(columns_wght):
            frame.columnconfigure(i, weight=weight)
        for i, weight in enumerate(rows_wght):
            frame.rowconfigure(i, weight=weight)

    @staticmethod
    def savePDF():
        """TODO"""
        # TODO: getting data from the grid and passing it to the pdf
        file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        # If user pressed [Cancel]:
        if file is None:
            return
        text2save = 'hello, guys'
        file.write(text2save)
        file.close()
        print('%s was saved.' % text2save)

    @staticmethod
    def saveWeb():
        """TODO"""
        # TODO: getting data from the grid and passing it to the html
        print('saved into Web!')

    @staticmethod
    def saveXLS():
        """TODO"""
        # TODO: getting data from the grid and passing it to the xls
        print('saved into XLS!')

    def addDish(self):
        """This function adds an entry to the order_view TreeView widget."""

        def insertTable(text, values):
            self.orders_view.insert('', 'end', text=text, values=values)

        packed_info = self.packInfo()
        if packed_info:
            insertTable(packed_info['dish'], packed_info['values'])

    def packInfo(self):
        """Pack values, that were inserted into Entries and Text, into dictionary"""
        # TODO: when .json will be ready, change configuration here.
        msg = self.validateForm()
        if msg == 'OK':
            name = self.entries['name'].get()
            pack = {
                'dish': name,
                'values': [
                    'none',  # self.dishes[name]['weight']
                    self.entries['amount'].get(),
                    self.comment_entry.get('1.0', END),
                    'none',  # self.dishes[name]['price']
                    'none'  # str(self.dishes[name]['amount'] * self.dishes[name]['price'])
                ]
            }
            return pack
        else:
            messagebox.showerror(
                'Input error',
                'You have some errors: \n%s' % msg
                )
            return False

    def validateForm(self):
        """Validate all Entry and Text Widgets"""
        msg = ''
        index = 1

        # Certain check for Text widget.
        if self.comment_entry.get('1.0', END).rstrip() == '':
            msg += '%i) Comment entry is empty.\n' % index
            index += 1

        for k in self.entries:
            # Check if some entry is empty.
            if self.entries[k].get() == '':
                msg += '%i) %s is empty.\n' % (index, k)
                index += 1
            # Check date entry.
            if k == 'date':
                match = re.search(r'(\d{2})[.](\d{2})[.](\d{4})$', self.entries[k].get())
                if not match:
                    msg += '%i) Incorrect date format.\nCorrect format: [dd.mm.yyyy]\n' % index
                    index += 1
            # Check date entry.
            if k == 'time':
                match = re.search(r'(\d{2})[:](\d{2})[-](\d{2})[:](\d{2})', self.entries[k].get())
                if not match:
                    msg += '%i) Incorrect time format.\nCorrect format: [00:00-00:00]\n' % index
                    index += 1
            # Check if some entries should contain only letters.
            def onlyLetters(str):
                return all(letter.isalpha() for letter in str)
            if k in ['client', 'manager']:
                if not onlyLetters(self.entries[k].get()):
                    msg += '%i) %s should contain only letters.\n' % (index, k)
                    index += 1
            # Check if some entries should contain only digits.
            def onlyDigits(str):
                return all(letter.isdigit() for letter in str)
            if k in ['location', 'personsamount']:
                if not onlyDigits(self.entries[k].get()):
                    msg += '%i) %s should contain only digits.\n' % (index, k)
                    index += 1

        # If all tests passed correctly, msg is 'OK'
        if msg == '':
            msg = 'OK'
        return msg


def main():
    root = tkinter.Tk()
    app = Program(root)
    root.mainloop()


if __name__ == '__main__':
    main()