from pages.locators import SearchPageLocators
from selene.support.shared.jquery_style import s, ss
from selene import by, be, have
from selene import command
from selene import query


class SearchPage:
    def __init__(self):
        self.locator = SearchPageLocators()
        self.result1 = []
        self.result2 = []

    def search_trains_from_city_a_to_city_b(self, city_a="Москва", city_b="Санкт-Петербург"):
        s("[name=schedule_station_from]").set_value(city_a)
        s("[name=schedule_station_to]").set_value(city_b)
        s("[data-ti='date_arrow_increase']").click()
        s(".button_wrp").click()

    def get_trains_from_city_a_to_city_b_schedule(self):
        if self.locator.results_load.should(be.visible, timeout=10):
            while self.locator.last_departure_time.get(query.text) != "23:55":
                self.locator.last_search_element.perform(command.js.scroll_into_view)
        result1 = []
        if self.locator.last_departure_time.get(query.text) == "23:55":
            route_time1 = self.locator.train_schedule
            for i in range(len(route_time1)):
                result1.append(route_time1[i].get(query.text))
        self.result1 = result1

    def search_trains_from_city_b_to_city_a(self):
        s("[data-ti='icon']").click()
        s("[data-ti='swap_stations']").click()
        s("[data-ti='submit_button']").click()

    def get_trains_from_city_b_to_city_a_schedule(self):
        if self.locator.results_load.should(be.visible, timeout=10):
            while self.locator.last_departure_time.get(query.text) != "23:55":
                self.locator.last_search_element.perform(command.js.scroll_into_view)
        result2 = []
        if self.locator.last_departure_time.get(query.text) == "23:55":
            route_time2 = self.locator.train_schedule
            for i in range(len(route_time2)):
                result2.append(route_time2[i].get(query.text))
        self.result2 = result2

    def should_be_different_trains_schedule(self):
        assert (self.result1 != self.result2), "Lists are matching"

    def print_trains_schedules(self):
        result1 = self.result1
        result2 = self.result2
        amount1 = int(len(result1) / 2)
        amount2 = int(len(result2) / 2)
        print("\nSearch 1 results amount:", amount1)
        print("Search 2 results amount:", amount2)
        k = 0
        j = 1
        for i in range(min(amount1, amount2)):
            print(i + 1, ": ", result1[k], "->", result1[j], " | ", result2[k], "->", result2[j])
            k = k + 2
            j = j + 2
