import time

from selene.support.shared.jquery_style import s, ss
from selene.support.shared import browser
from selene import have
from selene import by
import pytest


def test_common_tasks_management(add_text):
    add('a', 'b', 'c')
    assert_text('a', 'b', 'c')

    edit('b', add_text)

    toggle('b edited')
    clear_completed()
    assert_text('a', 'c')

    cancel_edit('c', ' to be edited')

    delete('c')
    assert_text('a')


def test_filtering():
    add('a', 'b', 'c')
    assert_text('a', 'b', 'c')

    toggle('b')

    filter_completed()
    assert_text('b')

    filter_active()
    assert_text('a', 'c')

    filter_all()


def add(*texts: str):
    for text in texts:
        s(".new-todo").type(text).press_enter()


def assert_text(*texts: str):
    ss('.todo-list>li').should(have.exact_texts(*texts))


def edit(text: str, add_text: str):
    ss(".todo-list>li").element_by(have.exact_text(text)).double_click()
    ss(".todo-list>li").element_by(have.css_class("editing")).s(".edit").type(add_text).press_enter()


def cancel_edit(text: str, add_text: str):
    ss(".todo-list>li").element_by(have.exact_text(text)).double_click()
    ss(".todo-list>li").element_by(have.css_class("editing")).s(".edit").type(add_text).press_escape()


def toggle(*texts: str):
    for text in texts:
        ss(".todo-list>li").element_by(have.exact_text(text)).s(".toggle").click()


def clear_completed():
    s(".clear-completed").click()


def delete(text: str):
    ss(".todo-list>li").element_by(have.exact_text(text)).hover().s(".destroy").click()


def open_app():
    browser.open("#/")


def filter_all():
    s(by.partial_link_text("All")).click()


def filter_completed():
    s(by.partial_link_text("Completed")).click()


def filter_active():
    s(by.partial_link_text("Active")).click()
