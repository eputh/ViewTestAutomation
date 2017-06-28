# -*- coding: utf-8 -*- 
"""
########################################################################
#
# SYNOPSIS
#   LiveView :  Include Test cases related to viewing tint activity throughout
#         the day for CRUDO, RUO, RO privilege users. These activities include
#         Intelligence and Manual adjustments
#
# AUTHOR
#  Emily Puth (emily.puth@viewglass.com)
#
#
# DESCRIPTION
#   Include Test cases related to viewing tint activity for CRUDO, RUO, RO privilege users.
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
from datetime import datetime

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from common import auth
from common import commonFunctions
from common import config
from common import site
from common import control


class LiveView(unittest.TestCase):
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

    # @attr('acceptance', sid=' TC-live-1.1, TC-live-1.4', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def test1VerifyLiveViewUIComponents(self):
        """
        To verify the UI components of the "LiveView screen"
        """
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'CRUDO')
        auth.loginAndSelectSite(self.driver, config.users['CRUDO']['username'], config.users['CRUDO']['password'],
                                config.sites['Default'])
        commonFunctions.navIcon(self.driver)

        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_live_viewTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_live_viewTV").click()
        else:
            raiseExceptions("LiveView option in navigation menu is missing")
        commonFunctions.checkLiveViewAccess(self.driver)

        if WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_LiveViewTV"))):
            pass
        else:
            raiseExceptions("LiveView heading is missing")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/zoneSelector_liveViewTV")) > 0:
            self.driver.find_element_by_id("com.view.viewglass:id/zoneSelector_liveViewTV").click()
            x = self.driver.find_element_by_class_name("android.widget.RelativeLayout").size['width'] + 10
            y = self.driver.find_element_by_class_name("android.widget.RelativeLayout").location['y'] + 10
            self.driver.tap([(x, y)])
        else:
            raiseExceptions("Name of the Zone is missing")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/homeBtnLiveViewLL")) > 0:
            pass
        else:
            raiseExceptions("Navigation icon is missing")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/TimeTempEnergy_liveViewLL")) > 0:
            pass
        else:
            raiseExceptions("Timeline is missing")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/GraphOver")) > 0:
            pass
        else:
            raiseExceptions("Currently applied program is not highlighted")

    # @attr('acceptance', sid='TC-live-1.2', bv=10)
    # unittest.skip('Test case temporarily disabled')
    def testNavigationIcon(self):
        """
        To verify the functionality of "navigation icon" in the upper left corner of the screen
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/title_LiveViewTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_live_viewTV"))):
                self.driver.find_element_by_id("com.view.viewglass:id/navigation_live_viewTV").click()
            else:
                raiseExceptions("LiveView option in navigation menu is missing")

        commonFunctions.navIcon(self.driver)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//android.widget.TextView[@resource-id='com.view.viewglass:id/view_btnTV']")))
        commonFunctions.navIcon(self.driver)

    # @attr('acceptance', sid='TC-live-1.3, TC-live-1.8', bv=10)
    # unittest.skip('Test case temporarily disabled')
    def testZoneNameDropDownList(self):
        """
        To verify the functionality of list of zones when any of the zone is selected
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/title_LiveViewTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_live_viewTV"))):
                self.driver.find_element_by_id("com.view.viewglass:id/navigation_live_viewTV").click()
            else:
                raiseExceptions("LiveView option in navigation menu is missing")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/zoneSelector_liveViewTV")) > 0:
            self.driver.find_element_by_id("com.view.viewglass:id/zoneSelector_liveViewTV").click()
        else:
            raiseExceptions("Zone name drop down menu is missing")

        if len(self.driver.find_elements(By.CLASS_NAME, "android.widget.RelativeLayout")) > 0:
            self.driver.find_element_by_id("com.view.viewglass:id/zoneSelector_liveViewTV").click()
        else:
            self.driver.find_element_by_id("com.view.viewglass:id/zoneSelector_liveViewTV").click()
            raiseExceptions("List of zone names is missing")

    # @attr('acceptance', sid='TC-live-1.5', bv=10)
    # unittest.skip('Test case temporarily disabled')
    def testScrollerAndTintDetails(self):
        """
        To check if the scroller on the arc is moved, then the tint event details also scroll with the time.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/title_LiveViewTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_live_viewTV"))):
                self.driver.find_element_by_id("com.view.viewglass:id/navigation_live_viewTV").click()
            else:
                raiseExceptions("LiveView option in navigation menu is missing")
        commonFunctions.checkLiveViewAccess(self.driver)

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/GraphOver")) > 0:
            self.driver.find_element_by_id("com.view.viewglass:id/GraphOver").click()
        else:
            raiseExceptions("Graph is missing")

        if len(self.driver.find_elements(By.CLASS_NAME, "android.widget.SeekBar")) > 0:
            size = self.driver.find_element_by_class_name("android.widget.SeekBar").size
            location = self.driver.find_element_by_class_name("android.widget.SeekBar").location
            self.driver.swipe(location['x'], location['y'], location['x'] + size['width']/2, location['y'], 3000)
        else:
            raiseExceptions("Seek bar is missing")

    # @attr('acceptance', sid='TC-live-1.6', bv=10)
    # unittest.skip('Test case temporarily disabled')
    def testVerifyTintEventTimes(self):
        """
        To verify if the first tint applied of the day is before 6 am.
        then the last applied tint should be displayed with the time and date.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/title_LiveViewTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_live_viewTV"))):
                self.driver.find_element_by_id("com.view.viewglass:id/navigation_live_viewTV").click()
            else:
                raiseExceptions("LiveView option in navigation menu is missing")
        commonFunctions.checkLiveViewAccess(self.driver)

        format = '%I:%M %p'
        sixAM = datetime.strptime("06:00 AM", format)
        isFirstTintBeforeSix = False
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/time_liveViewTV"))):
            for element in self.driver.find_elements(By.ID, "com.view.viewglass:id/time_liveViewTV"):
                elementsTime = datetime.strptime(element.text, format)
                if elementsTime < sixAM:
                    isFirstTintBeforeSix = True
        else:
            raiseExceptions("Bug: there are no tint activities in the list")

        if not isFirstTintBeforeSix:
            raiseExceptions("Bug: the first tint applied of the day is not before 6 am")

    # @attr('acceptance', sid='TC-live-1.7, TC-live-1.9', bv=10)
    # unittest.skip('Test case temporarily disabled')
    def testUIUpdateAfterApplyingTint(self):
        """
        To apply a tint from UI and check if it is updated on the UI of the LiveView.
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/title_LiveViewTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_live_viewTV"))):
                self.driver.find_element_by_id("com.view.viewglass:id/navigation_live_viewTV").click()
            else:
                raiseExceptions("LiveView option in navigation menu is missing")
        commonFunctions.checkLiveViewAccess(self.driver)

        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_controlTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_controlTV").click()
        else:
            raiseExceptions("Control option in navigation menu is missing")

        # search for a specific zone to cross-check with LiveView (With NC20Test, use Zone1)
        self.driver.find_element_by_id("com.view.viewglass:id/selected_zone_name_controlTV").click()
        self.driver.find_element_by_id("com.view.viewglass:id/search_ImageView").click()
        self.driver.find_element_by_id("com.view.viewglass:id/control_searchETV").send_keys("Zone1")
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Zone1']").click()
        control.selectRandomTint(self.driver)
        commonFunctions.overridebutton(self.driver)
        format = '%I:%M %p'
        now = datetime.now()
        timeOfEventJustAdded = datetime.strftime(now, format)

        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_live_viewTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_live_viewTV").click()
        else:
            raiseExceptions("LiveView option in navigation menu is missing")

        timeOfMostRecentActivity = ""
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/time_liveViewTV"))):
            self.driver.find_elements(By.ID, "com.view.viewglass:id/time_liveViewTV")[0].click()
            timeOfMostRecentActivity = self.driver.find_elements(By.ID, "com.view.viewglass:id/time_liveViewTV")[0].text
        else:
            raiseExceptions("Bug: there are no tint activities in the list")

        if timeOfMostRecentActivity != timeOfEventJustAdded:
            raiseExceptions("Bug: The recently applied tint was not added to the list of tint activities")

    # # @attr('acceptance', sid='TC-live-1.10', bv=10)
    # # unittest.skip('Test case temporarily disabled')
    # def testCorrectReasonAsIntelligence(self):
    #     """
    #     To check reason is coming or not in case of Intelligence.
    #     """
    #     if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/title_LiveViewTV']")) > 0:
    #         self.driver.find_element_by_id("com.view.viewglass:id/title_LiveViewTV'")
    #     else:
    #         commonFunctions.navIcon(self.driver)
    #         self.driver.find_element_by_id("com.view.viewglass:id/navigation_live_viewTV'").click()
    #
    #     if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/liveViewLV']")) > 0:
    #         self.driver.find_element_by_id("com.view.viewglass:id/liveViewLV'")
    #     else:
    #         raiseExceptions("tint event list is missing")
    #
    #     self.driver.elementSwipe("NATIVE", "xpath=//*[@class='android.widget.LinearLayout' and ./*[@id='liveViewLV']]",
    #                              0, "Down", 350, 1000)
    #     self.driver.elementSwipe("NATIVE", "xpath=//*[@class='android.widget.LinearLayout' and ./*[@id='liveViewLV']]",
    #                              0, "Down", 350, 1000)
    #     self.driver.elementSwipe("NATIVE", "xpath=//*[@class='android.widget.LinearLayout' and ./*[@id='liveViewLV']]",
    #                              0, "Down", 350, 1000)
    #     #
    #     # count number of tint events
    #     count = len(self.driver.find_elements(By.ID, "com.view.viewglass:id/time_liveViewTV"))
    #     for i in range(1, count - 1):
    #         if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/time_liveViewTV'[" + str(i) + "]")) > 0:
    #             if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/tintReason_liveViewTV'[" + str(i) + "]")) > 0:
    #                 message = self.driver.find_element_by_id("com.view.viewglass:id/tintReason_liveViewTV'[" + str(i) + "]").text
    #         else:
    #             pass

    def testUIUpdateAfterApplyingSchedule(self):
        """
         Create a schedule from schedule screen and verify the entry  with Schedule in  LiveView
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/title_LiveViewTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_live_viewTV"))):
                self.driver.find_element_by_id("com.view.viewglass:id/navigation_live_viewTV").click()
            else:
                raiseExceptions("LiveView option in navigation menu is missing")
        commonFunctions.checkLiveViewAccess(self.driver)

        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scheduleTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_scheduleTV").click()
        else:
            raiseExceptions("Schedule option in navigation menu is missing")

        startTime = ""
        endTime = ""
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/scheduleTV"))):
            commonFunctions.addbutton(self.driver)
            control.changeTint(self.driver)
            startTime = datetime.strptime(self.driver.find_element_by_id("com.view.viewglass:id/starts_value_schdSceneTintTV").text, '%I:%M %p')
            endTime = datetime.strptime(self.driver.find_element_by_id("com.view.viewglass:id/ends_value_schdSceneTintTV").text, '%I:%M %p')
            commonFunctions.savebutton(self.driver)
        if commonFunctions.foundAlert(self.driver):
            commonFunctions.respondToAlert(self.driver, 1)
            print("Unable to create schedule")
            commonFunctions.goback(self.driver)

        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_live_viewTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_live_viewTV").click()
        else:
            raiseExceptions("LiveView option in navigation menu is missing")

        timeOfMostRecentActivity = ""
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/time_liveViewTV"))):
            timeOfMostRecentActivity = datetime.strptime(self.driver.find_elements(By.ID, "com.view.viewglass:id/time_liveViewTV")[0].text, '%I:%M %p')
        else:
            raiseExceptions("Bug: there are no tint activities in the list")

        if startTime < timeOfMostRecentActivity and timeOfMostRecentActivity < endTime:
            raiseExceptions("Bug: The recently applied tint was not added to the list of tint activities")

    def testUIUpdateAfterApplyingSceneSchedule(self):
        """
         Create a scene schedule from scene screen and  verify the entry with scene schedule in  LiveView
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/title_LiveViewTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_live_viewTV"))):
                self.driver.find_element_by_id("com.view.viewglass:id/navigation_live_viewTV").click()
            else:
                raiseExceptions("LiveView option in navigation menu is missing")
        commonFunctions.checkLiveViewAccess(self.driver)

        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scheduleTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_scheduleTV").click()
        else:
            raiseExceptions("Schedule option in navigation menu is missing")

        startTime = ""
        endTime = ""
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/scheduleTV"))):
            commonFunctions.addbutton(self.driver)
            control.changeTint(self.driver)
            self.driver.find_element_by_id("com.view.viewglass:id/zone_scene_sel_selClsTypeTV").click()
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='SCENE']").click()
            startTime = datetime.strptime(
                self.driver.find_element_by_id("com.view.viewglass:id/starts_value_schdSceneTintTV").text, '%I:%M %p')
            endTime = datetime.strptime(
                self.driver.find_element_by_id("com.view.viewglass:id/ends_value_schdSceneTintTV").text, '%I:%M %p')
            commonFunctions.savebutton(self.driver)
        if commonFunctions.foundAlert(self.driver):
            commonFunctions.respondToAlert(self.driver, 1)
            print("Unable to create scene")
            commonFunctions.goback(self.driver)

        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_live_viewTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_live_viewTV").click()
        else:
            raiseExceptions("LiveView option in navigation menu is missing")

        timeOfMostRecentActivity = ""
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/time_liveViewTV"))):
            self.driver.find_elements(By.ID, "com.view.viewglass:id/time_liveViewTV")[0].click()
            timeOfMostRecentActivity = datetime.strptime(
                self.driver.find_elements(By.ID, "com.view.viewglass:id/time_liveViewTV")[0].text, '%I:%M %p')
        else:
            raiseExceptions("Bug: there are no tint activities in the list")

        if startTime < timeOfMostRecentActivity and timeOfMostRecentActivity < endTime:
            raiseExceptions("Bug: The recently applied tint was not added to the list of tint activities")

    def testAtLeastOneSunriseEntryInUI(self):
        """
        Open any LiveView for zone and verify at least one entry with reason Sunrise is displayed to user
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/title_LiveViewTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_live_viewTV"))):
                self.driver.find_element_by_id("com.view.viewglass:id/navigation_live_viewTV").click()
            else:
                raiseExceptions("LiveView option in navigation menu is missing")
        commonFunctions.checkLiveViewAccess(self.driver)

        hasSunriseEntry = False
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/tintReason_liveViewTV"))):
            for element in self.driver.find_elements(By.ID, "com.view.viewglass:id/tintReason_liveViewTV"):
                if element == "Sunrise":
                    hasSunriseEntry = True
        else:
            raiseExceptions("Bug: there are no tint activities in the list")

        if not hasSunriseEntry:
            raiseExceptions("Bug: No Sunrise entry in UI")

    def testAtLeastOneSunsetEntryInUI(self):
        """
        Open any LiveView for zone and verify at lease one entry with reason Sunset is displayed to user
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/title_LiveViewTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_live_viewTV"))):
                self.driver.find_element_by_id("com.view.viewglass:id/navigation_live_viewTV").click()
            else:
                raiseExceptions("LiveView option in navigation menu is missing")
        commonFunctions.checkLiveViewAccess(self.driver)

        hasSunsetEntry = False
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/tintReason_liveViewTV"))):
            for element in self.driver.find_elements(By.ID, "com.view.viewglass:id/tintReason_liveViewTV"):
                if element == "Sunset":
                    hasSunsetEntry = True
        else:
            raiseExceptions("Bug: there are no tint activities in the list")

        if not hasSunsetEntry:
            raiseExceptions("Bug: No Sunset entry in UI")

    def testDisplayDataEntryAndGraphSync(self):
        """
        Open any LiveView for zone
        click on any entry in LiveView history and according to that information should changed in Graph
        Eg: If user clicks on A20 Zone and selects the 9:35AM entry in table then in graph user should immediately
        see the Tint icon, control,carat icon moved to 9:35 am, reason for Tint and in center of graph time display should e 9:35 am
        """
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/title_LiveViewTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_live_viewTV"))):
                self.driver.find_element_by_id("com.view.viewglass:id/navigation_live_viewTV").click()
            else:
                raiseExceptions("LiveView option in navigation menu is missing")
        commonFunctions.checkLiveViewAccess(self.driver)

        firstActivityTime = ""
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/time_liveViewTV"))):
            self.driver.find_elements(By.ID, "com.view.viewglass:id/time_liveViewTV")[0].click()
            firstActivityTime = self.driver.find_elements(By.ID, "com.view.viewglass:id/time_liveViewTV")[0].text
        else:
            raiseExceptions("Bug: there are no tint activities in the list")

        timeSelectedInGraph = self.driver.find_element_by_id("com.view.viewglass:id/curTimeTV").text
        if timeSelectedInGraph != firstActivityTime:
            raiseExceptions("The Data Entry and Graph are not in sync")

    def testUIUpdateAfterApplyingTintFromWallInterface(self):
        """
        Applied the tint from wall Interface and verify the wall interface entry in  LiveView
        """

    def testUIAccessAfterSunset(self):
        """
        Login to app after sunset time and verify the accessibility of LiveView
        """
        now = datetime.now()
        sunset = datetime.strptime("06:00 PM", '%I:%M %p')
        if now < sunset:
            print("Cannot test because it is not after sunset yet")
        else:
            auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
            if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/title_LiveViewTV")) <= 0:
                commonFunctions.navIcon(self.driver)
                if WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_live_viewTV"))):
                    self.driver.find_element_by_id("com.view.viewglass:id/navigation_live_viewTV").click()
                else:
                    raiseExceptions("LiveView option in navigation menu is missing")

            if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/title_LiveViewTV")) <= 0:
                raiseExceptions("Unable to access LiveView after sunset")

    def testUICaratMoveAfterSunset(self):
        """
        Login to app after sunset time and select the entry after sunset from table and
        verify that user is unable to move carat after sunset but should be able to move carat any
        time between sunrise and sunset for that day
        """
        now = datetime.now()
        sunset = datetime.strptime("06:00 PM", '%I:%M %p')
        if now < sunset:
            print("Cannot test because it is not after sunset yet")
        else:
            auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
            if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/title_LiveViewTV")) <= 0:
                commonFunctions.navIcon(self.driver)
                if WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_live_viewTV"))):
                    self.driver.find_element_by_id("com.view.viewglass:id/navigation_live_viewTV").click()
                else:
                    raiseExceptions("LiveView option in navigation menu is missing")
            commonFunctions.checkLiveViewAccess(self.driver)

            if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/GraphOver")) > 0:
                self.driver.find_element_by_id("com.view.viewglass:id/GraphOver").click()
            else:
                raiseExceptions("Graph is missing")

            if len(self.driver.find_elements(By.CLASS_NAME, "android.widget.SeekBar")) > 0:
                size = self.driver.find_element_by_class_name("android.widget.SeekBar").size
                location = self.driver.find_element_by_class_name("android.widget.SeekBar").location
                self.driver.swipe(location['x'], location['y'], location['x'] + size['width'], location['y'], 3000)
            else:
                raiseExceptions("Seek bar is missing")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LiveView)
    unittest.TextTestRunner(verbosity=2).run(suite)
