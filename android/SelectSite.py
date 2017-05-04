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
from common import auth as auth
from common import commonFunctions as common
from common import site as site
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from common import config as config


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

    def testSelectSiteForCRUDOUser(self):
        """
        Verify the by logging using valid CRUDO privilege user
        """
        if auth.isUserLoggedIn(self.driver):
            if common.foundAlert(self.driver):
                common.respondToAlert(self.driver, 0)
            auth.logout(self.driver)
            sleep(30)
        auth.login(self.driver, config.users['CRUDO']['username'], config.users['CRUDO']['password'])

        if WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='Select Site']"))):
            headingHeight = self.driver.find_element_by_id("com.view.viewglass:id/viewLogoLL").size['height']
            middle = self.driver.find_element_by_id("com.view.viewglass:id/viewLogoLL").size['width']/2
            list = self.driver.find_element_by_id("com.view.viewglass:id/FL_siteListView")
            endx = headingHeight * 2
            startx = list.size['height'] - headingHeight
            self.driver.swipe(middle, startx, middle, endx, 3000)
        else:
            raiseExceptions("Failed to reach Select Site screen")

    def testSelectSiteForRUOUser(self):
        """
        Verify the app authentication by logging using valid RUO privilege user
        """
        if auth.isUserLoggedIn(self.driver):
            if common.foundAlert(self.driver):
                common.respondToAlert(self.driver, 0)
            auth.logout(self.driver)
            sleep(30)
        auth.login(self.driver, config.users['RUO']['username'], config.users['RUO']['password'])

        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='Select Site']")) > 0:
            raiseExceptions("RUO user has more than one site")
        else:
            pass

    def testSelectSiteForROUser(self):
        """
        Verify the app authentication by logging using valid RO privilege user
        """
        if auth.isUserLoggedIn(self.driver):
            if common.foundAlert(self.driver):
                common.respondToAlert(self.driver, 0)
            auth.logout(self.driver)
            sleep(30)
        auth.login(self.driver, config.users['RO']['username'], config.users['RO']['password'])

        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='Select Site']")) > 0:
            raiseExceptions("RUO user has more than one site")
        else:
            pass


    def testSelectsiteForLostNetworkConnectivity(self):
        """
        Verify the exceptional handling by logging using invalid user
        """
        if auth.isUserLoggedIn(self.driver):
            if common.foundAlert(self.driver):
                common.respondToAlert(self.driver, 0)
            auth.logout(self.driver)
            sleep(30)
        auth.login(self.driver, config.users['InvalidEmail']['username'], config.users['InvalidEmail']['password'])
        auth.loginScreenValidations(self.driver)

    def testSelectNotReachableSite(self):
        """
        Verify the exceptional handling by logging using invalid user
        """
        if auth.isUserLoggedIn(self.driver):
            if common.foundAlert(self.driver):
                common.respondToAlert(self.driver, 0)
            auth.logout(self.driver)
            sleep(30)
        auth.login(self.driver, config.users['InvalidPwd']['username'], config.users['InvalidPwd']['password'])
        auth.loginScreenValidations(self.driver)

    def testSelectSiteForMoreSite(self):
        if auth.isUserLoggedIn(self.driver):
            if common.foundAlert(self.driver):
                common.respondToAlert(self.driver, 0)
            auth.logout(self.driver)
            sleep(30)
        auth.login(self.driver, config.users['PwdStartingSpecialChar']['username'], config.users['PwdStartingSpecialChar']['password'])
        auth.signout(self.driver)

    def testSelectSiteForOneSiteAssignToUser(self):
        """
        Verify the exceptional handling by logging using invalid user
        """
        if auth.isUserLoggedIn(self.driver):
            if common.foundAlert(self.driver):
                common.respondToAlert(self.driver, 0)
            auth.logout(self.driver)
            sleep(30)
        auth.login(self.driver, config.users['MissingEmail']['username'], config.users['MissingEmail']['password'])
        auth.loginScreenValidations(self.driver)

    def testSelectSiteNoSiteAssignToUserInVRM(self):
        """
        Verify the exceptional handling by logging using invalid user
        """
        if auth.isUserLoggedIn(self.driver):
            if common.foundAlert(self.driver):
                common.respondToAlert(self.driver, 0)
            auth.logout(self.driver)
            sleep(30)
        auth.login(self.driver, config.users['MissingPwd']['username'], config.users['MissingPwd']['password'])
        auth.loginScreenValidations(self.driver)

    def testSelectSiteSignoutFunctionality(self):
        """
        Verify the functionality of the Sign Out button
        """
        if auth.isUserLoggedIn(self.driver):
            if common.foundAlert(self.driver):
                common.respondToAlert(self.driver, 0)
            auth.logout(self.driver)
            sleep(30)
        auth.login(self.driver, config.users['CRUDO']['username'], config.users['CRUDO']['password'])

        if WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID, "com.view.viewglass:id/button_cancel"))):
            self.driver.find_element_by_id("com.view.viewglass:id/button_cancel").click()
        else:
            raiseExceptions(" Missing Sign Out button")

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
            self.driver.press_keycode(66)
            self.driver.find_element_by_id("com.view.viewglass:id/login_bg_LL").click()
        else:
            raiseExceptions("Failed to reach Select Site screen")

        sleep(10)
        if common.foundAlert(self.driver):
            common.respondToAlert(self.driver, 0)
        auth.logout(self.driver)

    def testSelectSiteCancelFunctionality(self):
        """
        Verify the functionality of the cancel button
        """
        if auth.isUserLoggedIn(self.driver):
            if common.foundAlert(self.driver):
                common.respondToAlert(self.driver, 0)
            auth.logout(self.driver)
            sleep(30)
        auth.login(self.driver, config.users['CRUDO']['username'], config.users['CRUDO']['password'])

        site.selectSite(self.driver, config.site)
        if WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='Cancel']"))):
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Cancel']").click()
        else:
            raiseExceptions("Cancel button did not stop the process")

        if common.foundAlert(self.driver):
            common.respondToAlert(self.driver, 1)
            # if (self.driver.isElementFound("NATIVE", "xpath=//*[@id='button_cancel']", 0)):
            #     self.driver.click("NATIVE", "xpath=//*[@id='button_cancel']", 0, 1)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SelectSite)
    unittest.TextTestRunner(verbosity=2).run(suite)


