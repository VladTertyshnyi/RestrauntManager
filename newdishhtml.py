# encoding: utf-8

from newhtml import HtmlCreator


class DishesHTMLReport(HtmlCreator):

    def design_header(self):
        """Design a header for restaurant manager report."""
        # TODO: .js and .css content here.
        with self.tag('head'):
            self.doc.asis('<meta charset="UTF-8">')
            self.doc.asis('<link rel="stylesheet" href="style.css">')
            with self.tag('title'):
                self.text('Restaurant manager report')

    def design_body(self):
        """Design a body of restaurant manager report."""
        # TODO: .css classes + .js things
        tag, text = self.tag, self.text
        data = self.data

        with tag('body'):
            with tag('table', style='width:100%'):
                with tag('tr'):
                    with tag('td', klass='about'):
                        text('Замовник:', data['about']['client'])
                    with tag('td', klass="logo", rowspan="7", colspan="5"):
                        self.doc.stag('img', src="images/logo_2.jpg",width="210", height="86", alt="Vine e Cucina restaurant")
                with tag('tr'):
                    with tag('td', klass='about'):
                        text('Менеджер:', data['about']['manager'])
                with tag('tr'):
                    with tag('td', klass='about'):
                        text('Місце проведення:', data['about']['location'])
                with tag('tr'):
                    with tag('td', klass='about'):
                        text('Дата:', data['about']['date'])
                with tag('tr'):
                    with tag('td', klass='about'):
                        text('Вид заходу:', data['about']['type'])
                with tag('tr'):
                    with tag('td', klass='about'):
                        text('Час:', data['about']['time'])
                with tag('tr'):
                    with tag('td', klass='about'):
                        text('Кількість персон:', data['about']['persons'])
                with tag('tr'):
                    with tag('td', klass='top-header', colspan='6'):
                        text('Ми щиро вдячні Вам, що обрали саме нас!')
                with tag('tr'):
                    with tag('td', klass='top-header', colspan='6'):
                        text('Керуючись Вашими пріорітетами та вподобаннями, ми підготували данну пропозицію.')
                with tag('tr', klass='header'):
                    with tag('th', width='40%'):
                        text('Назва')
                    with tag('th', width='5%'):
                        text('Вихід')
                    with tag('th', width='5%'):
                        text('Кількість')
                    with tag('th', width='34%'):
                        text('Коментар')
                    with tag('th', width='8%'):
                        text('Ціна, грн')
                    with tag('th', width='8%'):
                        text('Сума, грн')
                total_cost = 0
                types = {}
                for dish in data['dishes']:
                    specific_type = data['dishes'][dish]['type']
                    types[specific_type] = {}
                for dish in data['dishes']:
                    specific_type = data['dishes'][dish]['type']
                    specific_dish = {dish: data['dishes'][dish]}
                    types[specific_type].update(specific_dish)

                for type in types:
                    with tag("tr", klass='header_line'):
                        with tag('th'):
                            text(type)
                    for dish in types[type]:
                        with tag('tr', klass='order_line'):
                            with tag('td', klass='name'):
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
                                total_cost += float(types[type][dish]['total'])

                with tag("tr"):
                    with tag('td', klass = "total"):
                        text('Загальна сума без обслуговування:')
                    with tag('td'):
                        text("")
                    with tag('td'):
                        text("")
                    with tag('td'):
                        text("")
                    with tag('td'):
                        text("")
                    with tag('td', klass = "total"):
                        text(total_cost)
                with tag("tr"):
                    with tag('td', klass = "total"):
                        text('Обслуговування 10%:')
                    with tag('td'):
                        text("")
                    with tag('td'):
                        text("")
                    with tag('td'):
                        text("")
                    with tag('td'):
                        text("")
                    with tag('td', klass = "total"):
                        text(0.1 * total_cost)
                with tag("tr"):
                    with tag('td', klass = "total"):
                        text('Загальна сума:')
                    with tag('td'):
                        text("")
                    with tag('td'):
                        text("")
                    with tag('td'):
                        text("")
                    with tag('td'):
                        text("")
                    with tag('td', klass = "total"):
                        text((0.1 * total_cost) + total_cost)






