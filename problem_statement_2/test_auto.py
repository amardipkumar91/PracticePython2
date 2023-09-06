import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class KiwiSaver(unittest.TestCase):
    
    def setUp(self):
         # create a new Safari session
        self.driver = webdriver.Safari()
        # navigate to the application home page
        self.driver.get("http://www.westpac.co.nz/")

    def test_kiwiSaver_retirement_calculater(self):
        """TC_002_01 :-Verify if a user will be able to login with a valid username and valid password."""
         # get the login textbox
        import pdb;pdb.set_trace()
        kiwisaver_tab = self.driver.find_element_by_id("ubermenu-section-link-kiwisaver-ps") #username for login
        hover = ActionChains(self.driver).move_to_element(kiwisaver_tab)
        hover.perform()

      


    def tearDown(self):
        #closing the Safari session
        self.driver.close()

if __name__ == "__main__":
    unittest.main()