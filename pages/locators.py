from selene.support.shared.jquery_style import s, ss
from selene import by, be, have
from selene import command
from selene import query


class SearchPageLocators:
    last_departure_time = s("(//div[@data-ti='card-departure-0']//span[@data-ti='stopover-time'])[last()]")
    results_load = s("[data-ti='filter-sapsan']")
    last_search_element = s("(//div[@data-ti='offer-card']/..)[last()]")
    train_schedule = ss("//span[@data-ti='stopover-time']")
