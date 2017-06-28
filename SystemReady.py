import os
import unittest
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By
from logging import raiseExceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from common import auth
from common import config
from common import site
from common import commonFunctions as common


class SystemReady(unittest.TestCase):
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

    def testCheckDeviceName(self):
        """
        Get the device name
        """
        device = config.devices[self.driver.desired_capabilities.get("deviceName")]["name"]
        print("Device : ", device)

    def testCheckIfSystemIsReadyForTesting(self):
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'CRUDO')
        attempts = 0
        while attempts < 3:
            if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/retry_btn")) > 0:
                self.driver.find_element_by_id("com.view.viewglass:id/retry_btn").click()

            if len(self.driver.find_elements(By.XPATH, "//android.widget.Button[@content-desc='Login']")) > 0:
                auth.loginOperation(self.driver, config.users['CRUDO']['username'], config.users['CRUDO']['password'])
                try:
                    findElements = [("ID", "com.view.viewglass:id/search_image_view"),
                                    ("XPATH", "//android.widget.TextView[@text='Recently Crashed!!!']"),
                                    ("ID", "com.view.viewglass:id/home_controlIV")]
                    common.waitForElement(self.driver, findElements, 120)
                    # WebDriverWait(self.driver, 120).until(lambda driver: len(driver.find_elements(By.ID,"com.view.viewglass:id/search_image_view")) > 0 or len(driver.find_elements(By.XPATH,"//android.widget.TextView[@text='Recently Crashed!!!']")) > 0 or len(driver.find_elements(By.ID,"com.view.viewglass:id/home_controlIV")) > 0)
                except TimeoutException:
                    print("didn't find anything after 2 minutes")
                    pass

            # after user enters valid credentials and clicks the login button, check if
            # (1) user is led to the Select Site screen, or (2) in the Control screen (RO user), or (3) in Control
            # screen with a 'Recently Crashed' alert. If so, break, and continue (maybe respond to alert)
            if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/search_image_view")) > 0:
                site.selectSite(self.driver, config.sites['Default'])

            if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/home_controlIV")) > 0:
                break
            elif len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='Recently Crashed!!!']")) > 0:
                common.respondToAlert(self.driver, 0)
                sleep(5)
                break
            elif len(self.driver.find_elements(By.ID, "com.view.viewglass:id/view_btnTV")) > 0:
                self.driver.find_element_by_id("com.view.viewglass:id/view_btnTV").click()
                break
            elif common.foundTour(self.driver):
                common.exitTour(self.driver)
                break
            elif len(self.driver.find_elements(By.XPATH,
                                          "//android.widget.TextView[@text='Site is not reachable. Please try again later or contact Facilities Manager or View Support at support@viewglass.com or (855)-478-8468']")) > 0:
                raiseExceptions("Site is not reachable at the moment")
            else:
                attempts += 1
                self.driver.close_app()
                self.driver.launch_app()
                sleep(20)

            if common.foundTour(self.driver):
                common.exitTour(self.driver)
            if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/view_btnTV")) > 0:
                self.driver.find_element_by_id("com.view.viewglass:id/view_btnTV").click()
                sleep(5)

        if attempts == 3:
            raiseExceptions("Unable to login after 3 tries")

    def tearDown(self):
        """Tear down the test"""
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SystemReady)
    unittest.TextTestRunner(verbosity=2).run(suite)


