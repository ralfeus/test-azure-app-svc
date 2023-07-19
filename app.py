from flask import Flask

app = Flask("MyApp at Azure")

@app.route('/')
def index():
  return "This is test"

@app.route('/<name>')
def greet(name):
  return f"<h1>Hello {name}!</h1>"
