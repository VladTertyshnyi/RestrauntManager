from newdialog import SpecificDialog
from tkinter import *
from tkinter import messagebox
import re


class NewDishDialog(SpecificDialog):
    def body(self, parent):
        self.result = {}
        self.entries = {}

        self.entries['name'] = Entry(parent)
        self.entries['type'] = Entry(parent)
        self.entries['weight'] = Entry(parent)
        self.entries['price'] = Entry(parent)

        Label(parent, text='Название:').grid(row=0, column=0, sticky=E)
        Label(parent, text='Тип:').grid(row=1, column=0, sticky=E)
        Label(parent, text='Выход:').grid(row=2, column=0, sticky=E)
        Label(parent, text='Цена, грн:').grid(row=3, column=0, sticky=E)

        self.entries['name'].grid(row=0, column=1, columnspan=3, sticky=W+E)
        self.entries['type'].grid(row=1, column=1, columnspan=3, sticky=W + E)
        self.entries['weight'].grid(row=2, column=1, sticky=W+E)
        self.entries['price'].grid(row=3, column=1, sticky=W+E)

        self.entries['name'].delete(0, END)
        self.entries['name'].insert(0, self.name_info)

        # Return an initial focus to [name] entry.
        return self.entries['type']

    def validate(self):
        msg = ''
        index = 1
        translations = {
            'name': 'Название',
            'type': 'Тип',
            'weight': 'Выход',
            'price': 'Цена',
        }

        for k in self.entries:
            # Check if some entry is empty.
            if self.entries[k].get() == '':
                msg += '%i) Поле [%s] пустое.\n' % (index, translations[k])
                index += 1
        # Check if [price] entry contains a float number.
        match = re.search(r'(\d+)[.](\d{2})$', self.entries['price'].get())
        if not match:
            msg += '%i) Неправильный формат цены.\nПравильный формат: гривны.кк\n' % index
            index += 1

        if msg == '':
            msg = 'OK'
        return msg

    def react_validate(self, report):
        messagebox.showerror(
            'Ошибка ввода',
            'При вводе случились ошибки: \n%s' % report
        )

    def apply(self):
        self.result = {
            'name': self.entries['name'].get(),
            'type': self.entries['type'].get(),
            'weight': self.entries['weight'].get(),
            'price': self.entries['price'].get(),
        }
