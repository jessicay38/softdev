#Jessica Yu
#JST
#SoftDev
#K04 - Create a program that can choose a random devo from one of the periods.
#2024-9-16
#time spent: 0.5 
    
krewes = {
           4: [ 
        'DUA','TAWAB','EVA','JACK','VICTOR','EVAN','JASON','COLYI','IVAN','TANZEEM',
        'TAHMIM','STANLEY','LEON','NAOMI','NIA','ANASTASIA','JADY','BRIAN','JACOB',
        'ALEX','CHONGTIAN','DANNY','MARCO','ABIDUR','ANKITA','ANDY','ETHAN','AMANDA',
        'AIDAN','LINDA','QIANJUN','JIAYING','KISHI'
        ],
           5: [ 
                'ADITYA','MARGIE','RACHEL','ALEXANDER','ZIYAD','DANNY','ENDRIT','CADEN',
                'VEDANT','SUHANA','KYLE','KEVIN','RAYMOND','CHRISTOPHER','JONATHAN','SASHA',
                'NAFIYU','TIM','WILL','DANIEL','BENJAMIN','CLAIRE','CHLOE','STELLA','TRACY',
                'JESSICA','JACKIE','WEN YUAN','YINWEI','TIFFANY','JAYDEN DANIEL','PRINCEDEN' 
              ]
         }

import random

def dic():
    period = random.choice(list(krewes)) # chooses a random period from the krewes list
    devo = random.choice(krewes[period]) # chooses a name of devo from the chosen period 
    return devo 

def dict():
    length = len(krewes) # gets the length of the list
    t = list(krewes.keys()) # gets the period numbers
    period = t[random.randint(0, length - 1)] # chooses a period
    length = len(krewes[period]) # gets number of devos in period
    name = krewes[period][random.randint(0, length - 1)] # chooses a devo
    return name
                
    
    
print(dic())
print(dict())