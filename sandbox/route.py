from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_word():
  return '<h1>Hello, World!</h1>'

@app.route('/about/<username>')
def about_page(username):
  return f'<h1>{username}</h1>'