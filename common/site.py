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

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from logging import raiseExceptions
from datetime import datetime
from time import sleep


def selectSite(driver, site):
    if WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.ID, "com.view.viewglass:id/search_image_view"))):
        search = driver.find_element_by_id("com.view.viewglass:id/search_image_view")
        search.click()
        search_text = driver.find_element_by_id("com.view.viewglass:id/search_site_edit_text")
        # search for the site and press ENTER
        search_text.send_keys(site)
        # self.driver.press_keycode(66)
        size = driver.find_element_by_id("com.view.viewglass:id/siteList_searchResultCountTV").size
        location = driver.find_element_by_id("com.view.viewglass:id/siteList_searchResultCountTV").location
        x = size['width']/2
        y = location['y'] + size['height'] * 3
        driver.tap([(x, y)])
    else:
        raiseExceptions("Failed to reach Select Site screen")

def getSiteList(driver):
    # assuming the space from the top of the siteListView to the first
    # site listed is the same size (height) as the heading/logo, get heading height
    headingHeight = driver.find_element_by_id("com.view.viewglass:id/viewLogoLL").size['height']