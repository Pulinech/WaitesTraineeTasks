import time

from selene.support.shared.jquery_style import s, ss
from selene.support.shared import browser
from selene import have

browser.open_url("https://todomvc.com/examples/react/")
tasks_list = ["a", "1"]


def test_common_tasks_management():
    add('a', 'b', 'c')
    should_have_text('a', 'b', 'c')

    edit('b', ' edited')

    complete('b edited')
    clear_completed()
    should_have_text('a', 'c')

    cancel_edit('c', ' to be edited')

    delete('c')
    should_have_text('a')


def add(*texts: str):
    for text in texts:
        s(".new-todo").type(text).press_enter()


def should_have_text(*texts: str):
    ss('.todo-list>li').should(have.exact_texts(*texts))


def edit(text: str, add_text: str):
    ss(".todo-list>li").element_by(have.exact_text(text)).double_click()
    return ss(".todo-list>li").element_by(have.css_class("editing")).s(".edit").type(add_text).press_enter()


def complete(text: str):
    ss(".todo-list>li").element_by(have.exact_text(text)).s(".toggle").click()


def clear_completed():
    s(".clear-completed").click()


def cancel_edit(text: str, add_text: str):
    ss(".todo-list>li").element_by(have.exact_text(text)).double_click()
    ss(".todo-list>li").element_by(have.css_class("editing")).s(".edit").type(add_text).press_escape()


def delete(text: str):
    ss(".todo-list>li").element_by(have.exact_text(text)).hover().s(".destroy").click()
