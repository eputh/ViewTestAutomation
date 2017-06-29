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

from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from common import commonFunctions as common
from common import site as site
from common import config as config


def isUserLoggedIn(driver):
    sleep(20)
    if len(driver.find_elements(By.ID, "com.view.viewglass:id/retry_btn")) > 0:
        driver.find_element_by_id("com.view.viewglass:id/retry_btn").click()
    try:
        findElements = [("XPATH", "//android.widget.Button[@content-desc='Login']"), ("XPATH", "//android.widget.TextView[@text='Recently Crashed!!!']"), ("ID", "com.view.viewglass:id/home_controlIV")]
        common.waitForElement(driver, findElements, 120)
        if len(driver.find_elements(By.ID, "com.view.viewglass:id/home_controlIV")) > 0 or len(driver.find_elements(By.XPATH, "//android.widget.TextView[@text='Recently Crashed!!!']")) > 0:
            return True
        elif len(driver.find_elements(By.XPATH, "//android.widget.Button[@content-desc='Login']")) > 0:
            return False
    except TimeoutException:
        if len(driver.find_elements(By.XPATH, "//android.widget.TextView[@text='Authenticating, Please wait..']")) > 0:
            print("Found authenticating progress")
        raiseExceptions("Loading the app has taken too long (over 2 minutes)")


def checkIfUserIsLoggedIn(driver, loginbool, user):
    """ Check if user needs to be logged in or logged out"""
    # user needs to be logged in
    isLoggedIn = isUserLoggedIn(driver)
    print("Logged in: ", isLoggedIn)
    if loginbool:
        if not isLoggedIn and user == 'RO':
            login(driver, config.users[user]['username'], config.users[user]['password'])
        elif not isLoggedIn:
            loginAndSelectSite(driver, config.users[user]['username'], config.users[user]['password'], config.sites['Default'])

        if common.foundAlert(driver):
            common.respondToAlert(driver, 0)
        if common.foundTour(driver):
            common.exitTour(driver)
        # if len(driver.find_elements(By.ID, "com.view.viewglass:id/view_btnTV")) > 0:
        #     common.navIcon(driver)
    # User needs to be logged out
    else:
        if isLoggedIn:
            if common.foundAlert(driver):
                common.respondToAlert(driver, 0)
            if common.foundTour(driver):
                common.exitTour(driver)
            if len(driver.find_elements(By.ID, "com.view.viewglass:id/view_btnTV")) > 0:
                common.navIcon(driver)
            logout(driver)
            sleep(20)
        else:
            sleep(20)


def login(driver, username, password):
    attempts = 0
    while attempts < 3:
        if len(driver.find_elements(By.ID, "com.view.viewglass:id/retry_btn")) > 0:
            driver.find_element_by_id("com.view.viewglass:id/retry_btn").click()

        if len(driver.find_elements(By.XPATH, "//android.widget.Button[@content-desc='Login']")) > 0:
            loginOperation(driver, username, password)
            try:
                findElements = [("ID", "com.view.viewglass:id/search_image_view"),
                                ("XPATH", "//android.widget.TextView[@text='Recently Crashed!!!']"),
                                ("ID", "com.view.viewglass:id/home_controlIV")]
                common.waitForElement(driver, findElements, 120)
                # WebDriverWait(driver, 120).until(lambda driver: len(driver.find_elements(By.ID,"com.view.viewglass:id/search_image_view")) > 0 or len(driver.find_elements(By.XPATH,"//android.widget.TextView[@text='Recently Crashed!!!']")) > 0 or len(driver.find_elements(By.ID,"com.view.viewglass:id/home_controlIV")) > 0)
            except TimeoutException:
                print("didn't find anything after 2 minutes")
                pass

        # after user enters valid credentials and clicks the login button, check if
        # (1) user is led to the Select Site screen, or (2) in the Control screen (RO user), or (3) in Control
        # screen with a 'Recently Crashed' alert. If so, break, and continue (maybe respond to alert)
        if len(driver.find_elements(By.ID, "com.view.viewglass:id/search_image_view")) > 0 or len(driver.find_elements(By.ID, "com.view.viewglass:id/home_controlIV")) > 0:
            break
        elif len(driver.find_elements(By.XPATH, "//android.widget.TextView[@text='Recently Crashed!!!']")) > 0:
            common.respondToAlert(driver, 0)
            break
        elif common.foundTour(driver):
            common.exitTour(driver)
            break
        elif len(driver.find_elements(By.XPATH, "//android.widget.TextView[@text='Site is not reachable. Please try again later or contact Facilities Manager or View Support at support@viewglass.com or (855)-478-8468']")) > 0:
            raiseExceptions("Site is not reachable for the user at the moment")
        else:
            attempts += 1
            driver.close_app()
            driver.launch_app()
            sleep(20)

    if attempts == 3:
        raiseExceptions("Unable to login after 3 tries")


def loginAndSelectSite(driver, username, password, siteToLogInto):
    attempts = 0
    while attempts < 3:
        if len(driver.find_elements(By.ID, "com.view.viewglass:id/retry_btn")) > 0:
            driver.find_element_by_id("com.view.viewglass:id/retry_btn").click()

        if len(driver.find_elements(By.XPATH, "//android.widget.Button[@content-desc='Login']")) > 0:
            loginOperation(driver, username, password)
            try:
                findElements = [("ID", "com.view.viewglass:id/search_image_view"),
                                ("XPATH", "//android.widget.TextView[@text='Recently Crashed!!!']"),
                                ("ID", "com.view.viewglass:id/retry_btn"),
                                ("ID", "com.view.viewglass:id/home_controlIV")]
                common.waitForElement(driver, findElements, 120)
                # WebDriverWait(driver, 120).until(lambda driver: len(driver.find_elements(By.ID,"com.view.viewglass:id/search_image_view")) > 0 or len(driver.find_elements(By.XPATH,"//android.widget.TextView[@text='Recently Crashed!!!']")) > 0 or len(driver.find_elements(By.ID,"com.view.viewglass:id/home_controlIV")) > 0)
            except TypeError:
                print("didn't find anything after 2 minutes")
                pass

        if len(driver.find_elements(By.ID, "com.view.viewglass:id/retry_btn")) > 0:
            driver.find_element_by_id("com.view.viewglass:id/retry_btn").click()

        # after user enters valid credentials and clicks the login button, check if
        # (1) user is led to the Select Site screen, or (2) in the Control screen (RO user), or (3) in Control
        # screen with a 'Recently Crashed' alert. If so, break, and continue (maybe respond to alert)
        if len(driver.find_elements(By.ID, "com.view.viewglass:id/search_image_view")) > 0:
            site.selectSite(driver, siteToLogInto)

        if len(driver.find_elements(By.ID, "com.view.viewglass:id/home_controlIV")) > 0:
            break
        elif len(driver.find_elements(By.XPATH, "//android.widget.TextView[@text='Recently Crashed!!!']")) > 0:
            common.respondToAlert(driver, 0)
            sleep(5)
            break
        elif len(driver.find_elements(By.ID, "com.view.viewglass:id/view_btnTV")) > 0:
            driver.find_element_by_id("com.view.viewglass:id/view_btnTV").click()
            break
        elif common.foundTour(driver):
            common.exitTour(driver)
            break
        elif len(driver.find_elements(By.XPATH, "//android.widget.TextView[@text='Site is not reachable. Please try again later or contact Facilities Manager or View Support at support@viewglass.com or (855)-478-8468']")) > 0:
            raiseExceptions("Site is not reachable at the moment")
        else:
            attempts += 1
            driver.close_app()
            driver.launch_app()
            sleep(20)

        if common.foundTour(driver):
            common.exitTour(driver)
        if len(driver.find_elements(By.ID, "com.view.viewglass:id/view_btnTV")) > 0:
            driver.find_element_by_id("com.view.viewglass:id/view_btnTV").click()
            sleep(5)

    if attempts == 3:
        raiseExceptions("Unable to login after 3 tries")


def loginOperation(driver, username, password):
    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@index='0']")))
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
    except TimeoutException:
        raiseExceptions("Missing Email text field")

    if WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@text='Password']"))):
        # some devices have trouble navigating to the password text field
        location = driver.find_element_by_id("com.view.viewglass:id/web_view_LL").location
        size = driver.find_element_by_id("com.view.viewglass:id/web_view_LL").size
        x = location['x'] + size['width'] / 2
        y = location['y'] + 260 + driver.find_element_by_xpath("//android.widget.EditText[@text='Password']").size['height']
        driver.tap([(x, y)])

        pw = driver.find_element_by_xpath("//android.widget.EditText[@text='Password']")
        pw.send_keys(password)
    else:
        raiseExceptions("Missing Password text field")

    if len(driver.find_elements(By.CLASS_NAME, "android.widget.CheckBox")):
        rememberMe = driver.find_element_by_class_name("android.widget.CheckBox")
        if rememberMe.get_attribute("checked") == "false":
            rememberMe.click()
        else:
            # close the keyboard to make the login button visible
            driver.hide_keyboard()
            # driver.find_element_by_xpath("//android.view.View[@index='3']").click()
    else:
        raiseExceptions("Missing Remember Me check box")

    if len(driver.find_elements(By.XPATH, "//android.widget.Button[@content-desc='Login']")):
        # some devices have trouble navigating to the login button
        if len(driver.find_elements(By.XPATH, "//android.widget.Button[@content-desc='Login']")) > 0:
            location = driver.find_elements(By.CLASS_NAME, "android.webkit.WebView")[0].location
            size = driver.find_elements(By.CLASS_NAME, "android.webkit.WebView")[0].size
            x = location['x'] + size['width'] / 2
            y = location['y'] + size['height'] - \
                driver.find_element_by_xpath("//android.widget.Button[@content-desc='Login']").size['height']
            driver.tap([(x, y - 100)])
            driver.tap([(x, y)])
            sleep(5)
        if len(driver.find_elements(By.XPATH, "//android.widget.Button[@content-desc='Login']")) > 0:
            driver.find_element_by_xpath("//android.widget.Button[@content-desc='Login']").click()
    else:
        raiseExceptions("Missing Login button")


def loginScreenValidations(driver):
    if len(driver.find_elements(By.XPATH, "//android.view.View[@content-desc='User Authentication Failed']")) > 0:
        pass
    elif len(driver.find_elements(By.XPATH, "//android.widget.Button[@content-desc='Login']")) > 0:
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
            EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@text='Password']"))):
        pw = driver.find_element_by_xpath("//android.widget.EditText[@text='Password']")
        pw.send_keys(password)
    else:
        print("Invalid password validation ")

    if WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "android.widget.CheckBox"))):
        rememberMe = driver.find_element_by_class_name("android.widget.CheckBox")
        if rememberMe.get_attribute("checked") == "false":
            rememberMe.click()
        else:
            driver.hide_keyboard()
            # close the keyboard to make the login button visible
            # driver.find_element_by_xpath("//android.view.View[@index='3']").click()
    else:
        print("Remember me validation ")

    if WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Login']"))):
        driver.find_element_by_xpath("//android.widget.Button[@content-desc='Login']").click()
    else:
        print("Login button validation ")

