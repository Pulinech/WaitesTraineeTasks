from steps.todomvc import TodoMVC

todomvc = TodoMVC()


class TestOnAllFilter:
    def test_add(self):
        todomvc.add('a')
        todomvc.assert_text('a')

    def test_edit(self):
        todomvc.add('a')
        todomvc.edit_enter('a', ' edited')
        todomvc.assert_text('a edited')

    def test_cancel_edit(self):
        todomvc.add('a')
        todomvc.cancel_edit('a', ' to be canceled')
        todomvc.assert_text('a')

    def test_edit_by_tab(self):
        todomvc.add('a')
        todomvc.edit_tab('a', ' edited')
        todomvc.assert_text('a edited')

    def test_edit_by_click_outside(self):
        todomvc.add('a')
        todomvc.edit_click_outside('a', ' edited')
        todomvc.assert_text('a edited')

    def test_delete(self):
        todomvc.add('a')
        todomvc.delete('a')
        todomvc.assert_text()

    def test_complete(self):
        todomvc.add('a')
        todomvc.toggle('a')
        todomvc.filter_by_completed()
        todomvc.assert_text('a')

    def test_uncomplete(self):
        todomvc.add('a')
        todomvc.toggle('a', 'a')
        todomvc.filter_by_active()
        todomvc.assert_text('a')

    def test_complete_all(self):
        todomvc.add('a', 'b')
        todomvc.toggle_all()
        todomvc.filter_by_completed()
        todomvc.assert_text('a', 'b')

    def test_uncomplete_all(self):
        todomvc.add('a', 'b')
        todomvc.toggle_all()
        todomvc.toggle_all()
        todomvc.filter_by_active()
        todomvc.assert_text('a', 'b')

    def test_clear_completed(self):
        todomvc.add('a', 'b')
        todomvc.toggle('b')
        todomvc.clear_completed()
        todomvc.assert_text('a')
