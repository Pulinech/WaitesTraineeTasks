from selene.support.shared import browser
import pytest


def pytest_addoption(parser):
    parser.addoption('--base-url', action='store', default="https://www.tutu.ru/poezda/",
                     help="Write url to open")


@pytest.fixture(autouse=True)
def browser_setup(request):
    base_url = request.config.getoption("base_url")
    browser.config.base_url = base_url
    browser.open(base_url)
    yield
    browser.quit()
