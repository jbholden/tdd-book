from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith checks out the home page
        self.browser.get('http://localhost:8000')

        # notices page title and header
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        # invited to enter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                'Enter a to-do item')

        # types "Buy peacock feathers" into text box
        inputbox.send_keys('Buy peacock feathers')

        # hits "enter", page updates, page shows todo item
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers',[row.text for row in rows])
        self.assertIn('2: Use peacock feathers to make a fly',[row.text for row in rows])

        # types "Use peacock features to make a fly" into text input
        self.fail('Finish the test!') 

        # page updates, shows both to-do items
        # Edith finds a unique URL for her
        # Edith visits URL

if __name__ == "__main__":
    unittest.main()
    #unittest.main(warnings='ignore')
