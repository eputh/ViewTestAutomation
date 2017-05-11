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

from common import commonFunctions

"""
Helper functions for creating schedules
"""


def changeTint(driver):
    tint_level = commonFunctions.generateRandomNumber(1, 4)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='Tint Level']")))
    driver.find_element_by_xpath("//android.widget.TextView[@text='Tint Level']").click()
    driver.find_element_by_xpath("//android.widget.TextView[@text='" + tint_level + "']").click()


def changeRepeat(driver, repeat):
    driver.find_element_by_xpath("//*[@id='repeats_value_schdSceneTintTV']").click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@text='" + repeat + "']")))
    driver.find_element_by_xpath("//android.widget.TextView[@text='" + repeat + "']").click()


def quickCreateSchedule(driver):
    if WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "com.view.viewglass:id/add_schdIV"))):
        commonFunctions.addbutton(driver)
        changeTint(driver)
        commonFunctions.savebutton(driver)
    else:
        raiseExceptions("add schedule button is missing")

    if commonFunctions.foundAlert(driver):
        commonFunctions.respondToAlert(driver, 1)
        commonFunctions.goback(driver)


def deleteSchedule(driver, schedule):
    print(schedule.size, schedule.location)
    size = schedule.size
    location = schedule.location
    x = location['x'] + size['width'] - 10
    y = location['y'] + 10
    driver.tap([(x, y)])

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
        if commonFunctions.foundAlert(driver):
            commonFunctions.respondToAlert(driver, 1)
    elif len(driver.find_elements(By.ID, "com.view.viewglass:id/tintLevelNum_controlTV")) > 0:
        pass
    else:
        raiseExceptions("tint image at the center of the control ring is missing")


def getCurrentTint(driver):
    if len(driver.find_elements(By.ID, "com.view.viewglass:id/tintImage_controlIV")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/tintImage_controlIV").click()
        if commonFunctions.foundAlert(driver):
            commonFunctions.respondToAlert(driver, 1)
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
        if commonFunctions.foundAlert(driver):
            commonFunctions.respondToAlert(driver, 1)
        driver.find_element_by_xpath(tintStr)
    elif len(driver.find_elements(By.ID, "com.view.viewglass:id/tintLevelNum_controlTV")) > 0:
        driver.find_element_by_xpath(tintStr)
    else:
        raiseExceptions("displayed tint is incorrect")


def verifyInvalidTintsNotFound(driver, tint):
    if len(driver.find_elements(By.ID, "com.view.viewglass:id/tintImage_controlIV")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/tintImage_controlIV").click()
        if commonFunctions.foundAlert(driver):
            commonFunctions.respondToAlert(driver, 1)
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
    commonFunctions.overridebutton(driver)


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
    commonFunctions.overridebutton(driver)
    return r
