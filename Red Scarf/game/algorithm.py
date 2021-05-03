#### IMPORTS ###
import pymongo
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

class Node2:
    def __init__(self, choiceName, choiceAnswer, choiceNumber, child1, child2):
        self.isLeaf = False
        self.isTriple = False
        self.choiceName = choiceName
        self.choiceAnswer = choiceAnswer
        self.choiceColumnNumber = choiceNumber
        self.children = []
        if child1 != None:
            self.addChild(child1)
            self.addChild(child2)
        

    def addChild(self, node):
        self.children.append(node)
        if len(self.children) > 2:
            self.isTriple = True
    
    def display(self, indent = 0):
        print( ('.'*indent)+self.choiceName+" ["+str(self.choiceAnswer)+"]")        
        for val in self.children:
            val.display(indent+1)

class Node3:
    def __init__(self, choiceName, choiceAnswer, choiceNumber,child1, child2, child3):
        self.isLeaf = False
        self.isTriple = True
        self.choiceName = choiceName
        self.choiceAnswer = choiceAnswer
        self.choiceColumnNumber = choiceNumber
        self.children = []
        self.addChild(child1)
        self.addChild(child2)
        self.addChild(child3)

    def addChild(self, node):
        self.children.append(node)
        if len(self.children) > 2:
            self.isTriple = True
    
    def display(self, indent = 0):
        print( ('.'*indent)+self.choiceName+" ["+str(self.choiceAnswer)+"]")        
        for val in self.children:
            val.display(indent+1)

### FUNCTIONS ###
def startTreeBuilding(columnObjectList, classList, depth, names):
    return subTreeBuilding(deepcopy(columnObjectList), classList[:], deepcopy(depth), names, None, None)

def subTreeBuilding(columnObjectList, classList, depth, names, nodeName, NodeValue):
    numberColumns = len(columnObjectList)
    if numberColumns <= 4 or depth >= 4:
         #print("Exit condition 1, size with depth of: "+str(depth)+" and num cols: "+str(numberColumns))
         return createLeafNode(deepcopy(columnObjectList), classList[:], names)
         
    
    
    #Get total Entropy
    classDetails = detailClassList(deepcopy(classList))
    total = classDetails['depressed']+classDetails['notDepressed']
    if classDetails['depressed'] == 0 or classDetails['notDepressed'] == 0:
        #print("Exit condition 2: classList one sided")
        return createLeafNode(deepcopy(columnObjectList), classList[:], names)
    
    totalEntropy = calculateEntropy(classDetails['depressed'], classDetails['notDepressed'], total)
    
    if totalEntropy == 0:
        #print("totalEntropy = 0")
        return createLeafNode(deepcopy(columnObjectList), classList[:], names)
    #Get col with highest gain ratio
    columnNumberWithHighestGain = ""
    columnNameWithHighestGain = ""
    maxGainRatio = 0.0
    numberOfColumns = len(columnObjectList)
    for i in range(numberOfColumns):
        gainRatio = getGainRatio(columnObjectList[i].colList[:], classList[:], totalEntropy)
        #print("Column: "+ names[columnObjectList[i].colNumber]+" has a GainRatio of: "+str(gainRatio)+" i is :"+str(i)+" with depth:"+str(depth))
        if gainRatio >= maxGainRatio:
            maxGainRatio = gainRatio
            columnNumberWithHighestGain = i
            columnNameWithHighestGain = names[i]
    
    if maxGainRatio <= 0:
        #print("Exit condition 3, maxgainRatio 0, depth: "+str(depth))
        return createLeafNode(deepcopy(columnObjectList), classList[:], names)
    
    answers = getAllPossibleAnswers(columnObjectList[columnNumberWithHighestGain].colList[:])
    if len(answers) == 2:
        data1 = partition(deepcopy(columnObjectList), classList[:], answers[1], columnNumberWithHighestGain)
        leftClassList = data1['classList']
        leftColumnList = data1['cols'] 
        data2 = partition(deepcopy(columnObjectList), classList[:], answers[0], columnNumberWithHighestGain)
        rightColumnList = data2['cols']
        rightClassList = data2['classList']
        node = Node2(columnNameWithHighestGain, answers, columnNumberWithHighestGain,subTreeBuilding(deepcopy(leftColumnList), leftClassList[:], deepcopy(depth + 1), names, columnNameWithHighestGain, answers[0]), subTreeBuilding(deepcopy(rightColumnList), rightClassList[:], deepcopy(depth + 1), names, columnNameWithHighestGain, answers[1]))
        return node
    elif len(answers) == 3:
        data1 = partitionTriple(deepcopy(columnObjectList), classList[:], answers[1], answers[2], columnNumberWithHighestGain)
        leftClassList = data1['classList']
        leftColumnList = data1['cols']
        data2 = partitionTriple(deepcopy(columnObjectList), classList[:], answers[0], answers[2], columnNumberWithHighestGain)
        rightColumnList = data2['cols']
        rightClassList = data2['classList']
        data3 = partitionTriple(deepcopy(columnObjectList), classList[:], answers[0], answers[1], columnNumberWithHighestGain)
        middleClassList = data3['classList']
        middleColumnList = data3['cols']
        node = Node3(columnNameWithHighestGain, answers, columnNumberWithHighestGain,subTreeBuilding(deepcopy(leftColumnList), leftClassList[:], deepcopy(depth + 1), names, columnNameWithHighestGain, answers[0]), subTreeBuilding(deepcopy(middleColumnList), middleClassList[:], deepcopy(depth + 1), names, columnNameWithHighestGain, answers[1]), subTreeBuilding(deepcopy(rightColumnList), rightClassList[:], deepcopy(depth + 1), names, columnNameWithHighestGain, answers[2]))
        return node
    else:
        print("Exit conditon 4: number of answers not 2 or 3")
        return createLeafNode(deepcopy(columnObjectList), classList[:], names)
    
#returns modified cols without value        
def partition(columnObject, classList, stringToSplitOn, choiceColNumber):
    indicesList = []
    for j in range(len(columnObject[0].colList)):
        if columnObject[choiceColNumber].colList[j] == stringToSplitOn:
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

def partitionTriple(columnObject, classList, stringToSplitOn1, stringToSplitOn2, choiceColNumber):
    indicesList = []
    for j in range(len(columnObject[0].colList)):
        if columnObject[choiceColNumber].colList[j] == stringToSplitOn1 or columnObject[choiceColNumber].colList[j] == stringToSplitOn2:
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
        #print("Number of possible answers: "+str(len(allPossibleAnswers)))
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
        #print("case1AndDepressed: "+str(case1AndDepressed)+" case2AndDepressed: "+str(case2AndDepressed)+" case1AndNotDepressed: "+str(case1AndNotDepressed)+" case2AndNotDepressed: "+str(case2AndNotDepressed))

        entropyFirst = calculateEntropy(case1AndDepressed, case1AndNotDepressed, case1AndDepressed+case1AndNotDepressed)
        entropySecond = calculateEntropy(case2AndDepressed, case2AndNotDepressed, case2AndDepressed+case2AndNotDepressed)
        first = case1AndDepressed+case1AndNotDepressed
        second = case2AndDepressed+case2AndNotDepressed
        total = first+second
        if total <= 0:
            return 0
        gain = totalEntropy-(first/total)*entropyFirst-(second/total)*entropySecond
        splitV1 = first/total
        splitV2 = second/total
        if gain <= 0:
            return 0
        #print("splitV1:"+str(splitV1)+" splitV2:"+str(splitV2))
        if splitV1 <= 0 and splitV2 <= 0:
            return 0
        elif splitV1 > 0 and splitV2 <= 0:
            splitInfo = -(splitV1)*math.log(splitV1, 2)
            gainRatio = (gain)/splitInfo
            return gainRatio
        elif splitV1 <= 0 and splitV2 > 0:
            splitInfo = -(splitV2)*math.log(splitV2, 2)
            gainRatio = (gain)/splitInfo
            return gainRatio
        else:
            splitInfo = -(splitV1)*math.log(splitV1, 2) -(splitV2)*math.log(splitV2, 2)
            gainRatio = (gain)/splitInfo
            return gainRatio

    elif len(allPossibleAnswers) == 3:
        #print("Number of possible answers: "+str(len(allPossibleAnswers)))
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
        
        #print("case1AndDepressed: "+str(case1AndDepressed)+" case2AndDepressed: "+str(case2AndDepressed)+" case1AndNotDepressed: "+str(case1AndNotDepressed)+" case2AndNotDepressed: "+str(case2AndNotDepressed)+" case3AndDepressed: "+str(case3AndDepressed)+" case3AndNotDepressed: "+str(case3AndNotDepressed))
        entropyFirst = calculateEntropy(case1AndDepressed, case1AndNotDepressed, case1AndDepressed+case1AndNotDepressed)
        entropySecond = calculateEntropy(case2AndDepressed, case2AndNotDepressed, case2AndDepressed+case2AndNotDepressed)
        entropyThird = calculateEntropy(case3AndDepressed, case3AndNotDepressed, case3AndDepressed+case2AndNotDepressed)
        first = case1AndDepressed+case1AndNotDepressed
        second = case2AndDepressed+case2AndNotDepressed
        third = case3AndDepressed+case3AndNotDepressed
        total = first+second+third
        if total <= 0:
            return 0
        sp1 = first / total
        sp2 = second / total
        sp3 = third / total
        gain = totalEntropy - sp1*entropyFirst - sp2*entropySecond - sp3*entropyThird
        if gain <= 0:
            return 0
        #print("sp1: "+str(sp1)+" sp2: "+str(sp2)+" sp3:"+str(sp3))
        if sp1 <= 0 and sp2 <= 0 and sp3 <= 0:
            return 0
        elif sp1 <= 0 and sp2 > 0 and sp3 > 0:
            splitInfo = - sp2*math.log(sp2, 2) - sp3*math.log(sp3, 2)
            gainRatio = gain / splitInfo
            return gainRatio
        elif sp1 > 0 and sp2 <= 0 and sp3 > 0:
            splitInfo = -sp1*math.log(sp1, 2) -sp3*math.log(sp3, 2)
            gainRatio = gain / splitInfo
            return gainRatio
        elif sp1 > 0 and sp2 > 0 and sp3 <= 0:
            splitInfo = -sp1*math.log(sp1, 2) - sp2*math.log(sp2, 2)
            gainRatio = gain / splitInfo
            return gainRatio
        elif sp1 > 0 and sp2 <= 0 and sp3 <= 0:
            splitInfo = -sp1*math.log(sp1, 2)
            gainRatio = gain / splitInfo
            return gainRatio
        elif sp1 <= 0 and sp2 > 0 and sp3 <= 0:
            splitInfo = -sp2*math.log(sp2, 2)
            gainRatio = gain / splitInfo
            return gainRatio
        elif sp1 <= 0 and sp2 <= 0 and sp3 > 0:
            splitInfo = -sp3*math.log(sp3, 2)
            gainRatio = gain / splitInfo
            return gainRatio
        else:
            splitInfo = -sp1*math.log(sp1, 2) - sp2*math.log(sp2, 2) - sp3*math.log(sp3, 2)
            gainRatio = gain / splitInfo
            return gainRatio
        

    else:
        #print("Number of possible answers in Entropy(): "+str(len(allPossibleAnswers)))
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
    if total <= 0:
        return 0
    
    first = value1 / total
    second = value2 / total

    if first <= 0 and second > 0:
        #print("Second: "+str(second))
        entropy = -(second)*math.log(second, 2)
        return entropy
    elif second <= 0 and first > 0:
        entropy = -(first)*math.log(first, 2)
        return entropy
    elif first <= 0 and second <= 0:
        return 0
    
    entropy = -(first)*math.log(first, 2)-(second)*math.log(second, 2)
    
    return entropy

def createLeafNode(Columns, classList, names):
    whichCol = None
    name = ""
    #Get number of columns, if more than 1 then find the one with the highest gain and use that one for leaf tree,else if single column use that
    if len(Columns) > 1:
        classDetails = detailClassList(deepcopy(classList))
        total = classDetails['depressed']+classDetails['notDepressed']
        totalEntropy = calculateEntropy(classDetails['depressed'], classDetails['notDepressed'], total)
        mxg = 0
        for i in range(len(Columns)):
            gainRatio = getGainRatio(Columns[i].colList[:], classList[:], totalEntropy)
            if gainRatio > mxg:
                mxg = gainRatio
                whichCol = i
        #if no gainRatio use first column
        if whichCol == None:
            name = names[Columns[0].colNumber]
            whichCol = 0
    elif len(Columns) == 1:
        name = names[Columns[0].colNumber]
        whichCol = 0
    
    #Children
    numberChildren = getAllPossibleAnswers(Columns[whichCol].colList)
    if len(numberChildren) == 1:
        data = detailClassList(classList[:])
        name  = ""
        value = ""
        if data['depressed'] > data['notDepressed']:
            name = "depressed"
            value = "depressed"
        elif data['depressed'] <= data['notDepressed']:
            name = "notdepressed"
            value = "notdepressed"
        else:
            print("No name error")

        node = Node2(name, value, None, None, None)
        node.isLeaf = True
        #print("Created leaf Node")
        return node
    elif len(numberChildren) == 2:
        res = getRootAnswer(Columns[whichCol].colList, classList, numberChildren[0])
        leftChild = Node2(res, res, whichCol, None,None)
        leftChild.isLeaf = True

        res = getRootAnswer(Columns[whichCol].colList, classList, numberChildren[1])
        rightChild = Node2(res, res, whichCol, None,None)
        rightChild.isLeaf = True

        nodeSelf = Node2(name,numberChildren, whichCol, leftChild, rightChild)
        return nodeSelf
    
    elif len(numberChildren) == 3:
        res = getRootAnswer(Columns[whichCol].colList, classList, numberChildren[0])
        leftChild = Node2(res, res, whichCol, None,None)
        leftChild.isLeaf = True

        res = getRootAnswer(Columns[whichCol].colList, classList, numberChildren[1])
        middleChild = Node2(res, res, whichCol, None,None)
        middleChild.isLeaf = True

        res = getRootAnswer(Columns[whichCol].colList, classList, numberChildren[2])
        rightChild = Node2(res, res, whichCol, None,None)
        rightChild.isLeaf = True

        nodeSelf = Node3(name, numberChildren, whichCol,leftChild, middleChild, rightChild)
        return nodeSelf
    else:
        print("Error in numberchildren in create leaf with num child: "+str(len(numberChildren)))


#Converts a columnObject into a row list, used for confusionMatrix
def columnsToColList(ColumnObject, index):
    outputList = []
    for i in range(len(ColumnObject)):
        for j in range(len(ColumnObject[i].colList)):
            if j == index:
                outputList.append(ColumnObject[i].colList[j])
    
    return outputList

def confusionMatrix(ColumnObject, classList, root, names):
    depressedAndActuallyDepressed = 0 #True Positive
    depressedAndActuallyNotDepressed = 0 #False Positive
    notDepressedAndActuallyDepressed = 0 #False Negative
    notDepressedAndActuallyNotDepressed = 0 #True Negative

    for i in range(len(ColumnObject[0].colList)):
        rowTest = columnsToColList(ColumnObject, i)
        answer = testingOfData(rowTest, root, names)
        if answer == classList[i]:
            #True
            if answer == "depressed":
                depressedAndActuallyDepressed += 1
            else:
                notDepressedAndActuallyNotDepressed += 1
        else:
            #False
            if answer == "depressed":
                depressedAndActuallyNotDepressed += 1
            else:
                notDepressedAndActuallyDepressed += 1
    
    a = depressedAndActuallyDepressed + notDepressedAndActuallyNotDepressed
    b = depressedAndActuallyNotDepressed + notDepressedAndActuallyDepressed + a
    res = (a / b)*100
    print("            Depressed  Not Depressed")
    print("Depressed     "+str(depressedAndActuallyDepressed)+"         "+str(depressedAndActuallyNotDepressed))
    print("Not Depressed "+str(depressedAndActuallyNotDepressed)+"         "+str(notDepressedAndActuallyNotDepressed) )
    print("Accuracy: "+str(res)+"%")
#colList is a list of columns in a row
def testingOfData(colList, root,names):
    node = root
    while not node.isLeaf:
        if len(node.children) == 3:
            if colList[node.choiceColumnNumber] == node.choiceAnswer[0]:
                node = node.children[0]
            elif colList[node.choiceColumnNumber] == node.choiceAnswer[1]:
                node = node.children[1]
            elif colList[node.choiceColumnNumber] == node.choiceAnswer[2]:
                node = node.children[2]
            else:
                print("3 Answer: "+colList[node.choiceColumnNumber]+" does not match any answer: "+str(node.choiceAnswer))
                break
        elif len(node.children) == 2:
            if colList[node.choiceColumnNumber] == node.choiceAnswer[0]:
                node = node.children[0]
                
            elif colList[node.choiceColumnNumber] == node.choiceAnswer[1]:
                node = node.children[1]
            else:
                print("2 Answer: "+colList[node.choiceColumnNumber]+" does not match any answer: "+str(node.choiceAnswer))
                break
        else:
            print("Broken")
    return node.choiceAnswer
                
def getRootAnswer(columnList, classList, childToUse):
    indexList = []
    for i in range(len(columnList)):
        if columnList[i] == childToUse:
            if i not in indexList:
                indexList.append(i)
    
    d =0
    nd = 0
    for j in range(len(classList)):
        if j in indexList:
            if classList[j] == "depressed":
                d += 1
            else:
                nd += 1
    
    if d >= nd:
        return "depressed"
    else:
        return "notdepressed"


def getDepressionAnswer(answerDict, root,names):
    node = root
    while not node.isLeaf:
        if len(node.children) == 3:
            if answerDict[node.choiceColumnNumber] == node.choiceAnswer[0]:
                node = node.children[0]
            elif answerDict[node.choiceColumnNumber] == node.choiceAnswer[1]:
                node = node.children[1]
            elif answerDict[node.choiceColumnNumber] == node.choiceAnswer[2]:
                node = node.children[2]
            else:
                print("3 Answer: "+answerDict[node.choiceColumnNumber]+" does not match any answer: "+str(node.choiceAnswer))
                break
        elif len(node.children) == 2:
            if answerDict[node.choiceColumnNumber] == node.choiceAnswer[0]:
                node = node.children[0]
                
            elif answerDict[node.choiceColumnNumber] == node.choiceAnswer[1]:
                node = node.children[1]
            else:
                print("2 Answer: "+answerDict[node.choiceColumnNumber]+" does not match any answer: "+str(node.choiceAnswer))
                break
        else:
            print("Broken")
    return node.choiceAnswer

def startAlgorithm(resultChoices):
    ### DATA PREP ###
    client = MongoClient('mongodb://mongodb4075kj:xy5myq@danu7.it.nuigalway.ie:8717/mongodb4075')
    db = client.mongodb4075
    data = db.game
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

    numberChoices = len(resultChoices)
    names = ["Choice 1","Choice 2","Choice 3","Choice 4","Choice 5","Choice 6","Choice 7","Choice 8","Choice 9","Choice 10","Choice 11","Choice 12"]
    node = startTreeBuilding(deepcopy(cols[0:numberChoices]), classColumn.colList[0:numberChoices], 0, names)
    res = getDepressionAnswer(resultChoices,node,names)
    #confusionMatrix(deepcopy(cols), classColumn.colList[:], node, names)
    if res == "notdepressed":
        return "Not Depressed"
    elif res == "depressed":
        return "Depressed"
    #node.display()
    
