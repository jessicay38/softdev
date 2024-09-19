#Jessica Yu
#Softdev
#K06 - Dictionary from CSV file
#2024-9-19
#time spent:

import csv
import random
dictionary = {}

with open('occupations.csv', newline=' ') as csvfile:
    occupations = csv.reader(csvfile) 
