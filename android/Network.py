"""
########################################################################
#
# SYNOPSIS
#   Control :  Include Test cases related to selecting a site
#
# AUTHOR
#  Emily Puth (emily.puth@viewglass.com)
#
#
# DESCRIPTION
#   Include Test cases related to selecting a site for CRUDO, RUO, RO privilege users.
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


class Network(unittest.TestCase):
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

    def testLoginForLostNetworkConnectivity(self):
        """
        Verify the exceptional handling for when network connectivity is lost in the Login screen
        """
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'CRUDO')
        self.driver.set_network_connection(1)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='Retry']")) > 0:
            self.driver.set_network_connection(6)
            sleep(5)
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Retry']").click()
        else:
            raiseExceptions("Exception handling for lost network connection is missing")

    def testLoginForRecoveryFromLostNetworkConnectivity(self):
        """
        Verify recovery of the app to the Login screen when network connectivity is restored
        """
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'CRUDO')
        self.driver.set_network_connection(1)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='Retry']")) > 0:
            self.driver.set_network_connection(6)
            sleep(5)
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Retry']").click()
        else:
            raiseExceptions("Exception handling for lost network connection is missing")

        if WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='LOGIN']"))):
            pass
        else:
            raiseExceptions("Retry button unsuccessfully recovers the app from lost network connectivity")

    def testSelectSiteForLostNetworkConnectivity(self):
        """
        Verify the exceptional handling for when network connectivity is lost in the Select Site screen
        """
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'CRUDO')
        auth.login(self.driver, config.users['CRUDO']['username'], config.users['CRUDO']['password'])
        self.driver.set_network_connection(1)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='Retry']")) > 0:
            self.driver.set_network_connection(6)
        else:
            raiseExceptions("Exception handling for lost network connection is missing")

    def testSelectSiteForRecoveryFromLostNetworkConnectivity(self):
        """
        Verify recovery of the app to the Login screen when network connectivity is restored
        """
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'CRUDO')
        auth.login(self.driver, config.users['CRUDO']['username'], config.users['CRUDO']['password'])
        self.driver.set_network_connection(1)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='Retry']")) > 0:
            self.driver.set_network_connection(6)
            sleep(5)
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Retry']").click()
        else:
            raiseExceptions("Exception handling for lost network connection is missing")

        if WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='LOGIN']"))):
            pass
        else:
            raiseExceptions("Retry button unsuccessfully recovers the app from lost network connectivity")

    def testLostNetworkConnectivityInLoggedInSession(self):
        """
        Verify the exceptional handling for when network connectivity is lost within the app
        (e.g. Control, Zones, LiveView, Schedule, Scenes screens)
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        self.driver.set_network_connection(1)
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/no_internet_msg")) > 0:
            sleep(5)
            self.driver.set_network_connection(6)
        else:
            raiseExceptions("Exception handling for lost network connection is missing")

    def testRecoveryFromLostNetworkConnectivityInLoggedInSession(self):
        """
        Verify recovery of the app to the previous screen when network connectivity is restored
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        self.driver.set_network_connection(1)
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/no_internet_msg")) > 0:
            sleep(5)
            self.driver.set_network_connection(6)
            sleep(5)
        else:
            raiseExceptions("Exception handling for lost network connection is missing")

        if self.driver.network_connection == 6 and len(self.driver.find_elements(By.ID, "com.view.viewglass:id/no_internet_msg")) > 0:
            raiseExceptions("Progress bar and no Internet message did not disappear after the network was recovered")

    def testExecutionOfTestCasesUsingData(self):
        """
        Verify ability to continue using the app with only Data connection
        """
        hasData = config.devices[self.driver.desired_capabilities.get("deviceName")]["hasData"]
        if hasData:
            self.driver.set_network_connection(0)
            self.driver.set_network_connection(4)
            print(self.driver.network_connection)
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Retry']").click()
            # auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')

    def testRunningAppInTheBackground(self):
        """
        Verify recovery of the app to the previous session when the
        app is re-opened after hanging in the background
        """
        # put user in the Zones screen, place the app in the background, re-open,
        # and verify the app returns to the Zones screen
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_zonesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_zonesTV").click()
        else:
            raiseExceptions("Zones option in navigation menu is missing")

        self.driver.background_app(10)
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/home_zonesIV")) <= 0:
            raiseExceptions("App did not return to the previous screen (Zones)")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Network)
    unittest.TextTestRunner(verbosity=2).run(suite)
