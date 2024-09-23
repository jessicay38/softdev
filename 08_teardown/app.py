# your heading here

'''
DISCO:
<note any discoveries you made here... no matter how small!>

You know you are in the virtual enviornment when you see the name of the enviornment in paranthesis.
You can install things in the virtual enviornment.
There's a couple files in there.
To activate you write . name_of_file/activate
To deactivate, you say deactivate
When you cd the files, there are other files inside.

QCC:
0. In java, when you create objects.
1. File system route
2. Print prints into the terminal.
3. It prints whatever is in the print statement
4. This appears on a website that is linked when you run it.
5. Javacado
 ...

INVESTIGATIVE APPROACH: Be open to exploring and testing through the things in the enviornment.
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__)
    print("hi")# Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?

app.run()                                # Q5: Where have you seen similar constructs in other languages?


