from context import app

def test_do_some_print():
    assert app.do_some_print('Bar') == 'Foo Bar Baz'