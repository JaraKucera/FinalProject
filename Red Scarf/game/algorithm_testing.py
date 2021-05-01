import algorithm
import unittest


class TestEntropy(unittest.TestCase):

    def test_correctEntropy(self):
        assert algorithm.calculateEntropy(10,100,200) == 0.7160964047443681, "Should be 0.7160964047443681"

    def test_incorrectTotalEntropy(self):
        assert algorithm.calculateEntropy(10, 100, 0) == 0, "Should be 0"

    def test_incorrectFirstEntropy(self):
        assert algorithm.calculateEntropy(-100, 100, 200) == 0.5, "Should be 0.5"

    def test_incorrectSecondEntropy(self):
        assert algorithm.calculateEntropy(-100, 100, 200) == 0.5, "Should be 0.5"

    def test_incorrectFirstAndSecondEntropy(self):
        assert algorithm.calculateEntropy(-110, -1100, 100) == 0, "Should be 0"
    

class TestUtilities(unittest.TestCase):

    def test_detailClassList(self):
        listOfClasses = ["depressed", "notdepressed", "depressed", "notdepressed"]
        resultDict = {'depressed': 2, 'notDepressed':2}
        self.assertDictEqual(algorithm.detailClassList(listOfClasses), resultDict, "should be two depressed and two not depressed")

    def test_startAlgorithm(self):
        fakeAnswerDict12 = {0:"Reconsider", 1:"Myself",2:"Blameself",3:"Dismissal",4:"Trust",5:"Nice",6:"Hopeful",7:"Yes",8:"Pressure",9:"Understanding",10:"FocusonSam",11:"Doesntmissparents"}
        assert algorithm.startAlgorithm(fakeAnswerDict12) == "Depressed", "Should be Depressed"
        fakeAnswerDict5 = {0:"Reconsider", 1:"Myself",2:"Blameself",3:"Dismissal",4:"Trust"}
        assert algorithm.startAlgorithm(fakeAnswerDict5) == "Not Depressed", "Should be Not Depressed"

class TestGain(unittest.TestCase):

    def test_getGainRatioTriple(self):
        listOfClasses = ["depressed", "notdepressed", "depressed", "notdepressed"]
        columnList = ["Understanding", "Silence", "Reconsider", "Silence"]
        assert algorithm.getGainRatio(columnList, listOfClasses,10 ) == 6.57861319440438, "Should be 6.57861319440438"

    def test_getGainRatioDouble(self):
        listOfClasses = ["depressed", "notdepressed", "depressed", "notdepressed"]
        columnList = ["Understanding", "Silence", "Understanding", "Silence"]
        assert algorithm.getGainRatio(columnList, listOfClasses,10 ) == 10.0, "Should be 10.0"
        


if __name__ == '__main__':
    unittest.main()    