from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    if name:
        return f"Hello, {name}!"
    else:
        return "Hello!"

if __name__ == '__main__':
    app.run()
