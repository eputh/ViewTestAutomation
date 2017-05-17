"""
########################################################################
#
# SYNOPSIS
#   commonly used module :  include modules related to generic functions 
#                           in selecting a site
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
import datetime

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from logging import raiseExceptions
from datetime import datetime
from time import sleep

from common import commonFunctions


def selectSite(driver, site):
    try:
        WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.ID, "com.view.viewglass:id/search_image_view")))
        search = driver.find_element_by_id("com.view.viewglass:id/search_image_view")
        search.click()
        search_text = driver.find_element_by_id("com.view.viewglass:id/search_site_edit_text")
        # search for the site and press ENTER
        search_text.send_keys(site)
        # self.driver.press_keycode(66)
        size = driver.find_element_by_id("com.view.viewglass:id/viewLogoLL").size
        location = driver.find_element_by_id("com.view.viewglass:id/viewLogoLL").location
        x = size['width']/2
        y = location['y'] + size['height'] * 2
        driver.tap([(x, y)])
        if len(driver.find_elements(By.ID, "com.view.viewglass:id/viewLogoLL")) > 0:
            y = location['y'] + size['height'] * 2.5
            driver.tap([(x, y)])
    except TimeoutException:
        raiseExceptions("Failed to reach Select Site screen")


def changeSite(driver, site):
    commonFunctions.navIcon(driver)
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
    commonFunctions.goback(driver)
    commonFunctions.navIcon(driver)