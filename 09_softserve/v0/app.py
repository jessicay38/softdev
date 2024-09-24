# Jessica Yu
# SoftDev
# September23, 2024

from flask import Flask
app = Flask(__name__)          # creates an instance of the class

@app.route("/")                # assigns a route to flask
def hello_world():
    print(__name__)            # prints the next return statement on the site
    return "No hablo queso!"   # prints this on the website

app.run()                      # runs it
                