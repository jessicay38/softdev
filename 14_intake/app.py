# Jessica Yu 
# JST
# SoftDev
# October 7, 2024
# Time Spent: 40 minutes

# import conventions:
# list most general first (standard python library)
# ...then pip installs (eg Flask)
# ...then your own home-rolled modules/packages (today's test module)

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

import testmod0

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
 * Some will work as written;
 *  ...other sections will not. 

TASK:
 Predict which.
 1. Devise simple tests to isolate components/behaviors.
 2. Execute your tests.
 3. Process results.
 4. Findings yield new ideas for more tests? Yes: do them.

PROTIP: Insert your own in-line comments
 wherever they will help
  your future self and/or current teammates
   understand what is going on.
'''

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    print("\n\n\n")   # We think this will print 3 line breaks in the terminal ## YES
    print("***DIAG: this Flask obj ***")   # We think this will print the words in bold ## NO! This created a folder called _pycache_ with UTF-8 files inside it. And added new line when reran: ## Rerunning has new line, '***DIAG: this Flask obj ***'
    print(app)   # We think this will produce an error ## <Flask 'app'>
    print("***DIAG: request obj ***")   # Never mind, we have no clue what this does! ## Added new line when reran: ## Rerunning has new line, '***DIAG: request obj ***'
    print(request)   # We ask for a user input and then print it in the terminal ## Added a new line in terminal that says <Request 'http://127.0.0.1:5000/' [GET]>
    print("***DIAG: request.args ***")   # Never mind, we have no clue what this does! ## Rerunning has new line, '***DIAG: request.args ***'
    print(request.args)   # Perhaps an error ## ImmutableMultiDict([])
    print("***DIAG: request.args['username']  ***")   # Never mind, we have no clue what this does! ## ***DIAG: request.args['username']  ***
    #print(request.args['username'])   # Maybe it asks for a 'username' input ## BadREquestKeyError
    print("***DIAG: request.headers ***")   # Never mind, we have no clue what this does! ## ***DIAG: request.headers ***
    print(request.headers)   # Mayhaps an error # Added a ton of lines 
    return render_template( 'login.html' )


@app.route("/auth" , methods=['GET', 'POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.args['username']  ***")
    print(request.args['username'])   ## did not crash this time
    print("***DIAG: request.headers ***")
    print(request.headers) ## same things as above
    return "Waaaa hooo HAAAH"  #response to a form submission


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
