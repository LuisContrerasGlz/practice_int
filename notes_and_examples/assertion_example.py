import unittest
from selenium import webdriver # pip install selenium

class GoogleTitleTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # You'll need to set the appropriate webdriver (e.g., Chrome, Firefox)

    def test_google_page_title(self):
        self.driver.get('https://www.google.com')
        expected_title = "Google"
        actual_title = self.driver.title
        # Assert whether the expected title matches the actual title
        self.assertEqual(expected_title, actual_title, f"Expected title '{expected_title}' but got '{actual_title}'")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


"""

This test case navigates to Google's homepage and checks whether the title of the page is "Google." 
If the page title doesn't match "Google," the test will fail, indicating that the assertion has failed. 

"""
