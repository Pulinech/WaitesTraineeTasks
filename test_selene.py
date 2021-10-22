from selene.support.shared.jquery_style import s, ss
from selene.support.shared import browser
from selene import by, be, have
from selene import command
from selene import query
import pytest
import time


browser.open_url("https://www.tutu.ru/poezda/")
s("[name=schedule_station_from]").set_value("Москва")
s("[name=schedule_station_to]").set_value("Санкт-Петербург")
s("[data-ti='date_arrow_increase']").click()
s(".button_wrp").click()


last_departure_time = s("(//div[@data-ti='card-departure-0']//span[@data-ti='stopover-time'])[last()]")
if s("[data-ti='filter-sapsan']").should(be.visible, timeout=10):
    while last_departure_time.get(query.text) != "23:55":
        s("(//div[@data-ti='offer-card']/..)[last()]").perform(command.js.scroll_into_view)
if last_departure_time.get(query.text) == "23:55":
    time_route1 = ss("//span[@data-ti='stopover-time']")


s("[data-ti='icon']").click()
s("[data-ti='swap_stations']").click()
s("[data-ti='submit_button']").click()


if s("[data-ti='filter-sapsan']").should(be.visible, timeout=10):
    while last_departure_time.get(query.text) != "23:55":
        s("(//div[@data-ti='offer-card']/..)[last()]").perform(command.js.scroll_into_view)
if last_departure_time.get(query.text) == "23:55":
    time_route2 = ss("//span[@data-ti='stopover-time']")


def test_different_search_results():
    print("\nSearch 1 results amount:", len(time_route1) / 2)
    print("Search 2 results amount:", len(time_route2) / 2)
    assert (time_route1 != time_route2), "Lists are matching"
