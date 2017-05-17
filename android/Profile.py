"""
########################################################################
#
# SYNOPSIS
#   Zones :  Include Test cases related to the user profile
#
# AUTHOR
#  Emily Puth (emily.puth@viewglass.com)
#
#
# DESCRIPTION
#   Include Test cases related to the user profile
#
# USAGE
#   
#
# EXIT STATUS
#   n/a
#
# FILES
#   n/a
#
# INDENTATION STYLE
#   One tab = four spaces
#
# LICENSE/COPYRIGHT
#   (c) 2016 View, All rights reserved.
#
########################################################################
"""

import os
import unittest
from logging import raiseExceptions
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from common import auth
from common import config
from common import commonFunctions
from common import site


class Profile(unittest.TestCase):
    """Class to run tests against the View app"""
    def setUp(self):
        """Setup for the test"""
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = os.path.abspath(os.path.join(os.getcwd(), 'apps\\Android.apk'))
        desired_caps['appPackage'] = 'com.view.viewglass'
        desired_caps['appActivity'] = 'com.view.viewglass.Splash'
        desired_caps['autoGrantPermissions'] = True
        desired_caps['noReset'] = True
        desired_caps['clearSystemFiles'] = True
        self.driver = webdriver.Remote('http://localhost:4444/wd/hub', desired_caps)

    def tearDown(self):
        """Tear down the test"""
        self.driver.quit()

    def testUIComponentsOfProfileScreenForCRUDO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/username_navigationTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/username_navigationTV").click()
        else:
            raiseExceptions("Profile option in navigation menu is missing")

        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_myProfileTV"))):
            pass
        else:
            raiseExceptions("Profile heading is missing")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/startup_myProfileTV")) <= 0:
            raiseExceptions("Send Feedback tab is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/change_site_myProfileTV")) <= 0:
            raiseExceptions("Change Site is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/change_appserverIP_myProfileTV")) <= 0:
            raiseExceptions("Change Appserver IP is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/tourPreferenceTV")) <= 0:
            raiseExceptions("Tour Preference is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/mobiledataTV")) <= 0:
            raiseExceptions("Cellular Data is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/signout_myProfileTV")) <= 0:
            raiseExceptions("Sign Out button is missing")
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Sign Out']").click()

    def testUIComponentsOfProfileScreenForRUO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'RUO')
        auth.login(self.driver, config.users['RUO']['username'], config.users['RUO']['password'])
        site.selectSite(self.driver, config.site[0])
        sleep(20)
        if commonFunctions.foundAlert(self.driver):
            commonFunctions.respondToAlert(self.driver, 0)

        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/username_navigationTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/username_navigationTV").click()
        else:
            raiseExceptions("Profile option in navigation menu is missing")

        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_myProfileTV"))):
            pass
        else:
            raiseExceptions("Profile heading is missing")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/startup_myProfileTV")) <= 0:
            raiseExceptions("Send Feedback tab is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/change_site_myProfileTV")) <= 0:
            raiseExceptions("Change Site is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/change_appserverIP_myProfileTV")) <= 0:
            raiseExceptions("Change Appserver IP is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/tourPreferenceTV")) <= 0:
            raiseExceptions("Tour Preference is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/mobiledataTV")) <= 0:
            raiseExceptions("Cellular Data is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/signout_myProfileTV")) <= 0:
            raiseExceptions("Sign Out button is missing")
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Sign Out']").click()

    def testUIComponentsOfProfileScreenForRO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'RO')
        auth.login(self.driver, config.users['RO']['username'], config.users['RO']['password'])
        sleep(20)
        if commonFunctions.foundAlert(self.driver):
            commonFunctions.respondToAlert(self.driver, 0)
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/view_btnTV")) > 0:
            commonFunctions.navIcon(self.driver)

        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/username_navigationTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/username_navigationTV").click()
        else:
            raiseExceptions("Profile option in navigation menu is missing")

        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_myProfileTV"))):
            pass
        else:
            raiseExceptions("Profile heading is missing")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/startup_myProfileTV")) <= 0:
            raiseExceptions("Send Feedback tab is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/change_appserverIP_myProfileTV")) <= 0:
            raiseExceptions("Change Appserver IP is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/tourPreferenceTV")) <= 0:
            raiseExceptions("Tour Preference is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/mobiledataTV")) <= 0:
            raiseExceptions("Cellular Data is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/signout_myProfileTV")) <= 0:
            raiseExceptions("Sign Out button is missing")
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Sign Out']").click()

    def testSendFeedback(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/username_navigationTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/username_navigationTV").click()
        else:
            raiseExceptions("Profile option in navigation menu is missing")

        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_myProfileTV"))):
            pass
        else:
            raiseExceptions("Profile heading is missing")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/startup_myProfileTV")) > 0:
            self.driver.find_element_by_id("com.view.viewglass:id/startup_myProfileTV").click()
        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='Send Device Logs...']"))):
            pass
        else:
            raiseExceptions("Send Device Logs panel is missing")

    def testChangeSite(self):
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'CRUDO')
        auth.login(self.driver, config.users['CRUDO']['username'], config.users['CRUDO']['password'])
        site.selectSite(self.driver, config.site[0])
        sleep(20)
        if commonFunctions.foundAlert(self.driver):
            commonFunctions.respondToAlert(self.driver, 0)

        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/username_navigationTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/username_navigationTV").click()
        else:
            raiseExceptions("Profile option in navigation menu is missing")

        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_myProfileTV"))):
            pass
        else:
            raiseExceptions("Profile heading is missing")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/change_site_myProfileTV")) > 0:
            self.driver.find_element_by_id("com.view.viewglass:id/change_site_myProfileTV").click()
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/search_layout")) > 0:
            self.driver.find_element_by_id("com.view.viewglass:id/search_layout").click()
            search = self.driver.find_element_by_xpath("//android.widget.EditText[@text='Search']")
            search.send_keys(config.site[1])
            self.driver.find_element_by_id("com.view.viewglass:id/zone_item_select_zoneTV").click()
        else:
            raiseExceptions("Missing Search option in Change Site")

        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@text='Yes']"))):
            self.driver.find_element_by_xpath("//android.widget.Button[@text='Yes']").click()
        else:
            raiseExceptions("confirmation message for changing site is missing")

    def testChangeAppserverIP(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/username_navigationTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/username_navigationTV").click()
        else:
            raiseExceptions("Profile option in navigation menu is missing")

        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_myProfileTV"))):
            pass
        else:
            raiseExceptions("Profile heading is missing")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/change_appserverIP_myProfileTV")) > 0:
            self.driver.find_element_by_id("com.view.viewglass:id/change_appserverIP_myProfileTV").click()
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/iP_myProfileTV")) <= 0:
            raiseExceptions("IP title is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/enterIP_myProfileTV")) <= 0:
            raiseExceptions("Enter IP text field is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/done_myProfileTV")) <= 0:
            raiseExceptions("Done button is missing")

    def testTourPreference(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/username_navigationTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/username_navigationTV").click()
        else:
            raiseExceptions("Profile option in navigation menu is missing")

        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_myProfileTV"))):
            pass
        else:
            raiseExceptions("Profile heading is missing")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/togglebtn_tourPreferenceIV")) > 0:
            self.driver.find_element_by_id("com.view.viewglass:id/togglebtn_tourPreferenceIV").click()
        if self.driver.find_element_by_id("com.view.viewglass:id/togglebtn_tourPreferenceIV").get_attribute("checked") == "false":
            raiseExceptions("Tour Preference toggle button did not work")
        else:
            self.driver.find_element_by_id("com.view.viewglass:id/togglebtn_tourPreferenceIV").click()

    def testCellularData(self):
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'CRUDO')
        auth.login(self.driver, config.users['CRUDO']['username'], config.users['CRUDO']['password'])
        site.selectSite(self.driver, config.site[0])
        sleep(20)
        if commonFunctions.foundAlert(self.driver):
            commonFunctions.respondToAlert(self.driver, 0)

        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/username_navigationTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/username_navigationTV").click()
        else:
            raiseExceptions("Profile option in navigation menu is missing")

        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_myProfileTV"))):
            pass
        else:
            raiseExceptions("Profile heading is missing")

        startingCheck = self.driver.find_element_by_id("com.view.viewglass:id/togglebtn_mobiledataIV").get_attribute(
            "checked")
        if startingCheck == "true":
            oppositeCheck = "false"
        else:
            oppositeCheck = "true"
        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/togglebtn_mobiledataIV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/togglebtn_mobiledataIV").click()
        status = self.driver.find_element_by_id("com.view.viewglass:id/togglebtn_mobiledataIV")
        if status.get_attribute("checked") != oppositeCheck:
            raiseExceptions("Cellular Data toggle button did not work")
        else:
            # return to previous setting
            self.driver.find_element_by_id("com.view.viewglass:id/togglebtn_mobiledataIV").click()

    def testSignOutButton(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/username_navigationTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/username_navigationTV").click()
        else:
            raiseExceptions("Profile option in navigation menu is missing")

        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_myProfileTV"))):
            pass
        else:
            raiseExceptions("Profile heading is missing")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/signout_myProfileTV")) > 0:
            self.driver.find_element_by_id("com.view.viewglass:id/signout_myProfileTV").click()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Profile)
    unittest.TextTestRunner(verbosity=2).run(suite)


