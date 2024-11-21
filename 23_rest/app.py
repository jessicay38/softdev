# Jessica Yu
# SoftDev
# K23 -- A RESTful Journey Skyward
# 2024-11-20
# Time Spent: 1

import urllib.request
import json
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def nasa():
    with open("key_nasa.txt", "r") as file:
        key = file.read()
    request = urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=' + key)
    page_content = json.loads(request.read())
    return render_template('main.html', explanation = page_content["explanation"], image = page_content["hdurl"])

if __name__ == "__main__":
    app.debug = True
    app.run()
