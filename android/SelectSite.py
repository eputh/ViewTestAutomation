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
from common import commonFunctions as common
from common import site as site
from common import config as config


class SelectSite(unittest.TestCase):
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

    def testSelectSiteForCRUDOUser(self):
        """
        Verify the by logging using valid CRUDO privilege user
        """
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'CRUDO')
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
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'RUO')
        auth.login(self.driver, config.users['RUO']['username'], config.users['RUO']['password'])

        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='Select Site']")) > 0:
            headingHeight = self.driver.find_element_by_id("com.view.viewglass:id/viewLogoLL").size['height']
            middle = self.driver.find_element_by_id("com.view.viewglass:id/viewLogoLL").size['width'] / 2
            list = self.driver.find_element_by_id("com.view.viewglass:id/FL_siteListView")
            endx = headingHeight * 2
            startx = list.size['height'] - headingHeight
            self.driver.swipe(middle, startx, middle, endx, 3000)

    def testSelectSiteForROUser(self):
        """
        Verify the app authentication by logging using valid RO privilege user
        """
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'RO')
        auth.login(self.driver, config.users['RO']['username'], config.users['RO']['password'])

        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='Select Site']")) > 0:
            headingHeight = self.driver.find_element_by_id("com.view.viewglass:id/viewLogoLL").size['height']
            middle = self.driver.find_element_by_id("com.view.viewglass:id/viewLogoLL").size['width'] / 2
            list = self.driver.find_element_by_id("com.view.viewglass:id/FL_siteListView")
            endx = headingHeight * 2
            startx = list.size['height'] - headingHeight
            self.driver.swipe(middle, startx, middle, endx, 3000)

    def testSelectNotReachableSite(self):
        """
        Verify the exceptional handling by logging into a site that is not reachable
        """
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'CRUDO')
        auth.login(self.driver, config.users['CRUDO']['username'], config.users['CRUDO']['password'])

        if WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID, "com.view.viewglass:id/search_image_view"))):
            search = self.driver.find_element_by_id("com.view.viewglass:id/search_image_view")
            search.click()
            search_text = self.driver.find_element_by_id("com.view.viewglass:id/search_site_edit_text")
            # search for the site and press ENTER
            search_text.send_keys("1.2CONFsys")
            self.driver.press_keycode(66)
            size = self.driver.find_element_by_id("com.view.viewglass:id/siteList_searchResultCountTV").size
            location = self.driver.find_element_by_id("com.view.viewglass:id/siteList_searchResultCountTV").location
            x = size['width'] / 2
            y = location['y'] + size['height'] * 3
            self.driver.tap([(x, y)])
        else:
            raiseExceptions("Failed to reach Select Site screen")

        sleep(10)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='Site is not reachable. Please try again later or contact Facilities Manager or View Support at support@viewglass.com or (855)-478-8468']")) > 0:
            common.respondToAlert(self.driver, 0)
        else:
            raiseExceptions("Exception handling for unreachable site is missing")

    def testSelectSiteForMultipleSites(self):
        """
        Verify the functionality of logging into a user assigned
        to multiple sites
        """
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'CRUDO')
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

    def testSelectSiteForOneSiteAssignToUser(self):
        """
        Verify the functionality of logging into a user assigned
        to only one site
        """
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'RUO')
        auth.login(self.driver, config.users['RUO']['username'], config.users['RUO']['password'])

        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='Select Site']")) > 0:
            raiseExceptions("This user has more than one site")
        else:
            pass

    def testSelectSiteNoSiteAssignToUserInVRM(self):
        """
        Verify the functionality of logging into a user not assigned
        to any site
        """
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'CRUDO')
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'UserNotConfiguredInVRM')
        auth.login(self.driver, config.users['UserNotConfiguredInVRM']['username'],
                   config.users['UserNotConfiguredInVRM']['password'])

    def testSelectSiteSignoutFunctionality(self):
        """
        Verify the functionality of the Sign Out button
        """
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'CRUDO')
        auth.login(self.driver, config.users['CRUDO']['username'], config.users['CRUDO']['password'])

        if WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID, "com.view.viewglass:id/button_cancel"))):
            self.driver.find_element_by_id("com.view.viewglass:id/button_cancel").click()
        else:
            raiseExceptions(" Missing Sign Out button")

    def testSelectSiteSearchFunctionality(self):
        """
        Verify the functionality of the search bar for selecting a site
        """
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'CRUDO')
        auth.login(self.driver, config.users['CRUDO']['username'], config.users['CRUDO']['password'])

        if WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID, "com.view.viewglass:id/search_image_view"))):
            search = self.driver.find_element_by_id("com.view.viewglass:id/search_image_view")
            search.click()
            search_text = self.driver.find_element_by_id("com.view.viewglass:id/search_site_edit_text")
            # search for the site and press ENTER
            search_text.send_keys(config.site[0])
            self.driver.press_keycode(66)
            size = self.driver.find_element_by_id("com.view.viewglass:id/siteList_searchResultCountTV").size
            location = self.driver.find_element_by_id("com.view.viewglass:id/siteList_searchResultCountTV").location
            x = size['width'] / 2
            y = location['y'] + size['height'] * 3
            self.driver.tap([(x, y)])
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
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'CRUDO')
        auth.login(self.driver, config.users['CRUDO']['username'], config.users['CRUDO']['password'])

        site.selectSite(self.driver, config.site[0])
        if WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='Cancel']"))):
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Cancel']").click()
        else:
            raiseExceptions("Cancel button did not stop the process")

        if common.foundAlert(self.driver):
            common.respondToAlert(self.driver, 1)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SelectSite)
    unittest.TextTestRunner(verbosity=2).run(suite)


