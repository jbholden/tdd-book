from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith checks out the home page
        browser.get('http://localhost:8000')

        # notices page title and header
        self.assertIn('To-Do',self.browser.title)
        self.fail('Finish the test!')

        # invited to enter a to-do item
        # types "Buy peacok feathers" into text box
        # hits "enter", page updates, page shows todo item
        # types "Use peacock features to make a fly" into text input
        # page updates, shows both to-do items
        # Edith finds a unique URL for her
        # Edith visits URL

if __name__ == "__main__":
    unittest.main(warnings='ignore')
