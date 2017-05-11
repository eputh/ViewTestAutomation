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

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from logging import raiseExceptions
from datetime import datetime
from time import sleep


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
        driver.find_element_by_xpath("//android.widget.TextView[@text='" + site + "']").click()
    else:
        raiseExceptions("Missing Search option in Change Site")

    if WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@text='Yes']"))):
        driver.find_element_by_xpath("//android.widget.Button[@text='Yes']").click()
    else:
        raiseExceptions("confirmation message for changing tint is missing")
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
    else:
        raiseExceptions("Back button is missing")


def savebutton(driver):
    if len(driver.find_elements(By.XPATH, "//android.widget.TextView[@text='Save']")) > 0:
        driver.find_element_by_xpath("//android.widget.TextView[@text='Save']").click()


def addbutton(driver):
    if len(driver.find_elements(By.ID, "com.view.viewglass:id/add_schdIV")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/add_schdIV").click()
    else:
        raiseExceptions("Add button is missing")


def editbutton(driver):
    if len(driver.find_elements(By.ID, "com.view.viewglass:id/saveBtn_schdTintTV")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/saveBtn_schdTintTV").click()
    elif len(driver.find_elements(By.XPATH, "//android.widget.TextView[@text='Edit']")) > 0:
        driver.find_element_by_xpath("//android.widget.TextView[@text='Edit']").click()


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


"""
Helper functions to navigate through LiveView
"""


def checkLiveViewAccess(driver):
    if len(driver.find_elements(By.ID, "com.view.viewglass:id/noLiveView_liveViewTV")) > 0:
        print("Live View Data not available")
        # change site? find a zone with accessible zone data?
        changeSite(driver, "APPCloudTest1")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "com.view.viewglass:id/zoneSelector_liveViewTV")))
        driver.find_element_by_id("com.view.viewglass:id/zoneSelector_liveViewTV").click()
        x = driver.find_element_by_class_name("android.widget.RelativeLayout").size['width'] + 10
        y = driver.find_element_by_class_name("android.widget.RelativeLayout").location['y'] + 10
        driver.tap([(x, y)])
