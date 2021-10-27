from pages.search_page import SearchPage
from selene.support.shared import browser

link = "https://www.tutu.ru/poezda/"
page = SearchPage()


def test_different_search_results():
    browser.open_url(link)
    page.search_trains_from_city_a_to_city_b()
    page.get_trains_from_city_a_to_city_b_schedule()
    page.search_trains_from_city_b_to_city_a()
    page.get_trains_from_city_b_to_city_a_schedule()
    page.should_be_different_trains_schedule()
    page.print_and_write_to_file_trains_schedules()
    browser.quit()


def test_find_certain_rating_trains():
    browser.open_url(link)
    page.search_trains_from_city_a_to_city_b()
    page.get_trains_from_city_a_to_city_b_schedule()
    page.get_trains_with_rating_lower_than()
    page.get_trains_with_rating_higher_than()
    page.print_and_write_to_file_low_rating_trains_schedule()
    page.print_and_write_to_file_high_rating_trains_schedule()
    browser.quit()


def test_find_certain_terminal_and_check_info_about_trip():
    browser.open_url(link)
    page.search_trains_from_city_a_to_city_b()
    page.get_trains_from_city_a_to_city_b_schedule()
    page.should_be_info_of_train_from_certain_terminal()
    page.should_be_trip_details_and_certain_city_terminal()
    browser.quit()
