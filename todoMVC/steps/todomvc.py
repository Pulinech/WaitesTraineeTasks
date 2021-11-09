from selene.support.shared.jquery_style import s, ss
from selene import have
from selene import by


class TodoMVC:

    # Page locators
    def __init__(self):
        self.todos = ss(".todo-list>li")
        self.click_outside = s("h1")

        # Input locators
        self.input_todo = s(".new-todo")
        self.input_edit = ss(".todo-list>li").element_by(have.css_class("editing")).s(".edit")

        # Button locators
        self.btn_clear_completed = s(".clear-completed")
        self.btn_toggle_all = s("[for='toggle-all']")

        # Filter locators
        self.filter_by_all = s(by.partial_link_text("All"))
        self.filter_by_active = s(by.partial_link_text("Active"))
        self.filter_by_completed = s(by.partial_link_text("Completed"))

    def add(self, *texts: str):
        for text in texts:
            self.input_todo.type(text).press_enter()

    def assert_text(self, *texts: str):
        self.todos.should(have.exact_texts(*texts))

    def edit_enter(self, text: str, add_text: str):
        self.todos.element_by(have.exact_text(text)).double_click()
        self.input_edit.type(add_text).press_enter()

    def edit_tab(self, text: str, add_text: str):
        self.todos.element_by(have.exact_text(text)).double_click()
        self.input_edit.type(add_text).press_tab()

    def edit_click_outside(self, text: str, add_text: str):
        self.todos.element_by(have.exact_text(text)).double_click()
        self.input_edit.type(add_text)
        self.click_outside.click()

    def cancel_edit(self, text: str, add_text: str):
        self.todos.element_by(have.exact_text(text)).double_click()
        self.input_edit.type(add_text).press_escape()

    def toggle(self, *texts: str):
        for text in texts:
            self.todos.element_by(have.exact_text(text)).s(".toggle").click()

    def clear_completed(self):
        self.btn_clear_completed.click()

    def delete(self, text: str):
        self.todos.element_by(have.exact_text(text)).hover().s(".destroy").click()

    def filter_all(self):
        self.filter_by_all.click()

    def filter_completed(self):
        self.filter_by_completed.click()

    def filter_active(self):
        self.filter_by_active.click()

    def toggle_all(self):
        self.btn_toggle_all.click()
