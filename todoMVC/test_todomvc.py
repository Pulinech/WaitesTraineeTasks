from selene.support.shared.jquery_style import s, ss
from selene.support.shared import browser
from selene import have


def test_common_tasks_management(add_text):
    browser.open_url("#/")

    # Add
    s(".new-todo").type('a').press_enter()
    s(".new-todo").type('b').press_enter()
    s(".new-todo").type('c').press_enter()
    ss(".todo-list>li").should(have.exact_texts('a', 'b', 'c'))

    # Edit
    ss(".todo-list>li").element_by(have.exact_text('b')).double_click()
    ss(".todo-list>li").element_by(have.css_class("editing")).s(".edit").type(add_text).press_enter()

    # Complete & Clear
    ss(".todo-list>li").element_by(have.exact_text('b edited')).s(".toggle").click()
    s(".clear-completed").click()
    ss(".todo-list>li").should(have.no.exact_text('b edited'))

    # Cancel Edit
    ss(".todo-list>li").element_by(have.exact_text('c')).double_click()
    ss(".todo-list>li").element_by(have.css_class("editing")).s(".edit").type(" to be canceled").press_escape()

    # Delete
    ss(".todo-list>li").element_by(have.exact_text('c')).hover().s(".destroy").click()
    ss(".todo-list>li").should(have.exact_text('a'))
