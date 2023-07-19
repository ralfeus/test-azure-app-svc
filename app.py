from flask import Flask

app = Flask("MyApp at Azure")

@app.route('/')
def index():
  return "This is test"
