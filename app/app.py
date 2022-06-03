from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello():
    view = 'Hello World!\n\n'
    view += str(request.headers)
    view = view.replace('\n', '<br>')
    return view