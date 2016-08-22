# encoding: utf-8

from newhtml import HtmlCreator


class DishesHTMLReport(HtmlCreator):

    def design_header(self):
        """Design a header for restaurant manager report."""
        # TODO: .js and .css content here.
        with self.tag('head'):
            self.doc.asis('<meta charset="UTF-8>')
            with self.tag('title'):
                self.text('Restaurant manager report')

    def design_body(self):
        """Design a body of restaurant manager report."""
        # TODO: .css classes + .js things
        tag, text = self.tag, self.text
        table_content = [
            ('Firstname', 'Lastname', 'Age'),
            ('Maxim', 'Gonchar', '18'),
            ('Vika', 'Zaporozhnya', '16')
        ]

        with tag('body'):
            with tag('table'):
                with tag('thead'):
                    with tag('tr'):
                        with tag('th', colspan=6):
                            text('Ми щиро вдячні Вам, що обрали саме нас!')
                    with tag('tr', colspan=6):  # , align='center'
                        with tag('th', colspan=6):
                            text('Керуючись Вашими пріорітетами та вподобаннями, ми підготували данну пропозицію.')
                with tag('tbody'):
                    for content in table_content:
                        with tag('tr'):
                            with tag('th'):
                                text(content[0])
                            with tag('th'):
                                text(content[1])
                            with tag('th'):
                                text(content[2])



"""
myhtmlobj = MyHtml()
myhtmlobj.create_html()
"""

"""
with self.tag('td'):
    self.doc.attr(('data-search', 'lemon'), ('data-order', '1384992000'))
    self.doc.text('Citrus Limon')
"""
# with self.tag('td', **{'data-order': 'my_value'}):
"""
with self.tag('td'):
self.doc.attr(**{'data-order': 'my_value'})
"""
