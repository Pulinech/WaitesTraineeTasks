from selene.support.shared.jquery_style import s, ss
from selene import be, command, query, have


class SearchPage:

    def __init__(self):
        # Global variables
        self.result1 = []
        self.result2 = []
        self.low_rating_trains = []
        self.high_rating_trains = []

        # Buttons
        self.next_day_btn = s("button.increase")
        self.find_results_btn = s(".button_wrp")
        self.change_city_btn = s("[data-ti='icon']")

        # Train schedules
        self.departure_time = ss("//div[@data-ti='card-departure-0']//span")
        self.results_load = s("[data-ti='filter-sapsan']")
        self.last_search_element = s("(//div[@data-ti='offer-card']/..)[last()]")
        self.train_schedule = ss("//span[@data-ti='stopover-time']")
        self.train_schedule_lower_rating = ss("//div[@data-ti='rating']/span[text()<8.5]/ancestor::"
                                              "div[@data-ti='train-offer-card']//span[@data-ti='stopover-time']")
        self.train_schedule_bigger_rating = ss("//div[@data-ti='rating']/span[text()>9]/ancestor::"
                                               "div[@data-ti='train-offer-card']//span[@data-ti='stopover-time']")
        self.certain_station_block = ss("//span[@data-ti='stopover-place']")\
            .element_by(have.text('Ленинградский вокзал, Москва')).s("//ancestor::div[@data-ti='offer-card']")
        self.certain_station_reviews = self.certain_station_block.s("//span[@data-ti='rating_badge_link']")

    def search_trains_from_city_a_to_city_b(self, city_a="Москва", city_b="Санкт-Петербург"):
        s("[name=schedule_station_from]").type(city_a)
        s("[name=schedule_station_to]").type(city_b)
        self.next_day_btn.click()
        self.find_results_btn.click()

    def get_trains_from_city_a_to_city_b_schedule(self):
        if self.results_load.should(be.visible, timeout=20):
            for i in range(len(self.departure_time)):
                self.last_search_element.perform(command.js.scroll_into_view)
        route_time1 = self.train_schedule
        for i in range(len(route_time1)):
            self.result1.append(route_time1[i].get(query.text))

    def search_trains_from_city_b_to_city_a(self):
        self.change_city_btn.click()
        s("[data-ti='swap_stations']").click()
        s("[data-ti='submit_button']").click()

    def get_trains_from_city_b_to_city_a_schedule(self):
        if self.results_load.should(be.visible, timeout=20):
            for i in range(len(self.departure_time)):
                self.last_search_element.perform(command.js.scroll_into_view)
        route_time2 = self.train_schedule
        for i in range(len(route_time2)):
            self.result2.append(route_time2[i].get(query.text))

    def should_be_different_trains_schedule(self):
        assert (self.result1 != self.result2), "Lists are matching"

    def print_and_write_to_file_trains_schedules(self):
        result1 = self.result1
        result2 = self.result2
        amount1 = int(len(result1) / 2)
        amount2 = int(len(result2) / 2)
        f = open("search_different_results.txt", "w")
        f.write("Search 1 results amount:" + str(amount1) + "\n" + "Search 2 results amount:" + str(amount2) + "\n")
        print("\nSearch 1 results amount:", amount1)
        print("Search 2 results amount:", amount2)
        k = 0
        j = 1
        for i in range(min(amount1, amount2)):
            print(i + 1, ": ", result1[k], "->", result1[j], " | ", result2[k], "->", result2[j])
            f.write(str(i+1) + ": " + result1[k] + "->" + result1[j] + " | " + result2[k] + "->" + result2[j] + "\n")
            k = k + 2
            j = j + 2
        f.close()

    def get_trains_with_rating_lower_than(self):
        for i in range(len(self.train_schedule_lower_rating)):
            self.low_rating_trains.append(self.train_schedule_lower_rating[i].get(query.text))
        assert self.low_rating_trains, "There are no trains with rating lower than 8.5"

    def get_trains_with_rating_higher_than(self):
        for i in range(len(self.train_schedule_bigger_rating)):
            self.high_rating_trains.append(self.train_schedule_bigger_rating[i].get(query.text))
        assert self.high_rating_trains, "There are no trains with rating higher than 9"

    def print_and_write_to_file_low_rating_trains_schedule(self):
        low_rating_trains = self.low_rating_trains
        amount = int(len(low_rating_trains) / 2)
        f = open("low_rating_trains.txt", "w")
        f.write("Low rating trains amount:" + str(amount) + "\n")
        print("\nLow rating trains amount:", amount)
        k = 0
        j = 1
        for i in range(amount):
            print(i + 1, ": ", low_rating_trains[k], "->", low_rating_trains[j])
            f.write(str(i + 1) + ": " + low_rating_trains[k] + "->" + low_rating_trains[j] + "\n")
            k = k + 2
            j = j + 2
        f.close()

    def print_and_write_to_file_high_rating_trains_schedule(self):
        high_rating_trains = self.high_rating_trains
        amount = int(len(high_rating_trains) / 2)
        f = open("high_rating_trains.txt", "w")
        f.write("High rating trains amount:" + str(amount) + "\n")
        print("\nHigh rating trains amount:", amount)
        k = 0
        j = 1
        for i in range(amount):
            print(i + 1, ": ", high_rating_trains[k], "->", high_rating_trains[j])
            f.write(str(i + 1) + ": " + high_rating_trains[k] + "->" + high_rating_trains[j] + "\n")
            k = k + 2
            j = j + 2
        f.close()

    def should_be_trip_details_and_certain_city_terminal(self):
        self.certain_station_block.perform(command.js.scroll_into_view)
        self.certain_station_reviews.click()
        s("//span[@data-ti='city']").should(be.visible)
        s("//span[@data-ti='station']").should(be.visible)
