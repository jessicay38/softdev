'''
Jessica Yu
Loonch
SoftDev
K09 -- Putting it Together : Learning about Flask and app.py
2024-09-24
Time spent: 1 hour
'''

import random
import csv

occupation_list = []
percentages = []

with open('occupations.csv', newline ='') as csvfile:
    file = csv.DictReader(csvfile)
    for row in file:
        occupation_list.append(row['Job Class'])
        percentages.append((float)(row['Percentage']))

occupation_list = occupation_list[1:-1]
percentages = percentages[1:-1]

def select_occupation(occupation_list, percentages):
    return random.choices(occupation_list, weights=percentages, k=1)
     
    # -------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def page():
    occupation = select_occupation(occupation_list, percentages)
    html = """
    <!DOCTYPE html>
    <html>
        <body>
            <p> Loonch with Wen, Tracy, and Jessica. </p>
            <h1> Selected Occupation: """ + occupation[0] + """</h1>
             Occupationlist 
    """
    jobs = "<table><tr><th> Job List </tr></th>"
    for job in occupation_list:
        jobs += "<tr><td> " + job + " </tr></td>"
        
    jobs += "</table>"
    html = html.replace("Occupationlist", jobs)
    return html
    
    
if __name__ == "__main__":      
    app.debug = True            
    app.run()