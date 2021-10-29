from pages.search_page import SearchPage
from selene.support.shared import browser, config
import pytest

link = "https://rozetka.com.ua/"
page = SearchPage()


@pytest.mark.parametrize("price_from, price_to", [(5000, 20000), (10000, 25000), (50, 17000)])
def test_filter_system(price_from, price_to):
    browser.open_url(link)
    config.driver.maximize_window()
    page.open_notebooks_page()
    page.filter_notebooks("Acer", min_price=price_from, max_price=price_to)
    page.check_filter_notebooks_price_and_model()
    browser.quit()
