from locators import SearchPageLocators
from selene.support.shared.jquery_style import s, ss
from selene import query
import time


class SearchPage:
    def __init__(self):
        self.locator = SearchPageLocators()
        self.model = ""
        self.from_price = 0
        self.to_price = 0

    def open_notebooks_page(self):
        self.locator.open_computers_and_notebooks.click()
        self.locator.open_notebooks.click()

    def filter_notebooks(self, model, min_price, max_price):
        self.model = model
        self.from_price = min_price
        self.to_price = max_price
        s(f"//label[@for='{model}']").click()
        s("[formcontrolname='min']").set_value(min_price)
        s("[formcontrolname='max']").set_value(max_price)
        s("//input[@formcontrolname='min']/../button").click()

    def check_filter_notebooks_price_and_model(self):
        time.sleep(2)
        get_all_prices = ss("[class='goods-tile__price-value']")
        get_all_titles = ss("[class='goods-tile__title']")
        amount = len(get_all_prices)
        for i in range(amount):
            title = get_all_titles[i].get(query.text)
            assert self.model in title, f"Not all notebooks form {self.model}"
            price = int(get_all_prices[i].get(query.text).replace(' ', ''))
            assert self.from_price < price < self.to_price, "Prices out of range"
