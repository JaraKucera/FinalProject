############### IMPORTS ###############
import pymongo
from pymongo import MongoClient

############### CLASSES ###############

class Rows:
    def __init__(self):
        self.c1 = 0
        self.c2 = 0
        self.c3 = 0
        self.c4 = 0
        self.c5 = 0
        self.c6 = 0
        self.c7 = 0
        self.c8 = 0
        self.c9 = 0
        self.c10 = 0
        self.c11 = 0
        self.c12 = 0
    

############### Main ###############
def setUpClass():
    client = MongoClient('mongodb://mongodb4075kj:xy5myq@danu7.it.nuigalway.ie:8717/mongodb4075')
    db = client.mongodb4075
    data = db.gameResults
    x = data.find()
    results = Rows()
    for result in x:
        if result['Choice 1'] != "null":
            results.c1 =  results + 1
    
        if result['Choice 2'] != "null":
            results.c2 =  results + 1

        if result['Choice 3'] != "null":
            results.c3 =  results + 1

        if result['Choice 4'] != "null":
            results.c4 =  results + 1

        if result['Choice 5'] != "null":
            results.c5 =  results + 1

        if result['Choice 6'] != "null":
            results.c6 =  results + 1

        if result['Choice 7'] != "null":
            results.c7 =  results + 1

        if result['Choice 8'] != "null":
            results.c8 =  results + 1

        if result['Choice 9'] != "null":
            results.c9 =  results + 1

        if result['Choice 10'] != "null":
            results.c10 =  results + 1

        if result['Choice 11'] != "null":
            results.c11 =  results + 1
        
    return results

def getPercentageResults():
    allResults = setUpClass()
    client = MongoClient('mongodb://mongodb4075kj:xy5myq@danu7.it.nuigalway.ie:8717/mongodb4075')
    db = client.mongodb4075
    totalRecords =  db.gameResults.count()
    resultDictionary = {1: allResults.c1 / totalRecords,2: allResults.c2 / totalRecords,3: allResults.c3 / totalRecords,4: allResults.c4 / totalRecords,5: allResults.c5 / totalRecords,6: allResults.c6 / totalRecords,7: allResults.c7 / totalRecords,8: allResults.c8 / totalRecords,9: allResults.c9 / totalRecords,10: allResults.c10 / totalRecords,11: allResults.c11 / totalRecords,12: allResults.c12 / totalRecords}
    return resultDictionary

def getCountResults():
    allResults = setUpClass()
    resultDict = {1: allResults.c1, 2: allResults.c2,3: allResults.c3,4: allResults.c4,5: allResults.c5,6: allResults.c6,7: allResults.c7,8: allResults.c8,9: allResults.c9,10: allResults.c10,11: allResults.c11,12: allResults.c12,}
    return resultDict