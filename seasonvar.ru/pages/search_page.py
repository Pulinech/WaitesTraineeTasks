from pages.locators import SearchPageLocators
from selene.support.shared.jquery_style import s, ss
from selene.support.shared import browser
from selene import command
from selene import query
from selene import be
import time


class SearchPage:

    def __init__(self):
        self.locator = SearchPageLocators()
        self.country = ""
        self.genre = ""
        self.amount = 0
        self.sites_to_open = []
        self.serials_names = []

    def select_country(self):
        self.country = self.locator.select_country.get(query.text)
        s("[data-filter='country']").click()
        self.locator.select_country.click()

    def select_genre(self):
        self.genre = self.locator.select_genre.get(query.text)
        s("[data-filter='genre']").click()
        self.locator.select_genre.click()

    def show_and_get_filter_results(self):
        s("//div[@data-click='fShowResult']").click()
        s("//div[@class='lside-serial']//a").should(be.visible)
        self.amount = len(self.locator.serials_links_side)
        if self.amount > 3:
            self.amount = 3
        assert self.amount > 0, f"'{self.country}' country doesn't have any serials"
        for i in range(self.amount):
            self.sites_to_open.append(self.locator.serials_links_side[i].get(query.attribute("href")))

    def should_be_country_for_every_serials(self):
        for i in range(self.amount):
            browser.open_url(self.sites_to_open[i])
            assert self.country in self.locator.country.get(query.text), \
                f"This series has no '{self.country}' country"
        self.sites_to_open = []

    def should_be_genre_for_every_serial(self):
        for i in range(self.amount):
            browser.open_url(self.sites_to_open[i])
            assert self.genre in self.locator.genre.get(query.text),\
                f"This serial has no '{self.genre}' genre"
        self.sites_to_open = []

    def should_be_search_serials_results(self, search_input):
        s("[data-input='search']").set_value(search_input)
        s("[class='svico-search']").click()
        search_results = ss("[class='pgs-search-wrap']")
        assert search_results, "Search results are empty"
        self.amount = len(search_results)

    def check_search_input_in_serials_names(self):
        if self.amount > 3:
            self.amount = 20
        serials_name = []
        for i in range(self.amount):
            serials_name.append(self.locator.serials_names[i].get(query.text))
            if "1" not in serials_name[i]:
                certain_serial_link = s(f"//div[@class='pgs-search-info']/a[position()=1][text()='{serials_name[i]}']")
                self.sites_to_open.append(certain_serial_link.get(query.attribute("href")))

    def should_be_search_input_in_serial_alternative_or_original_name(self):
        self.amount = len(self.sites_to_open)
        for i in range(self.amount):
            browser.open_url(self.sites_to_open[i])
            if "1" not in self.locator.original_name.get(query.text):
                if "1" not in self.locator.alternative_name.get(query.text):
                    check = false
                    assert check, f"Series has no '1' in it's name"
        self.sites_to_open = []

    @staticmethod
    def log_in_into_account():
        s("//a[@class='btn head-btn']").click()
        s("[name='login']").set_value("pulinech1@gmail.com")
        s("[name='password']").set_value("1234test!")
        s("//input[@name='password']/following-sibling::button").click()

    def get_serials_to_open(self):
        self.amount = 2
        for i in range(self.amount):
            self.sites_to_open.append(self.locator.serials_links_search[i].get(query.attribute("href")))
            self.serials_names.append(ss("//div[@class='news_n']")[i].get(query.text))

    def open_serials_and_mark_series_time(self):
        for i in range(self.amount):
            browser.open_url(self.sites_to_open[i])
            time.sleep(3)
            self.locator.start_player_btn.perform(command.js.scroll_into_view)
            self.locator.start_player_btn.click()
            s("[data-markset='settime']").click()

    def should_be_marks_with_serials_names(self):
        check_serials_names = []
        s("//a[@class='btn head-btn']").click()
        for i in range(self.amount):
            check_serials_names.append(ss("[class='pgs-marks-name']")[i].get(query.text))
        assert check_serials_names, "Page with marks doesn't have any marks"
        for i in range(self.amount):
            assert check_serials_names[i] in self.serials_names[i], "Series name doesn't match with marked series name"
            s("//div[@data-click='marksRemove']/..").hover()
            s("[data-click='marksRemove']").click()
