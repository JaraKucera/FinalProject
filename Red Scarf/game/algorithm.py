import pymongo
import numpy as np
from pymongo import MongoClient

class Row:
    def __init__(self, c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12):
        self.c1 = c1 #Choices 1-12
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
        self.c5 = c5
        self.c6 = c6
        self.c7 = c7
        self.c8 = c8
        self.c9 = c9
        self.c10 = c10
        self.c11 = c11
        self.c12 = c12
        self.c13 = "" #Depression level
    
class Col:
    def __init__(self):
        self.colList = []

    def add(self, element):
        self.colList.append(element)    

client = MongoClient('******')
db = client.mongodb4075
data = db.projectTest
x = data.find()
tableList = []
for dRow in x:
    row = Row(dRow['Choice 1'], dRow['Choice 2'], dRow['Choice 3'], dRow['Choice 4'], dRow['Choice 5'], dRow['Choice 6'], dRow['Choice 7'], dRow['Choice 8'], dRow['Choice 9'], dRow['Choice 10'], dRow['Choice 11'], dRow['Choice 12'])
    tableList.append(row)

#for obj in tableList:
 #   print(obj.c1, obj.c12, sep = ",")

cols = []
column = Col()
for obj in tableList:
    column.add(obj.c1)

cols.append(column)
column = Col()
for obj in tableList:
    column.add(obj.c2)

cols.append(column)
column = Col()
for obj in tableList:
    column.add(obj.c3)

cols.append(column)
column = Col()
for obj in tableList:
    column.add(obj.c4)

cols.append(column)
column = Col()
for obj in tableList:
    column.add(obj.c5)

cols.append(column)
column = Col()
for obj in tableList:
    column.add(obj.c6)

cols.append(column)
column = Col()
for obj in tableList:
    column.add(obj.c7)

cols.append(column)
column = Col()
for obj in tableList:
    column.add(obj.c8)

cols.append(column)
column = Col()
for obj in tableList:
    column.add(obj.c9)

cols.append(column)
column = Col()
for obj in tableList:
    column.add(obj.c10)

cols.append(column)
column = Col()
for obj in tableList:
    column.add(obj.c11)

cols.append(column)
column = Col()
for obj in tableList:
    column.add(obj.c12)

cols.append(column)
classColumn = Col()
for obj in tableList:
    classColumn.add(obj.c13)

print(cols[0].colList[0])

#Columns are Col list that contains a col object which contains a colList
def subTreeBuilding(Columns, depth):
    #check number of elements in column and depth
    if len(Columns[0].colList) <= 1 or depth >= 4:
        print("Exit condition 1, size")
        return createLeafNode(Columns)

    attributeWithHighestGain = ""
    attributeValueWithHighestGain = ""
    maxGainRatio = 0.0
    splitAttribute = ""  

    #Calculate Conditional entropy for each attribute
    length = len(Columns)
    #for i in range(length):
        #calculate max gain ratio
    #return True
def createLeafNode(Columns):
    return True
