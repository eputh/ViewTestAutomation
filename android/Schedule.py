"""
########################################################################
#
# SYNOPSIS
#   Schedule :  Include Test cases related to create, delete , edit, copy schedule for CRUDO, RUO, RO privilege users
#
# AUTHOR
#  Emily Puth (emily.puth@viewglass.com)
#
#
# DESCRIPTION
#   Include Test cases related to create, delete , edit, copy schedule for CRUDO, RUO, RO privilege users.
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
from common import control


class Schedule(unittest.TestCase):

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

    # @attr('acceptance', sid='TC-schedule-1.4, TC-schedule-1.6, TC-tievent-3.3, TC-tievent-3.7, TC-tievent-3.9, TC-tievent-3.10, TC-tievent-3.11, TC-tievent-3.12, TC-tievent-3.13, TC-tievent-3.14', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def test01CreateNoRepeatScheduleForCRUDO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scheduleTV"))):
                self.driver.find_element_by_id("com.view.viewglass:id/navigation_scheduleTV").click()
            else:
                raiseExceptions("Schedule option in navigation menu is missing")

        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/add_schdIV"))):
            commonFunctions.addbutton(self.driver)
        else:
            raiseExceptions("add schedule button is missing")

        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/tint_level_schdSceneTV"))):
            control.changeTint(self.driver)
        else:
            raiseExceptions("change tint option is missing")

        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='Save']"))):
            commonFunctions.savebutton(self.driver)
        else:
            raiseExceptions("add schedule button is missing")

        if commonFunctions.foundAlert(self.driver):
            commonFunctions.respondToAlert(self.driver, 1)
            commonFunctions.goback(self.driver)
            # raiseExceptions("Unable to create schedule")

    # @attr('acceptance', sid='TC-schedule-1.4, TC-schedule-1.6, TC-tievent-3.3, TC-tievent-3.7, TC-tievent-3.9, TC-tievent-3.10, TC-tievent-3.11, TC-tievent-3.12, TC-tievent-3.13, TC-tievent-3.14', bv=10)
    # @unittest.skip('Test case temporarily disabled')         
    def test02EditNoRepeatScheduleForCRUDO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scheduleTV"))):
                self.driver.find_element_by_id("com.view.viewglass:id/navigation_scheduleTV").click()
            else:
                raiseExceptions("Schedule option in navigation menu is missing")

        control.quickCreateSchedule(self.driver)
        schedule = ""
        while schedule == "":
            timeSlots = self.driver.find_elements(By.CLASS_NAME, "android.widget.RelativeLayout")
            for slot in timeSlots:
                if slot.size['height'] > 90:
                    schedule = slot
            if schedule == "" and len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='12AM']")):
                raiseExceptions("Unable to edit a schedule because the schedule is empty")
            elif schedule == "":
                # scroll down to see if there is an event
                location = self.driver.find_element_by_id("com.view.viewglass:id/vLineScroll_schdLL").location
                size = self.driver.find_element_by_id("com.view.viewglass:id/vLineScroll_schdLL").size
                self.driver.swipe(location['x'] + size['width']/2, location['y'], location['x'] + size['width']/2, location['y'] + size['height'], 2000)

        if schedule != "":
            schedule.click()
            commonFunctions.editbutton(self.driver)
            control.changeTint(self.driver)
            commonFunctions.savebutton(self.driver)
        if commonFunctions.foundAlert(self.driver):
            commonFunctions.respondToAlert(self.driver, 1)

    # @attr('acceptance', sid='TC-CTS-7.1, TC-CTS-7.2, TC-CTS-7.1', bv=10)
    # @unittest.skip('Test case temporarily disabled')            
    def test03CopyNoRepeatScheduleForCRUDO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scheduleTV"))):
                self.driver.find_element_by_id("com.view.viewglass:id/navigation_scheduleTV").click()
            else:
                raiseExceptions("Schedule option in navigation menu is missing")

        control.quickCreateSchedule(self.driver)
        schedule = ""
        while schedule == "":
            timeSlots = self.driver.find_elements(By.CLASS_NAME, "android.widget.RelativeLayout")
            for slot in timeSlots:
                if slot.size['height'] > 90:
                    schedule = slot
            if schedule == "" and len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='12AM']")):
                raiseExceptions("Unable to edit a schedule because the schedule is empty")
            elif schedule == "":
                # scroll down to see if there is an event
                location = self.driver.find_element_by_id("com.view.viewglass:id/vLineScroll_schdLL").location
                size = self.driver.find_element_by_id("com.view.viewglass:id/vLineScroll_schdLL").size
                self.driver.swipe(location['x'] + size['width'] / 2, location['y'], location['x'] + size['width'] / 2,
                                  location['y'] + size['height'], 2000)

        if schedule != "":
            schedule.click()
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/copy_schdTintTV")):
            self.driver.find_element_by_id("com.view.viewglass:id/copy_schdTintTV").click()
        WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/copy_tint_eventTV")))
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/copyTint_listItem_radioBtnIV")) > 0:
            firstZonegroup = self.driver.find_elements(By.ID, "com.view.viewglass:id/copyTint_listItem_radioBtnIV")[0]
            firstZonegroup.click()
        else:
            raiseExceptions("There are no zonegroups listed")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/perform_copy_textTV")) > 0:
            self.driver.find_element_by_id("com.view.viewglass:id/perform_copy_textTV").click()
        if commonFunctions.foundAlert(self.driver):
            commonFunctions.respondToAlert(self.driver, 1)
            commonFunctions.goback(self.driver)
        commonFunctions.goback(self.driver)

    # @attr('acceptance', sid='TC-schedule-1.7', bv=10)
    # @unittest.skip('Test case temporarily disabled')              
    def test04DeleteNoRepeatScheduleForCRUDO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1)
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scheduleTV"))):
                self.driver.find_element_by_id("com.view.viewglass:id/navigation_scheduleTV").click()
            else:
                raiseExceptions("Schedule option in navigation menu is missing")

        control.quickCreateSchedule(self.driver)
        schedule = ""
        while schedule == "":
            timeSlots = self.driver.find_elements(By.CLASS_NAME, "android.widget.RelativeLayout")
            for slot in timeSlots:
                if slot.size['height'] > 90:
                    schedule = slot
            if schedule == "" and len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='12AM']")):
                raiseExceptions("Unable to edit a schedule because the schedule is empty")
            elif schedule == "":
                # scroll down to see if there is an event
                location = self.driver.find_element_by_id("com.view.viewglass:id/vLineScroll_schdLL").location
                size = self.driver.find_element_by_id("com.view.viewglass:id/vLineScroll_schdLL").size
                self.driver.swipe(location['x'] + size['width'] / 2, location['y'], location['x'] + size['width'] / 2,
                                  location['y'] + size['height'], 2000)

        if schedule != "":
            control.deleteSchedule(self.driver, schedule)
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='Select Delete Type']")) > 0:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='All Repeated Days']").click()
        else:
            raiseExceptions("Select Delete Type prompt is missing")
        if commonFunctions.foundAlert(self.driver):
            commonFunctions.respondToAlert(self.driver, 1)

    # @attr('acceptance', sid='TC-schedule-1.4, TC-schedule-1.6, TC-tievent-3.3, TC-tievent-3.7, TC-tievent-3.9, TC-tievent-3.10, TC-tievent-3.11, TC-tievent-3.12, TC-tievent-3.13, TC-tievent-3.14', bv=10)
    # @unittest.skip('Test case temporarily disabled')        
    def test05CreateEverydayScheduleForCRUDO(self):
        print
        "(5) Create Everyday Schedule for CRUDO"
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='SCHEDULE']", 0, 30000)):
            self.driver.verifyElementFound("NATIVE", "xpath=//*[@text='SCHEDULE']", 0)
        addbutton(self.driver)
        helperFunctions.changeTint(self.driver)
        helperFunctions.changeRepeat(self.driver, "Everyday")
        savebutton(self.driver)
        if (foundAlert(self.driver)):
            respondToAlert(self.driver, 1)
            goback(self.driver)
            raiseExceptions("unable to create schedule")

    # @attr('acceptance', sid='TC-schedule-1.4, TC-schedule-1.6, TC-tievent-3.3, TC-tievent-3.7, TC-tievent-3.9, TC-tievent-3.10, TC-tievent-3.11, TC-tievent-3.12, TC-tievent-3.13, TC-tievent-3.14', bv=10)
    # @unittest.skip('Test case temporarily disabled')         
    def test06EditEverydayScheduleForCRUDO(self):
        print
        "(6) Edit Everyday Schedule for CRUDO"
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='SCHEDULE']", 0, 30000)):
            self.driver.verifyElementFound("NATIVE", "xpath=//*[@text='SCHEDULE']", 0)

        logging.info("If there is an event, edit the event")
        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                                       0)):
            self.driver.click("NATIVE",
                              "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                              0, 1)
            editbutton(self.driver)
            helperFunctions.changeTint(self.driver)
            savebutton(self.driver)
            if (foundAlert(self.driver)):
                respondToAlert(self.driver, 1)
        else:
            raiseExceptions("unable to find an event to edit")

    # @attr('acceptance', sid='TC-CTS-7.1, TC-CTS-7.2, TC-CTS-7.1', bv=10)
    # @unittest.skip('Test case temporarily disabled')            
    def test07CopyEverydayScheduleForCRUDO(self):
        print
        "(7) Copy Everyday Schedule for CRUDO"
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='SCHEDULE']", 0, 30000)):
            self.driver.verifyElementFound("NATIVE", "xpath=//*[@text='SCHEDULE']", 0)

        logging.info("If there is an event, copy the event")
        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                                       0)):
            self.driver.click("NATIVE",
                              "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                              0, 1)
        else:
            raiseExceptions("unable to find an event to copy")

        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='COPY SCHEDULE EVENT']", 0, 30000)):
            self.driver.click("NATIVE", "xpath=//*[@text='COPY SCHEDULE EVENT']", 0, 1)
        else:
            raiseExceptions("Copy schedule event option not found")

        logging.info("select a zone or zone group to copy the schedule event to")
        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@resource-id='com.view.viewglass:id/copyTint_listItem_radioBtnIV']",
                                       0)):
            self.driver.click("NATIVE", "xpath=//*[@resource-id='com.view.viewglass:id/copyTint_listItem_radioBtnIV']",
                              0, 1)
        else:
            raiseExceptions("Cannot select any zones or zonegroups")

        if (self.driver.isElementFound("NATIVE", "xpath=//*[@text='Perform Copy']", 0)):
            self.driver.click("NATIVE", "xpath=//*[@text='Perform Copy']", 0, 1)
            goback(self.driver)
        else:
            raiseExceptions("Perform Copy button missing or cannot be clicked")

    # @attr('acceptance', sid='TC-schedule-1.7', bv=10)
    # @unittest.skip('Test case temporarily disabled')                
    def test08DeleteEverydayScheduleForCRUDO(self):
        print
        "(8) Delete Everyday Schedule for CRUDO"
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='SCHEDULE']", 0, 30000)):
            self.driver.verifyElementFound("NATIVE", "xpath=//*[@text='SCHEDULE']", 0)

        logging.info("If there is an event, delete the event")
        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                                       0)):
            index = str(int(self.driver.getAllValues("NATIVE",
                                                     "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                                                     "index")[0]) + 1)
        else:
            raiseExceptions("unable to find an event to delete")

        if (self.driver.waitForElement("NATIVE",
                                       "xpath=((//*[@id='main_transp_LL']/*[@class='android.widget.RelativeLayout'])[" + index + "]/*[@class='android.widget.ImageView'])[1]",
                                       0, 30000)):
            self.driver.click("NATIVE",
                              "xpath=((//*[@id='main_transp_LL']/*[@class='android.widget.RelativeLayout'])[" + index + "]/*[@class='android.widget.ImageView'])[1]",
                              0, 1)
            self.driver.click("NATIVE", "xpath=//*[@text='All Repeated Days']", 0, 1)
        else:
            raiseExceptions("delete event icon is missing")

        if (foundAlert(self.driver)):
            respondToAlert(self.driver, 1)

    # @attr('acceptance', sid='TC-schedule-1.4, TC-schedule-1.6, TC-tievent-3.3, TC-tievent-3.7, TC-tievent-3.9, TC-tievent-3.10, TC-tievent-3.11, TC-tievent-3.12, TC-tievent-3.13, TC-tievent-3.14', bv=10)
    # @unittest.skip('Test case temporarily disabled')        
    def test09CreateWeeklyScheduleForCRUDO(self):
        print
        "(9) Create Weekly Schedule for CRUDO"
        addbutton(self.driver)
        helperFunctions.changeTint(self.driver)
        helperFunctions.changeRepeat(self.driver, "Everyday")
        savebutton(self.driver)
        if (foundAlert(self.driver)):
            respondToAlert(self.driver, 1)
            goback(self.driver)
            raiseExceptions("unable to create schedule")
        pass

        # @attr('acceptance', sid='TC-schedule-1.4, TC-schedule-1.6, TC-tievent-3.3, TC-tievent-3.7, TC-tievent-3.9, TC-tievent-3.10, TC-tievent-3.11, TC-tievent-3.12, TC-tievent-3.13, TC-tievent-3.14', bv=10)

    # @unittest.skip('Test case temporarily disabled')         
    def test10EditWeeklyScheduleForCRUDO(self):
        print
        "(10) Edit Weekly Schedule for CRUDO"
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='SCHEDULE']", 0, 30000)):
            self.driver.verifyElementFound("NATIVE", "xpath=//*[@text='SCHEDULE']", 0)

        logging.info("If there is an event, edit the event")
        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                                       0)):
            self.driver.click("NATIVE",
                              "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                              0, 1)
            editbutton(self.driver)
            helperFunctions.changeTint(self.driver)
            savebutton(self.driver)
            if (foundAlert(self.driver)):
                respondToAlert(self.driver, 1)
        else:
            raiseExceptions("unable to find an event to edit")

    # @attr('acceptance', sid='TC-CTS-7.1, TC-CTS-7.2, TC-CTS-7.1', bv=10)
    # @unittest.skip('Test case temporarily disabled')            
    def test11CopyWeeklyScheduleForCRUDO(self):
        print
        "(11) Copy Weekly Schedule for CRUDO"
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='SCHEDULE']", 0, 30000)):
            self.driver.verifyElementFound("NATIVE", "xpath=//*[@text='SCHEDULE']", 0)

        logging.info("If there is an event, copy the event")
        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                                       0)):
            self.driver.click("NATIVE",
                              "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                              0, 1)
        else:
            raiseExceptions("unable to find an event to copy")

        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='COPY SCHEDULE EVENT']", 0, 30000)):
            self.driver.click("NATIVE", "xpath=//*[@text='COPY SCHEDULE EVENT']", 0, 1)
        else:
            raiseExceptions("Copy schedule event option not found")

        logging.info("select a zone or zone group to copy the schedule event to")
        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@resource-id='com.view.viewglass:id/copyTint_listItem_radioBtnIV']",
                                       0)):
            self.driver.click("NATIVE", "xpath=//*[@resource-id='com.view.viewglass:id/copyTint_listItem_radioBtnIV']",
                              0, 1)
        else:
            raiseExceptions("Cannot select any zones or zonegroups")

        if (self.driver.isElementFound("NATIVE", "xpath=//*[@text='Perform Copy']", 0)):
            self.driver.click("NATIVE", "xpath=//*[@text='Perform Copy']", 0, 1)
            goback(self.driver)
        else:
            raiseExceptions("Perform Copy button missing or cannot be clicked")

    # @attr('acceptance', sid='TC-schedule-1.7', bv=10)
    # @unittest.skip('Test case temporarily disabled')                
    def test12DeleteWeeklyScheduleForCRUDO(self):
        print
        "(12) Delete Weekly Schedule for CRUDO"
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='SCHEDULE']", 0, 30000)):
            self.driver.verifyElementFound("NATIVE", "xpath=//*[@text='SCHEDULE']", 0)

        logging.info("If there is an event, delete the event")
        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                                       0)):
            index = str(int(self.driver.getAllValues("NATIVE",
                                                     "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                                                     "index")[0]) + 1)
        else:
            raiseExceptions("unable to find an event to delete")

        if (self.driver.waitForElement("NATIVE",
                                       "xpath=((//*[@id='main_transp_LL']/*[@class='android.widget.RelativeLayout'])[" + index + "]/*[@class='android.widget.ImageView'])[1]",
                                       0, 30000)):
            self.driver.click("NATIVE",
                              "xpath=((//*[@id='main_transp_LL']/*[@class='android.widget.RelativeLayout'])[" + index + "]/*[@class='android.widget.ImageView'])[1]",
                              0, 1)
            self.driver.click("NATIVE", "xpath=//*[@text='All Repeated Days']", 0, 1)
        else:
            raiseExceptions("delete event icon is missing")

        if (foundAlert(self.driver)):
            respondToAlert(self.driver, 1)

    # @attr('acceptance', sid='TC-schedule-1.4, TC-schedule-1.6, TC-tievent-3.3, TC-tievent-3.7, TC-tievent-3.9, TC-tievent-3.10, TC-tievent-3.11, TC-tievent-3.12, TC-tievent-3.13, TC-tievent-3.14', bv=10)
    # @unittest.skip('Test case temporarily disabled')        
    def test13CreateMondayToFridayScheduleForCRUDO(self):
        print
        "(13) Create MondayToFriday Schedule for CRUDO"
        addbutton(self.driver)
        helperFunctions.changeTint(self.driver)
        helperFunctions.changeRepeat(self.driver, "Monday to Friday")
        savebutton(self.driver)
        if (foundAlert(self.driver)):
            respondToAlert(self.driver, 1)
            goback(self.driver)
            raiseExceptions("unable to create schedule")
        pass

        # @attr('acceptance', sid='TC-schedule-1.4, TC-schedule-1.6, TC-tievent-3.3, TC-tievent-3.7, TC-tievent-3.9, TC-tievent-3.10, TC-tievent-3.11, TC-tievent-3.12, TC-tievent-3.13, TC-tievent-3.14', bv=10)

    # @unittest.skip('Test case temporarily disabled')         
    def test14EditMondayToFridayScheduleForCRUDO(self):
        print
        "(14) Edit MondayToFriday Schedule for CRUDO"
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='SCHEDULE']", 0, 30000)):
            self.driver.verifyElementFound("NATIVE", "xpath=//*[@text='SCHEDULE']", 0)

        logging.info("If there is an event, edit the event")
        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                                       0)):
            self.driver.click("NATIVE",
                              "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                              0, 1)
            editbutton(self.driver)
            helperFunctions.changeTint(self.driver)
            savebutton(self.driver)
            if (foundAlert(self.driver)):
                respondToAlert(self.driver, 1)
        else:
            raiseExceptions("unable to find an event to edit")

    # @attr('acceptance', sid='TC-CTS-7.1, TC-CTS-7.2, TC-CTS-7.1', bv=10)
    # @unittest.skip('Test case temporarily disabled')  
    def test15CopyMondayToFridayScheduleForCRUDO(self):
        print
        "(15) Copy MondayToFriday Schedule for CRUDO"
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='SCHEDULE']", 0, 30000)):
            self.driver.verifyElementFound("NATIVE", "xpath=//*[@text='SCHEDULE']", 0)

        logging.info("If there is an event, copy the event")
        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                                       0)):
            self.driver.click("NATIVE",
                              "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                              0, 1)
        else:
            raiseExceptions("unable to find an event to copy")

        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='COPY SCHEDULE EVENT']", 0, 30000)):
            self.driver.click("NATIVE", "xpath=//*[@text='COPY SCHEDULE EVENT']", 0, 1)
        else:
            raiseExceptions("Copy schedule event option not found")

        logging.info("select a zone or zone group to copy the schedule event to")
        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@resource-id='com.view.viewglass:id/copyTint_listItem_radioBtnIV']",
                                       0)):
            self.driver.click("NATIVE", "xpath=//*[@resource-id='com.view.viewglass:id/copyTint_listItem_radioBtnIV']",
                              0, 1)
        else:
            raiseExceptions("Cannot select any zones or zonegroups")

        if (self.driver.isElementFound("NATIVE", "xpath=//*[@text='Perform Copy']", 0)):
            self.driver.click("NATIVE", "xpath=//*[@text='Perform Copy']", 0, 1)
            goback(self.driver)
        else:
            raiseExceptions("Perform Copy button missing or cannot be clicked")

    # @attr('acceptance', sid='TC-schedule-1.7', bv=10)
    # @unittest.skip('Test case temporarily disabled')                
    def test16DeleteMondayToFridayScheduleForCRUDO(self):
        print
        "(16) Delete MondayToFriday Schedule for CRUDO"
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='SCHEDULE']", 0, 30000)):
            self.driver.verifyElementFound("NATIVE", "xpath=//*[@text='SCHEDULE']", 0)

        logging.info("If there is an event, delete the event")
        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                                       0)):
            index = str(int(self.driver.getAllValues("NATIVE",
                                                     "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                                                     "index")[0]) + 1)
        else:
            raiseExceptions("unable to find an event to delete")

        if (self.driver.waitForElement("NATIVE",
                                       "xpath=((//*[@id='main_transp_LL']/*[@class='android.widget.RelativeLayout'])[" + index + "]/*[@class='android.widget.ImageView'])[1]",
                                       0, 30000)):
            self.driver.click("NATIVE",
                              "xpath=((//*[@id='main_transp_LL']/*[@class='android.widget.RelativeLayout'])[" + index + "]/*[@class='android.widget.ImageView'])[1]",
                              0, 1)
            self.driver.click("NATIVE", "xpath=//*[@text='All Repeated Days']", 0, 1)
        else:
            raiseExceptions("delete event icon is missing")

        if (foundAlert(self.driver)):
            respondToAlert(self.driver, 1)

    # @attr('acceptance', sid='TC-schedule-1.3, TC-sedate-2.2, TC-sedate-2.3, TC-sedate-2.4', bv=10)
    # @unittest.skip('Test case temporarily disabled')     
    def test17CalendarIconForRandomDayForCRUDO(self):
        print
        "(17) Select a date to create a schedule for CRUDO"
        today = getToday()
        if (self.driver.waitForElement("NATIVE",
                                       "xpath=//*[@class='android.widget.ImageView' and ./parent::*[@id='calendar_schdLL']]",
                                       0, 10000)):
            self.driver.click("NATIVE",
                              "xpath=//*[@class='android.widget.ImageView' and ./parent::*[@id='calendar_schdLL']]", 0,
                              1)
        else:
            raiseExceptions("calendar icon not found")

        random_date = generateRandomNumber(today, 28)
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='" + random_date + "' and @height>0]", 0, 10000)):
            self.driver.click("NATIVE", "xpath=//*[@text='" + random_date + "' and @height>0]", 0, 1)
        else:
            raiseExceptions("Random day, " + random_date + ", cannot be clicked in the calendar")

    # @attr('acceptance', sid='TC-schedule-1.3, TC-sedate-2.2, TC-sedate-2.3, TC-sedate-2.4', bv=10)
    # @unittest.skip('Test case temporarily disabled')       
    def test18CalendarIconForTodayForCRUDO(self):
        print
        "(18) Select today to create a schedule for CRUDO"
        if (self.driver.waitForElement("NATIVE",
                                       "xpath=//*[@class='android.widget.ImageView' and ./parent::*[@id='calendar_schdLL']]",
                                       0, 10000)):
            self.driver.click("NATIVE",
                              "xpath=//*[@class='android.widget.ImageView' and ./parent::*[@id='calendar_schdLL']]", 0,
                              1)
        else:
            raiseExceptions("calendar icon cannot be found")

        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='Today']", 0, 10000)):
            self.driver.click("NATIVE", "xpath=//*[@text='Today']", 0, 1)
        else:
            raiseExceptions("Today cannot be selected in the calendar")

    # @attr('acceptance', sid='TC-schedule-1.9, TC-schedule-1.10', bv=10)
    # @unittest.skip('Test case temporarily disabled')    
    def test19ShowDefaultSchedulingForCRUDO(self):
        print
        "(19) View default scheduling for CRUDO"
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='Show Default Scheduling']", 0, 20000)):
            self.driver.click("NATIVE", "xpath=//*[@text='Show Default Scheduling']", 0, 1)
        elif (self.driver.waitForElement("NATIVE", "xpath=//*[@id='show_defaultTV']", 0, 20000)):
            self.driver.click("NATIVE", "xpath=//*[@id='show_defaultTV']", 0, 1)
        else:
            raiseExceptions("show default scheduling option is missing")

        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@text='INTELLIGENCE']]",
                                       0)):
            self.driver.verifyElementFound("NATIVE",
                                           "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@text='INTELLIGENCE']]",
                                           0)
        else:
            raiseExceptions("default scheduling is not displayed")

    # @attr('acceptance', sid='TC-schedule-1.9, TC-schedule-1.10', bv=10)
    # @unittest.skip('Test case temporarily disabled')          
    def test20HideDefaultSchedulingForCRUDO(self):
        print
        "(20) Hide default scheduling for CRUDO"
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='Hide Default Scheduling']", 0, 20000)):
            self.driver.click("NATIVE", "xpath=//*[@text='Hide Default Scheduling']", 0, 1)
        elif (self.driver.waitForElement("NATIVE", "xpath=//*[@id='show_defaultTV']", 0, 20000)):
            self.driver.click("NATIVE", "xpath=//*[@id='show_defaultTV']", 0, 1)
        else:
            raiseExceptions("hide default scheduling option is missing")

        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@text='INTELLIGENCE']]",
                                       0)):
            raiseExceptions("default scheduling is still displayed")
        else:
            self.driver.verifyElementNotFound("NATIVE",
                                              "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@text='INTELLIGENCE']]",
                                              0)

    # @attr('acceptance', sid='TC-tievent-3.2, TC-zn/zng-4.5, TC-zn/zng-4.6, TC-zn/zng-4.7', bv=10)
    # @unittest.skip('Test case temporarily disabled')   
    def test21AppliedToForCRUDO(self):
        print
        "(21) Search and select a zone while creating a schedule for CRUDO"
        addbutton(self.driver)
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='Applied to']", 0, 30000)):
            self.driver.click("NATIVE", "xpath=//*[@text='Applied to']", 0, 1)
        elif (self.driver.waitForElement("NATIVE", "xpath=//*[@id='show_defaultTV']", 0, 30000)):
            self.driver.click("NATIVE", "xpath=//*[@id='show_defaultTV']", 0, 1)
        else:
            raiseExceptions("applied to option is missing")

        if (self.driver.waitForElement("NATIVE",
                                       "xpath=//*[@class='android.widget.ImageView' and ./parent::*[@id='searchBtn_allZonesSelectLL']]",
                                       0, 120000)):
            self.driver.click("NATIVE",
                              "xpath=//*[@class='android.widget.ImageView' and ./parent::*[@id='searchBtn_allZonesSelectLL']]",
                              0, 1)
        else:
            raiseExceptions("search button in applied to is missing")

        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='Search']", 0, 30000)):
            self.driver.click("NATIVE", "xpath=//*[@text='Search']", 0, 1)
            self.driver.elementSendText("NATIVE", "xpath=//*[@text='Search']", 0, "emily1")
            self.driver.verifyElementFound("NATIVE", "xpath=//*[@text='emily1']", 0)
        else:
            raiseExceptions("search bar is missing or does not work correctly")

        if (self.driver.isElementFound("NATIVE", "xpath=//*[@text='Cancel']", 0)):
            self.driver.click("NATIVE", "xpath=//*[@text='Cancel']", 0, 1)
        else:
            raiseExceptions("cancel button is not found")

        if (self.driver.waitForElement("NATIVE", "xpath=//*[@id='listitem_ParentLL']", 0, 30000)):
            num_of_zones = self.driver.getElementCount("NATIVE", "xpath=//*[@id='listitem_ParentLL']")
            random_zone = generateRandomNumber(0, num_of_zones - 1)
            self.driver.click("NATIVE",
                              "xpath=(//*[@id='zoneExpand_allZonesSelectELV']/*[@id='listitem_ParentLL'])[" + random_zone + "]",
                              0, 1)
        else:
            raiseExceptions("random zone cannot be selected in Applied To screen")
        goback(self.driver)
        goback(self.driver)

    # @attr('acceptance', sid='TC-schedule-1.4, TC-schedule-1.6, TC-tievent-3.3, TC-tievent-3.7, TC-tievent-3.9, TC-tievent-3.10, TC-tievent-3.11, TC-tievent-3.12, TC-tievent-3.13, TC-tievent-3.14', bv=10)
    # @unittest.skip('Test case temporarily disabled')   
    def test22CreateScheduleWithInvalidInputForCRUDO(self):
        print
        "(22) Create a schedule with invalid input for CRUDO"
        addbutton(self.driver)
        savebutton(self.driver)
        self.driver.verifyElementFound("NATIVE", "xpath=//*[@id='alertDlg_tv_header']", 0)
        respondToAlert(self.driver, 1)
        goback(self.driver)
        auth.logout(self.driver)

    # @attr('acceptance', sid='TC-schedule-1.4, TC-schedule-1.6, TC-tievent-3.3, TC-tievent-3.7, TC-tievent-3.9, TC-tievent-3.10, TC-tievent-3.11, TC-tievent-3.12, TC-tievent-3.13, TC-tievent-3.14', bv=10)
    # @unittest.skip('Test case temporarily disabled')      
    def test23CreateNoRepeatScheduleForRUO(self):
        print
        "(23) Create No Repeat Schedule for RUO"
        logging.info("Login")
        if (self.driver.isElementFound("NATIVE", "xpath=//*[@contentDescription='LOGIN']")):
            auth.login(self.driver, cfg.users['RUO']['username'], cfg.users['RUO']['password'])
        else:
            raiseExceptions("currently not in login screen")

        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='Select Site']", 0, 30000)):
            selectSiteTemp(self.driver, "tintserver7700")
        else:
            raiseExceptions("difficulty logging in")

        if (foundAlert(self.driver)):
            respondToAlert(self.driver, 0)

        if (foundConnectToSiteError(self.driver)):
            self.driver.click("NATIVE", "xpath=//*[@text='Ok']", 0, 1)
            raiseExceptions("unable to connect to site")
        else:
            logging.info("create no repeat schedule")
            self.driver.waitForElement("NATIVE", "xpath=//*[@id='home_controlIV']", 0, 10000)
            commonFunctions.navIcon(self.driver)

        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='SCHEDULE']", 0, 30000)):
            self.driver.verifyElementFound("NATIVE", "xpath=//*[@text='SCHEDULE']", 0)
            self.driver.click("NATIVE", "xpath=//*[@text='SCHEDULE']", 0, 1)
            addbutton(self.driver)
            helperFunctions.changeTint(self.driver)
            savebutton(self.driver)
            if (foundAlert(self.driver)):
                respondToAlert(self.driver, 1)
                goback(self.driver)
                raiseExceptions("unable to create schedule")
        else:
            raiseExceptions("Navigated to wrong screen")

    # @attr('acceptance', sid='TC-schedule-1.4, TC-schedule-1.6, TC-tievent-3.3, TC-tievent-3.7, TC-tievent-3.9, TC-tievent-3.10, TC-tievent-3.11, TC-tievent-3.12, TC-tievent-3.13, TC-tievent-3.14', bv=10)
    # @unittest.skip('Test case temporarily disabled')          
    def test24EditNoRepeatScheduleForRUO(self):
        print
        "(24) Edit No Repeat Schedule for RUO"
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='SCHEDULE']", 0, 30000)):
            self.driver.verifyElementFound("NATIVE", "xpath=//*[@text='SCHEDULE']", 0)

        logging.info("If there is an event, edit the event")
        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                                       0)):
            self.driver.click("NATIVE",
                              "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                              0, 1)
            editbutton(self.driver)
            helperFunctions.changeTint(self.driver)
            savebutton(self.driver)
            if (foundAlert(self.driver)):
                respondToAlert(self.driver, 1)
        else:
            raiseExceptions("unable to find an event to edit")

    # @attr('acceptance', sid='TC-CTS-7.1, TC-CTS-7.2, TC-CTS-7.1', bv=10)
    # @unittest.skip('Test case temporarily disabled')             
    def test25CopyNoRepeatScheduleForRUO(self):
        print
        "(25) Copy No Repeat Schedule for RUO"
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='SCHEDULE']", 0, 30000)):
            self.driver.verifyElementFound("NATIVE", "xpath=//*[@text='SCHEDULE']", 0)

        logging.info("If there is an event, copy the event")
        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                                       0)):
            self.driver.click("NATIVE",
                              "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                              0, 1)
        else:
            raiseExceptions("unable to find an event to copy")

        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='COPY SCHEDULE EVENT']", 0, 30000)):
            self.driver.click("NATIVE", "xpath=//*[@text='COPY SCHEDULE EVENT']", 0, 1)
        else:
            raiseExceptions("Copy schedule event option not found")

        logging.info("select a zone or zone group to copy the schedule event to")
        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@resource-id='com.view.viewglass:id/copyTint_listItem_radioBtnIV']",
                                       0)):
            self.driver.click("NATIVE", "xpath=//*[@resource-id='com.view.viewglass:id/copyTint_listItem_radioBtnIV']",
                              0, 1)
        else:
            raiseExceptions("Cannot select any zones or zonegroups")

        if (self.driver.isElementFound("NATIVE", "xpath=//*[@text='Perform Copy']", 0)):
            self.driver.click("NATIVE", "xpath=//*[@text='Perform Copy']", 0, 1)
            goback(self.driver)
        else:
            raiseExceptions("Perform Copy button missing or cannot be clicked")

    # @attr('acceptance', sid='TC-schedule-1.7', bv=10)
    # @unittest.skip('Test case temporarily disabled')                 
    def test26DeleteNoRepeatScheduleForRUO(self):
        print
        "(26) Delete No Repeat Schedule for RUO"
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='SCHEDULE']", 0, 30000)):
            self.driver.verifyElementFound("NATIVE", "xpath=//*[@text='SCHEDULE']", 0)

        logging.info("If there is an event, delete the event")
        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                                       0)):
            index = str(int(self.driver.getAllValues("NATIVE",
                                                     "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                                                     "index")[0]) + 1)
        else:
            raiseExceptions("unable to find an event to delete")

        if (self.driver.waitForElement("NATIVE",
                                       "xpath=((//*[@id='main_transp_LL']/*[@class='android.widget.RelativeLayout'])[" + index + "]/*[@class='android.widget.ImageView'])[1]",
                                       0, 30000)):
            self.driver.click("NATIVE",
                              "xpath=((//*[@id='main_transp_LL']/*[@class='android.widget.RelativeLayout'])[" + index + "]/*[@class='android.widget.ImageView'])[1]",
                              0, 1)
            self.driver.click("NATIVE", "xpath=//*[@text='All Repeated Days']", 0, 1)
        else:
            raiseExceptions("delete event icon is missing")

        if (foundAlert(self.driver)):
            respondToAlert(self.driver, 1)

    # @attr('acceptance', sid='TC-schedule-1.4, TC-schedule-1.6, TC-tievent-3.3, TC-tievent-3.7, TC-tievent-3.9, TC-tievent-3.10, TC-tievent-3.11, TC-tievent-3.12, TC-tievent-3.13, TC-tievent-3.14', bv=10)
    # @unittest.skip('Test case temporarily disabled')         
    def test27CreateEverydayScheduleForRUO(self):
        print
        "(27) Create Everyday Schedule for RUO"
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='SCHEDULE']", 0, 30000)):
            self.driver.verifyElementFound("NATIVE", "xpath=//*[@text='SCHEDULE']", 0)
        addbutton(self.driver)
        helperFunctions.changeTint(self.driver)
        helperFunctions.changeRepeat(self.driver, "Everyday")
        savebutton(self.driver)
        if (foundAlert(self.driver)):
            respondToAlert(self.driver, 1)
            goback(self.driver)
            raiseExceptions("unable to create schedule")

    # @attr('acceptance', sid='TC-schedule-1.4, TC-schedule-1.6, TC-tievent-3.3, TC-tievent-3.7, TC-tievent-3.9, TC-tievent-3.10, TC-tievent-3.11, TC-tievent-3.12, TC-tievent-3.13, TC-tievent-3.14', bv=10)
    # @unittest.skip('Test case temporarily disabled')          
    def test28EditEverydayScheduleForRUO(self):
        print
        "(28) Edit Everyday Schedule for RUO"
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='SCHEDULE']", 0, 30000)):
            self.driver.verifyElementFound("NATIVE", "xpath=//*[@text='SCHEDULE']", 0)

        logging.info("If there is an event, edit the event")
        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                                       0)):
            self.driver.click("NATIVE",
                              "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                              0, 1)
            editbutton(self.driver)
            helperFunctions.changeTint(self.driver)
            savebutton(self.driver)
            if (foundAlert(self.driver)):
                respondToAlert(self.driver, 1)
        else:
            raiseExceptions("unable to find an event to edit")

    # @attr('acceptance', sid='TC-CTS-7.1, TC-CTS-7.2, TC-CTS-7.1', bv=10)
    # @unittest.skip('Test case temporarily disabled')             
    def test29CopyEverydayScheduleForRUO(self):
        print
        "(29) Copy Everyday Schedule for RUO"
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='SCHEDULE']", 0, 30000)):
            self.driver.verifyElementFound("NATIVE", "xpath=//*[@text='SCHEDULE']", 0)

        logging.info("If there is an event, copy the event")
        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                                       0)):
            self.driver.click("NATIVE",
                              "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                              0, 1)
        else:
            raiseExceptions("unable to find an event to copy")

        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='COPY SCHEDULE EVENT']", 0, 30000)):
            self.driver.click("NATIVE", "xpath=//*[@text='COPY SCHEDULE EVENT']", 0, 1)
        else:
            raiseExceptions("Copy schedule event option not found")

        logging.info("select a zone or zone group to copy the schedule event to")
        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@resource-id='com.view.viewglass:id/copyTint_listItem_radioBtnIV']",
                                       0)):
            self.driver.click("NATIVE", "xpath=//*[@resource-id='com.view.viewglass:id/copyTint_listItem_radioBtnIV']",
                              0, 1)
        else:
            raiseExceptions("Cannot select any zones or zonegroups")

        if (self.driver.isElementFound("NATIVE", "xpath=//*[@text='Perform Copy']", 0)):
            self.driver.click("NATIVE", "xpath=//*[@text='Perform Copy']", 0, 1)
            goback(self.driver)
        else:
            raiseExceptions("Perform Copy button missing or cannot be clicked")

    # @attr('acceptance', sid='TC-schedule-1.7', bv=10)
    # @unittest.skip('Test case temporarily disabled')                 
    def test30DeleteEverydayScheduleForRUO(self):
        print
        "(30) Delete Everyday Schedule for RUO"
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='SCHEDULE']", 0, 30000)):
            self.driver.verifyElementFound("NATIVE", "xpath=//*[@text='SCHEDULE']", 0)

        logging.info("If there is an event, delete the event")
        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                                       0)):
            index = str(int(self.driver.getAllValues("NATIVE",
                                                     "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                                                     "index")[0]) + 1)
        else:
            raiseExceptions("unable to find an event to delete")

        if (self.driver.waitForElement("NATIVE",
                                       "xpath=((//*[@id='main_transp_LL']/*[@class='android.widget.RelativeLayout'])[" + index + "]/*[@class='android.widget.ImageView'])[1]",
                                       0, 30000)):
            self.driver.click("NATIVE",
                              "xpath=((//*[@id='main_transp_LL']/*[@class='android.widget.RelativeLayout'])[" + index + "]/*[@class='android.widget.ImageView'])[1]",
                              0, 1)
            self.driver.click("NATIVE", "xpath=//*[@text='All Repeated Days']", 0, 1)
        else:
            raiseExceptions("delete event icon is missing")

        if (foundAlert(self.driver)):
            respondToAlert(self.driver, 1)

    # @attr('acceptance', sid='TC-schedule-1.4, TC-schedule-1.6, TC-tievent-3.3, TC-tievent-3.7, TC-tievent-3.9, TC-tievent-3.10, TC-tievent-3.11, TC-tievent-3.12, TC-tievent-3.13, TC-tievent-3.14', bv=10)
    # @unittest.skip('Test case temporarily disabled')         
    def test31CreateWeeklyScheduleForRUO(self):
        print
        "(31) Create Weekly Schedule for RUO"
        addbutton(self.driver)
        helperFunctions.changeTint(self.driver)
        helperFunctions.changeRepeat(self.driver, "Everyday")
        savebutton(self.driver)
        if (foundAlert(self.driver)):
            respondToAlert(self.driver, 1)
            goback(self.driver)
            raiseExceptions("unable to create schedule")
        pass

        # @attr('acceptance', sid='TC-schedule-1.4, TC-schedule-1.6, TC-tievent-3.3, TC-tievent-3.7, TC-tievent-3.9, TC-tievent-3.10, TC-tievent-3.11, TC-tievent-3.12, TC-tievent-3.13, TC-tievent-3.14', bv=10)

    # @unittest.skip('Test case temporarily disabled')          
    def test32EditWeeklyScheduleForRUO(self):
        print
        "(32) Edit Weekly Schedule for RUO"
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='SCHEDULE']", 0, 30000)):
            self.driver.verifyElementFound("NATIVE", "xpath=//*[@text='SCHEDULE']", 0)

        logging.info("If there is an event, edit the event")
        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                                       0)):
            self.driver.click("NATIVE",
                              "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                              0, 1)
            editbutton(self.driver)
            helperFunctions.changeTint(self.driver)
            savebutton(self.driver)
            if (foundAlert(self.driver)):
                respondToAlert(self.driver, 1)
        else:
            raiseExceptions("unable to find an event to edit")

    # @attr('acceptance', sid='TC-CTS-7.1, TC-CTS-7.2, TC-CTS-7.1', bv=10)
    # @unittest.skip('Test case temporarily disabled')             
    def test33CopyWeeklyScheduleForRUO(self):
        print
        "(33) Copy Weekly Schedule for RUO"
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='SCHEDULE']", 0, 30000)):
            self.driver.verifyElementFound("NATIVE", "xpath=//*[@text='SCHEDULE']", 0)

        logging.info("If there is an event, copy the event")
        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                                       0)):
            self.driver.click("NATIVE",
                              "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                              0, 1)
        else:
            raiseExceptions("unable to find an event to copy")

        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='COPY SCHEDULE EVENT']", 0, 30000)):
            self.driver.click("NATIVE", "xpath=//*[@text='COPY SCHEDULE EVENT']", 0, 1)
        else:
            raiseExceptions("Copy schedule event option not found")

        logging.info("select a zone or zone group to copy the schedule event to")
        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@resource-id='com.view.viewglass:id/copyTint_listItem_radioBtnIV']",
                                       0)):
            self.driver.click("NATIVE", "xpath=//*[@resource-id='com.view.viewglass:id/copyTint_listItem_radioBtnIV']",
                              0, 1)
        else:
            raiseExceptions("Cannot select any zones or zonegroups")

        if (self.driver.isElementFound("NATIVE", "xpath=//*[@text='Perform Copy']", 0)):
            self.driver.click("NATIVE", "xpath=//*[@text='Perform Copy']", 0, 1)
            goback(self.driver)
        else:
            raiseExceptions("Perform Copy button missing or cannot be clicked")

    # @attr('acceptance', sid='TC-schedule-1.7', bv=10)
    # @unittest.skip('Test case temporarily disabled')                 
    def test34DeleteWeeklyScheduleForRUO(self):
        print
        "(34) Delete Weekly Schedule for RUO"
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='SCHEDULE']", 0, 30000)):
            self.driver.verifyElementFound("NATIVE", "xpath=//*[@text='SCHEDULE']", 0)

        logging.info("If there is an event, delete the event")
        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                                       0)):
            index = str(int(self.driver.getAllValues("NATIVE",
                                                     "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                                                     "index")[0]) + 1)
        else:
            raiseExceptions("unable to find an event to delete")

        if (self.driver.waitForElement("NATIVE",
                                       "xpath=((//*[@id='main_transp_LL']/*[@class='android.widget.RelativeLayout'])[" + index + "]/*[@class='android.widget.ImageView'])[1]",
                                       0, 30000)):
            self.driver.click("NATIVE",
                              "xpath=((//*[@id='main_transp_LL']/*[@class='android.widget.RelativeLayout'])[" + index + "]/*[@class='android.widget.ImageView'])[1]",
                              0, 1)
            self.driver.click("NATIVE", "xpath=//*[@text='All Repeated Days']", 0, 1)
        else:
            raiseExceptions("delete event icon is missing")

        if (foundAlert(self.driver)):
            respondToAlert(self.driver, 1)

    # @attr('acceptance', sid='TC-schedule-1.4, TC-schedule-1.6, TC-tievent-3.3, TC-tievent-3.7, TC-tievent-3.9, TC-tievent-3.10, TC-tievent-3.11, TC-tievent-3.12, TC-tievent-3.13, TC-tievent-3.14', bv=10)
    # @unittest.skip('Test case temporarily disabled')         
    def test35CreateMondayToFridayScheduleForRUO(self):
        print
        "(35) Create MondayToFriday Schedule for RUO"
        addbutton(self.driver)
        helperFunctions.changeTint(self.driver)
        helperFunctions.changeRepeat(self.driver, "Monday to Friday")
        savebutton(self.driver)
        if (foundAlert(self.driver)):
            respondToAlert(self.driver, 1)
            goback(self.driver)
            raiseExceptions("unable to create schedule")
        pass

        # @attr('acceptance', sid='TC-schedule-1.4, TC-schedule-1.6, TC-tievent-3.3, TC-tievent-3.7, TC-tievent-3.9, TC-tievent-3.10, TC-tievent-3.11, TC-tievent-3.12, TC-tievent-3.13, TC-tievent-3.14', bv=10)

    # @unittest.skip('Test case temporarily disabled')          
    def test36EditMondayToFridayScheduleForRUO(self):
        print
        "(36) Edit MondayToFriday Schedule for RUO"
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='SCHEDULE']", 0, 30000)):
            self.driver.verifyElementFound("NATIVE", "xpath=//*[@text='SCHEDULE']", 0)

        logging.info("If there is an event, edit the event")
        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                                       0)):
            self.driver.click("NATIVE",
                              "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                              0, 1)
            editbutton(self.driver)
            helperFunctions.changeTint(self.driver)
            savebutton(self.driver)
            if (foundAlert(self.driver)):
                respondToAlert(self.driver, 1)
        else:
            raiseExceptions("unable to find an event to edit")

    # @attr('acceptance', sid='TC-CTS-7.1, TC-CTS-7.2, TC-CTS-7.1', bv=10)
    # @unittest.skip('Test case temporarily disabled')   
    def test37CopyMondayToFridayScheduleForRUO(self):
        print
        "(37) Copy MondayToFriday Schedule for RUO"
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='SCHEDULE']", 0, 30000)):
            self.driver.verifyElementFound("NATIVE", "xpath=//*[@text='SCHEDULE']", 0)

        logging.info("If there is an event, copy the event")
        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                                       0)):
            self.driver.click("NATIVE",
                              "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                              0, 1)
        else:
            raiseExceptions("unable to find an event to copy")

        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='COPY SCHEDULE EVENT']", 0, 30000)):
            self.driver.click("NATIVE", "xpath=//*[@text='COPY SCHEDULE EVENT']", 0, 1)
        else:
            raiseExceptions("Copy schedule event option not found")

        logging.info("select a zone or zone group to copy the schedule event to")
        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@resource-id='com.view.viewglass:id/copyTint_listItem_radioBtnIV']",
                                       0)):
            self.driver.click("NATIVE", "xpath=//*[@resource-id='com.view.viewglass:id/copyTint_listItem_radioBtnIV']",
                              0, 1)
        else:
            raiseExceptions("Cannot select any zones or zonegroups")

        if (self.driver.isElementFound("NATIVE", "xpath=//*[@text='Perform Copy']", 0)):
            self.driver.click("NATIVE", "xpath=//*[@text='Perform Copy']", 0, 1)
            goback(self.driver)
        else:
            raiseExceptions("Perform Copy button missing or cannot be clicked")

    # @attr('acceptance', sid='TC-schedule-1.7', bv=10)
    # @unittest.skip('Test case temporarily disabled')                 
    def test38DeleteMondayToFridayScheduleForRUO(self):
        print
        "(38) Delete MondayToFriday Schedule for RUO"
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='SCHEDULE']", 0, 30000)):
            self.driver.verifyElementFound("NATIVE", "xpath=//*[@text='SCHEDULE']", 0)

        logging.info("If there is an event, delete the event")
        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                                       0)):
            index = str(int(self.driver.getAllValues("NATIVE",
                                                     "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                                                     "index")[0]) + 1)
        else:
            raiseExceptions("unable to find an event to delete")

        if (self.driver.waitForElement("NATIVE",
                                       "xpath=((//*[@id='main_transp_LL']/*[@class='android.widget.RelativeLayout'])[" + index + "]/*[@class='android.widget.ImageView'])[1]",
                                       0, 30000)):
            self.driver.click("NATIVE",
                              "xpath=((//*[@id='main_transp_LL']/*[@class='android.widget.RelativeLayout'])[" + index + "]/*[@class='android.widget.ImageView'])[1]",
                              0, 1)
            self.driver.click("NATIVE", "xpath=//*[@text='All Repeated Days']", 0, 1)
        else:
            raiseExceptions("delete event icon is missing")

        if (foundAlert(self.driver)):
            respondToAlert(self.driver, 1)

    # @attr('acceptance', sid='TC-schedule-1.3, TC-sedate-2.2, TC-sedate-2.3, TC-sedate-2.4', bv=10)
    # @unittest.skip('Test case temporarily disabled')     
    def test39CalendarIconForRandomDayForRUO(self):
        print
        "(39) Select a date to create a schedule for RUO"
        today = getToday()
        if (self.driver.waitForElement("NATIVE",
                                       "xpath=//*[@class='android.widget.ImageView' and ./parent::*[@id='calendar_schdLL']]",
                                       0, 10000)):
            self.driver.click("NATIVE",
                              "xpath=//*[@class='android.widget.ImageView' and ./parent::*[@id='calendar_schdLL']]", 0,
                              1)
        else:
            raiseExceptions("calendar icon not found")

        random_date = generateRandomNumber(today, 28)
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='" + random_date + "' and @height>0]", 0, 10000)):
            self.driver.click("NATIVE", "xpath=//*[@text='" + random_date + "' and @height>0]", 0, 1)
        else:
            raiseExceptions("Random day, " + random_date + ", cannot be clicked in the calendar")

    # @attr('acceptance', sid='TC-schedule-1.3, TC-sedate-2.2, TC-sedate-2.3, TC-sedate-2.4', bv=10)
    # @unittest.skip('Test case temporarily disabled')       
    def test40CalendarIconForTodayForRUO(self):
        print
        "(40) Select today to create a schedule for RUO"
        if (self.driver.waitForElement("NATIVE",
                                       "xpath=//*[@class='android.widget.ImageView' and ./parent::*[@id='calendar_schdLL']]",
                                       0, 10000)):
            self.driver.click("NATIVE",
                              "xpath=//*[@class='android.widget.ImageView' and ./parent::*[@id='calendar_schdLL']]", 0,
                              1)
        else:
            raiseExceptions("calendar icon cannot be found")

        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='Today']", 0, 10000)):
            self.driver.click("NATIVE", "xpath=//*[@text='Today']", 0, 1)
        else:
            raiseExceptions("Today cannot be selected in the calendar")

    # @attr('acceptance', sid='TC-schedule-1.9, TC-schedule-1.10', bv=10)
    # @unittest.skip('Test case temporarily disabled')     
    def test41ShowDefaultSchedulingForRUO(self):
        print
        "(41) View default scheduling for RUO"
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='Show Default Scheduling']", 0, 20000)):
            self.driver.click("NATIVE", "xpath=//*[@text='Show Default Scheduling']", 0, 1)
        elif (self.driver.waitForElement("NATIVE", "xpath=//*[@id='show_defaultTV']", 0, 20000)):
            self.driver.click("NATIVE", "xpath=//*[@id='show_defaultTV']", 0, 1)
        else:
            raiseExceptions("show default scheduling option is missing")

        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@text='INTELLIGENCE']]",
                                       0)):
            self.driver.verifyElementFound("NATIVE",
                                           "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@text='INTELLIGENCE']]",
                                           0)
        else:
            raiseExceptions("default scheduling is not displayed")

    # @attr('acceptance', sid='TC-schedule-1.9, TC-schedule-1.10', bv=10)
    # @unittest.skip('Test case temporarily disabled')          
    def test42HideDefaultSchedulingForRUO(self):
        print
        "(42) Hide default scheduling for RUO"
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='Hide Default Scheduling']", 0, 20000)):
            self.driver.click("NATIVE", "xpath=//*[@text='Hide Default Scheduling']", 0, 1)
        elif (self.driver.waitForElement("NATIVE", "xpath=//*[@id='show_defaultTV']", 0, 20000)):
            self.driver.click("NATIVE", "xpath=//*[@id='show_defaultTV']", 0, 1)
        else:
            raiseExceptions("hide default scheduling option is missing")

        if (self.driver.isElementFound("NATIVE",
                                       "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@text='INTELLIGENCE']]",
                                       0)):
            raiseExceptions("default scheduling is still displayed")
        else:
            self.driver.verifyElementNotFound("NATIVE",
                                              "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@text='INTELLIGENCE']]",
                                              0)

    # @attr('acceptance', sid='TC-tievent-3.2, TC-zn/zng-4.5, TC-zn/zng-4.6, TC-zn/zng-4.7', bv=10)
    # @unittest.skip('Test case temporarily disabled')     
    def test43AppliedToForRUO(self):
        print
        "(43) Search and select a zone while creating a schedule for RUO"
        addbutton(self.driver)
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='Applied to']", 0, 30000)):
            self.driver.click("NATIVE", "xpath=//*[@text='Applied to']", 0, 1)
        elif (self.driver.waitForElement("NATIVE", "xpath=//*[@id='show_defaultTV']", 0, 30000)):
            self.driver.click("NATIVE", "xpath=//*[@id='show_defaultTV']", 0, 1)
        else:
            raiseExceptions("applied to option is missing")

        if (self.driver.waitForElement("NATIVE",
                                       "xpath=//*[@class='android.widget.ImageView' and ./parent::*[@id='searchBtn_allZonesSelectLL']]",
                                       0, 120000)):
            self.driver.click("NATIVE",
                              "xpath=//*[@class='android.widget.ImageView' and ./parent::*[@id='searchBtn_allZonesSelectLL']]",
                              0, 1)
        else:
            raiseExceptions("search button in applied to is missing")

        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='Search']", 0, 30000)):
            self.driver.click("NATIVE", "xpath=//*[@text='Search']", 0, 1)
            self.driver.elementSendText("NATIVE", "xpath=//*[@text='Search']", 0, "emily1")
            self.driver.verifyElementFound("NATIVE", "xpath=//*[@text='emily1']", 0)
        else:
            raiseExceptions("search bar is missing or does not work correctly")

        if (self.driver.isElementFound("NATIVE", "xpath=//*[@text='Cancel']", 0)):
            self.driver.click("NATIVE", "xpath=//*[@text='Cancel']", 0, 1)
        else:
            raiseExceptions("cancel button is not found")

        if (self.driver.waitForElement("NATIVE", "xpath=//*[@id='listitem_ParentLL']", 0, 30000)):
            num_of_zones = self.driver.getElementCount("NATIVE", "xpath=//*[@id='listitem_ParentLL']")
            random_zone = generateRandomNumber(0, num_of_zones - 1)
            self.driver.click("NATIVE",
                              "xpath=(//*[@id='zoneExpand_allZonesSelectELV']/*[@id='listitem_ParentLL'])[" + random_zone + "]",
                              0, 1)
        else:
            raiseExceptions("random zone cannot be selected in Applied To screen")
        goback(self.driver)
        goback(self.driver)

    # @attr('acceptance', sid='TC-schedule-1.4, TC-schedule-1.6, TC-tievent-3.3, TC-tievent-3.7, TC-tievent-3.9, TC-tievent-3.10, TC-tievent-3.11, TC-tievent-3.12, TC-tievent-3.13, TC-tievent-3.14', bv=10)
    # @unittest.skip('Test case temporarily disabled')    
    def test44CreateScheduleWithInvalidInputForRUO(self):
        print
        "(44) Create a schedule with invalid input for RUO"
        addbutton(self.driver)
        savebutton(self.driver)
        self.driver.verifyElementFound("NATIVE", "xpath=//*[@id='alertDlg_tv_header']", 0)
        respondToAlert(self.driver, 1)
        goback(self.driver)
        auth.logout(self.driver)

    # @attr('acceptance', sid='TC-schedule-1.4, TC-schedule-1.6, TC-tievent-3.3, TC-tievent-3.7, TC-tievent-3.9, TC-tievent-3.10, TC-tievent-3.11, TC-tievent-3.12, TC-tievent-3.13, TC-tievent-3.14', bv=10)
    # @unittest.skip('Test case temporarily disabled')       
    def test45CreateNoRepeatScheduleForRO(self):
        print
        "(45) Create No Repeat Schedule for RO"
        logging.info("Login")
        if (self.driver.isElementFound("NATIVE", "xpath=//*[@contentDescription='LOGIN']")):
            auth.login(self.driver, cfg.users['RO']['username'], cfg.users['RO']['password'])
        else:
            raiseExceptions("currently not in login screen")

        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='Select Site']", 0, 30000)):
            selectSiteTemp(self.driver, "tintserver7700")
        else:
            raiseExceptions("difficulty logging in")

        if (foundAlert(self.driver)):
            respondToAlert(self.driver, 0)

        if (foundConnectToSiteError(self.driver)):
            self.driver.click("NATIVE", "xpath=//*[@text='Ok']", 0, 1)
            raiseExceptions("unable to connect to site")
        else:
            logging.info("create no repeat schedule")
            self.driver.waitForElement("NATIVE", "xpath=//*[@id='home_controlIV']", 0, 10000)
            commonFunctions.navIcon(self.driver)

        if (self.driver.waitForElement("NATIVE", "xpath=//*[@text='SCHEDULE']", 0, 30000)):
            self.driver.verifyElementFound("NATIVE", "xpath=//*[@text='SCHEDULE']", 0)
            self.driver.click("NATIVE", "xpath=//*[@text='SCHEDULE']", 0, 1)
        addbutton(self.driver)
        helperFunctions.changeTint(self.driver)
        savebutton(self.driver)
        if (self.driver.waitForElement("NATIVE", "xpath=//*[@id='home_schdIV']", 0, 30000)):
            self.driver.verifyElementNotFound("NATIVE",
                                              "xpath=//*[@class='android.widget.RelativeLayout' and @height>0 and ./*[@class='android.view.View']]",
                                              0)
        auth.logout(self.driver)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Schedule)
    unittest.TextTestRunner(verbosity=2).run(suite)