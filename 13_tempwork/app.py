'''
Jessica Yu
JST
SoftDev
K13 -- Template for Success: Ultimate compilation of everything we have done and learned so far!
2024-10-02
Time Spent : 2h
'''
# most of the time was decorating the page

import csv, random
jobs = []
percents = []
link = []
header = []
occ_Dict = {}

with open ("data/occupations.csv", newline='') as csvfile:
    file = csv.DictReader(csvfile)
    for i in file:
        jobs.append(i["Job Class"]) # fill job
        percents.append((float)(i["Percentage"])) # fill percents
        link.append(i["Link"]) # fill link
        occ_Dict.update({i["Job Class"]:[(i["Percentage"]), (i["Link"])]}) # Dictionary with percents and links attached to each job
    header = list(i.keys()) # keys

# remove extraneous
jobs = jobs[:len(jobs)-1]
percents = percents[:len(percents)-1]
link = link[:len(link)-1]

# title info, team info
title = "Weighted Jobs in Room 250"
roster = ["Tracy Ye", "Jessica Yu", "Stella Yampolsky"]

# random weighted, built in function
def randWeighted():
    return random.choices(jobs, weights = percents) # (sequence, weight, num returns)

# -------------------------------------------------------

from flask import Flask, render_template
app = Flask(__name__)

# links to banaananananana
@app.route("/")
def main():
    return "<center>"+"<br>"*15+"<a href= 'http://127.0.0.1:5000/wdywtbwygp'>Click! Here!</a></center>"

# the route you asked for
@app.route("/wdywtbwygp")
def banana():
    return render_template("tablified.html", j = jobs, p = percents, h = header, t = title, r = roster, randW = randWeighted(), l = link)
    
# purple screen of death was helpful :D
if __name__ == "__main__":
        app.debug = True
        app.run()