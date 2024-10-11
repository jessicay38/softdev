# Jessica Yu
# JST
# K16 - Building onto the flask website 
# SoftDev
# Oct 09, 2024
# Time Spent: 

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session
import os

app = Flask(__name__)    #create Flask object
app.secret_key = os.urandom(32)

@app.route("/")
def disp_loginpage():
    if request.cookies.get('username') is None:
        return render_template( 'login.html' )
    else:
        return render_template("response.html", r = request.cookies.get('username'), method = request.method)

@app.route("/resp", methods=['GET', 'POST'])
def response():
    if request.method == "GET":
        session['username'] = request.args['username']
        return render_template("response.html", r = request.args['username'], method = request.method) #response to a form submission
    if request.method == "POST":
        session['username'] = request.form['username']
        return render_template("response.html", r = request.form['username'], method = request.method) #response to a form submission
    
@app.route("/logout", methods=['GET', 'POST'])
def logout():
    return render_template("logout.html")
    
if __name__ == "__main__": 
    app.debug = True 
    app.run()