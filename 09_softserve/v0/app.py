# Jessica Yu
# SoftDev
# September23, 2024

from flask import Flask
app = Flask(__name__)          # ... it resembles java syntax

@app.route("/")                # ... the things in print will print in the terminal
def hello_world():
    print(__name__)            # ... print(__name__) gives you the link
    return "No hablo queso!"
    return "hi"  # ... return will print straight onto the website

@app.route("/") 
def anything():
    print(__name__)
    return "hi"
app.run()                      # ... making another definition doesn't print onto the website
                