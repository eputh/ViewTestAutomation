from __future__ import print_function
"""
########################################################################
#
# SYNOPSIS
#   Runtest suite will run all the modules inside android package and generate a report 
#
# AUTHOR
#  Prinal khandelwal (Pkhandelwal@viewglass.com)
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
from datetime import datetime
from random import randint
from appium import webdriver

import SystemReady
from third_party import HTMLTestRunner as TestRunner

from android import Authentication, Control, LiveView, Profile, Scenes, Schedule, SelectSite, Settings, Zones, Network
from common import networkConnection as NetworkConnection


class RunTests(unittest.TestCase):

    def test_main(self):
        # Run HTMLTestRunner. Verify the HTML report.
        self.systemReadySuite = unittest.defaultTestLoader.loadTestsFromTestCase(SystemReady.SystemReady)
        self.networkConnectionSuite = unittest.defaultTestLoader.loadTestsFromTestCase(NetworkConnection.NetworkConnection)

        # suite of TestCases
        self.suite = unittest.TestSuite()
        self.suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Network.Network),
            unittest.defaultTestLoader.loadTestsFromTestCase(Profile.Profile),
            unittest.defaultTestLoader.loadTestsFromTestCase(Settings.Settings),
            unittest.defaultTestLoader.loadTestsFromTestCase(LiveView.LiveView),
            unittest.defaultTestLoader.loadTestsFromTestCase(Control.Control),
            unittest.defaultTestLoader.loadTestsFromTestCase(Zones.Zones),
            unittest.defaultTestLoader.loadTestsFromTestCase(Scenes.Scenes),
            unittest.defaultTestLoader.loadTestsFromTestCase(Schedule.Schedule),
            unittest.defaultTestLoader.loadTestsFromTestCase(Authentication.Authentication),
            unittest.defaultTestLoader.loadTestsFromTestCase(SelectSite.SelectSite)
        ])
        self.suite2 = unittest.TestSuite()
        self.suite2.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Network.Network),
            unittest.defaultTestLoader.loadTestsFromTestCase(Profile.Profile),
            unittest.defaultTestLoader.loadTestsFromTestCase(Settings.Settings),
            unittest.defaultTestLoader.loadTestsFromTestCase(LiveView.LiveView),
            unittest.defaultTestLoader.loadTestsFromTestCase(Control.Control),
            unittest.defaultTestLoader.loadTestsFromTestCase(Zones.Zones),
            unittest.defaultTestLoader.loadTestsFromTestCase(Scenes.Scenes),
            unittest.defaultTestLoader.loadTestsFromTestCase(Schedule.Schedule),
            unittest.defaultTestLoader.loadTestsFromTestCase(Authentication.Authentication),
            unittest.defaultTestLoader.loadTestsFromTestCase(SelectSite.SelectSite)
        ])

        # Invoke TestRunner
        random = randint(1, 200)
        id = datetime.strftime(datetime.now(), '%m%d%y-%H%M%S-')
        reportfile = os.path.abspath(os.path.join(os.path.dirname(__file__), 'report/ViewTestReport' + id + str(random) + '.html'))
        print("Creating file: ", reportfile)
        outfile = open(reportfile, "w+")
        # runner = unittest.TextTestRunner(buf)       #DEBUG: this is the unittest baseline
        runner = TestRunner.HTMLTestRunner(
            stream=outfile,
            title='View Inc Automation',
            description='View Inc Automation TestCases for iOS and Android.'
        )

        print("Beginning test suite")

        if runner.run(self.systemReadySuite).wasSuccessful():
            # self.driver.quit()
            # print("good")
            runner.run(self.suite)
            if runner.run(self.networkConnectionSuite).wasSuccessful():
                runner.run(self.suite2)
        else:
            print("Unsuccessful launch of test suite. System was not ready.")
        outfile.close()


if __name__ == '__main__':
    unittest.main()
