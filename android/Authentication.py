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
from logging import raiseExceptions
from time import sleep

from appium import webdriver
from common import auth as auth
from common import commonFunctions as common


class Authentication(unittest.TestCase):

    def setUp(self):
        """Setup for the test"""
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__), 'apps/Android.apk'))
        desired_caps['appPackage'] = 'com.view.viewglass'
        desired_caps['appActivity'] = 'com.view.viewglass.Splash'
        desired_caps['autoGrantPermissions'] = True
        desired_caps['noReset'] = True
        # desired_caps['clearSystemFiles'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    #@attr('acceptance', sid='TC-login-1.5-01', bv=10)
    #@unittest.skip('Test case temporarily disabled')    
    def testUIComponentsOfLoginScreen(self):
        """
        Verify the UI components of login screen like logo, user credentials parameters
        """
        if auth.isUserLoggedIn(self.driver):
            if common.foundAlert(self.driver):
                common.respondToAlert(self.driver, 0)
            auth.logout(self.driver)
            sleep(30)

        if(self.client.isElementFound("NATIVE", "xpath=//*[@text='view']", 0)):
                pass
        else:
            raiseExceptions("View logo is missing")
        if(self.client.isElementFound("NATIVE", "xpath=//*[@text='Dynamic Glass']", 0)):
                # If statement
                pass
        else:
            raiseExceptions("Dynamic Glass logo is missing")    
        
        if((self.client.waitForElement("WEB", "xpath=//*[@class='android.widget.EditText']", 0 , 3000)) or (self.client.waitForElement("NATIVE", "xpath=//*[@class='android.widget.EditText']", 0 , 3000))):
            if(self.client.isElementFound("WEB", "xpath=//*[@class='android.widget.EditText']", 0) and (self.client.getText("WEB", "xpath=//*[@class='android.widget.EditText']") != "Email")):
                self.client.click("WEB", "xpath=//*[@class='android.widget.EditText']", 0, 3)
                self.client.sendText("{BKSP}")
            elif(self.client.isElementFound("NATIVE", "xpath=//*[@class='android.widget.EditText']", 0) and (self.client.elementGetText("NATIVE", "xpath=//*[@class='android.widget.EditText']", 0) != "Email")):
                self.client.click("NATIVE", "xpath=//*[@class='android.widget.EditText']", 0, 3)
                self.client.sendText("{BKSP}")
                
        if((self.client.waitForElement("WEB", "text=Email", 0, 3000)) or (self.client.waitForElement("NATIVE", "text=Email", 0, 3000))): 
            if(self.client.isElementFound("WEB", "text=Email", 0)):
                pass
            else:
                raiseExceptions(" Enter username field is missing")
        
        if((self.client.waitForElement("WEB", "name=pwd", 0, 3000)) or (self.client.waitForElement("NATIVE", "xpath=//*[@text='Password']", 0, 3000))):
            if(self.client.isElementFound("WEB", "name=pwd", 0)):
                pass
            else:
                raiseExceptions("Enter Password field is missing")
        
        if(self.client.isElementFound("WEB", "text= Remember Me", 0)):
            pass
        elif(self.client.isElementFound("NATIVE", "xpath=//*[@class='android.widget.CheckBox']", 0)):
            pass
        else:
            raiseExceptions(" Remember me is missing on login screen")
            
        if(self.client.isElementFound("WEB", "xpath=//*[@contentDescription='LOGIN']", 0)):   
            pass
        elif(self.client.isElementFound("NATIVE", "xpath=//*[@contentDescription='LOGIN']")):
            pass
        else:
            raiseExceptions("unable to find login button")

    #@attr('acceptance', sid='TC-login-1.5-03', bv=10)
    #@unittest.skip('Test case temporarily disabled') 
    def testLoginUsingCRUDOUser(self):
        """
        Verify the app authentication by logging using valid CRUDO privilege user
        """
        auth.checkIfUserIsLoggedIn(self.client)
        logging.info(" login with CRUDO user") 
        auth.login(self.client, cfg.users['CRUDO']['username'], cfg.users['CRUDO']['password'])
        auth.signout(self.client)
    
    #@attr('acceptance', sid='TC-login-1.5-05', bv=10)
    #@unittest.skip('Test case temporarily disabled')      
    def testLoginUsingRUOUser(self):
        """
        Verify the app authentication by logging using valid RUO privilege user
        """
        auth.checkIfUserIsLoggedIn(self.client)
        auth.login(self.client, cfg.users['RUO']['username'], cfg.users['RUO']['password'])
        auth.signout(self.client)
    
    #@attr('acceptance', sid='TC-login-1.5-06', bv=10)
    #@unittest.skip('Test case temporarily disabled') 
    def testLoginUsingROUser(self):
        """
        Verify the app authentication by logging using valid RO privilege user
        """
        auth.checkIfUserIsLoggedIn(self.client)
        auth.login(self.client, cfg.users['RO']['username'], cfg.users['RO']['password'])
        auth.signout(self.client)
        
        
    #@attr('acceptance', sid='TC-login-1.5-06', bv=10)
    #@unittest.skip('Test case temporarily disabled') 
    def testLoginTo1dot2Site(self):
        """
        Verify the app authentication by logging using valid RO privilege user
        """
        auth.checkIfUserIsLoggedIn(self.client)
        auth.login(self.client, cfg.users['1dot2System']['username'], cfg.users['1dot2System']['password'])
        commonFunctions.selectSiteTemp(self.client, 'B195 Ballroom')
        auth.logout(self.client)
            
    
    #@attr('acceptance', sid='TC-login-1.5-07', bv=10)
    #@unittest.skip('Test case temporarily disabled')  
    def testLoginUsingInvalidUsername(self):
        """
        Verify the exceptional handling by logging using invalid user
        """
        auth.checkIfUserIsLoggedIn(self.client)
        auth.negativeTestCaseLoginValidation(self.client, cfg.users['InvalidEmail']['username'], cfg.users['InvalidEmail']['password'])
        auth.loginScreenValidations(self.client)
        
    #@attr('acceptance', sid='TC-login-1.5-08', bv=10)
    #@unittest.skip('Test case temporarily disabled')      
    def testLoginUsingInvalidPwd(self):
        """
        Verify the exceptional handling by logging using invalid user
        """
        auth.checkIfUserIsLoggedIn(self.client)
        auth.negativeTestCaseLoginValidation(self.client, cfg.users['InvalidPwd']['username'], cfg.users['InvalidPwd']['password'])
        auth.loginScreenValidations(self.client)
    
    #@attr('acceptance', sid='TC-login-1.5-17', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testLoginUsingSpecialPwd(self):
        auth.checkIfUserIsLoggedIn(self.client)
        auth.login(self.client, cfg.users['PwdStartingSpecialChar']['username'], cfg.users['PwdStartingSpecialChar']['password'])
        auth.signout(self.client)        
            
    def testLoginUsingMissingUsername(self):
        """
        Verify the exceptional handling by logging using invalid user
        """
        auth.checkIfUserIsLoggedIn(self.client)
        auth.negativeTestCaseLoginValidation(self.client, cfg.users['MissingEmail']['username'], cfg.users['MissingEmail']['password'])
        auth.loginScreenValidations(self.client)           
        
    def testLoginUsingMissingPwd(self):
        """
        Verify the exceptional handling by logging using invalid user
        """
        auth.checkIfUserIsLoggedIn(self.client)
        auth.negativeTestCaseLoginValidation(self.client, cfg.users['MissingPwd']['username'], cfg.users['MissingPwd']['password'])
        auth.loginScreenValidations(self.client)
        
        
    #@attr('acceptance', sid='TC-login-1.5-21', bv=10)
    #@unittest.skip('Test case temporarily disabled')     
# #     def testNetworkConnectivityLost(self):
# #         """
# #         Verify the App Exceptional handling when user lost network connectivity from mobile device.
# #         This will disable the Data usage and wifi during test runtime and verify error message
# #         """
# #         self.client.click("NATIVE", "xpath=//*[@text='Settings']", 0, 1)
# #         self.client.click("NATIVE", "xpath=//*[@text='Data usage']", 0, 1)
# #         self.client.click("NATIVE", "xpath=//*[@id='switch_widget']", 0, 1)
# #         self.client.click("NATIVE", "xpath=//*[@id='navigationBarBackground']", 0, 1)
# #         self.client.click("NATIVE", "xpath=//*[@text='ViewGlass']", 0, 1)
# #         self.client.click("NATIVE", "xpath=//*[@text='Retry']", 0, 1)
# #         if(self.client.isElementFound("NATIVE", "xpath=//*[@text='Unable to connect. Please enable WiFi or Mobile Data in your Settings.']", 0, 1)):
# #             logging.info("Verified Network connectivity issue ")
# #         else:
# #             raiseExceptions(" Missing exceptional handling for N/w connectivity issues")
# #         self.client.click("NATIVE", "xpath=//*[@text='Settings']", 0, 1)
# #         self.client.click("NATIVE", "xpath=//*[@text='Data usage']", 0, 1)
# #         self.client.click("NATIVE", "xpath=//*[@id='switch_widget']", 0, 1)
# #         self.client.click("NATIVE", "xpath=//*[@id='navigationBarBackground']", 0, 1)
# #         self.client.click("NATIVE", "xpath=//*[@text='ViewGlass']", 0, 1)
    
    #@attr('acceptance', sid='TC-login-1.5-04', bv=10)
    #@unittest.skip('Test case temporarily disabled') 
    def testUnconfiguredUserInVRM(self):
        """
        Verify the exceptional handling by logging using invalid user
        """
        auth.login(self.client, cfg.users['UserNotConfiguredInVRM']['username'], cfg.users['UserNotConfiguredInVRM']['password'])
        auth.loginScreenValidations(self.client)       
      
    #@attr('acceptance', sid='TC-login-1.5-09', bv=10)
    #@unittest.skip('Test case temporarily disabled')  
    def testNoSiteAssignedForUserInVRM(self):
        """
        Verify the exceptional handling by logging using invalid user
        """
        auth.login(self.client, cfg.users['RO']['username'], cfg.users['RO']['password'])
        auth.signout(self.client)
             
             
    def testSingleSiteUserLogin(self):
        """
        Verify the exceptional handling by logging using invalid user
        """
        auth.login(self.client, cfg.users['RUO']['username'], cfg.users['RUO']['password'])
        self.client.sleep(1000)
        auth.logout(self.client)
         
    #@attr('acceptance', sid='TC-login-1.5-18', bv=10)
    #@unittest.skip('Test case temporarily disabled')     
    def testLogoutFunctionality(self):
        """
        Verify the logout functionality
        """
        auth.login(self.client, cfg.users['RUO']['username'], cfg.users['RUO']['password'])
        self.client.sleep(1000)
        auth.logout(self.client)    
          
              
    def tearDown(self):
        # Generates a report of the test case.
        # For more information - https://docs.experitest.com/display/public/SA/Report+Of+Executed+Test
#         self.client.generateReport2(True);
        # Releases the client so that other clients can approach the agent in the near future. 
        self.client.releaseClient();

if __name__ == '__main__':
    unittest.main()


