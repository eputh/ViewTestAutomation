"""
########################################################################
#
# SYNOPSIS
#   Zones :  Include Test cases related to create, delete , edit zone groups for CRUDO, RUO, RO privilege users
#
# AUTHOR
#  Emily Puth (emily.puth@viewglass.com)
#
#
# DESCRIPTION
#   Include Test cases related to create, delete , edit zone groups for CRUDO, RUO, RO privilege users
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

import os
import unittest
from logging import raiseExceptions
from time import sleep

from appium import webdriver
from appium.webdriver.connectiontype import ConnectionType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from common import auth as auth
from common import commonFunctions as common
from common import site as site
from common import config as config


class SelectSite(unittest.TestCase):
    """Class to run tests against the View app"""
    def setUp(self):
        """Setup for the test"""
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = os.path.abspath(os.path.join(os.getcwd(), 'apps\\Android.apk'))
        desired_caps['appPackage'] = 'com.view.viewglass'
        desired_caps['appActivity'] = 'com.view.viewglass.Splash'
        desired_caps['autoGrantPermissions'] = True
        desired_caps['noReset'] = True
        desired_caps['clearSystemFiles'] = True
        self.driver = webdriver.Remote('http://localhost:4444/wd/hub', desired_caps)

    def tearDown(self):
        """Tear down the test"""
        self.driver.quit()

    # @attr('acceptance', sid='TC-zones-1.1, TC-zones-1.2, TC-zones-1.5, TC-zones-1.6', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testVerifyUIComponentsOfZonesScreen(self):
        print("Favorites, zone item names")

    # @attr('acceptance', sid='TC-zones-1.3, TC-zones-1.4. TC-zones-1.8-1.12', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testFunctionalityOfUIComponentsForZonesScreen(self):
        print("ui")

    # @attr('acceptance', sid='TC-zngrpdet-2.1,TC-zngrpdet-2.3,TC-zngrpdet-2.5, TC-zndet-3.3,TC-zndet-3.1', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def verifyUIComponentsOfZoneGroupDetailScreen(self):
        print("back button, etc.")

    # @attr('acceptance', sid='TC-crtzngp-9.1', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testVerifyUIComponentsOfCreateZoneGroupScreen(self):
        print("ui")

    # @attr('acceptance', sid='TC-crtzngp-9.2, TC-crtzngp-9.4', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testVerifyFunctionalityOfUIComponentsForCreateZoneGroupScreen(self):
        print("ui")

    # @attr('acceptance', sid='TC-zones-1.13', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testNavigationIconInZones(self):
        print("navigation icon")

    # @attr('acceptance', sid='TC-search-4.1, TC-search-4.6, TC-search-4.2-4.5, TC-search-4.8', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testFunctionalityOfSearching(self):
        print("ui")

    # @attr('acceptance', sid='TC-zngrpdet-2.2, TC-zndet-3.2', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testOverrideZoneGroupTint(self):
        print("ui")

    # @attr('acceptance', sid='TC-zngrpdet-2.6', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testZoneGroupsWithMixedTint(self):
        print("ui")

    def testManageFavorites(self):
        print("ui")

    # # @attr('acceptance', sid='TC-search-4.7', bv=10)
    # # @unittest.skip('Test case temporarily disabled')
    # def testCloseSearchWithCrossButton(self):
    #     print("ui")

    # @attr('acceptance', sid='TC-crtzngp-9.3, TC-crtzngp-9.5-9.8', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCreateZoneGroupForCRUDO(self):
        print("ui")

    # @attr('acceptance', sid='TC-crtzngp-9.3, TC-crtzngp-9.5-9.8', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCreateZoneGroupForRUO(self):
        print("ui")

    # @attr('acceptance', sid='TC-crtzngp-9.3, TC-crtzngp-9.5-9.8', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testCreateZoneGroupForRO(self):
        print("ui")

    # @attr('acceptance', sid='TC-zngrpdet-2.7, TC-zndet-3.5, TC-crtzngp-9.11, TC-crtzngp-9.12', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testEditZoneGroupForCRUDO(self):
        print("ui")

    # @attr('acceptance', sid='TC-zngrpdet-2.7, TC-zndet-3.5, TC-crtzngp-9.11, TC-crtzngp-9.12', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testEditZoneGroupForRUO(self):
        print("ui")

    # @attr('acceptance', sid='TC-zngrpdet-2.7, TC-zndet-3.5, TC-crtzngp-9.11, TC-crtzngp-9.12', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testEditZoneGroupForRO(self):
        print("ui")

    # @attr('acceptance', sid='TC-crtzngp-9.9, TC-crtzngp-9.10', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testDeleteZoneGroupForCRUDO(self):
        print("ui")

    # @attr('acceptance', sid='TC-crtzngp-9.9, TC-crtzngp-9.10', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testDeleteZoneGroupForRUO(self):
        print("ui")

    # @attr('acceptance', sid='TC-crtzngp-9.9, TC-crtzngp-9.10', bv=10)
    # @unittest.skip('Test case temporarily disabled')
    def testDeleteZoneGroupForRO(self):
        print("ui")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SelectSite)
    unittest.TextTestRunner(verbosity=2).run(suite)


