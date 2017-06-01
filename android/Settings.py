"""
########################################################################
#
# SYNOPSIS
#   Zones :  Include Test cases related to viewing and managing user settings
#
# AUTHOR
#  Emily Puth (emily.puth@viewglass.com)
#
#
# DESCRIPTION
#   Include Test cases related to changing mode, sending feedback, and other user-related operations
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
from common import commonFunctions
from common import config
from common import site


class Settings(unittest.TestCase):
    """Class to run tests against the View app"""
    def setUp(self):
        """Setup for the test"""
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = os.path.abspath(os.path.join(os.getcwd(), 'apps/Android.apk'))
        desired_caps['appPackage'] = 'com.view.viewglass'
        desired_caps['appActivity'] = 'com.view.viewglass.Splash'
        desired_caps['autoGrantPermissions'] = True
        desired_caps['noReset'] = True
        desired_caps['clearSystemFiles'] = True
        self.driver = webdriver.Remote('http://localhost:4444/wd/hub', desired_caps)

    def tearDown(self):
        """Tear down the test"""
        self.driver.quit()

    def testUIComponentsOfSettingsScreen(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        commonFunctions.navIcon(self.driver)

        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/settingIcon_navigationIV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/settingIcon_navigationIV").click()
        else:
            raiseExceptions("Settings option in navigation menu is missing")

        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_settingScreen_wallSwitchTV"))):
            pass
        else:
            raiseExceptions("Settings heading is missing")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/act_about_wallSwitchTV")) <= 0:
            raiseExceptions("About tab is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/legal_wallSwitchTV")) <= 0:
            raiseExceptions("Legal tab is missing")

    def testLegal(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        commonFunctions.navIcon(self.driver)

        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/settingIcon_navigationIV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/settingIcon_navigationIV").click()
        else:
            raiseExceptions("Settings option in navigation menu is missing")

        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_settingScreen_wallSwitchTV"))):
            pass
        else:
            raiseExceptions("Settings heading is missing")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/legal_wallSwitchTV")) > 0:
            self.driver.find_element_by_id("com.view.viewglass:id/legal_wallSwitchTV").click()
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/legal_contentTV")) <= 0:
            raiseExceptions("Legal content is missing")

    def testAboutForCRUDO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'CRUDO')
        auth.loginAndSelectSite(self.driver, config.users['CRUDO']['username'], config.users['CRUDO']['password'], config.site[0])
        commonFunctions.navIcon(self.driver)

        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/settingIcon_navigationIV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/settingIcon_navigationIV").click()
        else:
            raiseExceptions("Settings option in navigation menu is missing")

        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_settingScreen_wallSwitchTV"))):
            pass
        else:
            raiseExceptions("Settings heading is missing")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/act_about_wallSwitchTV")) > 0:
            self.driver.find_element_by_id("com.view.viewglass:id/act_about_wallSwitchTV").click()
        if WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_settingTV"))):
            pass
        else:
            raiseExceptions("About Viewglass heading is missing")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/application_settingTV")) <= 0:
            raiseExceptions("Application subheading is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/version_settingLL")) <= 0:
            raiseExceptions("Version is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/deviceid_settingLL")) <= 0:
            raiseExceptions("Show Device is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/masterController_settingsTV")) <= 0:
            raiseExceptions("Master Controller subheading is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/site_settingLL")) <= 0:
            raiseExceptions("Site is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/mode_settingLL")) <= 0:
            raiseExceptions("Mode is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/name_settingLL")) <= 0:
            raiseExceptions("Name is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/date_settingTV")) <= 0:
            raiseExceptions("Date setting is missing")
        size = self.driver.find_element_by_id("com.view.viewglass:id/appInfoParentLL").size
        location = self.driver.find_element_by_id("com.view.viewglass:id/appInfoParentLL").location
        self.driver.swipe(location['x'] + size['width'] / 2, location['y'] + size['height'] - 10,
                          location['x'] + size['width'] / 2, location['y'] + 10, 2000)
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/time_settingLL")) <= 0:
            raiseExceptions("Time setting is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/setting_timeZoneLL")) <= 0:
            raiseExceptions("Timezone setting is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/setting_PltfrmVersionLL")) <= 0:
            raiseExceptions("Platform Version is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/setting_DatabaseVersionLL")) <= 0:
            raiseExceptions("Database Version is missing")

    def testAboutForRUO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'RUO')
        auth.loginAndSelectSite(self.driver, config.users['RUO']['username'], config.users['RUO']['password'], config.site[0])
        commonFunctions.navIcon(self.driver)

        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/settingIcon_navigationIV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/settingIcon_navigationIV").click()
        else:
            raiseExceptions("Settings option in navigation menu is missing")

        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_settingScreen_wallSwitchTV"))):
            pass
        else:
            raiseExceptions("Settings heading is missing")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/act_about_wallSwitchTV")) > 0:
            self.driver.find_element_by_id("com.view.viewglass:id/act_about_wallSwitchTV").click()
        if WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_settingTV"))):
            pass
        else:
            raiseExceptions("About Viewglass heading is missing")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/application_settingTV")) <= 0:
            raiseExceptions("Application subheading is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/version_settingLL")) <= 0:
            raiseExceptions("Version is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/deviceid_settingLL")) <= 0:
            raiseExceptions("Show Device is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/masterController_settingsTV")) <= 0:
            raiseExceptions("Master Controller subheading is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/site_settingLL")) <= 0:
            raiseExceptions("Site is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/mode_settingLL")) <= 0:
            raiseExceptions("Mode is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/name_settingLL")) <= 0:
            raiseExceptions("Name is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/date_settingTV")) <= 0:
            raiseExceptions("Date setting is missing")
        size = self.driver.find_element_by_id("com.view.viewglass:id/appInfoParentLL").size
        location = self.driver.find_element_by_id("com.view.viewglass:id/appInfoParentLL").location
        self.driver.swipe(location['x'] + size['width'] / 2, location['y'] + size['height'] - 10,
                          location['x'] + size['width'] / 2, location['y'] + 10, 2000)
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/time_settingLL")) <= 0:
            raiseExceptions("Time setting is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/setting_timeZoneLL")) <= 0:
            raiseExceptions("Timezone setting is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/setting_PltfrmVersionLL")) <= 0:
            raiseExceptions("Platform Version is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/setting_DatabaseVersionLL")) <= 0:
            raiseExceptions("Database Version is missing")

    def testAboutForRO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'RO')
        auth.login(self.driver, config.users['RO']['username'], config.users['RO']['password'])
        sleep(20)
        if commonFunctions.foundAlert(self.driver):
            commonFunctions.respondToAlert(self.driver, 0)

        commonFunctions.navIcon(self.driver)

        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/settingIcon_navigationIV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/settingIcon_navigationIV").click()
        else:
            raiseExceptions("Settings option in navigation menu is missing")

        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_settingScreen_wallSwitchTV"))):
            pass
        else:
            raiseExceptions("Settings heading is missing")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/act_about_wallSwitchTV")) > 0:
            self.driver.find_element_by_id("com.view.viewglass:id/act_about_wallSwitchTV").click()
        if WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_settingTV"))):
            pass
        else:
            raiseExceptions("About Viewglass heading is missing")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/application_settingTV")) <= 0:
            raiseExceptions("Application subheading is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/version_settingLL")) <= 0:
            raiseExceptions("Version is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/deviceid_settingLL")) <= 0:
            raiseExceptions("Show Device is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/masterController_settingsTV")) <= 0:
            raiseExceptions("Master Controller subheading is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/site_settingLL")) <= 0:
            raiseExceptions("Site is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/mode_settingLL")) <= 0:
            raiseExceptions("Mode is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/name_settingLL")) <= 0:
            raiseExceptions("Name is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/date_settingTV")) <= 0:
            raiseExceptions("Date setting is missing")
        size = self.driver.find_element_by_id("com.view.viewglass:id/appInfoParentLL").size
        location = self.driver.find_element_by_id("com.view.viewglass:id/appInfoParentLL").location
        self.driver.swipe(location['x'] + size['width'] / 2, location['y'] + size['height'] - 10,
                          location['x'] + size['width'] / 2, location['y'] + 10, 2000)
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/time_settingLL")) <= 0:
            raiseExceptions("Time setting is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/setting_timeZoneLL")) <= 0:
            raiseExceptions("Timezone setting is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/setting_PltfrmVersionLL")) <= 0:
            raiseExceptions("Platform Version is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/setting_DatabaseVersionLL")) <= 0:
            raiseExceptions("Database Version is missing")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Settings)
    unittest.TextTestRunner(verbosity=2).run(suite)


