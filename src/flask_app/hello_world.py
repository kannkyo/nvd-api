
# https://realpython.com/flask-by-example-part-1-project-setup/

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """hello

    Returns:
        string: message
    """
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    """hello_name

    Args:
        name (string): 名前

    Returns:
        string: メッセージ
    """
    return "Hello {}!".format(name)


if __name__ == '__main__':
    """エントリポイント
    """
    app.run()
