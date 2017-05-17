"""
########################################################################
#
# SYNOPSIS
#   Auth module :  Include modules related to authentication 
#
# AUTHOR
#  Prinal khandelwal (Pkhandelwal@viewglass.com)
#
#
# DESCRIPTION
#   Include all the functions related to authentication
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

from logging import raiseExceptions
from time import sleep

from common import commonFunctions as common
from common import site as site
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from common import config as config


def isUserLoggedIn(driver):
    sleep(30)
    try:
        if len(driver.find_elements(By.ID, "com.view.viewglass:id/retry_btn")) > 0:
            driver.find_element_by_id("com.view.viewglass:id/retry_btn").click()
        if WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='LOGIN']"))):
            return False
    except TimeoutException:
        return True


def checkIfUserIsLoggedIn(driver, loginbool, user):
    """ Check if user needs to be logged in or logged out"""
    # user needs to be logged in
    if loginbool:
        if not isUserLoggedIn(driver):
            login(driver, config.users[user]['username'], config.users[user]['password'])
            site.selectSite(driver, config.site[0])
            sleep(20)

        if common.foundAlert(driver):
            common.respondToAlert(driver, 0)
        if common.foundTour(driver):
            common.exitTour(driver)
        if len(driver.find_elements(By.ID, "com.view.viewglass:id/view_btnTV")) > 0:
            common.navIcon(driver)
    # User needs to be logged out
    else:
        if isUserLoggedIn(driver):
            if common.foundAlert(driver):
                common.respondToAlert(driver, 0)
            if common.foundTour(driver):
                common.exitTour(driver)
            logout(driver)
            sleep(20)
        else:
            sleep(20)


def login(driver, username, password):
    attempts = 0
    while attempts <= 3:
        if len(driver.find_elements(By.ID, "com.view.viewglass:id/retry_btn")) > 0:
            driver.find_element_by_id("com.view.viewglass:id/retry_btn").click()
            attempts += 1

        if WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@index='0']"))):
            # some devices have trouble navigating to the username text field
            location = driver.find_element_by_id("com.view.viewglass:id/web_view_LL").location
            size = driver.find_element_by_id("com.view.viewglass:id/web_view_LL").size
            x = location['x'] + size['width'] / 2
            y = location['y'] + 240
            driver.tap([(x, y)])

            email = driver.find_element_by_xpath("//android.widget.EditText[@index='0']")
            text = email.text
            if text == "Email":
                email.send_keys(username)
            elif text == username:
                pass
            else:
                email.clear()
                email.send_keys(username)
        else:
            raiseExceptions("Missing Email text field")

        if WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@index='2']"))):
            # some devices have trouble navigating to the password text field
            location = driver.find_element_by_id("com.view.viewglass:id/web_view_LL").location
            size = driver.find_element_by_id("com.view.viewglass:id/web_view_LL").size
            x = location['x'] + size['width'] / 2
            y = location['y'] + 260 + driver.find_element_by_xpath("//android.widget.EditText[@index='2']").size['height']
            driver.tap([(x, y)])

            pw = driver.find_element_by_xpath("//android.widget.EditText[@index='2']")
            pw.send_keys(password)
        else:
            raiseExceptions("Missing Password text field")

        if WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "android.widget.CheckBox"))):
            rememberMe = driver.find_element_by_class_name("android.widget.CheckBox")
            if rememberMe.get_attribute("checked") == "false":
                rememberMe.click()
            else:
                # close the keyboard to make the login button visible
                driver.find_element_by_xpath("//android.view.View[@index='3']").click()
        else:
            raiseExceptions("Missing Remember Me check box")

        if WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='LOGIN']"))):
            # some devices have trouble navigating to the login button

            location = driver.find_elements(By.CLASS_NAME, "android.webkit.WebView")[0].location
            size = driver.find_elements(By.CLASS_NAME, "android.webkit.WebView")[0].size
            x = location['x'] + size['width'] / 2
            y = location['y'] + size['height'] - driver.find_element_by_xpath("//android.widget.Button[@content-desc='LOGIN']").size['height']
            driver.tap([(x, y-100)])
            driver.tap([(x, y)])

            if len(driver.find_elements(By.XPATH, "//android.widget.Button[@content-desc='LOGIN']")) > 0:
                driver.find_element_by_xpath("//android.widget.Button[@content-desc='LOGIN']").click()
            sleep(20)
        else:
            raiseExceptions("Missing Login button")

        if len(driver.find_elements(By.ID, "com.view.viewglass:id/retry_btn")) > 0:
            driver.find_element_by_id("com.view.viewglass:id/retry_btn").click()
            attempts += 1
        else:
            break


def loginScreenValidations(driver):
    if len(driver.find_elements(By.XPATH, "//android.view.View[@content-desc='User Authentication Failed']")) > 0:
        pass
    elif len(driver.find_elements(By.XPATH, "//android.widget.Button[@content-desc='LOGIN']")) > 0:
        pass
    else:
        raiseExceptions("Missing login Screen Exceptional handling")


def logout(driver):
    if common.foundAlert(driver):
        common.respondToAlert(driver, 0)
    common.navIcon(driver)
    if len(driver.find_elements(By.ID, "com.view.viewglass:id/username_navigationTV")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/username_navigationTV").click()
    else:
        raiseExceptions("Missing user profile option in navigation bar")
    if len(driver.find_elements(By.XPATH, "//android.widget.TextView[@text='Sign Out']")) > 0:
        driver.find_element_by_xpath("//android.widget.TextView[@text='Sign Out']").click()
    else:
        raiseExceptions("Missing Sign Out button")


def signout(driver):
    if WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@resource-id='com.view.viewglass:id/button_cancel']"))):
        driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.view.viewglass:id/button_cancel']").click()
    else:
        raiseExceptions("Missing Sign Out button in Select Site screen")


def negativeTestCaseLoginValidation(driver, username, password):
    if WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@index='0']"))):
        email = driver.find_element_by_xpath("//android.widget.EditText[@index='0']")
        text = email.text
        if text == "Email":
            email.send_keys(username)
        elif text == username:
            pass
        else:
            email.clear()
            email.send_keys(username)
    else:
        print("Invalid username validation ")

    if WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@index='2']"))):
        pw = driver.find_element_by_xpath("//android.widget.EditText[@index='2']")
        pw.send_keys(password)
    else:
        print("Invalid password validation ")

    if WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "android.widget.CheckBox"))):
        rememberMe = driver.find_element_by_class_name("android.widget.CheckBox")
        if rememberMe.get_attribute("checked") == "false":
            rememberMe.click()
        else:
            # close the keyboard to make the login button visible
            driver.find_element_by_xpath("//android.view.View[@index='3']").click()
    else:
        print("Remember me validation ")

    if WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='LOGIN']"))):
        driver.find_element_by_xpath("//android.widget.Button[@content-desc='LOGIN']").click()
    else:
        print("Login button validation ")

