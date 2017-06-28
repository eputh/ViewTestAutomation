import random
from logging import raiseExceptions
from datetime import datetime
from datetime import timedelta
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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


def quickCreateZonegroup(driver, zonegroup):
    commonFunctions.addbutton(driver)
    if WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "com.view.viewglass:id/title_createZoneGrpTV"))):
        pass
    else:
        raiseExceptions("Add button led to the wrong screen")

    if len(driver.find_elements(By.ID, "com.view.viewglass:id/name_createZoneGrp_addETV")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/name_createZoneGrp_addETV").send_keys("abc")
        firstZone = driver.find_elements(By.ID, "com.view.viewglass:id/zone_item_select_zoneTV")[0]
        firstZone.click()
        commonFunctions.savebutton(driver)
    else:
        raiseExceptions("Name text field is missing")

    foundCreatedZonegroup = False
    if len(driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")) > 0:
        zonegroups = driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")
        for group in zonegroups:
            if group.text == zonegroup:
                foundCreatedZonegroup = True
    if not foundCreatedZonegroup:
        raiseExceptions("Zonegroup 'abc' was not created")


def findZonegroup(driver, zonegroup):
    foundZonegroup = False
    if len(driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")) > 0:
        zonegroups = driver.find_elements(By.ID, "com.view.viewglass:id/listItemNameTV")
        for group in zonegroups:
            if group.text == zonegroup:
                foundZonegroup = True
                group.click()
                break
    return foundZonegroup


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

