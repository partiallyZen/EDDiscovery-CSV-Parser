import matplotlib.pyplot as plt
import pandas as pd                         #import whatcha need to parse and graph.
import numpy as np
import re
#%matplotlib inline


events=[]
event=()              #declare variables, events to be parsed and final lists
finallight=[]
finaldate=[]

df = pd.read_csv('C:\\Your\\Local\\Path\\YourFile.csv')

df = df.drop(['JID','EDSMID','EDDBID'], axis=1)    #remove extra columns (unless you need them)
df = df.dropna(how='all', axis=1) #remove empty columns
df = df.dropna(how='all', axis=0)  #remove empty rows

# An easy loop for removing or changing variables. 
to_remove = [c for c in df.columns if "Total" in c] # redundant
to_change = [c for c in df.columns if " ly" in c] # numeric# drop unwanted columns
# Notice that you need to specify inplace, otherwise pandas will return the data frame instead of changing it in place
#df.drop(to_remove, axis=1, inplace= True) # Change the target column data types
for c in to_change:
    df[c] = df[c].apply(lambda x: pd.to_numeric(x))

test = df[df['Whatever_Col_Name'].str.contains("STRING_TO_PARSE", na=False)] #here it pulls the column name and parses any with a string, ex. I used the 'Event' colum and pulled FSD Jumps


lightyears = test['Description'].tolist() #lightyears list
dateyears = test['Time'].tolist() #dates list


for row in lightyears:
    x = row[0:5]       
    finallight.append(x)                      #Appending finallists for more focused CSV file
    finallight = list(map(float, finallight))   #Making Lightyears into floats (for fun and future maths)

for row in dateyears:
    y = row[0:10]
    finaldate.append(y)

print(finallight)

print(finaldate)

import csv

myData = [finaldate, finallight]

with open('C:\\Users\\chick\\Desktop\\TESTER2.csv', 'w') as myFile:  #open csv for 'w'riting
    writer = csv.writer(myFile)
    for x in zip(*myData):                      
        myFile.write("{0}\t{1}\n".format(*x))

results = np.concatenate((finaldate, finallight), axis=0)  #concatenate list for following graph

plt.plot(results)
plt.xlabel('Date')
plt.ylabel('Lightyears Traveled')    #Little messy when using all that data, might need to move to aggregating items to date.
plt.title('Elite Dangerous Travels')

plt.show()