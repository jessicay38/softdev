#Jessica Yu
#JST
#SoftDev
#skeleton/stub :: SQLITE3 BASICS
#Oct 18, 2024
#Time Spent:

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~s~~~~~~~~~~~~~~~~~~~~~~~~
< < < INSERT YOUR TEAM'S DB-POPULATING CODE HERE > > >
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
dict = []
with open("course.csv", newline = '') as file:
    courses = csv.DictReader(file)
    for i in courses:
        dict.append(i)

c.execute("CREATE TABLE course (code TEXT, mark INTEGER, id INTEGER)")
for row in dict:
    v = "(" + (row.get("code")) + ", " + (row.get("mark")) + ", " + (row.get("id")) + ")"

    c.execute(f'INSERT INTO course (code, mark, id) VALUES {v}')

with open("students.csv", newline = '') as file:
    students = csv.DictReader(file)
    for i in students:
        dict.append(i)

c.execute("CREATE TABLE roster (name TEXT, age INTEGER, id INTEGER)")
for row in dict:
    v = "(" + (row.get("name")) + ", " + (row.get("age")) + ", " + (row.get("id")) + ")"

    c.execute(f'INSERT INTO roster (name, age, id) VALUES {v}')


command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
