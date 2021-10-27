from selene.support.shared.jquery_style import s, ss
from selene import by, be, have
from selene import command
from selene import query


class SearchPageLocators:
    last_departure_time = s("(//div[@data-ti='card-departure-0']//span[@data-ti='stopover-time'])[last()]")
    results_load = s("[data-ti='filter-sapsan']")
    last_search_element = s("(//div[@data-ti='offer-card']/..)[last()]")
    train_schedule = ss("//span[@data-ti='stopover-time']")
    low_rating = "8.5"
    train_schedule_lower_rating = ss(f"//div[@data-ti='rating']/span[text()<{low_rating}]"
                                     f"/ancestor::div[@data-ti='train-offer-card']//span[@data-ti='stopover-time']")
    high_rating = "9"
    train_schedule_bigger_rating = ss(f"//div[@data-ti='rating']/span[text()>{high_rating}]"
                                      f"/ancestor::div[@data-ti='train-offer-card']//span[@data-ti='stopover-time']")
    station = "Ленинградский вокзал"
    station_city = "Москва"
    certain_station_block = s(f"//span[@data-ti='stopover-place'][text()='{station}, {station_city}']"
                              "/ancestor::div[@data-ti='offer-card']")
    certain_station_reviews = s(f"//span[@data-ti='stopover-place'][text()='{station}, {station_city}']"
                                f"/ancestor::div[@data-ti='offer-card']//span[@data-ti='rating_badge_link']")
