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
from appium import webdriver
from random import randint

import SystemReady
from third_party import HTMLTestRunner as TestRunner

from test import Test
from android import Control
from android import LiveView
from android import Authentication
from android import SelectSite


class RunTests(unittest.TestCase):

    def test_main(self):
        # Run HTMLTestRunner. Verify the HTML report.
        self.systemReadySuite = unittest.defaultTestLoader.loadTestsFromTestCase(SystemReady.SystemReady)
        # suite of TestCases
        self.suite = unittest.TestSuite()
        self.suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Test),
            unittest.defaultTestLoader.loadTestsFromTestCase(LiveView.LiveView),
            unittest.defaultTestLoader.loadTestsFromTestCase(Control.Control),
            #         unittest.defaultTestLoader.loadTestsFromTestCase(Schedule.Schedule),
            unittest.defaultTestLoader.loadTestsFromTestCase(Authentication.Authentication),
            unittest.defaultTestLoader.loadTestsFromTestCase(SelectSite.SelectSite)
            #             unittest.defaultTestLoader.loadTestsFromTestCase(Zones.Zones)
        ])

        # Invoke TestRunner
        random = randint(1, 200)
        reportfile = os.path.abspath(os.path.join(os.path.dirname(__file__), 'report/ViewTestReport' + str(random) + '.html'))
        print("Creating file: ", reportfile)
        outfile = open(reportfile, "w+")
        # runner = unittest.TextTestRunner(buf)       #DEBUG: this is the unittest baseline
        runner = TestRunner.HTMLTestRunner(
            stream=outfile,
            title='View Inc Automation',
            description='View Inc Automation TestCases for iOS and Android.'
        )
        # if runner.run(self.systemReadySuite).wasSuccessful():
        print("Beginning test suite")
        runner.run(self.suite)
        # else:
        #     print("Unsuccessful launch of test suite. System was not ready.")
        outfile.close()


if __name__ == '__main__':
    unittest.main()
