from flask import Flask
from flask import render_template, request


app = Flask(__name__)

@app.route('/')
def hello_func():
    name = request.args.get('name')
    message = request.args.get('message')
    result = render_template('main.html', name=name, text=message)
    return result

if __name__ == '__main__':
    app.run(port=8000)
    