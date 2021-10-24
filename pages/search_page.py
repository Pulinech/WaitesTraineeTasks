from pages.locators import SearchPageLocators
from selene.support.shared.jquery_style import s, ss
from selene import by, be, have
from selene import command
from selene import query


class SearchPage:

    locator = SearchPageLocators()
    low_rating = ""
    high_rating = ""

    def __init__(self):
        self.result1 = []
        self.result2 = []
        self.low_rating_trains = []
        self.high_rating_trains = []

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

    def get_trains_with_rating_lower_than(self, low_rating="8.5"):
        self.low_rating = low_rating
        for i in range(len(self.locator.train_schedule_lower_rating)):
            self.low_rating_trains.append(self.locator.train_schedule_lower_rating[i].get(query.text))
        assert self.low_rating_trains, "There are no trains with rating lower than 8.5"

    def get_trains_with_rating_higher_than(self, high_rating="9"):
        self.high_rating = high_rating
        for i in range(len(self.locator.train_schedule_bigger_rating)):
            self.high_rating_trains.append(self.locator.train_schedule_bigger_rating[i].get(query.text))
        assert self.high_rating_trains, "There are no trains with rating higher than 9"

    def print_low_rating_trains_schedule(self):
        low_rating_trains = self.low_rating_trains
        amount = int(len(low_rating_trains) / 2)
        print("\nLow rating trains amount:", amount)
        k = 0
        j = 1
        for i in range(amount):
            print(i + 1, ": ", low_rating_trains[k], "->", low_rating_trains[j])
            k = k + 2
            j = j + 2

    def print_high_rating_trains_schedule(self):
        high_rating_trains = self.high_rating_trains
        amount = int(len(high_rating_trains) / 2)
        print("\nHigh rating trains amount:", amount)
        k = 0
        j = 1
        for i in range(amount):
            print(i + 1, ": ", high_rating_trains[k], "->", high_rating_trains[j])
            k = k + 2
            j = j + 2

    def should_be_info_of_train_from_certain_terminal(self):
        s("[data-ti='icon']").perform(command.js.scroll_into_view)
        assert self.locator.certain_station_reviews.click(), f"There is no train from {self.locator.station}, {self.locator.station_city}"

    def should_be_trip_details_and_certain_city_terminal(self):
        assert s("//div[@data-ti='order-popper-slot-top']").should(be.visible), "Trip details doesn't open"
        assert s("//span[@data-ti='city']").should(be.visible), "Trip details city doesn't match"
        assert s("//span[@data-ti='station']").should(be.visible), "Trip details terminal doesn't match"
