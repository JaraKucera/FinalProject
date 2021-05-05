############### IMPORTS ###############
import pymongo
from pymongo import MongoClient
import copy

############### CLASSES ###############

class Rows:
    def __init__(self):
        self.c1 = 0
        self.c1Reconsider = 0
        self.c1Silence = 0
        self.c1Understanding = 0
        self.c2 = 0
        self.c2Myself = 0
        self.c2Family = 0
        self.c2Noonesfault = 0
        self.c3 = 0
        self.c3Blameself = 0
        self.c3BlameBully = 0
        self.c3Distrust = 0
        self.c4 = 0
        self.c4Dismissal = 0
        self.c4Appreciation = 0
        self.c4Relatetolosingpassion = 0
        self.c5 = 0
        self.c5Trust = 0
        self.c5Distrust = 0
        self.c6 = 0
        self.c6Nice = 0
        self.c6Dismiss = 0
        self.c7 = 0
        self.c7Hopeful = 0
        self.c7Anger = 0
        self.c7Optimistic = 0
        self.c8 = 0
        self.c8Yes = 0
        self.c8Somewhat = 0
        self.c8No = 0
        self.c9 = 0
        self.c9Pressure = 0
        self.c9Careful = 0
        self.c9Pushing = 0
        self.c10 = 0
        self.c10Understanding = 0
        self.c10Apologetic = 0
        self.c10Getoverit = 0
        self.c11 = 0
        self.c11FocusgettingHome = 0
        self.c11FocusonSam = 0
        self.c12 = 0
        self.c12MissParents = 0
        self.c12Doesntmissparents = 0
        
    

############### Main ###############
def setUpClass():
    client = MongoClient('mongodb://mongodb4075kj:xy5myq@danu7.it.nuigalway.ie:8717/mongodb4075')
    db = client.mongodb4075
    data = db.gameResults
    x = data.find()
    results = Rows()
    for result in x:
        if result['Choice 1'] != "null":
            results.c1 =  results.c1 + 1
    
        if result['Choice 1'] == "Reconsider":
            results.c1Reconsider =  results.c1Reconsider + 1
        
        if result['Choice 1'] == "Silence":
            results.c1Silence =  results.c1Silence + 1

        if result['Choice 1'] == "Understanding":
            results.c1Understanding =  results.c1Understanding + 1

        if result['Choice 2'] != "null":
            results.c2 =  results.c2 + 1
        
        if result['Choice 2'] == "Myself":
            results.c2Myself =  results.c2Myself + 1
        
        if result['Choice 2'] == "Family":
            results.c2Family =  results.c2Family + 1
        
        if result['Choice 2'] == "Noonesfault":
            results.c2Noonesfault =  results.c2Noonesfault + 1

        if result['Choice 3'] != "null":
            results.c3 =  results.c3 + 1

        if result['Choice 3'] == "Blameself":
            results.c3Blameself =  results.c3Blameself + 1
        
        if result['Choice 3'] == "BlameBully":
            results.c3BlameBully =  results.c3BlameBully + 1
        
        if result['Choice 3'] == "Distrust":
            results.c3Distrust =  results.c3Distrust + 1
        
        if result['Choice 4'] != "null":
            results.c4 =  results.c4 + 1
        
        if result['Choice 4'] == "Dismissal":
            results.c4Dismissal =  results.c4Dismissal + 1
        
        if result['Choice 4'] == "Appreciation":
            results.c4Appreciation =  results.c4Appreciation + 1
        
        if result['Choice 4'] == "Relatetolosingpassion":
            results.c4Relatetolosingpassion =  results.c4Relatetolosingpassion + 1

        if result['Choice 5'] != "null":
            results.c5 =  results.c5 + 1
        
        if result['Choice 5'] == "Trust":
            results.c5Trust =  results.c5Trust + 1
        
        if result['Choice 5'] == "Distrust":
            results.c5Distrust =  results.c5Distrust + 1

        if result['Choice 6'] != "null":
            results.c6 =  results.c6 + 1
        
        if result['Choice 6'] == "Nice":
            results.c6Nice =  results.c6Nice + 1
        
        if result['Choice 6'] == "Dismiss":
            results.c6Dismiss =  results.c6Dismiss + 1

        if result['Choice 7'] != "null":
            results.c7 =  results.c7 + 1

        if result['Choice 7'] == "Hopeful":
            results.c7Hopeful =  results.c7Hopeful + 1
        
        if result['Choice 7'] == "Anger":
            results.c7Anger =  results.c7Anger + 1
        
        if result['Choice 7'] == "Optimistic":
            results.c7Optimistic =  results.c7Optimistic + 1
        
        if result['Choice 8'] != "null":
            results.c8 =  results.c8 + 1

        if result['Choice 8'] == "Yes":
            results.c8Yes =  results.c8Yes + 1

        if result['Choice 8'] == "Somewhat":
            results.c8Somewhat =  results.c8Somewhat + 1

        if result['Choice 8'] == "No":
            results.c8No =  results.c8No + 1

        if result['Choice 9'] != "null":
            results.c9 =  results.c9 + 1
        
        if result['Choice 9'] == "Pressure":
            results.c9Pressure =  results.c9Pressure + 1

        if result['Choice 9'] == "Careful":
            results.c9Careful =  results.c9Careful + 1

        if result['Choice 9'] == "Pushing":
            results.c9Pushing =  results.c9Pushing + 1

        if result['Choice 10'] != "null":
            results.c10 =  results.c10 + 1

        if result['Choice 10'] == "Understanding":
            results.c10Understanding =  results.c10Understanding + 1

        if result['Choice 10'] == "Apologetic":
            results.c10Apologetic =  results.c10Apologetic + 1

        if result['Choice 10'] == "Getoverit":
            results.c10Getoverit =  results.c10Getoverit + 1

        if result['Choice 11'] != "null":
            results.c11 =  results.c11 + 1
        
        if result['Choice 11'] == "FocusgettingHome":
            results.c11FocusgettingHome =  results.c11FocusgettingHome + 1
        
        if result['Choice 11'] == "FocusonSam":
            results.c11FocusonSam =  results.c11FocusonSam + 1

        if result['Choice 12'] != "null":
            results.c12 =  results.c12 + 1

        if result['Choice 12'] == "MissParents":
            results.c12MissParents =  results.c12MissParents + 1
        
        if result['Choice 12'] == "Doesntmissparents":
            results.c12Doesntmissparents =  results.c12Doesntmissparents + 1
        
    return results

def convertToFloat(row):
    row.c1 = float(row.c1)
    row.c1Reconsider = float(row.c1Reconsider)
    row.c1Silence = float(row.c1Silence)
    row.c1Understanding = float(row.c1Understanding)
    row.c2 = float(row.c2)
    row.c2Myself = float(row.c2Myself)
    row.c2Family = float(row.c2Family)
    row.c2Noonesfault = float(row.c2Noonesfault)
    row.c3 = float(row.c3)
    row.c3Blameself = float(row.c3Blameself)
    row.c3BlameBully = float(row.c3BlameBully)
    row.c3Distrust = float(row.c3Distrust)
    row.c4 = float(row.c4)
    row.c4Dismissal = float(row.c4Dismissal)
    row.c4Appreciation = float(row.c4Appreciation)
    row.c4Relatetolosingpassion = float(row.c4Relatetolosingpassion)
    row.c5 = float(row.c5)
    row.c5Trust = float(row.c5Trust)
    row.c5Distrust = float(row.c5Distrust)
    row.c6 = float(row.c6)
    row.c6Nice = float(row.c6Nice)
    row.c6Dismiss = float(row.c6Dismiss)
    row.c7 = float(row.c7)
    row.c7Hopeful = float(row.c7Hopeful)
    row.c7Anger = float(row.c7Anger)
    row.c7Optimistic = float(row.c7Optimistic)
    row.c8 = float(row.c8)
    row.c8Yes = float(row.c8Yes)
    row.c8Somewhat = float(row.c8Somewhat)
    row.c8No = float(row.c8No)
    row.c9 = float(row.c9)
    row.c9Pressure = float(row.c9Pressure)
    row.c9Careful = float(row.c9Careful)
    row.c9Pushing = float(row.c9Pushing)
    row.c10 = float(row.c10)
    row.c10Understanding = float(row.c10Understanding)
    row.c10Apologetic = float(row.c10Apologetic)
    row.c10Getoverit = float(row.c10Getoverit)
    row.c11 = float(row.c11)
    row.c11FocusgettingHome = float(row.c11FocusgettingHome)
    row.c11FocusonSam = float(row.c11FocusonSam)
    row.c12 = float(row.c12)
    row.c12MissParents = float(row.c12MissParents)
    row.c12Doesntmissparents = float(row.c12Doesntmissparents)

    return row

def getPercentageResults():
    allResults = setUpClass()
    allResults = convertToFloat(allResults)
    client = MongoClient('mongodb://mongodb4075kj:xy5myq@danu7.it.nuigalway.ie:8717/mongodb4075')
    db = client.mongodb4075
    resultDict = {'1a': str(round((allResults.c1Reconsider/allResults.c1)*100,2)), '1b':str(round((allResults.c1Silence/allResults.c1)*100,2)),'1c':str(round((allResults.c1Understanding/allResults.c1)*100,2)),'2a':str(round((allResults.c2Myself/allResults.c2)*100,2)),'2b':str(round((allResults.c2Family/allResults.c2)*100,2)),'2c':str(round((allResults.c2Noonesfault/allResults.c2)*100,2)),'3a':str(round((allResults.c3Blameself/allResults.c3)*100,2)),'3b':str(round((allResults.c3BlameBully/allResults.c3)*100,2)),'3c':str(round((allResults.c3Distrust/allResults.c3)*100,2)) , '4a':str(round((allResults.c4Dismissal/allResults.c4)*100,2)), '4b':str(round((allResults.c4Appreciation/allResults.c4)*100,2)), '4c':str(round((allResults.c4Relatetolosingpassion/allResults.c4)*100,2)), '5a':str(round((allResults.c5Trust/allResults.c5)*100,2)), '5b':str(round((allResults.c5Distrust/allResults.c5)*100,2)), '6a': str(round((allResults.c6Nice/allResults.c6)*100,2)), '6b':str(round((allResults.c6Dismiss/allResults.c6)*100,2)), '7a':str(round((allResults.c7Hopeful/allResults.c7)*100,2)), '7b':str(round((allResults.c7Anger/allResults.c7)*100,2)), '7c':str(round((allResults.c7Optimistic/allResults.c7)*100,2)), '8a':str(round((allResults.c8Yes/allResults.c8)*100,2)), '8b':str(round((allResults.c8Somewhat/allResults.c8)*100,2)), '8c':str(round((allResults.c8No/allResults.c8)*100,2)), '9a':str(round((allResults.c9Pressure/allResults.c9)*100,2)), '9b':str(round((allResults.c9Careful/allResults.c9)*100,2)), '9c':str(round((allResults.c9Pushing/allResults.c9)*100,2)), '10a':str(round((allResults.c10Understanding/allResults.c10)*100,2)), '10b':str(round((allResults.c10Apologetic/allResults.c10)*100,2)), '10c':str(round((allResults.c10Getoverit/allResults.c10)*100,2)), '11a':str(round((allResults.c11FocusgettingHome/allResults.c11)*100,2)), '11b':str(round((allResults.c11FocusonSam/allResults.c11)*100,2)), '12a':str(round((allResults.c12MissParents/allResults.c12)*100,2)), '12b':str(round((allResults.c12Doesntmissparents/allResults.c12)*100,2))}
    return resultDict

def getCountResults():
    allResults = setUpClass()
    resultDict = {'1a': allResults.c1Reconsider, '1b':allResults.c1Silence,'1c':allResults.c1Understanding,'2a': allResults.c2Myself,'2b':allResults.c2Family,'2c':allResults.c2Noonesfault,'3a':allResults.c3Blameself,'3b':allResults.c3BlameBully,'3c': allResults.c3Distrust, '4a':allResults.c4Dismissal, '4b':allResults.c4Appreciation, '4c':allResults.c4Relatetolosingpassion, '5a':allResults.c5Trust, '5b':allResults.c5Distrust, '6a': allResults.c6Nice, '6b':allResults.c6Dismiss, '7a':allResults.c7Hopeful, '7b':allResults.c7Anger, '7c':allResults.c7Optimistic, '8a':allResults.c8Yes, '8b':allResults.c8Somewhat, '8c':allResults.c8No, '9a':allResults.c9Pressure, '9b':allResults.c9Careful, '9c':allResults.c9Pushing, '10a':allResults.c10Understanding, '10b':allResults.c10Apologetic, '10c':allResults.c10Getoverit, '11a':allResults.c11FocusgettingHome, '11b':allResults.c11FocusonSam, '12a':allResults.c12MissParents, '12b':allResults.c12Doesntmissparents}
    return resultDict

print(getPercentageResults())