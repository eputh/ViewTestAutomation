"""
########################################################################
#
# SYNOPSIS
#   authentication :  Include Test cases related to user authentication using  CRUDO, RUO, RO privilege users
#
# AUTHOR
#  Prinal khandelwal (Pkhandelwal@viewglass.com)
#
#
# DESCRIPTION
#   Include Test cases login using valid and invalid user credentials in app . 
#   Exceptional handling in case of Network connectivity issue
#   Exceptional handling in case of user not configured in VRM
#   Exceptional handling when no site is associated with valid VRM user
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
import logging
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


class Authentication(unittest.TestCase):

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

    # @attr('acceptance', sid='TC-login-1.5-01', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testUIComponentsOfLoginScreen(self):
        """
        Verify the UI components of login screen like logo, user credentials parameters
        """
        if auth.isUserLoggedIn(self.driver):
            if commonFunctions.foundAlert(self.driver):
                commonFunctions.respondToAlert(self.driver, 0)
            auth.logout(self.driver)
            sleep(30)

        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='view']")) > 0:
                pass
        else:
            raiseExceptions("View logo is missing")
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='Dynamic Glass']")) > 0:
                # If statement
                pass
        else:
            raiseExceptions("Dynamic Glass logo is missing")

        if WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@index='0']"))):
            email = self.driver.find_element_by_xpath("//android.widget.EditText[@index='0']")
            text = email.text
            if text != "Email":
                email.clear()

        if WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@text='Email']"))):
            pass
        else:
            raiseExceptions(" Enter username field is missing")

        if WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@text='Password']"))):
            pass
        else:
            raiseExceptions("Enter Password field is missing")

        if len(self.driver.find_elements(By.XPATH, "//android.view.View[@content-desc='Remember Me']")) > 0:
            pass
        elif len(self.driver.find_elements(By.CLASS_NAME, "android.widget.CheckBox")) > 0:
            pass
        else:
            raiseExceptions(" Remember me is missing on login screen")

        if len(self.driver.find_elements(By.XPATH, "//android.widget.Button[@content-desc='Login']")) > 0:
            pass
        else:
            raiseExceptions("unable to find login button")

    # @attr('acceptance', sid='TC-login-1.5-03', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testLoginUsingCRUDOUser(self):
        """
        Verify the app authentication by logging using valid CRUDO privilege user
        """
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'CRUDO')
        auth.login(self.driver, config.users['CRUDO']['username'], config.users['CRUDO']['password'])
        auth.signout(self.driver)

    # @attr('acceptance', sid='TC-login-1.5-05', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testLoginUsingRUOUser(self):
        """
        Verify the app authentication by logging using valid RUO privilege user
        """
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'RUO')
        auth.login(self.driver, config.users['RUO']['username'], config.users['RUO']['password'])
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/home_controlIV")) > 0:
            auth.logout(self.driver)
        elif len(self.driver.find_elements(By.XPATH, "//android.widget.Button[@resource-id='com.view.viewglass:id/button_cancel']")) > 0:
            auth.signout(self.driver)

    # @attr('acceptance', sid='TC-login-1.5-06', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testLoginUsingROUser(self):
        """
        Verify the app authentication by logging using valid RO privilege user
        """
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'RO')
        auth.login(self.driver, config.users['RO']['username'], config.users['RO']['password'])
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/home_controlIV")) > 0:
            auth.logout(self.driver)
        elif len(self.driver.find_elements(By.XPATH, "//android.widget.Button[@resource-id='com.view.viewglass:id/button_cancel']")) > 0:
            auth.signout(self.driver)

    # @attr('acceptance', sid='TC-login-1.5-06', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testLoginTo1dot2Site(self):
        """
        Verify the app authentication by logging using valid RO privilege user
        """
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'CRUDO')
        auth.login(self.driver, config.users['1dot2System']['username'], config.users['1dot2System']['password'])
        site.selectSite(self.driver, 'B195 Ballroom')

    # @attr('acceptance', sid='TC-login-1.5-07', bv=10)
    # @unittest.skip('Test case temporarily disabled')  
    def testLoginUsingInvalidUsername(self):
        """
        Verify the exceptional handling by logging using invalid user
        """
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'CRUDO')
        auth.negativeTestCaseLoginValidation(self.driver, config.users['InvalidEmail']['username'], config.users['InvalidEmail']['password'])
        auth.loginScreenValidations(self.driver)
        
    # @attr('acceptance', sid='TC-login-1.5-08', bv=10)
    # @unittest.skip('Test case temporarily disabled')      
    def testLoginUsingInvalidPwd(self):
        """
        Verify the exceptional handling by logging using invalid user
        """
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'CRUDO')
        auth.negativeTestCaseLoginValidation(self.driver, config.users['InvalidPwd']['username'], config.users['InvalidPwd']['password'])
        auth.loginScreenValidations(self.driver)
    
    # @attr('acceptance', sid='TC-login-1.5-17', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testLoginUsingSpecialPwd(self):
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'CRUDO')
        auth.loginOperation(self.driver, config.users['PwdStartingSpecialChar']['username'], config.users['PwdStartingSpecialChar']['password'])
        auth.loginScreenValidations(self.driver)

    def testLoginUsingMissingUsername(self):
        """
        Verify the exceptional handling by logging using invalid user
        """
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'CRUDO')
        auth.negativeTestCaseLoginValidation(self.driver, config.users['MissingEmail']['username'], config.users['MissingEmail']['password'])
        auth.loginScreenValidations(self.driver)           
        
    def testLoginUsingMissingPwd(self):
        """
        Verify the exceptional handling by logging using invalid user
        """
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'CRUDO')
        auth.negativeTestCaseLoginValidation(self.driver, config.users['MissingPwd']['username'], config.users['MissingPwd']['password'])
        auth.loginScreenValidations(self.driver)

    # @attr('acceptance', sid='TC-login-1.5-21', bv=10)
    # @unittest.skip('Test case temporarily disabled')     
    def testNetworkConnectivityLost(self):
        """
        Verify the App Exceptional handling when user lost network connectivity from mobile device.
        This will disable the Data usage and wifi during test runtime and verify error message
        """
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'CRUDO')
        self.driver.set_network_connection(1)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='Retry']")) > 0:
            self.driver.set_network_connection(6)
            sleep(5)
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Retry']").click()
        else:
            raiseExceptions("Exception handling for lost network connection is missing")
    
    # @attr('acceptance', sid='TC-login-1.5-04', bv=10)
    # @unittest.skip('Test case temporarily disabled') 
    def testUnconfiguredUserInVRM(self):
        """
        Verify the exceptional handling by logging using invalid user
        """
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'UserNotConfiguredInVRM')
        auth.login(self.driver, config.users['UserNotConfiguredInVRM']['username'], config.users['UserNotConfiguredInVRM']['password'])

    # @attr('acceptance', sid='TC-login-1.5-09', bv=10)
    # @unittest.skip('Test case temporarily disabled')  
    def testNoSiteAssignedForUserInVRM(self):
        """
        Verify the exceptional handling by logging using invalid user
        """
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'RO')
        auth.login(self.driver, config.users['RO']['username'], config.users['RO']['password'])
        auth.logout(self.driver)

    def testSingleSiteUserLogin(self):
        """
        Verify the exceptional handling by logging using invalid user
        """
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'RUO')
        auth.login(self.driver, config.users['RUO']['username'], config.users['RUO']['password'])
        sleep(30)
        auth.logout(self.driver)
         
    # @attr('acceptance', sid='TC-login-1.5-18', bv=10)
    # @unittest.skip('Test case temporarily disabled')     
    def testLogoutFunctionality(self):
        """
        Verify the logout functionality
        """
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'CRUDO')
        auth.login(self.driver, config.users['CRUDO']['username'], config.users['CRUDO']['password'])
        sleep(30)
        auth.signout(self.driver)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Authentication)
    unittest.TextTestRunner(verbosity=2).run(suite)
