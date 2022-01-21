# import unittest
import unittest

# import module to test
import calc 

# create a test class, inheriting from unittest
class TestCalc(unittest.TestCase):
    # need start method with test for python to recognise this as a test

    def test_add(self):
        #use the assert methods from the unittest module to check
        result = calc.add(10, 5) # do the calc
        self.assertEquals(result, 15) # check if it is equal to 15

# if we run this module directly, run this conditional
if __name__ == '__main__':
    unittest.main()
