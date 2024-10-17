# Jessica Yu
# JST
# Softdev
# K18 - More Flask
# 2024-10-16
# Time Spent:

from flask import Flask
from flask import render_template
from flask import request
from flask import session

app = Flask(__name__)

@app.route('/')
def display():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()