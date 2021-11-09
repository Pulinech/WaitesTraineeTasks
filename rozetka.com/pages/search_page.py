from selene.support.shared.jquery_style import s, ss
from selene import query
from selene import have
from selene import be
import time


class SearchPage:
    def __init__(self):
        self.model = ""
        self.from_price = 0
        self.to_price = 0

    @staticmethod
    def open_notebooks_page():
        ss("a").element_by(have.exact_text("Ноутбуки и компьютеры")).should(be.visible).click()
        ss("a").element_by(have.exact_text("Ноутбуки")).should(be.visible).click()

    def filter_notebooks(self, model, min_price, max_price):
        self.model = model
        self.from_price = min_price
        self.to_price = max_price
        ss(".checkbox-filter__link").element_by(have.text(model)).click()
        s("[formcontrolname='min']").set_value(min_price)
        s("[formcontrolname='max']").set_value(max_price)
        s(".slider-filter__button").click()

    def check_filter_notebooks_price_and_model(self):
        time.sleep(2)
        get_all_prices = ss(".goods-tile__price-value")
        ss(".goods-tile__title").should(have.text(self.model))
        amount = len(get_all_prices)
        for i in range(amount):
            price = int(get_all_prices[i].get(query.text).replace(' ', ''))
            assert self.from_price < price < self.to_price, "Prices out of range"
