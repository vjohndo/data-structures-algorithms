import unittest
import requests
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):
    # TESTS DONT RUN IN ORDER
    # notice how our classes are repeated. 
    
    ##### Mocking #####
    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'


    ###### setUpClass and tearDownClass ######

    @classmethod # working with the class rather than the instance itself
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')


    def setUp(self):
        """Code to run before every single test"""
        # Notice the self
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)
        # will want to add self. infront of every call
        

    def tearDown(self):
        """Code to run after every single test"""
        pass

    def test_email(self):
        # create two employees... but there's a better way to do this
        # Can avoid this using setup
        # emp_1 = Employee('Corey', 'Schafer', 50000) --> can remove
        # emp_2 = Employee('Sue', 'Smith', 60000) --> can remove

        # Check emails are matching
        # Notice how all the tests have self. We're using the set up 
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        # emp_1 = Employee('Corey', 'Schafer', 50000) --> can remove
        # emp_2 = Employee('Sue', 'Smith', 60000) --> can remove

        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        # emp_1 = Employee('Corey', 'Schafer', 50000) --> can remove
        # emp_2 = Employee('Sue', 'Smith', 60000) --> can remove

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        # Mock the employee/requests.get 
        with patch('employee.requests.get') as mocked_get:
            # Instead of going to website by 
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"
            schedule = self.emp_1.monthly_schedule("May")

            # check correct url
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, "Success")

            ## Checking a bad repsonse
            mocked_get.return_value.ok = False
            mocked_get.return_value.text = "Success"
            schedule = self.emp_2.monthly_schedule("June")

            # check correct url
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, "Bad Response!")


if __name__ == '__main__':
    unittest.main()