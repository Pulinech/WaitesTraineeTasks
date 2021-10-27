from pages.search_page import SearchPage
from selene.support.shared import browser

link = "http://seasonvar.ru/"
page = SearchPage()


def test_filter_for_countries():
    browser.open_url(link)
    page.select_country()
    page.show_and_get_filter_results()
    page.should_be_country_for_every_serial()
    browser.quit()


def test_filter_for_genres():
    browser.open_url(link)
    page.select_genre()
    page.show_and_get_filter_results()
    page.should_be_genre_for_every_serial()
    browser.quit()


def test_search_system():
    browser.open_url(link)
    page.should_be_search_serials_results("1")
    page.check_search_input_in_serials_names()
    page.should_be_search_input_in_serial_alternative_or_original_name()
    browser.quit()


def test_search_system_fail():
    browser.open_url(link)
    page.should_be_search_serials_results("%")
    browser.quit()


def test_mark_serials_time_system():
    browser.open_url(link)
    page.log_in_into_account()
    page.get_serials_to_open()
    page.open_serials_and_mark_series_time()
    page.should_be_marks_with_serials_names()
    browser.quit()
