'''
Jessica Yu
Loonch
SoftDev
K09 -- Putting it Together : Learning about Flask and app.py
2024-09-24
Time spent: 
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
def randOccupation():
    print(__name__)
    return select_occupation(occupation_list, percentages)

app.run()