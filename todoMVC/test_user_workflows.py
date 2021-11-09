from steps.todomvc import TodoMVC

todomvc = TodoMVC()


class TestUserWorkflow:
    def test_common_tasks_management(self, add_text):
        todomvc.add('a', 'b', 'c')
        todomvc.assert_text('a', 'b', 'c')

        todomvc.edit_enter('b', add_text)

        todomvc.toggle('b edited')
        todomvc.clear_completed()
        todomvc.assert_text('a', 'c')

        todomvc.cancel_edit('c', ' to be edited')

        todomvc.delete('c')
        todomvc.assert_text('a')

    def test_filtering(self):
        todomvc.add('a', 'b', 'c')
        todomvc.assert_text('a', 'b', 'c')

        todomvc.toggle('b')

        todomvc.filter_completed()
        todomvc.assert_text('b')

        todomvc.filter_active()
        todomvc.assert_text('a', 'c')
