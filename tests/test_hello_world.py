from flask_app.hello_world import app


# def test_app():
#     app.config['TESTING'] = True
#     client = app.test_client()


def test_hello():
    app.config['TESTING'] = True
    client = app.test_client()
    result = client.get('/')
    assert b"Hello World!" == result.data


def test_hello_name():
    app.config['TESTING'] = True
    client = app.test_client()
    result = client.get('/my_name')
    assert b"Hello my_name!" == result.data
