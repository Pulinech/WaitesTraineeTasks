from pages.search_page import SearchPage
from selene.support.shared import browser
import pytest


def test_different_search_results():
    link = "https://www.tutu.ru/poezda/"
    browser.open_url(link)
    page = SearchPage()
    page.search_trains_from_city_a_to_city_b()
    page.get_trains_from_city_a_to_city_b_schedule()
    page.search_trains_from_city_b_to_city_a()
    page.get_trains_from_city_b_to_city_a_schedule()
    page.should_be_different_trains_schedule()
    page.print_trains_schedules()
