from selene.support.shared.jquery_style import s, ss
from selene import have
from selene import by
import pytest


def test_common_tasks_management(add_text):
    add('a', 'b', 'c')
    assert_text('a', 'b', 'c')

    edit_enter('b', add_text)

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


def test_add():
    add('a')
    assert_text('a')


def test_edit():
    add('a')
    edit_enter('a', ' edited')
    assert_text('a edited')


def test_cancel_edit():
    add('a')
    cancel_edit('a', ' to be canceled')
    assert_text('a')


def test_edit_by_tab():
    add('a')
    edit_tab('a', ' edited')
    assert_text('a edited')


def test_edit_by_click_outside():
    add('a')
    edit_click_outside('a', ' edited')
    assert_text('a edited')


def test_delete():
    add('a')
    delete('a')
    assert_text()


def test_complete():
    add('a')
    toggle('a')
    filter_completed()
    assert_text('a')


def test_uncomplete():
    add('a')
    toggle('a', 'a')
    filter_active()
    assert_text('a')


def test_complete_all():
    add('a', 'b')
    toggle_all()
    filter_completed()
    assert_text('a', 'b')


def test_uncomplete_all():
    add('a', 'b')
    toggle_all()
    toggle_all()
    filter_active()
    assert_text('a', 'b')


def test_clear_completed():
    add('a', 'b')
    toggle('b')
    clear_completed()
    assert_text('a')


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
