# -*- coding: utf-8 -*-

import codecs

from yattag import Doc
from yattag import indent


class HtmlCreator:
    def __init__(self, file, data=None):
        # Create header, body and write the whole content to html file.
        self.filestream = file
        self.data = data
        self.initDocTagText()

    def initDocTagText(self):
        """
        Create main yattag variables.
        This method can be overridden.
        """
        self.doc, self.tag, self.text = Doc().tagtext()

    def create_html(self):
        """
        Create a html file from header and body content.
        Next, write html content to the hard drive.
        This method cannot be overridden.
        """
        # Add html content to the self.doc
        self.doc.asis('<!DOCTYPE html>')
        with self.tag('html'):
            self.design_header()
            self.design_body()
        # Write html content from self.doc
        with codecs.open(self.filestream.name, 'w', 'utf-8') as f:
            html_content = indent(
                self.doc.getvalue(),
                indentation='  ',
                newline='\n'
            )
            f.write(html_content)

    def design_header(self):
        """
        Create a header for your html file here.
        This method should be overridden.
        """
        with self.tag('head'):
            self.doc.asis('<meta charset="UTF-8>')
            with self.tag('title'):
                self.text('Restaurant manager report')

    def design_body(self):
        """
        Create a body for your html file here.
        This method should be overridden.
        """
        tag, text = self.tag, self.text
        with tag('body'):
            with tag('table', style = 'width:100%'):
                with tag('tr'):
                    with tag('td', klass = 'about'):
                        text('Замовник:', data['about']['client'])
                    with tag('td', klass="logo", rowspan="7", colspan="5"):
                        text('<img src="images/logo_2.jpg" alt="Vino e Cucina restaurant">')
                with tag('tr'):
                    with tag('td', klass = 'about'):
                        text('Менеджер:', data['about']['manager'])
                with tag('tr'):
                    with tag('td', klass = 'about'):
                        text('Місце проведення:', data['about']['location'])    
                with tag('tr'):
                    with tag('td', klass = 'about'):
                        text('Дата:', data['about']['date'])
                with tag('tr'):
                    with tag('td', klass = 'about'):
                        text('Вид заходу:', data['about']['type'])
                with tag('tr'):
                    with tag('td', klass = 'about'):
                        text('Час:', data['about']['time'])
                with tag('tr'):
                    with tag('td', klass = 'about'):
                        text('Кількість персон:', data['about']['persons'])
                with tag('tr'):
                    with tag('td', klass = 'top-header', colspan = '6'):
                        text('Ми щиро вдячні Вам, що обрали саме нас!')
                with tag('tr'):
                    with tag('td', klass = 'top-header', colspan = '6'):
                        text('Керуючись Вашими пріорітетами та вподобаннями, ми підготували данну пропозицію.')
                with tag('tr', klass = 'header'):
                    with tag('th', width = '40%'):
                        text('Назва')
                    with tag('th', width = '5%'):
                        text('Вихід')
                    with tag('th', width = '5%'):
                        text('Кількість')
                    with tag('th', width = '20%'):
                        text('Коментар')
                    with tag('th', width = '15%'):
                        text('Ціна, грн')
                    with tag('th', width = '15%'):
                        text('Сума, грн')

                types = {}
                for dish in data['dishes']:
                    specific_type = data['dishes'][dish]['type']
                    types[specific_type] = {}
                for dish in data['dishes']:
                    specific_type = data['dishes'][dish]['type']
                    specific_dish = {
                        dish: data['dishes'][dish]
                    }
                    types[specific_type].update(specific_dish)

                for type in types:
                    with tag("tr", klass = 'header_line'):
                        with tag('th'):
                            text(type)
                    for dish in types[type]:
                        with tag('tr', klass = 'order_line'):
                            with tag('td', klass = 'name'):
                                text(dish)
                            with tag('td'):
                                text(types[type][dish]['weight'])
                            with tag('td'):
                                text(types[type][dish]['amount'])
                            with tag('td'):
                                text(types[type][dish]['comment'])
                            with tag('td'):
                                text(types[type][dish]['price'])
                            with tag('td'):
                                text(types[type][dish]['total'])

