"""
########################################################################
#
# SYNOPSIS
#   Zones :  Include Test cases related to create, delete , edit zone groups for CRUDO, RUO, RO privilege users
#
# AUTHOR
#  Emily Puth (emily.puth@viewglass.com)
#
#
# DESCRIPTION
#   Include Test cases related to create, delete , edit zone groups for CRUDO, RUO, RO privilege users
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
from common import control
from common import zones_and_scenes


class Zones(unittest.TestCase):
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

    # @attr('acceptance', sid='TC-zones-1.1, TC-zones-1.2, TC-zones-1.5, TC-zones-1.6', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testVerifyUIComponentsOfZonesScreen(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_zonesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_zonesTV").click()
        else:
            raiseExceptions("Zones option in navigation menu is missing")

            if WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_zonesTV"))):
                pass
            else:
                raiseExceptions("Zones heading is missing")
            if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='FAVORITES']")) <= 0:
                raiseExceptions("Favorites sub-heading is missing")
            if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='ZONE GROUPS']")) <= 0:
                raiseExceptions("Zonegroups sub-heading is missing")
            if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/expanEditIV")) <= 0:
                raiseExceptions("Manage Favorites icon is missing")
            if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/actZone_addIV")) <= 0:
                raiseExceptions("Add icon is missing")
            if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/search_zonesIV")) <= 0:
                raiseExceptions("Search icon is missing")

    # @attr('acceptance', sid='TC-zones-1.3,TC-zones-1.6-1.12', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testFunctionalityOfUIComponentsForZonesScreen(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_zonesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_zonesTV").click()
        else:
            raiseExceptions("Zones option in navigation menu is missing")

            WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "com.view.viewglass:id/actZone_addIV")))
            self.driver.find_element_by_id("com.view.viewglass:id/actZone_addIV").click()
            if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/title_createZoneGrpTV")) <= 0:
                raiseExceptions("Add icon led to the wrong screen.")
            if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/back_btn_create_newZoneGrpIV")) > 0:
                self.driver.find_element_by_id("com.view.viewglass:id/back_btn_create_newZoneGrpIV").click()

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/search_zonesIV")))
            self.driver.find_element_by_id("com.view.viewglass:id/search_zonesIV").click()
            if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/serachParentLL")) <= 0:
                raiseExceptions("Search icon led to the wrong screen.")
            if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/searchCancelTV")) > 0:
                self.driver.find_element_by_id("com.view.viewglass:id/searchCancelTV").click()

    # @attr('acceptance', sid='TC-zngrpdet-2.1,TC-zngrpdet-2.3,TC-zngrpdet-2.5, TC-zndet-3.3,TC-zndet-3.1', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def verifyUIComponentsOfZoneGroupDetailScreen(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_zonesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_zonesTV").click()
        else:
            raiseExceptions("Zones option in navigation menu is missing")

        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_zonesTV"))):
            pass
        else:
            raiseExceptions("Zones heading is missing")

        zones_and_scenes.selectTopZonegroup(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/heading_zngrpdetailTV"))):
            pass
        else:
            raiseExceptions("Zonegroup name is missing")
        if len(self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='ZONEGROUP']")) <= 0:
            raiseExceptions("Zonegroup text is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/tintImage_zngrpdetailIV")) <= 0:
            raiseExceptions("Tint is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/tint_level_zngrpdetailTV")) <= 0:
            raiseExceptions("Tint detail is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/tintAgent_zngrpdetailTV")) <= 0:
            raiseExceptions("Tint source/agent/mode is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/setTintBtn_zngrpdetailTV")) <= 0:
            raiseExceptions("Override button is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/headingZnList__zngrpdetailTV")) <= 0:
            raiseExceptions("Number of zones subheading is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/name_zone_item_listTV")) <= 0:
            raiseExceptions("Zone name in zonegroup is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/editZoneGrpTextTV")) <= 0:
            raiseExceptions("Edit button is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/backBtn_zngrpdetailLL")) <= 0:
            raiseExceptions("Back button is missing")
        else:
            self.driver.find_element_by_id("com.view.viewglass:id/backBtn_zngrpdetailLL").click()

    # @attr('acceptance', sid='TC-crtzngp-9.1', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testVerifyUIComponentsOfCreateZoneGroupScreen(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_zonesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_zonesTV").click()
        else:
            raiseExceptions("Zones option in navigation menu is missing")

        if WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "com.view.viewglass:id/actZone_addIV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/actZone_addIV").click()
        else:
            raiseExceptions("Add icon is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/title_createZoneGrpTV")) <= 0:
            raiseExceptions("Add icon led to the wrong screen.")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/save_zoneGrpTV")) <= 0:
            raiseExceptions("Save button is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/name_createZoneGrp_addETV")) <= 0:
            raiseExceptions("Name text field is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/zone_item_select_zoneTV")) <= 0:
            raiseExceptions("Names of available zones is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/back_btn_create_newZoneGrpIV")) <= 0:
            raiseExceptions("Back button is missing")
        else:
            self.driver.find_element_by_id("com.view.viewglass:id/back_btn_create_newZoneGrpIV").click()


    # @attr('acceptance', sid='TC-zones-1.13', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testNavigationIconInZones(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_zonesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_zonesTV").click()
        else:
            raiseExceptions("Zones option in navigation menu is missing")

        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_zonesTV"))):
            pass
        else:
            raiseExceptions("Zones heading is missing")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/home_zonesIV")) <= 0:
            raiseExceptions("Navigation icon in Zones is missing")

    # @attr('acceptance', sid='TC-search-4.1, TC-search-4.6, TC-search-4.2-4.5, TC-search-4.8', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testFunctionalityOfSearching(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_zonesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_zonesTV").click()
        else:
            raiseExceptions("Zones option in navigation menu is missing")

        if WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "com.view.viewglass:id/search_zonesIV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/search_zonesIV").click()
        else:
            raiseExceptions("Search icon is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/searchEditTV")) > 0:
            self.driver.find_element_by_id("com.view.viewglass:id/searchEditTV").send_keys("z")
        else:
            raiseExceptions("Search text field is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/exapdChildTitle")) > 0:
            searchResults = self.driver.find_elements(By.ID, "com.view.viewglass:id/exapdChildTitle")
            for result in searchResults:
                if not ("z" in result.text or "Z" in result.text):
                    raiseExceptions("Bug: found incorrect result ", result.text)
        elif len(self.driver.find_elements(By.ID, "com.view.viewglass:id/exapdChildTitle")) == 0:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='0 SEARCH RESULT']")
        else:
            raiseExceptions("Missing exception handling for unmatching search results")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/searchCancelTV")) > 0:
            self.driver.find_element_by_id("com.view.viewglass:id/searchCancelTV").click()
        else:
            raiseExceptions("Cancel button is missing")


    # @attr('acceptance', sid='TC-zngrpdet-2.2, TC-zndet-3.2', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testOverrideZoneGroupTint(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_zonesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_zonesTV").click()
        else:
            raiseExceptions("Zones option in navigation menu is missing")

        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_zonesTV"))):
            pass
        else:
            raiseExceptions("Zones heading is missing")

        zones_and_scenes.selectTopZonegroup(self.driver)
        tint = 0
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/setTintBtn_zngrpdetailTV")) <= 0:
            raiseExceptions("Override button is missing")
        else:
            commonFunctions.overridebutton(self.driver)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/Control_headingTV")))
            tint = control.selectRandomTint(self.driver)
            commonFunctions.overridebutton(self.driver)
        if tint != 0:
            commonFunctions.navIcon(self.driver)
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_zonesTV").click()
            zones_and_scenes.selectTopZonegroup(self.driver)
        else:
            raiseExceptions("unable to override tint")
        currentTint = self.driver.find_element_by_id("com.view.viewglass:id/tint_level_zngrpdetailTV").text
        if str(tint) not in currentTint:
            raiseExceptions("Control screen is not in sync with Zones screen")

    # @attr('acceptance', sid='TC-zngrpdet-2.6', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testZoneGroupsWithMixedTint(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_zonesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_zonesTV").click()
        else:
            raiseExceptions("Zones option in navigation menu is missing")

        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_zonesTV"))):
            pass
        else:
            raiseExceptions("Zones heading is missing")

        zones_and_scenes.selectTopZonegroup(self.driver)
        zonegroups = self.driver.find_elements(By.ID, "com.view.viewglass:id/parent_zone_item_listLL")
        if len(zonegroups) >= 2:
            zonegroups[0].click()
            commonFunctions.overridebutton(self.driver)
            control.selectTint(self.driver, 1)

            commonFunctions.navIcon(self.driver)
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_zonesTV").click()
            zones_and_scenes.selectTopZonegroup(self.driver)

            zonegroups[1].click()
            commonFunctions.overridebutton(self.driver)
            control.selectTint(self.driver, 2)
        else:
            commonFunctions.goback(self.driver)
            print("there are not enough zones to have a mixed tint detail")

        commonFunctions.navIcon(self.driver)
        self.driver.find_element_by_id("com.view.viewglass:id/navigation_zonesTV").click()
        zones_and_scenes.selectTopZonegroup(self.driver)
        currentTint = self.driver.find_element_by_id("com.view.viewglass:id/tint_level_zngrpdetailTV").text
        if currentTint != "Mixed Tint":
            raiseExceptions("Control screen is not in sync with Zones screen")

    # # @attr('acceptance', sid='TC-search-4.7', bv=10)
    # # @unittest.skip('Test case temporarily disabled')
    # def testCloseSearchWithCrossButton(self):
    #     print("ui")

    # @attr('acceptance', sid='TC-crtzngp-9.2 to TC-crtzngp-9.8', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCreateZoneGroupForCRUDO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'CRUDO')
        auth.loginAndSelectSite(self.driver, config.users['CRUDO']['username'], config.users['CRUDO']['password'],
                                config.site[0])

        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_zonesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_zonesTV").click()
        else:
            raiseExceptions("Zones option in navigation menu is missing")

        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_zonesTV"))):
            pass
        else:
            raiseExceptions("Zones heading is missing")

        commonFunctions.addbutton(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_createZoneGrpTV"))):
            pass
        else:
            raiseExceptions("Add button led to the wrong screen")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/name_createZoneGrp_addETV")) > 0:
            self.driver.find_element_by_id("com.view.viewglass:id/name_createZoneGrp_addETV").send_keys("abc")
            firstZone = self.driver.find_elements(By.ID, "com.view.viewglass:id/zone_item_select_zoneTV")[0]
            firstZone.click()
            commonFunctions.savebutton(self.driver)
        else:
            raiseExceptions("Name text field is missing")

        foundCreatedZonegroup = False
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")) > 0:
            zonegroups = self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")
            for group in zonegroups:
                if group.text == "abc":
                    foundCreatedZonegroup = True
        if not foundCreatedZonegroup:
            raiseExceptions("Zonegroup 'abc' was not created")

    # @attr('acceptance', sid='TC-crtzngp-9.2 to TC-crtzngp-9.8', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCreateZoneGroupForRUO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'RUO')
        auth.loginAndSelectSite(self.driver, config.users['RUO']['username'], config.users['RUO']['password'],
                                config.site[0])

        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_zonesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_zonesTV").click()
        else:
            raiseExceptions("Zones option in navigation menu is missing")

        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_zonesTV"))):
            pass
        else:
            raiseExceptions("Zones heading is missing")

        commonFunctions.addbutton(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_createZoneGrpTV"))):
            pass
        else:
            raiseExceptions("Add button led to the wrong screen")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/name_createZoneGrp_addETV")) > 0:
            self.driver.find_element_by_id("com.view.viewglass:id/name_createZoneGrp_addETV").send_keys("abc")
            firstZone = self.driver.find_elements(By.ID, "com.view.viewglass:id/zone_item_select_zoneTV")[0]
            firstZone.click()
            commonFunctions.savebutton(self.driver)
        else:
            raiseExceptions("Name text field is missing")

        foundCreatedZonegroup = False
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")) > 0:
            zonegroups = self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")
            for group in zonegroups:
                if group.text == "abc":
                    foundCreatedZonegroup = True
        if not foundCreatedZonegroup:
            raiseExceptions("Zonegroup 'abc' was not created")

        # @attr('acceptance', sid='TC-crtzngp-9.2 to TC-crtzngp-9.8', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCreateZoneGroupForRO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'RO')
        auth.login(self.driver, config.users['RO']['username'], config.users['RO']['password'])
        sleep(20)
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/home_controlIV")) > 0:
            pass
        elif len(self.driver.find_elements(By.XPATH, "//android.widget.Button[@resource-id='com.view.viewglass:id/button_cancel']")) > 0:
            site.selectSite(self.driver, config.users['RO']['testsite'])
        if commonFunctions.foundAlert(self.driver):
            commonFunctions.respondToAlert(self.driver, 0)
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/view_btnTV")) > 0:
            commonFunctions.navIcon(self.driver)

        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_zonesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_zonesTV").click()
        else:
            raiseExceptions("Zones option in navigation menu is missing")

        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_zonesTV"))):
            pass
        else:
            raiseExceptions("Zones heading is missing")

        commonFunctions.addbutton(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_createZoneGrpTV"))):
            pass
        else:
            raiseExceptions("Add button led to the wrong screen")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/name_createZoneGrp_addETV")) > 0:
            self.driver.find_element_by_id("com.view.viewglass:id/name_createZoneGrp_addETV").send_keys("abc")
            firstZone = self.driver.find_elements(By.ID, "com.view.viewglass:id/zone_item_select_zoneTV")[0]
            firstZone.click()
            commonFunctions.savebutton(self.driver)
        else:
            raiseExceptions("Name text field is missing")

        foundCreatedZonegroup = False
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")) > 0:
            zonegroups = self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")
            for group in zonegroups:
                if group.text == "abc":
                    foundCreatedZonegroup = True
        if not foundCreatedZonegroup:
            raiseExceptions("Zonegroup 'abc' was not created")

    # @attr('acceptance', sid='TC-zngrpdet-2.7, TC-zndet-3.5, TC-crtzngp-9.11, TC-crtzngp-9.12', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testEditZoneGroupForCRUDO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'CRUDO')
        auth.loginAndSelectSite(self.driver, config.users['CRUDO']['username'], config.users['CRUDO']['password'],
                                config.site[0])

        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_zonesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_zonesTV").click()
        else:
            raiseExceptions("Zones option in navigation menu is missing")

        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_zonesTV"))):
            pass
        else:
            raiseExceptions("Zones heading is missing")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")) > 0:
            zonegroups = self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")
            for group in zonegroups:
                if group.text == "abc":
                    group.click()
                    break
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='abc']"))):
            commonFunctions.editbutton(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_createZoneGrpTV"))):
            zones = self.driver.find_elements(By.ID, "com.view.viewglass:id/zone_item_select_zoneTV")
            zones[2].click()
            zones[3].click()
            commonFunctions.savebutton(self.driver)
        else:
            raiseExceptions("Edit button led to the wrong screen")


    # @attr('acceptance', sid='TC-zngrpdet-2.7, TC-zndet-3.5, TC-crtzngp-9.11, TC-crtzngp-9.12', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testEditZoneGroupForRUO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'RUO')
        auth.loginAndSelectSite(self.driver, config.users['RUO']['username'], config.users['RUO']['password'],
                                config.site[0])

        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_zonesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_zonesTV").click()
        else:
            raiseExceptions("Zones option in navigation menu is missing")

        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_zonesTV"))):
            pass
        else:
            raiseExceptions("Zones heading is missing")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")) > 0:
            zonegroups = self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")
            for group in zonegroups:
                if group.text == "abc":
                    group.click()
                    break
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='abc']"))):
            commonFunctions.editbutton(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_createZoneGrpTV"))):
            zones = self.driver.find_elements(By.ID, "com.view.viewglass:id/zone_item_select_zoneTV")
            zones[2].click()
            zones[3].click()
            commonFunctions.savebutton(self.driver)
        else:
            raiseExceptions("Edit button led to the wrong screen")

    # @attr('acceptance', sid='TC-zngrpdet-2.7, TC-zndet-3.5, TC-crtzngp-9.11, TC-crtzngp-9.12', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testEditZoneGroupForRO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'RO')
        auth.login(self.driver, config.users['RO']['username'], config.users['RO']['password'])
        sleep(20)
        if commonFunctions.foundAlert(self.driver):
            commonFunctions.respondToAlert(self.driver, 0)
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/view_btnTV")) > 0:
            commonFunctions.navIcon(self.driver)

        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_zonesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_zonesTV").click()
        else:
            raiseExceptions("Zones option in navigation menu is missing")

        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_zonesTV"))):
            pass
        else:
            raiseExceptions("Zones heading is missing")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")) > 0:
            zonegroups = self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")
            for group in zonegroups:
                if group.text == "abc":
                    group.click()
                    break
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='abc']"))):
            commonFunctions.editbutton(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_createZoneGrpTV"))):
            zones = self.driver.find_elements(By.ID, "com.view.viewglass:id/zone_item_select_zoneTV")
            zones[2].click()
            zones[3].click()
            commonFunctions.savebutton(self.driver)
        else:
            raiseExceptions("Edit button led to the wrong screen")

    # @attr('acceptance', sid='TC-crtzngp-9.9, TC-crtzngp-9.10', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testRemoveZoneGroupForCRUDO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'CRUDO')
        auth.loginAndSelectSite(self.driver, config.users['CRUDO']['username'], config.users['CRUDO']['password'],
                                config.site[0])

        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_zonesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_zonesTV").click()
        else:
            raiseExceptions("Zones option in navigation menu is missing")

        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_zonesTV"))):
            pass
        else:
            raiseExceptions("Zones heading is missing")

        foundZonegroupabc = False
        size = 0
        location = 0
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")) > 0:
            zonegroups = self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")
            for group in zonegroups:
                if group.text == "abc":
                    foundZonegroupabc = True
                    size = group.size
                    location = group.location
                    break
        if foundZonegroupabc:
            startx = location['x'] + size['width']
            endx = location['x'] + size['width'] / 2
            y = location['y'] + size['height'] / 2
            self.driver.swipe(startx, y, endx, y, 3000)
            x = location['x'] + size['width'] - 10
            self.driver.tap([(x, y)])
            sleep(5)

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")) > 0:
            zonegroups = self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")
            for group in zonegroups:
                if group.text == "abc":
                    raiseExceptions("Zonegroup was not deleted")

    # @attr('acceptance', sid='TC-crtzngp-9.9, TC-crtzngp-9.10', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testRemoveDeleteZoneGroupForRUO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'RUO')
        auth.loginAndSelectSite(self.driver, config.users['RUO']['username'], config.users['RUO']['password'],
                                config.site[0])

        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_zonesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_zonesTV").click()
        else:
            raiseExceptions("Zones option in navigation menu is missing")

        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_zonesTV"))):
            pass
        else:
            raiseExceptions("Zones heading is missing")

        foundZonegroupabc = False
        size = 0
        location = 0
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")) > 0:
            zonegroups = self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")
            for group in zonegroups:
                if group.text == "abc":
                    foundZonegroupabc = True
                    size = group.size
                    location = group.location
                    break
        if foundZonegroupabc:
            startx = location['x'] + size['width']
            endx = location['x'] + size['width']/2
            y = location['y'] + size['height']/2
            self.driver.swipe(startx, y, endx, y, 3000)
            x = location['x'] + size['width'] - 10
            self.driver.tap([(x, y)])
            sleep(5)

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")) > 0:
            zonegroups = self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")
            for group in zonegroups:
                if group.text == "abc":
                    raiseExceptions("Zonegroup was not deleted")

    # @attr('acceptance', sid='TC-crtzngp-9.9, TC-crtzngp-9.10', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testRemoveDeleteZoneGroupForRO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'RO')
        auth.login(self.driver, config.users['RO']['username'], config.users['RO']['password'])
        sleep(20)
        if commonFunctions.foundAlert(self.driver):
            commonFunctions.respondToAlert(self.driver, 0)
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/view_btnTV")) > 0:
            commonFunctions.navIcon(self.driver)

        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_zonesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_zonesTV").click()
        else:
            raiseExceptions("Zones option in navigation menu is missing")

        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_zonesTV"))):
            pass
        else:
            raiseExceptions("Zones heading is missing")

        foundZonegroupabc = False
        size = 0
        location = 0
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")) > 0:
            zonegroups = self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")
            for group in zonegroups:
                if group.text == "abc":
                    foundZonegroupabc = True
                    size = group.size
                    location = group.location
                    break
        if foundZonegroupabc:
            startx = location['x'] + size['width']
            endx = location['x'] + size['width'] / 2
            y = location['y'] + size['height'] / 2
            self.driver.swipe(startx, y, endx, y, 3000)
            x = location['x'] + size['width'] - 10
            self.driver.tap([(x, y)])
            sleep(5)

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")) > 0:
            zonegroups = self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")
            for group in zonegroups:
                if group.text == "abc":
                    raiseExceptions("Zonegroup was not deleted")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Zones)
    unittest.TextTestRunner(verbosity=2).run(suite)


