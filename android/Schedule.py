"""
########################################################################
#
# SYNOPSIS
#   Schedule :  Include Test cases related to creating, deleting, editing, and copying schedules for CRUDO, RUO, RO privilege users
#
# AUTHOR
#  Emily Puth (emily.puth@viewglass.com)
#
#
# DESCRIPTION
#   Include Test cases related to creating, deleting, editing, and copying schedules for CRUDO, RUO, RO privilege users.
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

    # @attr('acceptance', sid='TC-schedule-1.4, TC-schedule-1.6, TC-tievent-3.3, TC-tievent-3.7, TC-tievent-3.9, TC-tievent-3.10, TC-tievent-3.11, TC-tievent-3.12, TC-tievent-3.13, TC-tievent-3.14', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def test01CreateNoRepeatScheduleForCRUDO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'CRUDO')
        auth.loginAndSelectSite(self.driver, config.users['CRUDO']['username'], config.users['CRUDO']['password'],
                                config.site[0])

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
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
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
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
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
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
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
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
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
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
            control.changeRepeat(self.driver, "Everyday")
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

    # @attr('acceptance', sid='TC-schedule-1.7', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def test06DeleteEverydayScheduleForCRUDO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
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
    def test07CreateWeeklyScheduleForCRUDO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
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
            control.changeRepeat(self.driver, "Weekly")
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

    # @attr('acceptance', sid='TC-schedule-1.7', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def test08DeleteWeeklyScheduleForCRUDO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
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
    def test09CreateMondayToFridayScheduleForCRUDO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
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
            control.changeRepeat(self.driver, "Monday to Friday")
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

    # @attr('acceptance', sid='TC-schedule-1.7', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def test10DeleteMondayToFridayScheduleForCRUDO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
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

    # @attr('acceptance', sid='TC-schedule-1.3, TC-sedate-2.2, TC-sedate-2.3, TC-sedate-2.4', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def test11CalendarIconForRandomDayForCRUDO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
                    EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scheduleTV"))):
                self.driver.find_element_by_id("com.view.viewglass:id/navigation_scheduleTV").click()
            else:
                raiseExceptions("Schedule option in navigation menu is missing")

        today = commonFunctions.getToday()
        if WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "com.view.viewglass:id/calendar_schdLL"))):
            self.driver.find_element_by_id("com.view.viewglass:id/calendar_schdLL").click()
        else:
            raiseExceptions("calendar icon is missing")

        random_date = commonFunctions.generateRandomNumber(today, 28)
        if WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='" + random_date + "']"))):
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='" + random_date + "']").click()
        else:
            raiseExceptions("Random day, " + random_date + ", cannot be clicked in the calendar")

    # @attr('acceptance', sid='TC-schedule-1.3, TC-sedate-2.2, TC-sedate-2.3, TC-sedate-2.4', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def test12CalendarIconForTodayForCRUDO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
                    EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scheduleTV"))):
                self.driver.find_element_by_id("com.view.viewglass:id/navigation_scheduleTV").click()
            else:
                raiseExceptions("Schedule option in navigation menu is missing")

        today = commonFunctions.getToday()
        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/calendar_schdLL"))):
            self.driver.find_element_by_id("com.view.viewglass:id/calendar_schdLL").click()
        else:
            raiseExceptions("calendar icon is missing")

        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/todayBtn_calTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/todayBtn_calTV").click()
        else:
            raiseExceptions("Today button is missing")

    # @attr('acceptance', sid='TC-schedule-1.9, TC-schedule-1.10', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def test13ShowDefaultSchedulingForCRUDO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
                    EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scheduleTV"))):
                self.driver.find_element_by_id("com.view.viewglass:id/navigation_scheduleTV").click()
            else:
                raiseExceptions("Schedule option in navigation menu is missing")

        if WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@text='Show Default Scheduling']"))):
            self.driver.find_element_by_xpath("//*[@text='Show Default Scheduling']").click()
        elif WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='show_defaultTV']"))):
            self.driver.find_element_by_xpath("//*[@id='show_defaultTV']").click()
        else:
            raiseExceptions("show default scheduling option is missing")

        hasFoundIntelligence = False
        while not hasFoundIntelligence:
            if not hasFoundIntelligence and len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='12AM']")) > 0:
                raiseExceptions("Intelligence icon for Default Scheduling is missing")
            elif len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='INTELLIGENCE']")) > 0:
                hasFoundIntelligence = True
            else:
                # scroll down to see if there is an event
                location = self.driver.find_element_by_id("com.view.viewglass:id/vLineScroll_schdLL").location
                size = self.driver.find_element_by_id("com.view.viewglass:id/vLineScroll_schdLL").size
                self.driver.swipe(location['x'] + size['width'] / 2, location['y'], location['x'] + size['width'] / 2,
                                  location['y'] + size['height'], 2000)

    # @attr('acceptance', sid='TC-schedule-1.9, TC-schedule-1.10', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def test14HideDefaultSchedulingForCRUDO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
                    EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scheduleTV"))):
                self.driver.find_element_by_id("com.view.viewglass:id/navigation_scheduleTV").click()
            else:
                raiseExceptions("Schedule option in navigation menu is missing")

        if WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@text='Show Default Scheduling']"))):
            self.driver.find_element_by_xpath("//*[@text='Show Default Scheduling']").click()
        elif WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='show_defaultTV']"))):
            self.driver.find_element_by_xpath("//*[@id='show_defaultTV']").click()
        else:
            raiseExceptions("show default scheduling option is missing")

        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//*[@text='Hide Default Scheduling']"))):
            self.driver.find_element_by_xpath("//*[@text='Hide Default Scheduling']").click()
        elif WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='show_defaultTV']"))):
            self.driver.find_element_by_xpath("//*[@id='show_defaultTV']").click()
        else:
            raiseExceptions("hide default scheduling option is missing")

        hasFoundIntelligence = True
        while hasFoundIntelligence:
            if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='12AM']")) > 0:
                hasFoundIntelligence = False
            elif len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='INTELLIGENCE']")) > 0:
                raiseExceptions("Default Scheduling was not hidden")
            else:
                # scroll down to see if there is an event
                location = self.driver.find_element_by_id("com.view.viewglass:id/vLineScroll_schdLL").location
                size = self.driver.find_element_by_id("com.view.viewglass:id/vLineScroll_schdLL").size
                self.driver.swipe(location['x'] + size['width'] / 2, location['y'], location['x'] + size['width'] / 2,
                                  location['y'] + size['height'], 2000)

    # @attr('acceptance', sid='TC-schedule-1.4, TC-schedule-1.6, TC-tievent-3.3, TC-tievent-3.7, TC-tievent-3.9, TC-tievent-3.10, TC-tievent-3.11, TC-tievent-3.12, TC-tievent-3.13, TC-tievent-3.14', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def test15CreateScheduleWithInvalidInputForCRUDO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
                    EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scheduleTV"))):
                self.driver.find_element_by_id("com.view.viewglass:id/navigation_scheduleTV").click()
            else:
                raiseExceptions("Schedule option in navigation menu is missing")

        commonFunctions.addbutton(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/tint_level_schdSceneTV"))):
            commonFunctions.savebutton(self.driver)

        if commonFunctions.foundAlert(self.driver):
            commonFunctions.respondToAlert(self.driver, 1)
            commonFunctions.goback(self.driver)
            auth.logout(self.driver)
        else:
            raiseExceptions("Exception handling for invalid input is missing")

    # @attr('acceptance', sid='TC-schedule-1.4, TC-schedule-1.6, TC-tievent-3.3, TC-tievent-3.7, TC-tievent-3.9, TC-tievent-3.10, TC-tievent-3.11, TC-tievent-3.12, TC-tievent-3.13, TC-tievent-3.14', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def test16CreateNoRepeatScheduleForRUO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'RUO')
        auth.login(self.driver, config.users['RUO']['username'], config.users['RUO']['password'])
        site.selectSite(self.driver, config.site[0])
        sleep(20)
        if commonFunctions.foundAlert(self.driver):
            commonFunctions.respondToAlert(self.driver, 0)
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/view_btnTV")) > 0:
            commonFunctions.navIcon(self.driver)

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
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
    def test17EditNoRepeatScheduleForRUO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'RUO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
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
            commonFunctions.editbutton(self.driver)
            control.changeTint(self.driver)
            commonFunctions.savebutton(self.driver)
        if commonFunctions.foundAlert(self.driver):
            commonFunctions.respondToAlert(self.driver, 1)

    # @attr('acceptance', sid='TC-CTS-7.1, TC-CTS-7.2, TC-CTS-7.1', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def test18CopyNoRepeatScheduleForRUO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'RUO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
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
    def test19DeleteNoRepeatScheduleForRUO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'RUO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
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
    def test20CreateEverydayScheduleForRUO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'RUO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
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
            control.changeRepeat(self.driver, "Everyday")
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

    # @attr('acceptance', sid='TC-schedule-1.7', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def test21DeleteEverydayScheduleForRUO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'RUO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
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
    def test22CreateWeeklyScheduleForRUO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'RUO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
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
            control.changeRepeat(self.driver, "Weekly")
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

    # @attr('acceptance', sid='TC-schedule-1.7', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def test23DeleteWeeklyScheduleForRUO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'RUO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
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
    def test24CreateMondayToFridayScheduleForRUO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'RUO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
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

    # @attr('acceptance', sid='TC-schedule-1.7', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def test25DeleteMondayToFridayScheduleForRUO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'RUO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
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

    # @attr('acceptance', sid='TC-schedule-1.3, TC-sedate-2.2, TC-sedate-2.3, TC-sedate-2.4', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def test26CalendarIconForRandomDayForRUO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'RUO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
                    EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scheduleTV"))):
                self.driver.find_element_by_id("com.view.viewglass:id/navigation_scheduleTV").click()
            else:
                raiseExceptions("Schedule option in navigation menu is missing")

        today = commonFunctions.getToday()
        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/calendar_schdLL"))):
            self.driver.find_element_by_id("com.view.viewglass:id/calendar_schdLL").click()
        else:
            raiseExceptions("calendar icon is missing")

        random_date = commonFunctions.generateRandomNumber(today, 28)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='" + random_date + "']"))):
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='" + random_date + "']").click()
        else:
            raiseExceptions("Random day, " + random_date + ", cannot be clicked in the calendar")

    # @attr('acceptance', sid='TC-schedule-1.3, TC-sedate-2.2, TC-sedate-2.3, TC-sedate-2.4', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def test27CalendarIconForTodayForRUO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'RUO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
                    EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scheduleTV"))):
                self.driver.find_element_by_id("com.view.viewglass:id/navigation_scheduleTV").click()
            else:
                raiseExceptions("Schedule option in navigation menu is missing")

        today = commonFunctions.getToday()
        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/calendar_schdLL"))):
            self.driver.find_element_by_id("com.view.viewglass:id/calendar_schdLL").click()
        else:
            raiseExceptions("calendar icon is missing")

        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/todayBtn_calTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/todayBtn_calTV").click()
        else:
            raiseExceptions("Today button is missing")

    # @attr('acceptance', sid='TC-schedule-1.9, TC-schedule-1.10', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def test28ShowDefaultSchedulingForRUO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'RUO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
                    EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scheduleTV"))):
                self.driver.find_element_by_id("com.view.viewglass:id/navigation_scheduleTV").click()
            else:
                raiseExceptions("Schedule option in navigation menu is missing")

        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//*[@text='Show Default Scheduling']"))):
            self.driver.find_element_by_xpath("//*[@text='Show Default Scheduling']").click()
        elif WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='show_defaultTV']"))):
            self.driver.find_element_by_xpath("//*[@id='show_defaultTV']").click()
        else:
            raiseExceptions("show default scheduling option is missing")

        hasFoundIntelligence = False
        while not hasFoundIntelligence:
            if not hasFoundIntelligence and len(
                    self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='12AM']")) > 0:
                raiseExceptions("Intelligence icon for Default Scheduling is missing")
            elif len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='INTELLIGENCE']")) > 0:
                hasFoundIntelligence = True
            else:
                # scroll down to see if there is an event
                location = self.driver.find_element_by_id("com.view.viewglass:id/vLineScroll_schdLL").location
                size = self.driver.find_element_by_id("com.view.viewglass:id/vLineScroll_schdLL").size
                self.driver.swipe(location['x'] + size['width'] / 2, location['y'], location['x'] + size['width'] / 2,
                                  location['y'] + size['height'], 2000)

    # @attr('acceptance', sid='TC-schedule-1.9, TC-schedule-1.10', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def test29HideDefaultSchedulingForRUO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'RUO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
                    EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scheduleTV"))):
                self.driver.find_element_by_id("com.view.viewglass:id/navigation_scheduleTV").click()
            else:
                raiseExceptions("Schedule option in navigation menu is missing")

        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//*[@text='Show Default Scheduling']"))):
            self.driver.find_element_by_xpath("//*[@text='Show Default Scheduling']").click()
        elif WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='show_defaultTV']"))):
            self.driver.find_element_by_xpath("//*[@id='show_defaultTV']").click()
        else:
            raiseExceptions("show default scheduling option is missing")

        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//*[@text='Hide Default Scheduling']"))):
            self.driver.find_element_by_xpath("//*[@text='Hide Default Scheduling']").click()
        elif WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='show_defaultTV']"))):
            self.driver.find_element_by_xpath("//*[@id='show_defaultTV']").click()
        else:
            raiseExceptions("hide default scheduling option is missing")

        hasFoundIntelligence = True
        while hasFoundIntelligence:
            if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='12AM']")) > 0:
                hasFoundIntelligence = False
            elif len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='INTELLIGENCE']")) > 0:
                raiseExceptions("Default Scheduling was not hidden")
            else:
                # scroll down to see if there is an event
                location = self.driver.find_element_by_id("com.view.viewglass:id/vLineScroll_schdLL").location
                size = self.driver.find_element_by_id("com.view.viewglass:id/vLineScroll_schdLL").size
                self.driver.swipe(location['x'] + size['width'] / 2, location['y'], location['x'] + size['width'] / 2,
                                  location['y'] + size['height'], 2000)

    # @attr('acceptance', sid='TC-tievent-3.2, TC-zn/zng-4.5, TC-zn/zng-4.6, TC-zn/zng-4.7', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def test30AppliedToForRUO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'RUO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
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
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/zone_scene_sel_schdSceneTintTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/zone_scene_sel_schdSceneTintTV").click()
            self.driver.find_elements(By.ID, "com.view.viewglass:id/listItem_radioBtnIV")[0].click()
        else:
            raiseExceptions("applied to option is missing")

        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='Save']"))):
            commonFunctions.savebutton(self.driver)
            commonFunctions.savebutton(self.driver)
        else:
            raiseExceptions("save button is missing")

        if commonFunctions.foundAlert(self.driver):
            commonFunctions.respondToAlert(self.driver, 1)
            commonFunctions.goback(self.driver)
            # raiseExceptions("Unable to create schedule")

    # @attr('acceptance', sid='TC-schedule-1.4, TC-schedule-1.6, TC-tievent-3.3, TC-tievent-3.7, TC-tievent-3.9, TC-tievent-3.10, TC-tievent-3.11, TC-tievent-3.12, TC-tievent-3.13, TC-tievent-3.14', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def test31CreateScheduleWithInvalidInputForRUO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'RUO')
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
                    EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scheduleTV"))):
                self.driver.find_element_by_id("com.view.viewglass:id/navigation_scheduleTV").click()
            else:
                raiseExceptions("Schedule option in navigation menu is missing")

        commonFunctions.addbutton(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/tint_level_schdSceneTV"))):
            commonFunctions.savebutton(self.driver)

        if commonFunctions.foundAlert(self.driver):
            commonFunctions.respondToAlert(self.driver, 1)
            commonFunctions.goback(self.driver)
            auth.logout(self.driver)
        else:
            raiseExceptions("Exception handling for invalid input is missing")

    # @attr('acceptance', sid='TC-schedule-1.4, TC-schedule-1.6, TC-tievent-3.3, TC-tievent-3.7, TC-tievent-3.9, TC-tievent-3.10, TC-tievent-3.11, TC-tievent-3.12, TC-tievent-3.13, TC-tievent-3.14', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def test32CreateNoRepeatScheduleForRO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'RO')
        auth.login(self.driver, config.users['RO']['username'], config.users['RO']['password'])
        if commonFunctions.foundAlert(self.driver):
            commonFunctions.respondToAlert(self.driver, 0)
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/view_btnTV")) > 0:
            commonFunctions.navIcon(self.driver)

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scheduleTV")) <= 0:
            commonFunctions.navIcon(self.driver)
            if WebDriverWait(self.driver, 60).until(
                    EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scheduleTV"))):
                self.driver.find_element_by_id("com.view.viewglass:id/navigation_scheduleTV").click()
            else:
                raiseExceptions("Schedule option in navigation menu is missing")

        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/add_schdIV"))):
            raiseExceptions("Bug: RO user is able to create a schedule")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Schedule)
    unittest.TextTestRunner(verbosity=2).run(suite)
