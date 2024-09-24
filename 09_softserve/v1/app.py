# Jessica Yu
# SoftDev
# September 24 2024

from flask import Flask
app = Flask(__name__)            #create instance of class Flask

@app.route("/")                  #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

'''
the app route connects to the website where the return statement is displayed
'''
