import os
import unittest
from time import sleep

from appium import webdriver
from common import auth as auth
from common import site as site
from selenium import webdriver
from selenium.common.exceptions import *

from common import config as config


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

    def testCheckIfSystemIsReadyForTesting(self):
        sleep(30)
        attempts = 0
        while attempts < 3:
            try:
                auth.login(self.driver, config.users['CRUDO']['username'], config.users['CRUDO']['password'])
                site.selectSite(self.driver, config.site[0])
                break
            except TimeoutException:
                print("Unable to login and connect to a site. Try again.")
                attempts += 1
                self.driver.quit()
                self.driver.launch_app()

#             if len(self.driver.find_elements(By.XPATH,
#                                        "//android.widget.TextView[@text='Site is not reachable. Please try again later or contact Facilities Manager or View Support at support@viewglass.com or (855)-478-8468']")) > 0:
#                 attempts += 1
#                 self.driver.find_element_by_xpath("//android.widget.TextView[@text='Ok']").click()
#             elif len(self.driver.find_elements(By.XPATH,
#                                        "//android.widget.TextView[@text='Retry']")) > 0:
#                 attempts += 1
#                 self.driver.find_element_by_xpath("//android.widget.TextView[@text='Retry']").click()
#             elif len(self.driver.find_elements(By.XPATH, "//android.widget.Button[@content-desc='LOGIN']")) > 0:
#                 attempts += 1
#             else:
#                 sleep(20)
#                 if common.foundAlert(self.driver):
#                     common.respondToAlert(self.driver, 0)
#                 if common.foundTour(self.driver):
#                     common.exitTour(self.driver)
# #                     auth.logout(self.client)
#                 break

    def tearDown(self):
        """Tear down the test"""
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SystemReady)
    unittest.TextTestRunner(verbosity=2).run(suite)


