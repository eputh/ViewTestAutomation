"""
########################################################################
#
# SYNOPSIS
#   Zones :  Include Test cases related to creating, editing, scheduling, and removing scenes for CRUDO, RUO, RO privilege users
#
# AUTHOR
#  Emily Puth (emily.puth@viewglass.com)
#
#
# DESCRIPTION
#   Include Test cases related to creating, editing, scheduling, and removing scenes for CRUDO, RUO, RO privilege users
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
from time import sleep
from logging import raiseExceptions
from datetime import datetime
from datetime import timedelta

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from common import auth
from common import commonFunctions
from common import config
from common import site
from common import zones_and_scenes


class Scenes(unittest.TestCase):
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

    # @attr('acceptance', sid='TC-scene-1.1, TC-scene-1.4', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testVerifyUIComponentsOfSceneScreen(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scenesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_scenesTV").click()
        else:
            raiseExceptions("Scenes option in navigation menu is missing")

        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/scene_headertext"))):
            pass
        else:
            raiseExceptions("Scenes heading is missing")
        commonFunctions.navIcon(self.driver)
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/view_btnTV")) <= 0:
            raiseExceptions("Navigation icon in Scenes screen is missing")
        commonFunctions.navIcon(self.driver)

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scene_addIconIV")) <= 0:
            raiseExceptions("Add icon in Scenes screen is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/desc_SceneItemTV")) <= 0:
            raiseExceptions("Number of zones each scene is applied to is missing")

    # @attr('acceptance', sid='TC-scene-1.3, TC-scendet-2.1', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testVerifyUIComponentsOfSceneDetailScreen(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scenesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_scenesTV").click()
        else:
            raiseExceptions("Scenes option in navigation menu is missing")

        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/scene_headertext"))):
            firstScene = self.driver.find_elements(By.ID, "com.view.viewglass:id/parent_scene_item")[0]
            firstScene.click()
        else:
            raiseExceptions("Scenes heading is missing")

        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/scene_Detail"))):
            pass
        else:
            raiseExceptions("Scene Detail heading is missing")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/back_scene_detailLL")) <= 0:
            raiseExceptions("Back button in Scenes Detail screen is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/editbtn_sceneTV")) <= 0:
            raiseExceptions("Edit button in Scenes Detail screen is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/sceneNameTV")) <= 0:
            raiseExceptions("Name of scene is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/tintEvents_scene_detailTV")) <= 0:
            raiseExceptions("Tint Event subheading is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/listitemImageIV")) <= 0:
            raiseExceptions("Tint level icon is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")) <= 0:
            raiseExceptions("Name of zone in scene is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/schedule_scene_TV")) <= 0:
            raiseExceptions("Schedule Scene button is missing")

    # @attr('acceptance', sid='TC-Editscen-3.1', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testVerifyUIComponentsOfEditSceneScreen(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scenesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_scenesTV").click()
        else:
            raiseExceptions("Scenes option in navigation menu is missing")

        WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/scene_headertext")))
        firstScene = self.driver.find_elements(By.ID, "com.view.viewglass:id/parent_scene_item")[0]
        firstScene.click()

        WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/scene_Detail")))
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/editbtn_sceneTV")) <= 0:
            raiseExceptions("Edit button in Scenes Detail screen is missing")
        else:
            commonFunctions.editbutton(self.driver)

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scene_Detail")) <= 0:
            raiseExceptions("Edit Scene heading is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/editbtn_sceneTV")) <= 0:
            raiseExceptions("Save button is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/add_tint_eventTV")) <= 0:
            raiseExceptions("Add Tint Event button is missing")
        if self.driver.find_element_by_id("com.view.viewglass:id/name_scene_editETV").text == "":
            raiseExceptions("Name of Scene is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/tintEvents_scene_detailTV")) <= 0:
            raiseExceptions("Tint Event subheading is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")) <= 0:
            raiseExceptions("Name of tint event is missing")

    # @attr('acceptance', sid='TC-addtnt-4.1', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testVerifyUIComponentsOfAddTintEventScreen(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scenesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_scenesTV").click()
        else:
            raiseExceptions("Scenes option in navigation menu is missing")

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "com.view.viewglass:id/scene_headertext")))
        firstScene = self.driver.find_elements(By.ID, "com.view.viewglass:id/parent_scene_item")[0]
        firstScene.click()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "com.view.viewglass:id/scene_Detail")))

        commonFunctions.editbutton(self.driver)
        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/add_tint_eventTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/add_tint_eventTV").click()
        else:
            raiseExceptions("Add Tint Event button is missing")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/title_scene_add_TintEventTV")) <= 0:
            raiseExceptions("Add Tint Event heading is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/back_btn_scene_add_TintEventIV")) <= 0:
            raiseExceptions("Back button is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/save_scene_add_TintEventTV")) <= 0:
            raiseExceptions("Save button is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/zone_add_TintEventTV")) <= 0:
            raiseExceptions("Zone option is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/tintLevel_scene_TintEventTV")) <= 0:
            raiseExceptions("Tint Level option is missing")

    # @attr('acceptance', sid='TC-scnevent-5.1', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testVerifyUIComponentsOfSceneEventScreen(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scenesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_scenesTV").click()
        else:
            raiseExceptions("Scenes option in navigation menu is missing")

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "com.view.viewglass:id/scene_headertext")))
        firstScene = self.driver.find_elements(By.ID, "com.view.viewglass:id/parent_scene_item")[0]
        firstScene.click()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "com.view.viewglass:id/scene_Detail")))

        commonFunctions.editbutton(self.driver)
        if WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "com.view.viewglass:id/listItemNameTV"))):
            self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")[0].click()
        else:
            raiseExceptions("Zones in Scene is missing")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/title_sceneEventTV")) <= 0:
            raiseExceptions("Scene Detail heading is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/back_scene_eventLL")) <= 0:
            raiseExceptions("Back button is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/savebtn_sceneEventTV")) <= 0:
            raiseExceptions("Save button is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/zone_TintEventTV")) <= 0:
            raiseExceptions("Zone option is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/tintLevel_tintEventTV")) <= 0:
            raiseExceptions("Tint Level option is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/tintLevel_SceneEventTV")) <= 0:
            raiseExceptions("Tint Level text is missing")

    # @attr('acceptance', sid='TC-scene-1.2, TC-addnewscene-6.1, TC-addtintevent-7.1', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testVerifyUIComponentsOfAddNewScene(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scenesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_scenesTV").click()
        else:
            raiseExceptions("Scenes option in navigation menu is missing")

        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/scene_headertext"))):
            commonFunctions.addbutton(self.driver)
        else:
            raiseExceptions("Scenes heading is missing")

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/title_scene_addTV")) <= 0:
            raiseExceptions("Add New Scene heading is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/back_btn_add_newSceneIV")) <= 0:
            raiseExceptions("Back button is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/save_scene_addTV")) <= 0:
            raiseExceptions("Save button is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/name_scene_addETV")) <= 0:
            raiseExceptions("Name text field is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/no_tint_eventTV")) <= 0:
            raiseExceptions("Message: No tint event is available, is missing")
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/add_tint_eventTV")) <= 0:
            raiseExceptions("Add Tint Event button is missing")

    # # @attr('acceptance', sid='TC-scendet-2.5', bv=10)
    # # @unittest.skip('Test case temporarily disabled')
    # def testDeleteTintEvent(self):
    #     print("delete from Scene Detail screen")

    # @attr('acceptance', sid='TC-scendet-2.2, TC-scendet-2.6, TC-Editscen-3.2-3.5,TC-SceneSchedule-9.20-9.27', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testEditScene(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scenesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_scenesTV").click()
        else:
            raiseExceptions("Scenes option in navigation menu is missing")

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "com.view.viewglass:id/scene_headertext")))
        firstScene = self.driver.find_elements(By.ID, "com.view.viewglass:id/parent_scene_item")[0]
        firstScene.click()

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "com.view.viewglass:id/scene_Detail")))
        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/editbtn_sceneTV")) <= 0:
            raiseExceptions("Edit button in Scenes Detail screen is missing")
        else:
            commonFunctions.editbutton(self.driver)

        self.driver.find_element_by_id("com.view.viewglass:id/name_scene_editETV").send_keys("abc")
        commonFunctions.goback(self.driver)
        commonFunctions.goback(self.driver)

    # @attr('acceptance', sid='TC-Editscen-3.6, TC-addtnt-4.2-4.6', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testAddTintEvent(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scenesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_scenesTV").click()
        else:
            raiseExceptions("Scenes option in navigation menu is missing")

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "com.view.viewglass:id/scene_headertext")))
        firstScene = self.driver.find_elements(By.ID, "com.view.viewglass:id/parent_scene_item")[0]
        firstScene.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "com.view.viewglass:id/scene_Detail")))

        commonFunctions.editbutton(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/add_tint_eventTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/add_tint_eventTV").click()
        else:
            raiseExceptions("Add Tint Event button is missing")

        self.driver.find_element_by_id("com.view.viewglass:id/zone_add_TintEventTV").click()
        if WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_repeatTV"))):
            self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")[0].click()
        else:
            raiseExceptions("Zone option led to the wrong screen")
        self.driver.find_element_by_id("com.view.viewglass:id/tintLevel_scene_TintEventTV").click()
        if WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_scene_selectTintTV"))):
            zones_and_scenes.selectRandomTint(self.driver)
        else:
            raiseExceptions("Tint Level option led to the wrong screen")
        commonFunctions.savebutton(self.driver)

    # @attr('acceptance', sid='TC-Editscen-3.6, TC-addtnt-4.2-4.6', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testAddTintEventExceptionHandling(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scenesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_scenesTV").click()
        else:
            raiseExceptions("Scenes option in navigation menu is missing")

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "com.view.viewglass:id/scene_headertext")))
        firstScene = self.driver.find_elements(By.ID, "com.view.viewglass:id/parent_scene_item")[0]
        firstScene.click()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "com.view.viewglass:id/scene_Detail")))

        commonFunctions.editbutton(self.driver)
        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/add_tint_eventTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/add_tint_eventTV").click()
        else:
            raiseExceptions("Add Tint Event button is missing")

        commonFunctions.savebutton(self.driver)
        if commonFunctions.foundAlert(self.driver):
            commonFunctions.respondToAlert(self.driver, 1)
        else:
            raiseExceptions("Missing exception handling for invalid input for Add Tint Event")

    # @attr('acceptance', sid='TC-scnevent-5.2, TC-scnevent-5.3, TC-scnevent-5.5', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testEditTintEvent(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scenesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_scenesTV").click()
        else:
            raiseExceptions("Scenes option in navigation menu is missing")

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "com.view.viewglass:id/scene_headertext")))
        firstScene = self.driver.find_elements(By.ID, "com.view.viewglass:id/parent_scene_item")[0]
        firstScene.click()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "com.view.viewglass:id/scene_Detail")))

        commonFunctions.editbutton(self.driver)
        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/listItemNameTV"))):
            self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")[0].click()
        else:
            raiseExceptions("Zones in Scene is missing")

        self.driver.find_element_by_id("com.view.viewglass:id/tintLevel_tintEventTV").click()
        selectedTint = zones_and_scenes.selectRandomTint(self.driver)
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "com.view.viewglass:id/tintLevel_SceneEventTV")))
        currentTint = self.driver.find_element_by_id("com.view.viewglass:id/tintLevel_SceneEventTV").text
        if str(selectedTint) not in currentTint:
            raiseExceptions("Bug: Edited Tint Level has not been updated")

    # @attr('acceptance', sid='TC-addnewscene-6.2-6.5, TC-addtintevent-7.2, TC-addtintevent-7.3, TC-SCS-8.1', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testAddNewSceneForCRUDO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'CRUDO')
        auth.loginAndSelectSite(self.driver, config.users['CRUDO']['username'], config.users['CRUDO']['password'],
                                config.site[0])

        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scenesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_scenesTV").click()
        else:
            raiseExceptions("Scenes option in navigation menu is missing")

        WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/scene_headertext")))
        commonFunctions.addbutton(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_scene_addTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/name_scene_addETV").send_keys("newscene")
            self.driver.find_element_by_id("com.view.viewglass:id/no_tint_eventTV").click()
            self.driver.find_element_by_id("com.view.viewglass:id/add_tint_eventTV").click()
        else:
            raiseExceptions("Add New Scene heading is missing")

        self.driver.find_element_by_id("com.view.viewglass:id/zone_add_TintEventTV").click()
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_repeatTV"))):
            self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")[0].click()
        else:
            raiseExceptions("Zone option led to the wrong screen")
        self.driver.find_element_by_id("com.view.viewglass:id/tintLevel_scene_TintEventTV").click()
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_scene_selectTintTV"))):
            zones_and_scenes.selectRandomTint(self.driver)
        else:
            raiseExceptions("Tint Level option led to the wrong screen")
        commonFunctions.savebutton(self.driver)
        commonFunctions.savebutton(self.driver)
        if commonFunctions.foundAlert(self.driver):
            commonFunctions.respondToAlert(self.driver, 1)

    # @attr('acceptance', sid='TC-addnewscene-6.2-6.5, TC-addtintevent-7.2, TC-addtintevent-7.3, TC-SCS-8.1', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testAddNewSceneForRUO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'RUO')
        auth.loginAndSelectSite(self.driver, config.users['RUO']['username'], config.users['RUO']['password'],
                                config.site[0])

        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scenesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_scenesTV").click()
        else:
            raiseExceptions("Scenes option in navigation menu is missing")

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "com.view.viewglass:id/scene_headertext")))
        commonFunctions.addbutton(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_scene_addTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/name_scene_addETV").send_keys("newscene")
            self.driver.find_element_by_id("com.view.viewglass:id/no_tint_eventTV").click()
            self.driver.find_element_by_id("com.view.viewglass:id/add_tint_eventTV").click()
        else:
            raiseExceptions("Add New Scene heading is missing")

        self.driver.find_element_by_id("com.view.viewglass:id/zone_add_TintEventTV").click()
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_repeatTV"))):
            self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")[0].click()
        else:
            raiseExceptions("Zone option led to the wrong screen")
        self.driver.find_element_by_id("com.view.viewglass:id/tintLevel_scene_TintEventTV").click()
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_scene_selectTintTV"))):
            zones_and_scenes.selectRandomTint(self.driver)
        else:
            raiseExceptions("Tint Level option led to the wrong screen")
        commonFunctions.savebutton(self.driver)
        commonFunctions.savebutton(self.driver)
        if commonFunctions.foundAlert(self.driver):
            commonFunctions.respondToAlert(self.driver, 1)

    # @attr('acceptance', sid='TC-addnewscene-6.2-6.5, TC-addtintevent-7.2, TC-addtintevent-7.3, TC-SCS-8.1', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testAddNewSceneForRO(self):
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'RO')
        auth.login(self.driver, config.users['RO']['username'], config.users['RO']['password'])
        sleep(20)
        if commonFunctions.foundAlert(self.driver):
            commonFunctions.respondToAlert(self.driver, 0)

        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scenesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_scenesTV").click()
        else:
            raiseExceptions("Scenes option in navigation menu is missing")

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "com.view.viewglass:id/scene_headertext")))

        if len(self.driver.find_elements(By.ID, "com.view.viewglass:id/scene_addIconIV")) > 0:
            raiseExceptions("Bug: RO user is able to add a new scene")
        auth.logout(self.driver)

    # @attr('acceptance', sid='TC-SCS-8.2-8.5', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testAddNewSceneWithMultipleTintEvents(self):
        auth.checkIfUserIsLoggedIn(self.driver, 0, 'CRUDO')
        auth.loginAndSelectSite(self.driver, config.users['CRUDO']['username'], config.users['CRUDO']['password'],
                                config.site[0])

        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scenesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_scenesTV").click()
        else:
            raiseExceptions("Scenes option in navigation menu is missing")

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "com.view.viewglass:id/scene_headertext")))
        commonFunctions.addbutton(self.driver)
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_scene_addTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/name_scene_addETV").send_keys("newscene")
            self.driver.find_element_by_id("com.view.viewglass:id/no_tint_eventTV").click()
        else:
            raiseExceptions("Add New Scene heading is missing")

        for i in range(0, 2):
            self.driver.find_element_by_id("com.view.viewglass:id/add_tint_eventTV").click()
            self.driver.find_element_by_id("com.view.viewglass:id/zone_add_TintEventTV").click()
            if WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_repeatTV"))):
                self.driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")[0].click()
            else:
                raiseExceptions("Zone option led to the wrong screen")
            self.driver.find_element_by_id("com.view.viewglass:id/tintLevel_scene_TintEventTV").click()
            if WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_scene_selectTintTV"))):
                zones_and_scenes.selectRandomTint(self.driver)
            else:
                raiseExceptions("Tint Level option led to the wrong screen")
            commonFunctions.savebutton(self.driver)
        commonFunctions.savebutton(self.driver)
        if commonFunctions.foundAlert(self.driver):
            commonFunctions.respondToAlert(self.driver, 1)

    # @attr('acceptance', sid='TC-SceneSchedule-9.1, TC-SceneSchedule-9.2, TC-SceneSchedule-9.11, TC-SceneSchedule-9.17', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCreateAndRemoveFutureSceneSchedule(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scenesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_scenesTV").click()
        else:
            raiseExceptions("Scenes option in navigation menu is missing")

        selectedScene = ""
        WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/scene_headertext")))
        selectedScene = self.driver.find_elements(By.ID, "com.view.viewglass:id/parent_scene_item")[0]
        selectedScene.click()

        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/schedule_scene_TV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/schedule_scene_TV").click()
        else:
            raiseExceptions("Schedule Scene button is missing")

        now = datetime.now()
        futureHours = [now + timedelta(hours=1), now + timedelta(hours=2)]
        startHour = datetime.strftime(futureHours[0], '%I:00 %p')
        endHour = datetime.strftime(futureHours[1], '%I:00 %p')

        self.driver.find_element_by_id("com.view.viewglass:id/starts_schdSceneTintTV").click()
        startPicker = self.driver.find_elements(By.ID, "android:id/timePickerLayout")[0]
        startPicker.send_keys(startHour)
        self.driver.find_element_by_id("com.view.viewglass:id/ends_schdSceneTintTV").click()
        endPicker = self.driver.find_elements(By.ID, "android:id/timePickerLayout")[0]
        endPicker.send_keys(endHour)
        commonFunctions.savebutton(self.driver)

    # @attr('acceptance', sid='TC-SceneSchedule-9.3, TC-SceneSchedule-9.4, TC-SceneSchedule-9.11, TC-SceneSchedule-9.12, TC-SceneSchedule-9.16, TC-SceneSchedule-9.18', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def tesCreateCurrentSceneSchedule(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scenesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_scenesTV").click()
        else:
            raiseExceptions("Scenes option in navigation menu is missing")

        selectedScene = ""
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "com.view.viewglass:id/scene_headertext")))
        selectedScene = self.driver.find_elements(By.ID, "com.view.viewglass:id/parent_scene_item")[0]
        selectedScene.click()

        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/schedule_scene_TV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/schedule_scene_TV").click()
        else:
            raiseExceptions("Schedule Scene button is missing")

        now = datetime.now()
        hours = [now - timedelta(hours=1), now + timedelta(hours=2)]
        startHour = datetime.strftime(hours[0], '%I:00 %p')
        endHour = datetime.strftime(hours[1], '%I:00 %p')

        self.driver.find_element_by_id("com.view.viewglass:id/starts_schdSceneTintTV").click()
        startPicker = self.driver.find_elements(By.ID, "android:id/timePickerLayout")[0]
        startPicker.send_keys(startHour)
        self.driver.find_element_by_id("com.view.viewglass:id/ends_schdSceneTintTV").click()
        endPicker = self.driver.find_elements(By.ID, "android:id/timePickerLayout")[0]
        endPicker.send_keys(endHour)
        commonFunctions.savebutton(self.driver)

    # @attr('acceptance', sid='TC-SceneSchedule-9.5, TC-SceneSchedule-9.11, TC-SceneSchedule-9.13, TC-SceneSchedule-9.14', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCreateEverydaySceneSchedule(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scenesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_scenesTV").click()
        else:
            raiseExceptions("Scenes option in navigation menu is missing")

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "com.view.viewglass:id/scene_headertext")))
        selectedScene = self.driver.find_elements(By.ID, "com.view.viewglass:id/parent_scene_item")[0]
        selectedScene.click()

        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/schedule_scene_TV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/schedule_scene_TV").click()
        else:
            raiseExceptions("Schedule Scene button is missing")

        self.driver.find_element_by_id("com.view.viewglass:id/repeats_schdSceneTintTV").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Everyday']").click()
        commonFunctions.savebutton(self.driver)

    # @attr('acceptance', sid='TC-SceneSchedule-9.6, TC-SceneSchedule-9.7, TC-SceneSchedule-9.11, TC-SceneSchedule-9.15', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCreateWeeklySceneSchedule(self):
        auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
        commonFunctions.navIcon(self.driver)
        if WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scenesTV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/navigation_scenesTV").click()
        else:
            raiseExceptions("Scenes option in navigation menu is missing")

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "com.view.viewglass:id/scene_headertext")))
        selectedScene = self.driver.find_elements(By.ID, "com.view.viewglass:id/parent_scene_item")[0]
        selectedScene.click()

        if WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/schedule_scene_TV"))):
            self.driver.find_element_by_id("com.view.viewglass:id/schedule_scene_TV").click()
        else:
            raiseExceptions("Schedule Scene button is missing")

        self.driver.find_element_by_id("com.view.viewglass:id/repeats_schdSceneTintTV").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Weekly']").click()
        commonFunctions.savebutton(self.driver)

    # # @attr('acceptance', sid='TC-SceneSchedule-9.8, TC-SceneSchedule-9.9', bv=10)
    # # @unittest.skip('Test case temporarily disabled')
    # def testOverlappingScenesSchedule(self):
    #     auth.checkIfUserIsLoggedIn(self.driver, 1, 'CRUDO')
    #     commonFunctions.navIcon(self.driver)
    #     if WebDriverWait(self.driver, 20).until(
    #             EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_scenesTV"))):
    #         self.driver.find_element_by_id("com.view.viewglass:id/navigation_scenesTV").click()
    #     else:
    #         raiseExceptions("Scenes option in navigation menu is missing")
    #
    #     now = datetime.now()
    #     hours = [now + timedelta(hours=1), now + timedelta(hours=2), now + timedelta(hours=3)]
    #     startHour1 = datetime.strftime(hours[0], '%I:00 %p')
    #     startHour2 = datetime.strftime(hours[1], '%I:00 %p')
    #     endHour = datetime.strftime(hours[2], '%I:00 %p')
    #
    #     WebDriverWait(self.driver, 20).until(
    #         EC.presence_of_element_located((By.ID, "com.view.viewglass:id/scene_headertext")))
    #     selectedScene = self.driver.find_elements(By.ID, "com.view.viewglass:id/parent_scene_item")[0]
    #     selectedScene.click()
    #
    #     if WebDriverWait(self.driver, 20).until(
    #             EC.presence_of_element_located((By.ID, "com.view.viewglass:id/schedule_scene_TV"))):
    #         self.driver.find_element_by_id("com.view.viewglass:id/schedule_scene_TV").click()
    #     else:
    #         raiseExceptions("Schedule Scene button is missing")
    #
    #     self.driver.find_element_by_id("com.view.viewglass:id/starts_schdSceneTintTV").click()
    #     startPicker = self.driver.find_elements(By.ID, "android:id/timePickerLayout")[0]
    #     startPicker.send_keys(startHour1)
    #     self.driver.find_element_by_id("com.view.viewglass:id/ends_schdSceneTintTV").click()
    #     endPicker = self.driver.find_elements(By.ID, "android:id/timePickerLayout")[0]
    #     endPicker.send_keys(endHour)
    #     commonFunctions.savebutton(self.driver)
    #
    #     if WebDriverWait(self.driver, 20).until(
    #             EC.presence_of_element_located((By.ID, "com.view.viewglass:id/schedule_scene_TV"))):
    #         self.driver.find_element_by_id("com.view.viewglass:id/schedule_scene_TV").click()
    #     else:
    #         raiseExceptions("Schedule Scene button is missing")
    #
    #     self.driver.find_element_by_id("com.view.viewglass:id/starts_schdSceneTintTV").click()
    #     startPicker = self.driver.find_elements(By.ID, "android:id/timePickerLayout")[0]
    #     startPicker.send_keys(startHour2)
    #     self.driver.find_element_by_id("com.view.viewglass:id/ends_schdSceneTintTV").click()
    #     endPicker = self.driver.find_elements(By.ID, "android:id/timePickerLayout")[0]
    #     endPicker.send_keys(endHour)
    #     commonFunctions.savebutton(self.driver)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Scenes)
    unittest.TextTestRunner(verbosity=2).run(suite)


