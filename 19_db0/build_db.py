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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
< < < INSERT YOUR TEAM'S DB-POPULATING CODE HERE > > >
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
CREATE TABLE students (
    name TEXT PRIMARY KEY,
    id INTEGER NOT NULL UNIQUE
)

insert into students values();

CREATE TABLE courses (
    course_name TEXT PRIMARY KEY,
    grade INTEGER,
    id INTEGER NOT NULL UNIQUE
)

insert into courses values();

command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
