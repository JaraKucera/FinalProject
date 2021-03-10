#### IMPORTS ###
import pymongo
import numpy as np
import math
from pymongo import MongoClient
from copy import deepcopy

### CLASSES ###
class Row:
    def __init__(self,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13):
        self.c1 = c1.replace(" ","") #Choices 1-12
        self.c2 = c2.replace(" ","")
        self.c3 = c3.replace(" ","")
        self.c4 = c4.replace(" ","")
        self.c5 = c5.replace(" ","")
        self.c6 = c6.replace(" ","")
        self.c7 = c7.replace(" ","")
        self.c8 = c8.replace(" ","")
        self.c9 = c9.replace(" ","")
        self.c10 = c10.replace(" ","")
        self.c11 = c11.replace(" ","")
        self.c12 = c12.replace(" ","")
        self.c13 = c13.replace(" ","") #Depression level
    
class Col:
    def __init__(self):
        self.colList = []
        self.colNumber = None

    def add(self, element):
        self.colList.append(element)

    def setColNumber(self, number):
        self.colNumber = number    

class Node:
    def __init__(self):
        self.children = []
        self.leftChild = None
        self.rightChild = None
        self.middleChild = None
        self.isLeaf = True
        self.isTriple = None
        self.name = None
        self.value = None

    def setLeftChild(self, child):
        self.leftChild = child
        self.isLeaf = False
        self.children.append(self.leftChild)
    
    def setRightChild(self, child):
        self.rightChild = child
        self.isLeaf = False
        self.children.append(self.rightChild)
    
    def setMiddleChild(self, child):
        self.middleChild = child
        self.isLeaf = False
        self.children.append(self.middleChild)
        self.isTriple = True

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild
    
    def getMiddleChild(self):
        return self.middleChild
    
    def display(self, indent = 0):
        print( (' '*indent)+self.name)        
        for val in self.children:
            val.display(indent+1)

### FUNCTIONS ###

#Columns are Col list that contains a col object which contains a colList, classList is a list of results, depth is an int, names is a list of column names
def subTreeBuilding(columnObjectList, classList, depth, names):
    #check number of elements in column and depth
    if len(columnObjectList[0].colList) <= 5 or depth >= 6:
        print("Exit condition 1, size with depth of: "+str(depth))
        return createLeafNode(deepcopy(columnObjectList), classList[:], names)

    columnNumberWithHighestGain = ""
    columnNameWithHighestGain = ""
    maxGainRatio = 0.0
    #Get total entropy
    classDetails = detailClassList(deepcopy(classList))
    x = classDetails['depressed']+classDetails['notDepressed']
    totalEntropy = calculateEntropy(classDetails['depressed'], classDetails['notDepressed'], x)

    #Get column with highest gain Ratio
    numberOfColumns = len(columnObjectList)
    for i in range(numberOfColumns):
        gainRatio = getGainRatio(columnObjectList[i].colList[:], classList[:], totalEntropy)
        if gainRatio >= maxGainRatio:
            maxGainRatio = gainRatio
            columnNumberWithHighestGain = i
            columnNameWithHighestGain = names[i]
    
    #Separate data into two node streams
    
    node = Node()
    if depth == 0:
        node.value = "root"
    
    node.isLeaf = False
    node.name = columnNameWithHighestGain
    answers = getAllPossibleAnswers(columnObjectList[columnNumberWithHighestGain].colList[:])
    if len(answers) == 2:
        print("######### Number of answers is 2 #############")
        data = partition(deepcopy(columnObjectList), classList[:], answers[0])
        leftClassList = data['classList']
        leftColumnList = data['cols']
        leftChild = Node()
        #leftChild.name = 
        node.setLeftChild(subTreeBuilding(leftColumnList, leftClassList, depth + 1, names))
        data = partition(deepcopy(columnObjectList), classList[:], answers[1])
        rightColumnList = data['cols']
        rightClassList = data['classList']
        node.setRightChild(subTreeBuilding(rightColumnList, rightClassList, depth + 1, names))
    elif len(answers) == 3:
        print("########## Number of answers is 3 ###########")
        data = partition(deepcopy(columnObjectList), classList[:], answers[0])
        leftClassList = data['classList']
        leftColumnList = data['cols']
        node.setLeftChild(subTreeBuilding(leftColumnList, leftClassList, depth + 1, names))
        data = partition(deepcopy(columnObjectList), classList[:], answers[1])
        rightColumnList = data['cols']
        rightClassList = data['classList']
        node.setRightChild(subTreeBuilding(rightColumnList, rightClassList, depth + 1, names))
        data = partition(deepcopy(columnObjectList), classList[:], answers[2])
        middleClassList = data['classList']
        middleColumnList = data['cols']
        node.setMiddleChild(subTreeBuilding(middleColumnList, middleClassList, depth + 1, names))
    else:
        print("Answers != 2 or 3")
        return createLeafNode(deepcopy(columnObjectList), classList[:], names)
    
    return node


#returns modified cols without value        
def partition(columnObject, classList, stringToSplitOn):
    indicesList = []
    for i in range(len(columnObject)):
        for j in range(len(columnObject[0].colList)):
            if columnObject[i].colList[j] == stringToSplitOn:
                if j not in indicesList:
                    indicesList.append(j)
    
    for i in reversed(range(len(columnObject))):
        for j in reversed(range(len(columnObject[0].colList))):
            if j in indicesList:
                del columnObject[i].colList[j]
    
    for i in reversed(range(len(classList))):
        if i in indicesList:
            del classList[i]
    
    return {'cols': columnObject, 'classList': classList}
                       


def getGainRatio(oneColumn, classList, totalEntropy):
    allPossibleAnswers = getAllPossibleAnswers(oneColumn[:])
    if len(allPossibleAnswers) == 2:
            case1AndDepressed = 0
            case2AndDepressed = 0
            case1AndNotDepressed = 0
            case2AndNotDepressed = 0
            for j in range(len(classList)):
                if oneColumn[j] == allPossibleAnswers[0] and classList[j] == "depressed":
                    case1AndDepressed += 1
                elif oneColumn[j] == allPossibleAnswers[0] and classList[j] == "notdepressed":
                    case1AndNotDepressed += 1
                elif oneColumn[j] == allPossibleAnswers[1] and classList[j] == "depressed":
                    case2AndDepressed += 1
                elif oneColumn[j] == allPossibleAnswers[1] and classList[j] == "notdepressed":
                    case2AndNotDepressed += 1
            
            entropyFirst = calculateEntropy(case1AndDepressed, case1AndNotDepressed, case1AndDepressed+case1AndNotDepressed)
            entropySecond = calculateEntropy(case2AndDepressed, case2AndNotDepressed, case2AndDepressed+case2AndNotDepressed)
            first = case1AndDepressed+case1AndNotDepressed
            second = case2AndDepressed+case2AndNotDepressed
            total = first+second
            gain = totalEntropy-(first/total)*entropyFirst-(second/total)*entropySecond
            splitV1 = first/total
            splitV2 = second/total
            splitInfo = -(splitV1)*math.log2(splitV1) -(splitV2)*math.log2(splitV2)
            gainRatio = (gain)/splitInfo
            return gainRatio

    elif len(allPossibleAnswers) == 3:
        case1AndDepressed = 0
        case2AndDepressed = 0
        case3AndDepressed = 0
        case1AndNotDepressed = 0
        case2AndNotDepressed = 0
        case3AndNotDepressed = 0
        for j in range(len(classList)):
                if oneColumn[j] == allPossibleAnswers[0] and classList[j] == "depressed":
                    case1AndDepressed += 1
                elif oneColumn[j] == allPossibleAnswers[0] and classList[j] == "notdepressed":
                    case1AndNotDepressed += 1
                elif oneColumn[j] == allPossibleAnswers[1] and classList[j] == "depressed":
                    case2AndDepressed += 1
                elif oneColumn[j] == allPossibleAnswers[1] and classList[j] == "notdepressed":
                    case2AndNotDepressed += 1
                elif oneColumn[j] == allPossibleAnswers[2] and classList[j] == "notdepressed":
                    case3AndNotDepressed += 1
                elif oneColumn[j] == allPossibleAnswers[2] and classList[j] == "depressed":
                    case3AndDepressed += 1
        
        entropyFirst = calculateEntropy(case1AndDepressed, case1AndNotDepressed, case1AndDepressed+case1AndNotDepressed)
        entropySecond = calculateEntropy(case2AndDepressed, case2AndNotDepressed, case2AndDepressed+case2AndNotDepressed)
        entropyThird = calculateEntropy(case3AndDepressed, case3AndNotDepressed, case3AndDepressed+case2AndNotDepressed)
        first = case1AndDepressed+case1AndNotDepressed
        second = case2AndDepressed+case2AndNotDepressed
        third = case3AndDepressed+case3AndNotDepressed
        total = first+second+third
        sp1 = first / total
        sp2 = second / total
        sp3 = third / total
        gain = totalEntropy - (sp1)*entropyFirst - sp2*entropySecond - sp3*entropyThird
        splitInfo = -(sp1)*math.log2(sp1) - sp2*math.log2(sp2) - sp3*math.log2(sp3)
        gainRatio = gain / splitInfo
        return gainRatio

    else:
        #print("Number of possible answers: "+str(len(allPossibleAnswers)))
        return 0

    return 0
    
#Returns a list of all possible answers in column
def getAllPossibleAnswers(columnList):
    listofAnswers = []
    for i in range(len(columnList)):
        if columnList[i] not in listofAnswers:
            listofAnswers.append(columnList[i])
    #for val in listofAnswers:
        #print(val)
    
    return listofAnswers

#Returns total number depressed && notdepressed
def detailClassList(classList):
    depressed = 0
    notDepressed = 0
    for val in classList:
        if val == "depressed":
            depressed+=1
        elif val == "notdepressed":
            notDepressed+=1
        else:
            print("Error in detailClassList() val == :"+str(val))
    
    return {'depressed':depressed, 'notDepressed':notDepressed}
    
#Entropy = -value1/total*log2(value1/total)-value2/total*log2(value2/total)
def calculateEntropy(value1, value2, total):
    if total == 0 or value1 == 0 or value2 == 0:
        print("entropy equal to 0 Total: "+str(total) + " Value 1:"+str(value1)+" Value 2: "+str(value2))
        return 0
    
    first = value1 / total
    second = value2 / total
    if first <= 0 or second <= 0:
        print("First or second below or equal to 0\nFirst: "+str(first)+" Second: "+str(second))
        return 0
    entropy = -(first)*math.log2(first)-(second)*math.log2(second)
    return entropy

def createLeafNode(Columns, classList, names):
    data = detailClassList(classList[:])
    node = Node()
    node.isLeaf = True
    if data['depressed'] >= data['notDepressed']:
        node.name = "depressed"
        node.value = "depressed"
    elif data['depressed'] < data['notDepressed']:
        node.name = "notdepressed"
        node.value = "notdepressed"
    else:
        print("No name error")

    return node


def testingOfData(ColumnObject, root):
    while(root.name != None):
        attribute = root.name

def columnsToColList(ColumnObject, index):
    outputList = []
    for i in range(len(ColumnObject)):
        for j in range(len(ColumnObject[i].colList)):
            if j == index:
                outputList.append(ColumnObject[i].colList[j])

### DATA PREP ###
client = MongoClient('*')
db = client.mongodb4075
data = db.gameData
x = data.find()
tableList = []
for dRow in x:
    row = Row(dRow['Choice 1'].strip(), dRow['Choice 2'].strip(), dRow['Choice 3'].strip(), dRow['Choice 4'].strip(), dRow['Choice 5'].strip(), dRow['Choice 6'].strip(), dRow['Choice 7'].strip(), dRow['Choice 8'].strip(), dRow['Choice 9'].strip(), dRow['Choice 10'].strip(), dRow['Choice 11'].strip(), dRow['Choice 12'].strip(), dRow['Result'].strip())
    tableList.append(row)

cols = []
column = Col()
for obj in tableList:
    column.add(obj.c1)

column.setColNumber(0)
cols.append(column)
column = Col()
for obj in tableList:
    column.add(obj.c2)

column.setColNumber(1)
cols.append(column)
column = Col()
for obj in tableList:
    column.add(obj.c3)

column.setColNumber(2)
cols.append(column)
column = Col()
for obj in tableList:
    column.add(obj.c4)

column.setColNumber(3)
cols.append(column)
column = Col()
for obj in tableList:
    column.add(obj.c5)

column.setColNumber(4)
cols.append(column)
column = Col()
for obj in tableList:
    column.add(obj.c6)

column.setColNumber(5)
cols.append(column)
column = Col()
for obj in tableList:
    column.add(obj.c7)

column.setColNumber(6)
cols.append(column)
column = Col()
for obj in tableList:
    column.add(obj.c8)

column.setColNumber(7)
cols.append(column)
column = Col()
for obj in tableList:
    column.add(obj.c9)

column.setColNumber(8)
cols.append(column)
column = Col()
for obj in tableList:
    column.add(obj.c10)

column.setColNumber(9)
cols.append(column)
column = Col()
for obj in tableList:
    column.add(obj.c11)

column.setColNumber(10)
cols.append(column)
column = Col()
for obj in tableList:
    column.add(obj.c12)

column.setColNumber(11)
cols.append(column)
classColumn = Col()
for obj in tableList:
    classColumn.add(obj.c13)

classColumn.setColNumber(12)
print(cols[0].colList[0])

### TRAINING ###
#classColumn object with list of results [depressed] [notdepressed]
#cols list with  column objects, each column object has a list of that particular column number
names = ["Choice 1","Choice 2","Choice 3","Choice 4","Choice 5","Choice 6","Choice 7","Choice 8","Choice 9","Choice 10","Choice 11","Choice 12"]
node = subTreeBuilding(deepcopy(cols), classColumn.colList[:], 0, names)
print("###################")
node.display()

