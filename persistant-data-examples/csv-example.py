import csv

#import pandas - have to make a venv and do pip install pandas in the terminal
import pandas

#create a csv file with a list of villains first name and last name
#we can use lists and other collection to help do this
#we will use 2 dimenionsal list to this (a list of lists)

villians = [
    ["Doctor", "Doom"],
    ["Lex", "Luther"],
    ["Rosa", "Kleb" ]
]


#wt writes with a stream (collection) of data
with open('villains.csv', "wt") as myfile:
    csvout = csv.writer(myfile)
    csvout.writerows(villians)

#use pandas to read csv
data = pandas.read_csv('villains.csv')
print(data)