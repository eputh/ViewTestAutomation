import random
from logging import raiseExceptions
from datetime import datetime
from datetime import timedelta

from selenium.webdriver.common.by import By
from common import commonFunctions


"""
Helper functions for Zones
"""


def selectTopZonegroup(driver):
    if len(driver.find_elements(By.ID, "com.view.viewglass:id/listItem_parentLL")) > 0:
        size = driver.find_element_by_xpath("//android.widget.TextView[@text='ZONE GROUPS']").size
        location = driver.find_element_by_xpath("//android.widget.TextView[@text='ZONE GROUPS']").location
        x = location['x'] + size['width']
        y = location['y'] * 2
        driver.tap([(x, y)])
    else:
        raiseExceptions("The list of zonegroups is empty")


"""
Helper functions for Scenes
"""


def selectRandomTint(driver):
    r = random.randint(1, 4)
    if r == 1:
        driver.find_element_by_id("com.view.viewglass:id/tint1_selectTintLL").click()
    elif r == 2:
        driver.find_element_by_id("com.view.viewglass:id/tint2_selectTintLL").click()
    elif r == 3:
        driver.find_element_by_id("com.view.viewglass:id/tint3_selectTintLL").click()
    elif r == 4:
        driver.find_element_by_id("com.view.viewglass:id/tint4_selectTintLL").click()
    return r

