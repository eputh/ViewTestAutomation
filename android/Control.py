"""
########################################################################
#
# SYNOPSIS
#   Control :  Include Test cases related to overriding zones to and from tints 1, 2, 3, and 4,
#   canceling override, changing tint duration, and control ring interactions , RUO, RO privilege users
#
# AUTHOR
#  Emily Puth (emily.puth@viewglass.com)
#
#
# DESCRIPTION
#   Include Test cases related to create, delete , edit, copy schedule, etc. for CRUDO, RUO, RO privilege users.
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

from common import auth as auth
from common import commonFunctions as common
from common import control


class Control(unittest.TestCase):
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
        
    """------------------ Control Screen ------------------"""

    # @attr('acceptance', sid=' TC-Control-1.1, TC-Ctrlcnfrm-2.2, TC-ctrltint-5.1', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testControlScreenUIComponents(self):
        """
        To verify the UI components of the "Control screen"
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        print("check control screen components")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/selected_zone_name_controlTV")) > 0:
            self.driver.find_element_by_id("com.view.viewglass:id/selected_zone_name_controlTV")
        else:
            raiseExceptions("Zone group name is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/arcOneSeekBar_controlSA")) > 0:
            self.driver.find_element_by_id("com.view.viewglass:id/arcOneSeekBar_controlSA")
        else:
            raiseExceptions("Tint dial is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/home_controlIV")) > 0:
            self.driver.find_element_by_id("com.view.viewglass:id/home_controlIV")
        else:
            raiseExceptions("Navigation icon is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/flipViewBack_controlLL")) > 0:
            self.driver.find_element_by_id("com.view.viewglass:id/flipViewBack_controlLL")
        else:
            raiseExceptions("Tint image and/or tint number icons are missing")

    # @attr('acceptance', sid='TC-Control-1.2, TC-Ctrlcnfrm-2.4, TC-ctrltint-5.5', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testControlNavigationIcon(self):
        """
        To verify the functionality of "navigation icon" in the upper left corner of the screen
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        common.navIcon(self.driver)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@resource-id='com.view.viewglass:id/view_btnTV']")))
        common.navIcon(self.driver)

    # @attr('acceptance', sid='TC-Control-1.3, TC-Control-1.4, TC-Ctrldial-3.2, TC-ctrltint-5.6', bv=10)
    # @unittest.skip('Test case temporarily disabled') 
    def testSelectZoneGroup(self):
        """
        To verify the functionality of the quick list
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        print("check select zone group")
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@resource-id='com.view.viewglass:id/selected_zone_name_controlTV']")) > 0:
            self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.view.viewglass:id/selected_zone_name_controlTV']").click()
        else:
            raiseExceptions("quick list is missing; unable to select zone group")

        if len(self.driver.find_elements(By.XPATH, "//android.widget.LinearLayout[@resource-id='com.view.viewglass:id/controlMainLL']")) > 0:
            self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.view.viewglass:id/selected_zone_name_controlTV']").click()
        else:
            raiseExceptions("unable to find any zone groups in the list")

    # @attr('acceptance', sid='TC-Control-1.5, TC-Ctrldial-3.1, TC-ctrltint-5.3, TC-ctrltint-5.4', bv=10)
    # @unittest.skip('Test case temporarily disabled') 
    def testControlRing(self):
        """
        Verify the functionality of the Control Ring
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        print("check if the control ring is there and working")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/tintImage_controlIV")) > 0:
            self.driver.find_element_by_id("com.view.viewglass:id/tintImage_controlIV").click()
            self.driver.find_element_by_id("com.view.viewglass:id/tintLevelNum_controlTV")
        elif len(self.driver.find_elements(By.ID, "com.view.viewglass:id/tintLevelNum_controlTV")) > 0:
            self.driver.find_element_by_id("com.view.viewglass:id/tintLevelNum_controlTV").click()
            self.driver.find_element_by_id("com.view.viewglass:id/tintImage_controlIV")
        else:
            raiseExceptions("control ring is missing")

        if common.foundAlert(self.driver):
            common.respondToAlert(self.driver, 1)

    """------------------ tint level 1 ------------------"""

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.2, TC-Ctrldial-3.2', TC-Ctrldial-3.3, TC-Ctrldial-3.4, TC-Ctrldial-3.5', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCancelTint1To2(self):
        """
        To verify the functionality of "Cancel" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)

        print("Cancel a change from tint 1 to tint 2  and verify that the tint is still 1")
        # Check to see if the current tint is at 1
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='1']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 1)
        tint2 = control.getTint2(self.driver)
        self.driver.tap([(tint2[0], tint2[1])])
        common.cancelbutton(self.driver)
        # verify tint is still 1
        control.verifyValidTintFound(self.driver, 1)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.2, TC-Ctrldial-3.2', TC-Ctrldial-3.3, TC-Ctrldial-3.4, TC-Ctrldial-3.5', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCancelTint1To2WithInvalidTints(self):
        """
        To verify the functionality of "Cancel" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)

        print("Cancel a change from tint 1 to tint 2  and verify that the tint is not 2, 3, or 4")
        # Check to see if the current tint is at 1
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='1']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 1)
        tint2 = control.getTint2(self.driver)
        self.driver.tap([(tint2[0], tint2[1])])
        common.cancelbutton(self.driver)
        # verify tint is not 2, 3, or 4
        control.verifyInvalidTintsNotFound(self.driver, 1)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.2, TC-Ctrldial-3.2', TC-Ctrldial-3.3, TC-Ctrldial-3.4, TC-Ctrldial-3.5', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCancelTint1To3(self):
        """
        To verify the functionality of "Cancel" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)

        print("Cancel a change from tint 1 to tint 3  and verify that the tint is still 1")
        # Check to see if the current tint is at 1
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='1']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 1)
        tint3 = control.getTint3(self.driver)
        self.driver.tap([(tint3[0], tint3[1])])
        common.cancelbutton(self.driver)
        # verify tint is still 1
        control.verifyValidTintFound(self.driver, 1)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.2, TC-Ctrldial-3.2', TC-Ctrldial-3.3, TC-Ctrldial-3.4, TC-Ctrldial-3.5', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCancelTint1To3WithInvalidTints(self):
        """
        To verify the functionality of "Cancel" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)

        print(" Cancel a change from tint 1 to tint 3  and verify that the tint is not 2, 3, or 4")
        # Check to see if the current tint is at 1
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='1']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 1)
        tint3 = control.getTint3(self.driver)
        self.driver.tap([(tint3[0], tint3[1])])
        common.cancelbutton(self.driver)
        # verify tint is not 2, 3, or 4
        control.verifyInvalidTintsNotFound(self.driver, 1)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.2, TC-Ctrldial-3.2', TC-Ctrldial-3.3, TC-Ctrldial-3.4, TC-Ctrldial-3.5', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCancelTint1To4(self):
        """
        To verify the functionality of "Cancel" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)

        print("Cancel a change from tint 1 to tint 4  and verify that the tint is still 1")
        # Check to see if the current tint is at 1
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='1']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 1)
        tint4 = control.getTint4(self.driver)
        self.driver.tap([(tint4[0], tint4[1])])
        common.cancelbutton(self.driver)
        # verify tint is still 1
        control.verifyValidTintFound(self.driver, 1)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.2, TC-Ctrldial-3.2', TC-Ctrldial-3.3, TC-Ctrldial-3.4, TC-Ctrldial-3.5', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCancelTint1To4WithInvalidTints(self):
        """
        To verify the functionality of "Cancel" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)

        print(" Cancel a change from tint 1 to tint 4  and verify that the tint is not 2, 3, or 4")
        # Check to see if the current tint is at 1
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='1']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 1)
        tint4 = control.getTint4(self.driver)
        self.driver.tap([(tint4[0], tint4[1])])
        common.cancelbutton(self.driver)
        # verify tint is not 2, 3, or 4
        control.verifyInvalidTintsNotFound(self.driver, 1)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.3', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testOverrideTint1To2(self):
        """
        To verify the functionality of "Override" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)

        print("Override a change from tint 1 to tint 2  and verify that the tint is now 2")
        # Check to see if the current tint is at 1
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='1']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 1)
        control.selectTint(self.driver, 2)
        # verify tint is now 2
        control.verifyValidTintFound(self.driver, 2)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.3', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testOverrideTint1To2WithInvalidTints(self):
        """
        To verify the functionality of "Override" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)

        print("Override a change from tint 1 to tint 2  and verify that the tint is not 1, 3, or 4")
        # Check to see if the current tint is at 1
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='1']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 1)
        control.selectTint(self.driver, 2)
        # verify tint is not 1, 3, or 4
        control.verifyInvalidTintsNotFound(self.driver, 2)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.3', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testOverrideTint1To3(self):
        """
        To verify the functionality of "Override" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)

        print("Override a change from tint 1 to tint 3  and verify that the tint is now 3")
        # Check to see if the current tint is at 1
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='1']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 1)
        control.selectTint(self.driver, 3)
        # verify tint is now 3
        control.verifyValidTintFound(self.driver, 3)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.3', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testOverrideTint1To3WithInvalidTints(self):
        """
        To verify the functionality of "Override" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)

        print("Override a change from tint 1 to tint 3  and verify that the tint is not 1, 2, or 4")
        # Check to see if the current tint is at 1
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='1']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 1)
        control.selectTint(self.driver, 3)
        # verify tint is not 1, 2, or 4
        control.verifyInvalidTintsNotFound(self.driver, 3)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.3', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testOverrideTint1To4(self):
        """
        To verify the functionality of "Override" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)

        print("Override a change from tint 1 to tint 4  and verify that the tint is now 4")
        # Check to see if the current tint is at 1
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='1']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 1)
        control.selectTint(self.driver, 4)
        # verify tint is now 4
        control.verifyValidTintFound(self.driver, 4)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.3', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testOverrideTint1To4WithInvalidTints(self):
        """
        To verify the functionality of "Override" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)

        print("Override a change from tint 1 to tint 4  and verify that the tint is not 1, 2, or 3")
        # Check to see if the current tint is at 1
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='1']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 1)
        control.selectTint(self.driver, 4)
        # verify tint is not 1, 2, or 3
        control.verifyInvalidTintsNotFound(self.driver, 4)

    """------------------ tint level 2 ------------------"""

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.2, TC-Ctrldial-3.2', TC-Ctrldial-3.3, TC-Ctrldial-3.4, TC-Ctrldial-3.5', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCancelTint2To1(self):
        """
        To verify the functionality of "Cancel" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print("Cancel a change from tint 2 to tint 1  and verify that the tint is still 2")
        # Check to see if the current tint is at 2
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='2']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 2)
        tint1 = control.getTint1(self.driver)
        self.driver.tap([(tint1[0], tint1[1])])
        common.cancelbutton(self.driver)
        # verify tint is still 2
        control.verifyInvalidTintsNotFound(self.driver, 2)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.2, TC-Ctrldial-3.2', TC-Ctrldial-3.3, TC-Ctrldial-3.4, TC-Ctrldial-3.5', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCancelTint2To1WithInvalidTints(self):
        """
        To verify the functionality of "Cancel" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print("Cancel a change from tint 2 to tint 1  and verify that the tint is not 1, 3, or 4")
        # Check to see if the current tint is at 2
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//*[@id='tintLevelNum_controlTV' and text='2']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 2)
        tint1 = control.getTint1(self.driver)
        self.driver.tap([(tint1[0], tint1[1])])
        common.cancelbutton(self.driver)
        # verify tint is not 1, 3, or 4
        control.verifyInvalidTintsNotFound(self.driver, 2)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.2, TC-Ctrldial-3.2', TC-Ctrldial-3.3, TC-Ctrldial-3.4, TC-Ctrldial-3.5', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCancelTint2To3(self):
        """
        To verify the functionality of "Cancel" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print("Cancel a change from tint 2 to tint 3  and verify that the tint is still 2")
        # Check to see if the current tint is at 2
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='2']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 2)
        tint3 = control.getTint3(self.driver)
        self.driver.tap([(tint3[0], tint3[1])])
        common.cancelbutton(self.driver)
        # verify tint is still 2
        control.verifyInvalidTintsNotFound(self.driver, 2)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.2, TC-Ctrldial-3.2', TC-Ctrldial-3.3, TC-Ctrldial-3.4, TC-Ctrldial-3.5', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCancelTint2To3WithInvalidTints(self):
        """
        To verify the functionality of "Cancel" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print(" Cancel a change from tint 2 to tint 3  and verify that the tint is not 1, 3, or 4")
        # Check to see if the current tint is at 2
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='2']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 2)
        tint3 = control.getTint3(self.driver)
        self.driver.tap([(tint3[0], tint3[1])])
        common.cancelbutton(self.driver)
        # verify tint is not 1, 3, or 4
        control.verifyInvalidTintsNotFound(self.driver, 2)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.2, TC-Ctrldial-3.2', TC-Ctrldial-3.3, TC-Ctrldial-3.4, TC-Ctrldial-3.5', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCancelTint2To4(self):
        """
        To verify the functionality of "Cancel" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print("Cancel a change from tint 2 to tint 4  and verify that the tint is still 2")
        # Check to see if the current tint is at 2
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='2']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 2)
        tint4 = control.getTint4(self.driver)
        self.driver.tap([(tint4[0], tint4[1])])
        common.cancelbutton(self.driver)
        # verify tint is still 2
        control.verifyInvalidTintsNotFound(self.driver, 2)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.2, TC-Ctrldial-3.2', TC-Ctrldial-3.3, TC-Ctrldial-3.4, TC-Ctrldial-3.5', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCancelTint2To4WithInvalidTints(self):
        """
        To verify the functionality of "Cancel" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print(" Cancel a change from tint 2 to tint 4  and verify that the tint is not 1, 3, or 4")
        # Check to see if the current tint is at 2
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='2']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 2)
        tint4 = control.getTint4(self.driver)
        self.driver.tap([(tint4[0], tint4[1])])
        common.cancelbutton(self.driver)
        # verify tint is not 1, 3, or 4
        control.verifyInvalidTintsNotFound(self.driver, 2)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.3', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testOverrideTint2To1(self):
        """
        To verify the functionality of "Override" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print("Override a change from tint 2 to tint 1  and verify that the tint is now 1")
        # Check to see if the current tint is at 2
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='2']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 2)
        control.selectTint(self.driver, 1)
        # verify tint is now 1
        control.verifyInvalidTintsNotFound(self.driver, 1)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.3', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testOverrideTint2To1WithInvalidTints(self):
        """
        To verify the functionality of "Override" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print("Override a change from tint 2 to tint 1  and verify that the tint is not 2, 3, or 4")
        # Check to see if the current tint is at 2
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='2']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 2)
        control.selectTint(self.driver, 1)
        # verify tint is not 2, 3, or 4
        control.verifyInvalidTintsNotFound(self.driver, 1)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.3', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testOverrideTint2To3(self):
        """
        To verify the functionality of "Override" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print("Override a change from tint 2 to tint 3  and verify that the tint is now 3")
        # Check to see if the current tint is at 2
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='2']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 2)
        control.selectTint(self.driver, 3)
        # verify tint is now 3
        control.verifyInvalidTintsNotFound(self.driver, 3)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.3', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testOverridetint2To3WithInvalidTints(self):
        """
        To verify the functionality of "Override" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print("Override a change from tint 2 to tint 3  and verify that the tint is not 1, 2, or 4")
        # Check to see if the current tint is at 2
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='2']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 2)
        control.selectTint(self.driver, 3)

        # verify tint is not 1, 2, or 4
        control.verifyInvalidTintsNotFound(self.driver, 3)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.3', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testOverridetint2To4(self):
        """
        To verify the functionality of "Override" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print("Override a change from tint 2 to tint 4  and verify that the tint is now 4")
        # Check to see if the current tint is at 2
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='2']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 2)
        control.selectTint(self.driver, 4)
        # verify tint is now 4
        control.verifyInvalidTintsNotFound(self.driver, 4)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.3', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testOverridetint2To4WithInvalidTints(self):
        """
        To verify the functionality of "Override" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print("Override a change from tint 2 to tint 4  and verify that the tint is not 1, 2, or 3")
        # Check to see if the current tint is at 2
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='2']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 2)
        control.selectTint(self.driver, 4)
        # verify tint is not 1, 2, or 3
        control.verifyInvalidTintsNotFound(self.driver, 4)

    """------------------ tint level 3 ------------------"""

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.2, TC-Ctrldial-3.2', TC-Ctrldial-3.3, TC-Ctrldial-3.4, TC-Ctrldial-3.5', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCancelTint3To2(self):
        """
        To verify the functionality of "Cancel" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print("Cancel a change from tint 3 to tint 2  and verify that the tint is still 3")
        # Check to see if the current tint is at 3
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='3']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 3)
        tint2 = control.getTint2(self.driver)
        self.driver.tap([(tint2[0], tint2[1])])
        common.cancelbutton(self.driver)
        # verify tint is still 3
        control.verifyInvalidTintsNotFound(self.driver, 3)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.2, TC-Ctrldial-3.2', TC-Ctrldial-3.3, TC-Ctrldial-3.4, TC-Ctrldial-3.5', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCancelTint3To2WithInvalidTints(self):
        """
        To verify the functionality of "Cancel" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print("Cancel a change from tint 3 to tint 2  and verify that the tint is not 1, 2, or 4")
        # Check to see if the current tint is at 3
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='3']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 3)
        tint2 = control.getTint2(self.driver)
        self.driver.tap([(tint2[0], tint2[1])])
        common.cancelbutton(self.driver)
        # verify tint is not 1, 2, or 4
        control.verifyInvalidTintsNotFound(self.driver, 3)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.2, TC-Ctrldial-3.2', TC-Ctrldial-3.3, TC-Ctrldial-3.4, TC-Ctrldial-3.5', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCancelTint3To1(self):
        """
        To verify the functionality of "Cancel" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print("Cancel a change from tint 3 to tint 1  and verify that the tint is still 3")
        # Check to see if the current tint is at 3
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='3']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 3)
        tint1 = control.getTint1(self.driver)
        self.driver.tap([(tint1[0], tint1[1])])
        common.cancelbutton(self.driver)
        # verify tint is still 3
        control.verifyInvalidTintsNotFound(self.driver, 3)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.2, TC-Ctrldial-3.2', TC-Ctrldial-3.3, TC-Ctrldial-3.4, TC-Ctrldial-3.5', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCancelTint3To1WithInvalidTints(self):
        """
        To verify the functionality of "Cancel" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print(" Cancel a change from tint 3 to tint 1  and verify that the tint is not 1, 2, or 4")
        # Check to see if the current tint is at 3
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='3']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 3)
        tint1 = control.getTint1(self.driver)
        self.driver.tap([(tint1[0], tint1[1])])
        common.cancelbutton(self.driver)
        # verify tint is not 1, 2, or 4
        control.verifyInvalidTintsNotFound(self.driver, 3)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.2, TC-Ctrldial-3.2', TC-Ctrldial-3.3, TC-Ctrldial-3.4, TC-Ctrldial-3.5', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCancelTint3To4(self):
        """
        To verify the functionality of "Cancel" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print()
        # Check to see if the current tint is at 3
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='3']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 3)
        tint4 = control.getTint4(self.driver)
        self.driver.tap([(tint4[0], tint4[1])])
        common.cancelbutton(self.driver)
        # verify tint is still 3
        control.verifyInvalidTintsNotFound(self.driver, 3)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.2, TC-Ctrldial-3.2', TC-Ctrldial-3.3, TC-Ctrldial-3.4, TC-Ctrldial-3.5', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCancelTint3To4WithInvalidTints(self):
        """
        To verify the functionality of "Cancel" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print(" Cancel a change from tint 3 to tint 4  and verify that the tint is not 1, 2, or 4")
        # Check to see if the current tint is at 3
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='3']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 3)
        tint4 = control.getTint4(self.driver)
        self.driver.tap([(tint4[0], tint4[1])])
        common.cancelbutton(self.driver)
        # verify tint is not 1, 2, or 4
        control.verifyInvalidTintsNotFound(self.driver, 3)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.3', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testOverrideTint3To1(self):
        """
        To verify the functionality of "Override" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print("Override a change from tint 3 to tint 1  and verify that the tint is now 1")
        # Check to see if the current tint is at 3
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='3']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 3)
        control.selectTint(self.driver, 1)
        # verify tint is now 1
        control.verifyInvalidTintsNotFound(self.driver, 1)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.3', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testOverrideTint3To1WithInvalidTints(self):
        """
        To verify the functionality of "Override" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print("Override a change from tint 3 to tint 1  and verify that the tint is not 2, 3, or 4")
        # Check to see if the current tint is at 3
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='3']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 3)
        control.selectTint(self.driver, 1)
        # verify tint is not 2, 3, or 4
        control.verifyInvalidTintsNotFound(self.driver, 1)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.3', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testOverrideTint3To2(self):
        """
        To verify the functionality of "Override" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print("Override a change from tint 3 to tint 2  and verify that the tint is now 2")
        # Check to see if the current tint is at 3
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='3']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 3)
        control.selectTint(self.driver, 2)
        # verify tint is now 2
        control.verifyInvalidTintsNotFound(self.driver, 2)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.3', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testOverrideTint3To2WithInvalidTints(self):
        """
        To verify the functionality of "Override" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print("Override a change from tint 3 to tint 2  and verify that the tint is not 1, 3, or 4")
        # Check to see if the current tint is at 3
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='3']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 3)
        control.selectTint(self.driver, 2)
        # verify tint is not 1, 3, or 4
        control.verifyInvalidTintsNotFound(self.driver, 2)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.3', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testOverrideTint3To4(self):
        """
        To verify the functionality of "Override" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print("Override a change from tint 3 to tint 4  and verify that the tint is now 4")
        # Check to see if the current tint is at 3
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='3']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 3)
        control.selectTint(self.driver, 4)
        # verify tint is now 4
        control.verifyInvalidTintsNotFound(self.driver, 4)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.3', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testOverrideTint3To4WithInvalidTints(self):
        """
        To verify the functionality of "Override" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print("Override a change from tint 3 to tint 4  and verify that the tint is not 1, 2, or 3")
        # Check to see if the current tint is at 3
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='3']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 3)
        control.selectTint(self.driver, 4)
        # verify tint is not 1, 2, or 3
        control.verifyInvalidTintsNotFound(self.driver, 4)

    """------------------ tint level 4 ------------------"""

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.2, TC-Ctrldial-3.2', TC-Ctrldial-3.3, TC-Ctrldial-3.4, TC-Ctrldial-3.5', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCancelTint4To2(self):
        """
        To verify the functionality of "Cancel" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print("Cancel a change from tint 4 to tint 2  and verify that the tint is still 4")
        # Check to see if the current tint is at 4
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='4']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 4)
        tint2 = control.getTint2(self.driver)
        self.driver.tap([(tint2[0], tint2[1])])
        common.cancelbutton(self.driver)
        # verify tint is still 4
        control.verifyInvalidTintsNotFound(self.driver, 4)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.2, TC-Ctrldial-3.2', TC-Ctrldial-3.3, TC-Ctrldial-3.4, TC-Ctrldial-3.5', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCancelTint4To2WithInvalidTints(self):
        """
        To verify the functionality of "Cancel" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print("Cancel a change from tint 4 to tint 2  and verify that the tint is not 1, 2, or 3")
        # Check to see if the current tint is at 4
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='4']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 4)
        tint2 = control.getTint2(self.driver)
        self.driver.tap([(tint2[0], tint2[1])])
        common.cancelbutton(self.driver)
        # verify tint is not 1, 2, or 3
        control.verifyInvalidTintsNotFound(self.driver, 4)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.2, TC-Ctrldial-3.2', TC-Ctrldial-3.3, TC-Ctrldial-3.4, TC-Ctrldial-3.5', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCancelTint4To3(self):
        """
        To verify the functionality of "Cancel" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print("Cancel a change from tint 4 to tint 3  and verify that the tint is still 4")
        # Check to see if the current tint is at 4
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='4']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 4)
        tint3 = control.getTint3(self.driver)
        self.driver.tap([(tint3[0], tint3[1])])
        common.cancelbutton(self.driver)
        # verify tint is still 4
        control.verifyInvalidTintsNotFound(self.driver, 4)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.2, TC-Ctrldial-3.2', TC-Ctrldial-3.3, TC-Ctrldial-3.4, TC-Ctrldial-3.5', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCancelTint4To3WithInvalidTints(self):
        """
        To verify the functionality of "Cancel" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print(" Cancel a change from tint 4 to tint 3  and verify that the tint is not 1, 2, or 3")
        # Check to see if the current tint is at 4
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='4']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 4)
        tint3 = control.getTint3(self.driver)
        self.driver.tap([(tint3[0], tint3[1])])
        common.cancelbutton(self.driver)
        # verify tint is not 1, 2, or 3
        control.verifyInvalidTintsNotFound(self.driver, 4)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.2, TC-Ctrldial-3.2', TC-Ctrldial-3.3, TC-Ctrldial-3.4, TC-Ctrldial-3.5', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCancelTint41To1(self):
        """
        To verify the functionality of "Cancel" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print("Cancel a change from tint 4 to tint 1  and verify that the tint is still 4")
        # Check to see if the current tint is at 4
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='4']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 4)
        tint1 = control.getTint1(self.driver)
        self.driver.tap([(tint1[0], tint1[1])])
        common.cancelbutton(self.driver)
        # verify tint is still 4
        control.verifyInvalidTintsNotFound(self.driver, 4)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.2, TC-Ctrldial-3.2', TC-Ctrldial-3.3, TC-Ctrldial-3.4, TC-Ctrldial-3.5', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCancelTint4To1WithInvalidTints(self):
        """
        To verify the functionality of "Cancel" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print(" Cancel a change from tint 4 to tint 1  and verify that the tint is not 1, 2, or 3")
        # Check to see if the current tint is at 4
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='4']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 4)
        tint1 = control.getTint1(self.driver)
        self.driver.tap([(tint1[0], tint1[1])])
        common.cancelbutton(self.driver)
        # verify tint is not 1, 2, or 3
        control.verifyInvalidTintsNotFound(self.driver, 4)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.3', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testOverrideTint4To1(self):
        """
        To verify the functionality of "Override" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print("Override a change from tint 4 to tint 1  and verify that the tint is now 1")
        # Check to see if the current tint is at 4
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='4']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 4)
        control.selectTint(self.driver, 1)
        # verify tint is now 1
        control.verifyInvalidTintsNotFound(self.driver, 1)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.3', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testOverrideTint4To1WithInvalidTints(self):
        """
        To verify the functionality of "Override" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print("Override a change from tint 4 to tint 1  and verify that the tint is not 2, 3, or 4")
        # Check to see if the current tint is at 4
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='4']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 4)
        control.selectTint(self.driver, 1)
        # verify tint is not 2, 3, or 4
        control.verifyInvalidTintsNotFound(self.driver, 1)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.3', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testOverrideTint4To2(self):
        """
        To verify the functionality of "Override" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print("Override a change from tint 4 to tint 2  and verify that the tint is now 4")
        # Check to see if the current tint is at 4
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='4']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 4)
        control.selectTint(self.driver, 2)
        # verify tint is now 2
        control.verifyInvalidTintsNotFound(self.driver, 2)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.3', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testOverrideTint4To2WithInvalidTints(self):
        """
        To verify the functionality of "Override" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print("Override a change from tint 4 to tint 2  and verify that the tint is not 1, 3, or 4")
        # Check to see if the current tint is at 4
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='4']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 4)
        control.selectTint(self.driver, 2)
        # verify tint is not 1, 3, or 4
        control.verifyInvalidTintsNotFound(self.driver, 2)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.3', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testOverrideTint4To3(self):
        """
        To verify the functionality of "Override" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print("Override a change from tint 4 to tint 3  and verify that the tint is now 3")
        # Check to see if the current tint is at 4
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='4']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 4)
        control.selectTint(self.driver, 3)
        # verify tint is now 3
        control.verifyInvalidTintsNotFound(self.driver, 3)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.3', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testOverrideTint4To3WithInvalidTints(self):
        """
        To verify the functionality of "Override" button.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print("Override a change from tint 4 to tint 3  and verify that the tint is not 1, 2, or 4")
        # Check to see if the current tint is at 4
        control.clickTintLevelNum(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='4']")) > 0:
            pass
        else:
            control.selectTint(self.driver, 4)
        control.selectTint(self.driver, 3)
        # verify tint is not 1, 2, or 4
        control.verifyInvalidTintsNotFound(self.driver, 3)

    """------------------ Control Tint Duration Screen ------------------"""

    # @attr('acceptance', sid='TC-duratn-4.1, ', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testTintDurationUIComponents(self):
        """
        To verify the UI components of "Tint Duration" screen.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print("check tint duration UI components")
        tint1 = control.getTint1(self.driver)
        self.driver.tap([(tint1[0], tint1[1])])
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/time_remaining_controlLL")) > 0:
            self.driver.find_element_by_id("com.view.viewglass:id/time_remaining_controlLL").click()
        else:
            raiseExceptions("tint duration button is missing")
        # if len(self.driver.find_elements(By.XPATH, "//*[@id='home_controlIV']")) > 0:
        #             (self.driver.find_element_by_xpath("//*[@id='home_controlIV']")).is_displayed()
        #         else:
        #             common.cancelbutton(self.driver)
        #             raiseExceptions("navigation icon is missing")
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='TINT DURATION']")) > 0:
            assert len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='TINT DURATION']")) > 0, "missing Tint Duration heading"
        else:
            common.cancelbutton(self.driver)
            raiseExceptions("tint duration heading is missing")
        if len(self.driver.find_elements(By.XPATH, "//android.widget.NumberPicker[@index='0']")) > 0:
            assert len(self.driver.find_elements(By.XPATH, "//android.widget.NumberPicker[@index='1']")) > 0, "missing number picker"
        else:
            common.cancelbutton(self.driver)
            raiseExceptions("tint number picker is missing")
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='CANCEL']")) > 0:
            assert len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='CANCEL']")) > 0, "missing cancel button"
        else:
            common.cancelbutton(self.driver)
            raiseExceptions("cancel button is missing")
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='OVERRIDE']")) > 0:
            assert len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='OVERRIDE']")) > 0, "missing override button"
        else:
            common.cancelbutton(self.driver)
            raiseExceptions("override button is missing")
        common.cancelbutton(self.driver)

    # @attr('acceptance', sid='TC-Ctrlcnfrm-2.5, TC-duratn-4.2, TC-duratn-4.3, TC-duratn-4.4', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testTimeSelection(self):
        """
        To verify the functionality of time selection.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        
        print("check time selection functionality")
        tint1 = control.getTint1(self.driver)
        self.driver.tap([(tint1[0], tint1[1])])
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/time_remaining_controlLL")) > 0:
            self.driver.find_element_by_id("com.view.viewglass:id/time_remaining_controlLL").click()
        else:
            raiseExceptions("tint duration button is missing")

        if len(self.driver.find_elements(By.XPATH, "//android.widget.NumberPicker[@index='0']")) > 0:
           self.driver.find_element_by_xpath("//android.widget.EditText[@index='1']").send_keys('2 Hrs')
        else:
            raiseExceptions("hour number picker is missing")
        if len(self.driver.find_elements(By.XPATH, "//android.widget.NumberPicker[@index='1']")) > 0:
            self.driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys('15 Mins')
        else:
            raiseExceptions("minute number picker is missing")

        hours = self.driver.find_element_by_xpath("//android.widget.EditText[@index='1']").text
        minutes = self.driver.find_element_by_xpath("//android.widget.EditText[@index='0']").text
        minutesSplit = minutes.split(" ")
        minutes = str(int(minutesSplit[0]) - 1) + " " + minutesSplit[1]
        common.overridebutton(self.driver)
        if len(self.driver.find_elements(By.XPATH, "//*[@id='timeRemaining_controlTV']")) > 0:
            (self.driver.find_element_by_xpath("//*[@text='" + hours + " " + minutes + "']")).is_displayed()

    # @attr('acceptance', sid='TC-ctrltint-5.7, TC-ctrltint-5.8', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCancelOverride(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1)

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/clear_quick_control_requestsLL")) > 0:
            pass
        else:
            currentTint = control.getCurrentTint(self.driver)
            control.selectTint(self.driver, currentTint)
        currentTint = control.getCurrentTint(self.driver)
        control.selectRandomTint(self.driver)

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/clear_quick_control_requestsLL")) > 0:
            self.driver.find_element_by_id("com.view.viewglass:id/clear_quick_control_requestsLL").click()
        else:
            raiseExceptions("Cancel override button is missing")
        if common.foundAlert(self.driver):
            common.respondToAlert(self.driver, 1)

        newTint = control.getCurrentTint(self.driver)
        if currentTint == newTint:
            pass
        else:
            raiseExceptions("cancel override did not return to previous tint")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Control)
    unittest.TextTestRunner(verbosity=2).run(suite)