import logging
import os
import unittest
from logging import raiseExceptions
from time import sleep

from appium import webdriver
from common import auth as auth
from common import commonFunctions as common
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from common import config as config

logging.basicConfig(filename="log.txt", level=logging.INFO)


# print("In the test with device: ", runner.getDeviceID())
class SelectSite(unittest.TestCase):
    """Class to run tests against the View app"""
    def setUp(self):
        """Setup for the test"""
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__), 'apps/Android.apk'))
        desired_caps['appPackage'] = 'com.view.viewglass'
        desired_caps['appActivity'] = 'com.view.viewglass.Splash'
        desired_caps['autoGrantPermissions'] = True
        desired_caps['noReset'] = True
        desired_caps['clearSystemFiles'] = True
        self.driver = webdriver.Remote('http://localhost:4444/wd/hub', desired_caps)

    def tearDown(self):
        """Tear down the test"""
        self.driver.quit()

    def testSelectSiteSearchFunctionality(self):
        """
        Verify the functionality of the search bar for selecting a site
        """
        if auth.isUserLoggedIn(self.driver):
            if common.foundAlert(self.driver):
                common.respondToAlert(self.driver, 0)
            auth.logout(self.driver)
            sleep(30)
        auth.login(self.driver, config.users['CRUDO']['username'], config.users['CRUDO']['password'])

        if WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID, "com.view.viewglass:id/search_image_view"))):
            search = self.driver.find_element_by_id("com.view.viewglass:id/search_image_view")
            search.click()
            search_text = self.driver.find_element_by_id("com.view.viewglass:id/search_site_edit_text")
            # search for the site and press ENTER
            search_text.send_keys(config.site)
            # self.driver.press_keycode(66)
            self.driver.find_element_by_id("com.view.viewglass:id/login_bg_LL").click()
        else:
            raiseExceptions("Failed to reach Select Site screen")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SelectSite)
    unittest.TextTestRunner(verbosity=2).run(suite)
