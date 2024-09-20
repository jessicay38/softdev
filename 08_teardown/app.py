# your heading here

'''
DISCO:
<note any discoveries you made here... no matter how small!>

QCC:
0. You know you are in the virtual enviornment when you see the name of the enviornment in paranthesis.
1. You can install things in the virtual enviornment.
2. There's a couple files in there.
3. To activate you write . name_of_file/activate
4. To deactivate, you say deactivate
5. When you cd the files, there are other files inside.
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
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?

app.run()                                # Q5: Where have you seen similar constructs in other languages?


