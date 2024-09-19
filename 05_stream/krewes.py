#Jessica Yu
#JST
#SoftDev
#K05 - Working with File Parsing
#2024-9-18
#time spent: 1 hour

import random

def makeList():
    krew = open("krewes.txt", "r") #opens text file
    devos = []
    members = krew.read().split("@@@") #splits members
    for m in members:
        i = m.split("$$$") #splits into rsepective categories
        devos.append({"Period": i[0], "Devo": i[1], "Ducky": i[2]}) #make list
makeList()
def randDevo():
    number = random.randint(0, len(devos) - 1) #chooses a number from the range
    r = devos[number] #chooses the devo assigned to that number
    return (r["Devo"] + " " + r["Period"] + " " + r["Ducky"]) #return info about devo

    
print(randDevo())
    
