import csv
import unittest
from selenium import webdriver

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_login_with_multiple_users(self):
        with open('test_data.csv', 'r') as file:
            data = csv.DictReader(file)
            for row in data:
                self.driver.get('https://example.com/login')  # Replace with your login URL
                username = row['username']
                password = row['password']

                # Locate username and password fields and perform login
                self.driver.find_element_by_id('username').send_keys(username)
                self.driver.find_element_by_id('password').send_keys(password)
                self.driver.find_element_by_id('loginBtn').click()

                # Perform assertions or further actions
                # Example:
                # self.assertIn("Welcome", self.driver.page_source)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

"""

This example uses a CSV file (test_data.csv) with 'username' and 'password' columns. 
The test case iterates through the CSV rows, logging in using different sets of credentials.

"""