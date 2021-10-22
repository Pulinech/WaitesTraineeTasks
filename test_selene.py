from selene.support.shared.jquery_style import s, ss
from selene.support.shared import browser
from selene import by, be, have
from selene import command
from selene import query
import pytest
import time

result1 = []
result2 = []

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
    route_time1 = ss("//span[@data-ti='stopover-time']")
    for i in range(len(route_time1)):
        result1.append(route_time1[i].get(query.text))


s("[data-ti='icon']").click()
s("[data-ti='swap_stations']").click()
s("[data-ti='submit_button']").click()


if s("[data-ti='filter-sapsan']").should(be.visible, timeout=10):
    while last_departure_time.get(query.text) != "23:55":
        s("(//div[@data-ti='offer-card']/..)[last()]").perform(command.js.scroll_into_view)
if last_departure_time.get(query.text) == "23:55":
    route_time2 = ss("//span[@data-ti='stopover-time']")
    for i in range(len(route_time2)):
        result2.append(route_time2[i].get(query.text))


def test_different_search_results():
    amount1 = int(len(result1)/2)
    amount2 = int(len(result2)/2)
    print("\nSearch 1 results amount:", amount1)
    print("Search 2 results amount:", amount2)
    k = 0
    j = 1
    for i in range(min(amount1, amount2)):
        print(i+1, ": ", result1[k], "->", result1[j], " | ", result2[k], "->", result2[j])
        k = k + 2
        j = j + 2

    assert (result1 != result2), "Lists are matching"
