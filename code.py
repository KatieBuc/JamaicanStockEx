import csv
import matplotlib.pyplot as plt
#import numpy as np
import matplotlib as mpl #using repl.it, no GUI server to display this on
mpl.use('Agg')
JSEIndex = []
JSEJunior = []
CombIndex = []
AllJamacian = []
JSESelect = []
USEquities =[]

#JSE Index
with open('index-history.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        myList = row[2]
        myList = float(myList)
        JSEIndex.append(myList)
        
print(JSEIndex)

#JSE Junior
with open('index-history (1).csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        myList = row[2]
        myList = float(myList)
        JSEJunior.append(myList)
        
print(JSEJunior)

#Combined Index
with open('index-history (2).csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        myList = row[2]
        myList = float(myList)
        CombIndex.append(myList)
        
print(CombIndex)

#All Jamacian
with open('index-history (3).csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        myList = row[2]
        myList = float(myList)
        AllJamacian.append(myList)
        
print(AllJamacian)

#JSE Select
with open('index-history (4).csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        myList = row[2]
        myList = float(myList)
        JSESelect.append(myList)
        
print(JSESelect)

#US Equities
with open('index-history (5).csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        myList = row[2]
        myList = float(myList)
        USEquities.append(myList)
        
print(USEquities)

#plot prices
plt.plot(JSEJunior)
plt.plot(JSEIndex)
plt.plot(CombIndex)
plt.plot(AllJamacian)
plt.plot(JSESelect)
plt.plot(USEquities)
plt.savefig('graph.png')
