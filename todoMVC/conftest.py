import time

from selene.support.shared import config, browser
import requests
import pytest


def pytest_addoption(parser):
    parser.addoption('--base-url', action='store', default='https://todomvc.com/examples/react/',
                     help="Write url to open")
    parser.addoption('--timeout', action='store', default=2,
                     help="Set explicit timeout")
    parser.addoption('--save_page_source', action='store', default=True,
                     help="Save page source on failure true/false")
    parser.addoption('--edit_task', action='store', default=" edited",
                     help="Set text to add to task")


@pytest.fixture(autouse=True)
def browser_setup(request):
    base_url = request.config.getoption("base_url")
    browser.config.base_url = base_url

    timeout = request.config.getoption("timeout")
    browser.config.timeout = float(timeout)

    save_page_source = request.config.getoption("save_page_source")
    browser.config.save_page_source_on_failure = save_page_source

    browser.config.set_value_by_js = True


@pytest.fixture(autouse=True)
def todomvc_with_cleared_data_after_test():
    browser.open('#/')
    yield
    # Reopen filter All, because clear_local_storage doesn't work at Active/Completed filters
    browser.open('#/')
    browser.clear_local_storage()



@pytest.fixture
def add_text(request):
    return request.config.getoption('--edit_task')
