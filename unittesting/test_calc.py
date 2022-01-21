# import unittest
import unittest

# import module to test
import calc 

# create a test class, inheriting from unittest
class TestCalc(unittest.TestCase):
    # need start method with test for python to recognise this as a test
    # need to start the code with test
    def test_add(self):
        #use the assert methods from the unittest module to check
        # result = calc.add(10, 5) # do the calc
        # self.assertEquals(result, 15) # check if it is equal to 15

        # can pass result directly in
        self.assertEquals(calc.add(10, 5), 15)
        self.assertEquals(calc.add(10, -5), 5)
        self.assertEquals(calc.add(-1, -5), -6)

    def test_subtract(self):
        self.assertEquals(calc.subtract(10, 5), 5)
        self.assertEquals(calc.subtract(10, -5), 15)
        self.assertEquals(calc.subtract(-1, -5), 4)

    def test_divide(self):
        self.assertEquals(calc.divide(10, 5), 2)
        # self.assertRaises(ValueError, calc.divide, 10, 0) # Error we want to see, function, args into the funciton. Need to do this as if we run divide directly, python will think there's an error

        # alternatively, use a context manager to test
        with self.assertRaises(ValueError):
            calc.divide(10, 0)
      


# if we run this module directly, run this conditional
# easier than typing this into the terminal --> python -m unittest test_calc.py
if __name__ == '__main__':
    unittest.main()
