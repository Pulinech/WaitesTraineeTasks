from steps.todomvc import TodoMVC
from selene.support.shared import browser

todomvc = TodoMVC()


class TestWithMultipleTabs:

    def test_open_and_close_new_tab(self):
        todomvc.open_in_new_tab('https://github.com/yashaka/selene')
        todomvc.switch_to_tab(1)
        todomvc.check_tab_name("GitHub - yashaka/selene: User-oriented Web UI browser tests in Python")
        browser.close_current_tab()
        todomvc.switch_to_tab(0)
        todomvc.check_tab_name("React • TodoMVC")

    def test_work_in_two_tabs(self):
        todomvc.add('a', 'b', 'c')
        todomvc.open_in_new_tab('#/')
        todomvc.switch_to_tab(1)
        todomvc.assert_text('a', 'b', 'c')
        todomvc.delete('c')
        todomvc.switch_to_tab(0)
        todomvc.assert_text('a', 'b')
        todomvc.edit_enter('b', ' edited')
        todomvc.switch_to_tab(1)
        todomvc.assert_text('a', 'b edited')
