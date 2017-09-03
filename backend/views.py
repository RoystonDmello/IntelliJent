# from backend import app
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def show():
    return render_template('test.html')