import unittest
import main

class BalanceDiceTest(unittest.TestCase):

    def test(self):
        #self.assertTrue(0 < numSides <= 101)
        #main.main()
        self.assertTrue(0 < main.main.numSides <= 101)

if __name__ == '__main__':
    unittest.main()
    #unittest.testing()