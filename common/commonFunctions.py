# -*- coding: utf-8 -*- 
"""
########################################################################
#
# SYNOPSIS
#   commonly used module :  include modules related to generic functions 
#
# AUTHOR
#  Prinal khandelwal (Pkhandelwal@viewglass.com)
#
#
# DESCRIPTION
#   Include modules related to generic functions which is used by any or all the functionalities
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

import random
import datetime
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from logging import raiseExceptions
from datetime import datetime
from time import sleep

from common import config
from common import control


def changeSite(driver, site):
    navIcon(driver)
    driver.find_element_by_id("username_navigationTV").click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='Change Site']")))
    driver.find_element_by_xpath("//android.widget.TextView[@text='Change Site']").click()
    if len(driver.find_elements(By.ID, "com.view.viewglass:id/search_layout")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/search_layout").click()
        search = driver.find_element_by_xpath("//android.widget.EditText[@text='Search']")
        search.send_keys(site)
        driver.find_element_by_id("com.view.viewglass:id/zone_item_select_zoneTV").click()
    else:
        raiseExceptions("Missing Search option in Change Site")

    if WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@text='Yes']"))):
        driver.find_element_by_xpath("//android.widget.Button[@text='Yes']").click()
    else:
        raiseExceptions("confirmation message for changing site is missing")
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "com.view.viewglass:id/home_btn_myProfileLL")))
    goback(driver)
    navIcon(driver)


def navIcon(driver):
    if len(driver.find_elements(By.ID, "com.view.viewglass:id/home_controlIV")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/home_controlIV").click()
    elif len(driver.find_elements(By.ID, "com.view.viewglass:id/home_zonesIV")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/home_zonesIV").click()
    elif len(driver.find_elements(By.ID, "com.view.viewglass:id/homeBtnLiveViewLL")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/homeBtnLiveViewLL").click()
    elif len(driver.find_elements(By.ID, "com.view.viewglass:id/home_schdIV")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/home_schdIV").click()
    elif len(driver.find_elements(By.ID, "com.view.viewglass:id/menuBtn_scene")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/menuBtn_scene").click()


def goback(driver):
    if len(driver.find_elements(By.ID, "com.view.viewglass:id/backBtn_schdTintTV")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/backBtn_schdTintTV").click()
    elif len(driver.find_elements(By.ID, "com.view.viewglass:id/backBtn_allZonesSelectLL']")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/backBtn_allZonesSelectLL']").click()
    elif len(driver.find_elements(By.ID, "com.view.viewglass:id/backBtn_schdSTintLL']")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/backBtn_schdSTintLL']").click()
    elif len(driver.find_elements(By.ID, "com.view.viewglass:id/home_btn_myProfileLL")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/home_btn_myProfileLL").click()
    elif len(driver.find_elements(By.ID, "com.view.viewglass:id/back_copy_tint_eventIV")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/back_copy_tint_eventIV").click()
    elif len(driver.find_elements(By.ID, "com.view.viewglass:id/back_btn_create_newZoneGrpIV")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/back_btn_create_newZoneGrpIV").click()
    elif len(driver.find_elements(By.ID, "com.view.viewglass:id/backBtn_zngrpdetailLL")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/backBtn_zngrpdetailLL").click()
    elif len(driver.find_elements(By.ID, "com.view.viewglass:id/back_scene_detailLL")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/back_scene_detailLL").click()
    elif len(driver.find_elements(By.ID, "com.view.viewglass:id/back_scene_eventLL")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/back_scene_eventLL").click()
    elif len(driver.find_elements(By.ID, "com.view.viewglass:id/back_btn_settingIV")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/back_btn_settingIV").click()
    elif len(driver.find_elements(By.ID, "com.view.viewglass:id/back_btn_settingscreenIV")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/back_btn_settingscreenIV").click()
    else:
        raiseExceptions("Back button is missing")


def savebutton(driver):
    if len(driver.find_elements(By.XPATH, "//android.widget.TextView[@text='Save']")) > 0:
        driver.find_element_by_xpath("//android.widget.TextView[@text='Save']").click()
    elif len(driver.find_elements(By.ID, "com.view.viewglass:id/save_zoneGrpTV")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/save_zoneGrpTV").click()
    elif len(driver.find_elements(By.ID, "com.view.viewglass:id/editbtn_sceneTV")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/editbtn_sceneTV").click()
    elif len(driver.find_elements(By.ID, "com.view.viewglass:id/save_scene_add_TintEventTV")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/save_scene_add_TintEventTV").click()
    elif len(driver.find_elements(By.ID, "com.view.viewglass:id/savebtn_sceneEventTV")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/savebtn_sceneEventTV").click()
    else:
        raiseExceptions("Save button is missing")

def addbutton(driver):
    if len(driver.find_elements(By.ID, "com.view.viewglass:id/add_schdIV")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/add_schdIV").click()
    elif len(driver.find_elements(By.ID, "com.view.viewglass:id/actZone_addIV")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/actZone_addIV").click()
    elif len(driver.find_elements(By.ID, "com.view.viewglass:id/scene_addIconIV")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/scene_addIconIV").click()
    else:
        raiseExceptions("Add button is missing")


def editbutton(driver):
    if len(driver.find_elements(By.ID, "com.view.viewglass:id/saveBtn_schdTintTV")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/saveBtn_schdTintTV").click()
    elif len(driver.find_elements(By.XPATH, "//android.widget.TextView[@text='Edit']")) > 0:
        driver.find_element_by_xpath("//android.widget.TextView[@text='Edit']").click()
    elif len(driver.find_elements(By.ID, "com.view.viewglass:id/editZoneGrpTextTV")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/editZoneGrpTextTV").click()
    elif len(driver.find_elements(By.ID, "com.view.viewglass:id/editbtn_sceneTV")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/editbtn_sceneTV").click()
    else:
        raiseExceptions("Edit button is missing")

def cancelbutton(driver):
    if len(driver.find_elements(By.ID, "com.view.viewglass:id/cross_btn_controlLL")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/cross_btn_controlLL").click()
    elif len(driver.find_elements(By.XPATH, "//android.widget.TextView[@text='CANCEL']")) > 0:
        driver.find_element_by_xpath("//android.widget.TextView[@text='CANCEL']").click()
    else:
        raiseExceptions("cancel button is missing")


def overridebutton(driver):
    if len(driver.find_elements(By.ID, "com.view.viewglass:id/tick_button_controlLL")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/tick_button_controlLL").click()
    elif len(driver.find_elements(By.XPATH, "//android.widget.TextView[@text='OVERRIDE']")) > 0:
        driver.find_element_by_xpath("//android.widget.TextView[@text='OVERRIDE']").click()
    elif len(driver.find_elements(By.ID, "com.view.viewglass:id/setTintBtn_zngrpdetailTV")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/setTintBtn_zngrpdetailTV").click()
    elif len(driver.find_elements(By.ID, "com.view.viewglass:id/setTint_zoneDetailTV")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/setTint_zoneDetailTV").click()
    else:
        raiseExceptions("override button is missing")


def foundConnectToSiteError(driver):
    try:
        driver.find_element_by_xpath("//*[@text='Site is not reachable. Please try again later or contact Facilities Manager or View Support at support@viewglass.com or (855)-478-8468']")
        print("unable to connect to selected site")
    except NoSuchElementException:
        print("no connect to site error")


def foundAlert(driver):
    if len(driver.find_elements(By.XPATH, "//android.widget.TextView[@text='Recently Crashed!!!']")) > 0:
        return True
    elif len(driver.find_elements(By.XPATH, "com.view.viewglass:id/mobile_data_select_tv_header")) > 0:
        return True
    elif len(driver.find_elements(By.XPATH, "//*[@id='alertDlg_tv_header']")) > 0:
        return True
    elif len(driver.find_elements(By.XPATH, "//*[@text='Info']")) > 0:
        return True
    elif len(driver.find_elements(By.XPATH, "//*[@text='Error']")) > 0:
        return True
    elif len(driver.find_elements(By.XPATH, "//*[@id='mobile_data_select_tv_header']")) > 0:
        return True
    elif len(driver.find_elements(By.XPATH, "//*[@id='dialogTitleTV']")) > 0:
        return True
    return False


def respondToAlert(driver, response):
    if response == 0:
        if len(driver.find_elements(By.XPATH, "//*[@id='alertDlg_cancelBtn']")) > 0:
            driver.find_element_by_xpath("//*[@id='alertDlg_cancelBtn']").click()
        elif len(driver.find_elements(By.XPATH, "//*[@text='NO']")) > 0:
            driver.find_element_by_xpath("//*[@text='NO']").click()
        elif len(driver.find_elements(By.XPATH, "//*[@text='CANCEL']")) > 0:
            driver.find_element_by_xpath("//*[@text='CANCEL']").click()
    elif response == 1:
        if len(driver.find_elements(By.XPATH, "//*[@id='alertDlg_okBtn']")) > 0:
            driver.find_element_by_xpath("//*[@id='alertDlg_okBtn']").click()
        elif len(driver.find_elements(By.XPATH, "//*[@text='YES']")) > 0:
            driver.find_element_by_xpath("//*[@text='YES']").click()
        elif len(driver.find_elements(By.XPATH, "//*[@text='OK']")) > 0:
            driver.find_element_by_xpath("//*[@text='OK']").click()
        elif len(driver.find_elements(By.XPATH, "//*[@text='Ok']")) > 0:
            driver.find_element_by_xpath("//*[@text='Ok']").click()


def foundTour(driver):
    if len(driver.find_elements(By.ID, "com.view.viewglass:id/exit_btn")) > 0:
        return True
    else:
        return False


def exitTour(driver):
    driver.find_element_by_id("com.view.viewglass:id/exit_btn").click()


def generateRandomNumber(min, max):
    return str(random.randint(min, max))


def getToday():
    today = datetime.now()
    return today.day


def findAnyOneOfTheseElements(driver, listOfTupleElements):
    for locator in listOfTupleElements:
        if len(driver.find_elements(eval("By." + locator[0]), locator[1])) > 0:
            print("Found: ", locator[1])
            return True
    return False


def waitForElement(driver, listOfTupleElements, timeout):
    start = time.time()
    while (time.time() - start) < timeout:
        if findAnyOneOfTheseElements(driver, listOfTupleElements):
            return True
    raiseExceptions("Neither one of the elements given were found.")


"""
Helper functions to navigate through LiveView
"""


def checkLiveViewAccess(driver):
    if len(driver.find_elements(By.ID, "com.view.viewglass:id/noLiveView_liveViewTV")) > 0:
        print("Live View Data not available")
        # change site? find a zone with accessible zone data?
        # changeSite(driver, config.site[2])
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.ID, "com.view.viewglass:id/zoneSelector_liveViewTV")))
        # driver.find_element_by_id("com.view.viewglass:id/zoneSelector_liveViewTV").click()
        # x = driver.find_element_by_class_name("android.widget.RelativeLayout").size['width'] + 10
        # y = driver.find_element_by_class_name("android.widget.RelativeLayout").location['y'] + 10
        # driver.tap([(x, y)])

        selectedZone = driver.find_element_by_id("com.view.viewglass:id/zoneSelector_liveViewTV").text
        navIcon(driver)
        if WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_controlTV"))):
            driver.find_element_by_id("com.view.viewglass:id/navigation_controlTV").click()
        else:
            raiseExceptions("Control option in navigation menu is missing")
        driver.find_element_by_id("com.view.viewglass:id/selected_zone_name_controlTV").click()
        driver.find_element_by_id("com.view.viewglass:id/search_ImageView").click()
        driver.find_element_by_id("com.view.viewglass:id/control_searchETV").send_keys(selectedZone)
        results = driver.find_elements(By.ID, "com.view.viewglass:id/exapdChildTitle")
        for r in results:
            if r.text == selectedZone:
                r.click()
        control.selectRandomTint(driver)
        overridebutton(driver)

        navIcon(driver)
        if WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.view.viewglass:id/navigation_live_viewTV"))):
            driver.find_element_by_id("com.view.viewglass:id/navigation_live_viewTV").click()
        else:
            raiseExceptions("LiveView option in navigation menu is missing")
