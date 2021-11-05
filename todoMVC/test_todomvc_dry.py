from selene.support.shared.jquery_style import s, ss
from selene.support.shared import browser
from selene import have


def test_common_tasks_management(add_text):
    # Open
    open_app()

    # Add
    add('a', 'b', 'c')
    assert_text('a', 'b', 'c')

    # Edit
    edit('b', add_text).press_enter()

    # Delete
    find_by_text('b edited').s('.toggle').click()
    clear_completed()
    assert_text('a', 'c')

    # Cancel Edit
    edit('c', ' to be canceled').press_escape()

    # Delete
    find_by_text('c').hover().s('.destroy').click()
    assert_text('a')


def add(*texts: str):
    for text in texts:
        s(".new-todo").type(text).press_enter()


def edit(text: str, add_text: str):
    ss(".todo-list>li").element_by(have.exact_text(text)).double_click()
    return ss(".todo-list>li").element_by(have.css_class("editing")).s(".edit").type(add_text)


def assert_text(*texts: str):
    ss('.todo-list>li').should(have.exact_texts(*texts))


def find_by_text(text: str):
    return ss('.todo-list>li').element_by(have.exact_text(text))


def clear_completed():
    s('.clear-completed').click()


def open_app():
    browser.open("#/")
