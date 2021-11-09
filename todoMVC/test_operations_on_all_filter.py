from steps import todomvc


def test_add():
    todomvc.add('a')
    todomvc.assert_text('a')


def test_edit():
    todomvc.add('a')
    todomvc.edit_enter('a', ' edited')
    todomvc.assert_text('a edited')


def test_cancel_edit():
    todomvc.add('a')
    todomvc.cancel_edit('a', ' to be canceled')
    todomvc.assert_text('a')


def test_edit_by_tab():
    todomvc.add('a')
    todomvc.edit_tab('a', ' edited')
    todomvc.assert_text('a edited')


def test_edit_by_click_outside():
    todomvc.add('a')
    todomvc.edit_click_outside('a', ' edited')
    todomvc.assert_text('a edited')


def test_delete():
    todomvc.add('a')
    todomvc.delete('a')
    todomvc.assert_text()


def test_complete():
    todomvc.add('a')
    todomvc.toggle('a')
    todomvc.filter_completed()
    todomvc.assert_text('a')


def test_uncomplete():
    todomvc.add('a')
    todomvc.toggle('a', 'a')
    todomvc.filter_active()
    todomvc.assert_text('a')


def test_complete_all():
    todomvc.add('a', 'b')
    todomvc.toggle_all()
    todomvc.filter_completed()
    todomvc.assert_text('a', 'b')


def test_uncomplete_all():
    todomvc.add('a', 'b')
    todomvc.toggle_all()
    todomvc.toggle_all()
    todomvc.filter_active()
    todomvc.assert_text('a', 'b')


def test_clear_completed():
    todomvc.add('a', 'b')
    todomvc.toggle('b')
    todomvc.clear_completed()
    todomvc.assert_text('a')
