"""
########################################################################
#
# SYNOPSIS
#   commonly used module :  include modules related to generic functions 
#
# AUTHOR
#  Emily Puth (emily.puth@viewglass.com)
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
from logging import raiseExceptions

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from common import commonFunctions as common

"""
Helper functions for creating schedules
"""


def changeTint(driver):
    tint_level = common.generateRandomNumber(1, 4)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='Tint Level']")))
    driver.find_element_by_xpath("//android.widget.TextView[@text='Tint Level']").click()
    driver.find_element_by_xpath("//android.widget.TextView[@text='" + tint_level + "']").click()


def changeRepeat(driver, repeat):
    driver.find_element_by_xpath("//*[@id='repeats_value_schdSceneTintTV']").click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@text='" + repeat + "']")))
    driver.find_element_by_xpath("//android.widget.TextView[@text='" + repeat + "']").click()


"""
Helper functions for navigating through the control ring
"""


def getControlRingWidthAndHeight(driver):
    size = driver.find_element_by_id("com.view.viewglass:id/control_parentLL").size
    controlRingWidth = size['width']
    controlRingHeight = size['height']
    return [controlRingWidth, controlRingHeight]


def getControlRingLocation(driver):
    location = driver.find_element_by_id("com.view.viewglass:id/control_parentLL").location
    xLocation = location['x']
    yLocation = location['y']
    return [xLocation, yLocation]


def getTint1(driver):
    controlRingWidthAndHeight = getControlRingWidthAndHeight(driver)
    controlRingLocation = getControlRingLocation(driver)
    width = int(controlRingWidthAndHeight[0])
    height = int(controlRingWidthAndHeight[1])
    xLocation = width / 4 + int(controlRingLocation[0])
    yLocation = height / 4 * 3 + int(controlRingLocation[1])
    return [xLocation, yLocation]


def getTint2(driver):
    controlRingWidthAndHeight = getControlRingWidthAndHeight(driver)
    controlRingLocation = getControlRingLocation(driver)
    width = int(controlRingWidthAndHeight[0])
    height = int(controlRingWidthAndHeight[1])
    xLocation = width / 4 + int(controlRingLocation[0])
    yLocation = height / 4 + int(controlRingLocation[1])
    return [xLocation, yLocation]


def getTint3(driver):
    controlRingWidthAndHeight = getControlRingWidthAndHeight(driver)
    controlRingLocation = getControlRingLocation(driver)
    width = int(controlRingWidthAndHeight[0])
    height = int(controlRingWidthAndHeight[1])
    xLocation = width / 4 * 3 + int(controlRingLocation[0])
    yLocation = height / 4 + int(controlRingLocation[1])
    return [xLocation, yLocation]


def getTint4(driver):
    controlRingWidthAndHeight = getControlRingWidthAndHeight(driver)
    controlRingLocation = getControlRingLocation(driver)
    width = int(controlRingWidthAndHeight[0])
    height = int(controlRingWidthAndHeight[1])
    xLocation = width / 4 * 3 + int(controlRingLocation[0])
    yLocation = height / 4 * 3 + int(controlRingLocation[1])
    return [xLocation, yLocation]


def clickTintLevelNum(driver):
    if len(driver.find_elements(By.ID, "com.view.viewglass:id/tintImage_controlIV")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/tintImage_controlIV").click()
        if common.foundAlert(driver):
            common.respondToAlert(driver, 1)
    elif len(driver.find_elements(By.ID, "com.view.viewglass:id/tintLevelNum_controlTV")) > 0:
        pass
    else:
        raiseExceptions("tint image at the center of the control ring is missing")


def getCurrentTint(driver):
    if len(driver.find_elements(By.ID, "com.view.viewglass:id/tintImage_controlIV")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/tintImage_controlIV").click()
        if common.foundAlert(driver):
            common.respondToAlert(driver, 1)
    elif len(driver.find_elements(By.ID, "com.view.viewglass:id/tintLevelNum_controlTV")) > 0:
        pass
    else:
        raiseExceptions("tint image at the center of the control ring is missing")
    currentTint = driver.find_element_by_id("com.view.viewglass:id/tintLevelNum_controlTV").text
    return currentTint


def verifyValidTintFound(driver, tint):
    tintStr = "//android.widget.TextView[@text='" + str(tint) + "']"
    print(tintStr)
    if len(driver.find_elements(By.ID, "com.view.viewglass:id/tintImage_controlIV")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/tintImage_controlIV").click()
        if common.foundAlert(driver):
            common.respondToAlert(driver, 1)
        driver.find_element_by_xpath(tintStr)
    elif len(driver.find_elements(By.ID, "com.view.viewglass:id/tintLevelNum_controlTV")) > 0:
        driver.find_element_by_xpath(tintStr)
    else:
        raiseExceptions("displayed tint is incorrect")


def verifyInvalidTintsNotFound(driver, tint):
    if len(driver.find_elements(By.ID, "com.view.viewglass:id/tintImage_controlIV")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/tintImage_controlIV").click()
        if common.foundAlert(driver):
            common.respondToAlert(driver, 1)
    elif len(driver.find_elements(By.ID, "com.view.viewglass:id/tintLevelNum_controlTV")) > 0:
        pass
    else:
        raiseExceptions("tint image at the center of the control ring is missing")

    for i in range(1, 5):
        if i != tint:
            tintStr = "//android.widget.TextView[@text='" + str(i) + "']"
            assert len(driver.find_elements(By.XPATH, tintStr)) == 0, "incorrect tint was found"


def selectTint(driver, t):
    t = int(t)
    tint = getTint1(driver)
    if t == 1:
        tint = getTint1(driver)
    elif t == 2:
        tint = getTint2(driver)
    elif t == 3:
        tint = getTint3(driver)
    elif t == 4:
        tint = getTint4(driver)
    driver.tap([(tint[0], tint[1])])
    common.overridebutton(driver)


def selectRandomTint(driver):
    r = random.randint(1, 4)
    tint = getTint1(driver)
    if r == 1:
        tint = getTint1(driver)
    elif r == 2:
        tint = getTint2(driver)
    elif r == 3:
        tint = getTint3(driver)
    elif r == 4:
        tint = getTint4(driver)
    driver.tap([(tint[0], tint[1])])
    common.overridebutton(driver)
    return r


# def create_schedule(driver, repeat):
#     # navigate to the SCHEDULE screen
#     navigation = driver.find_element_by_id("com.view.viewglass:id/home_controlIV")
#     navigation.click()
#     schedule = driver.find_element_by_id("com.view.viewglass:id/navigation_scheduleTV")
#     schedule.click()
#     add_schedule = driver.find_element_by_id("com.view.viewglass:id/add_schdIV")
#     add_schedule.click()
#     # select tint level (1 in this case)
#     driver.find_element_by_id("com.view.viewglass:id/tint_level_value_schdSceneTintTV").click()
#     driver.find_element_by_id("com.view.viewglass:id/sel_schdSceneTintCircle1TV").click()
#     # select repeat
#     driver.find_element_by_id("com.view.viewglass:id/repeats_schdSceneTintTV").click()
#     driver.find_element_by_name(repeat).click()
#     # Line below: used to save the schedule being created
#     # driver.find_element_by_id("com.view.viewglass:id/saveBtn_schdTintTV").click()
#
#     # The current site "APPCloudTest1" does not allow for new schedules to be saved, so the
#     # line below presses the back button and proceeds with the rest of the test case
#     driver.find_element_by_id("com.view.viewglass:id/backBtn_schdTintTV").click()
#
#
# def change_tint(driver):
#     # navigate to CONTROL
#     navigation = driver.find_element_by_id("com.view.viewglass:id/home_controlIV")
#     navigation.click()
#     control = driver.find_element_by_id("com.view.viewglass:id/navigation_controlTV")
#     control.click()
#     sleep(5)
#     # select the tint level (2 in this case) - this is based on its location on the screen
#     driver.swipe(270, 900, 270, 900, 3)
#     # approve of override
#     driver.find_element_by_id("com.view.viewglass:id/tick_button_controlLL").click()
#
