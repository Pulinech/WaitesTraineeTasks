from selene.support.shared.jquery_style import s, ss
from selene import have
from selene import by


def add(*texts: str):
    for text in texts:
        s(".new-todo").type(text).press_enter()


def assert_text(*texts: str):
    ss('.todo-list>li').should(have.exact_texts(*texts))


def edit_enter(text: str, add_text: str):
    ss(".todo-list>li").element_by(have.exact_text(text)).double_click()
    ss(".todo-list>li").element_by(have.css_class("editing")).s(".edit").type(add_text).press_enter()


def edit_tab(text: str, add_text: str):
    ss(".todo-list>li").element_by(have.exact_text(text)).double_click()
    ss(".todo-list>li").element_by(have.css_class("editing")).s(".edit").type(add_text).press_tab()


def edit_click_outside(text: str, add_text: str):
    ss(".todo-list>li").element_by(have.exact_text(text)).double_click()
    ss(".todo-list>li").element_by(have.css_class("editing")).s(".edit").type(add_text)
    s("h1").click()


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


def filter_all():
    s(by.partial_link_text("All")).click()


def filter_completed():
    s(by.partial_link_text("Completed")).click()


def filter_active():
    s(by.partial_link_text("Active")).click()


def toggle_all():
    s("[for='toggle-all']").click()
