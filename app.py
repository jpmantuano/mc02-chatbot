from flask import Flask
from swiplserver import PrologMQI, PrologThread

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    with PrologMQI() as mqi:
        with mqi.create_thread() as prolog_thread:
            result = prolog_thread.query("atom(a)")
            return str(result)
    # return 'Hello World!'


if __name__ == '__main__':
    app.run()
