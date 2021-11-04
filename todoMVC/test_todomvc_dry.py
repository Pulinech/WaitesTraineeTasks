import time

from selene.support.shared.jquery_style import s, ss
from selene.support.shared import browser
from selene import have

browser.open_url("https://todomvc.com/examples/react/")


def test_common_tasks_management():
    # Add
    add('a', 'b', 'c')
    should_have_text('a', 'b', 'c')

    # Edit
    edit('b', ' edited').press_enter()

    # Delete
    find_by_text('b edited').s('.toggle').click()
    s('.clear-completed').click()
    should_have_text('a', 'c')

    # Cancel Edit
    edit('c', ' to be canceled').press_escape()

    # Delete
    find_by_text('c').hover().s('.destroy').click()
    should_have_text('a')


def add(*texts: str):
    for text in texts:
        s(".new-todo").type(text).press_enter()


def edit(text: str, add_text: str):
    ss(".todo-list>li").element_by(have.exact_text(text)).double_click()
    return ss(".todo-list>li").element_by(have.css_class("editing")).s(".edit").type(add_text)


def should_have_text(*texts: str):
    ss('.todo-list>li').should(have.exact_texts(*texts))


def find_by_text(text: str):
    return ss('.todo-list>li').element_by(have.exact_text(text))
