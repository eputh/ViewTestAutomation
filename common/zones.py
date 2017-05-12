import random
from logging import raiseExceptions

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from common import commonFunctions


def selectTopZonegroup(driver):
    if len(driver.find_elements(By.ID, "com.view.viewglass:id/listItem_parentLL")) > 0:
        size = driver.find_element_by_xpath("//android.widget.TextView[@text='ZONE GROUPS']").size
        location = driver.find_element_by_xpath("//android.widget.TextView[@text='ZONE GROUPS']").location
        x = location['x'] + size['width']
        y = location['y'] * 2
        driver.tap([(x, y)])
    else:
        raiseExceptions("The list of zonegroups is empty")
