import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl #using repl.it, no GUI server to display this on
mpl.use('Agg')

JSEIndex = []
JSEJunior = []
CombIndex = []
AllJamaican = []
JSESelect = []
USEquities =[]
ValuesDF = []

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

#All Jamaican
with open('index-history (3).csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        myList = row[2]
        myList = float(myList)
        AllJamaican.append(myList)
        
print(AllJamaican)

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
plt.plot(JSEJunior, label="JSE Junior")
plt.plot(JSEIndex, label="JSE Index")
plt.plot(CombIndex, label="Combined Index")
plt.plot(AllJamaican, label="All Jamacian")
plt.plot(JSESelect, label="JSE Select")
plt.plot(USEquities, label="US Equities")
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=3, mode="expand", borderaxespad=0.)
plt.savefig('graph.png')
plt.clf()

#finding cross correlations
#print(np.correlate(JSEJunior, JSEIndex))

#normalising each Index price
JSEJunior_normed = [i/sum(JSEJunior) for i in JSEJunior]
JSEIndex_normed = [i/sum(JSEIndex) for i in JSEIndex]
CombIndex_normed = [i/sum(CombIndex) for i in CombIndex]
AllJamaican_normed = [i/sum(AllJamaican) for i in AllJamaican]
JSESelect_normed = [i/sum(JSESelect) for i in JSESelect]
USEquities_normed = [i/sum(USEquities) for i in USEquities]
#print(JSEJunior_normed)

#plotting the normalised price values
plt.plot(JSEJunior_normed, label="JSE Junior")
plt.plot(JSEIndex_normed, label="JSE Index")
plt.plot(CombIndex_normed, label="Combined Index")
plt.plot(AllJamaican_normed, label="All Jamaican")
plt.plot(JSESelect_normed, label="JSE Select")
plt.plot(USEquities_normed, label="US Equities")
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=3, mode="expand", borderaxespad=0.)
plt.savefig('graph-norm.png')
plt.clf()

#ValuesDF = pd.DataFrame(list(zip(JSEJunior, JSEIndex, CombIndex, AllJamacian, JSESelect, USEquities)))
#print(ValuesDF)
StringCorr = []

#claculating the Pearson correlation
ValCorr = np.corrcoef(JSEJunior_normed, JSEIndex_normed)[0, 1]
StringCorr.append(ValCorr)
ValCorr = np.corrcoef(JSEJunior_normed, CombIndex_normed)[0, 1]
StringCorr.append(ValCorr)
ValCorr = np.corrcoef(JSEJunior_normed, AllJamaican_normed)[0, 1]
StringCorr.append(ValCorr)
ValCorr = np.corrcoef(JSEJunior_normed, JSESelect_normed)[0, 1]
StringCorr.append(ValCorr)
ValCorr = np.corrcoef(JSEJunior_normed, USEquities_normed)[0, 1]
StringCorr.append(ValCorr)
ValCorr = np.corrcoef(JSEIndex_normed, CombIndex_normed)[0, 1]
StringCorr.append(ValCorr)
ValCorr = np.corrcoef(JSEIndex_normed, AllJamaican_normed)[0, 1]
StringCorr.append(ValCorr)
ValCorr = np.corrcoef(JSEIndex_normed, JSESelect_normed)[0, 1]
StringCorr.append(ValCorr)
ValCorr = np.corrcoef(JSEIndex_normed, USEquities_normed)[0, 1]
StringCorr.append(ValCorr)
ValCorr = np.corrcoef(CombIndex_normed, AllJamaican_normed)[0, 1]
StringCorr.append(ValCorr)
ValCorr = np.corrcoef(CombIndex_normed, JSESelect_normed)[0, 1]
StringCorr.append(ValCorr)
ValCorr = np.corrcoef(CombIndex_normed, USEquities_normed)[0, 1]
StringCorr.append(ValCorr)
ValCorr = np.corrcoef(AllJamaican_normed, JSESelect_normed)[0, 1]
StringCorr.append(ValCorr)
ValCorr = np.corrcoef(AllJamaican_normed, USEquities_normed)[0, 1]
StringCorr.append(ValCorr)
ValCorr = np.corrcoef(JSESelect_normed, USEquities_normed)[0, 1]
StringCorr.append(ValCorr)

print(StringCorr)

plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],StringCorr,'g^', label="")
plt.savefig('graph-Corr.png')
plt.clf()

