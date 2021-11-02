from selene.support.shared.jquery_style import s, ss
from selene.support.shared import browser
from selene import have

browser.open_url("https://todomvc.com/examples/react/")
tasks_list = ["a", "1"]


def test_todo_creation():
    for i in range(len(tasks_list)):
        s(".new-todo").set_value(tasks_list[i]).press_enter()
        ss(".todo-list label")[i].should(have.text(tasks_list[i]))


def test_todo_toggle_on_and_off():
    s(".toggle").click()
    s(".todo-list .completed label").should(have.text(tasks_list[0]))
    s(".toggle").click()
    s(".todo-list label").should(have.text(tasks_list[0]))


def test_todo_renaming():
    s(".todo-list label").double_click()
    s(".todo-list .edit").press(1).press_enter()
    tasks_list[0] += "1"
    s(".todo-list label").should(have.text(tasks_list[0]))


def test_todo_deletion():
    s(".destroy").hover().click()
    s(".todo-list label").should(have.no.text(tasks_list[0]))
