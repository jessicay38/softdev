# Jessica Yu
# SoftDev
# September 24 2024

from flask import Flask
app = Flask(__name__)             #create instance of class Flask

@app.route("/")                   #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)               #where will this go? in the terminal
    return "No hablo queso!"

app.run()

'''
it printed both of the messages in the terminal when I ran it
'''