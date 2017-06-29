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
import sys
import unittest
from datetime import datetime
from random import randint
from appium import webdriver

import SystemReady
from third_party import HTMLTestRunner as TestRunner

from android import Authentication, Control, LiveView, Profile, Scenes, Schedule, SelectSite, Settings, Zones, Network
from common import networkConnection as NetworkConnection
from common import config


# for each device, create a report file where the name includes
# the name of the device and the time at which the test began
def create_file(device):
    id = datetime.strftime(datetime.now(), '%m-%d-%y-%H%M%S-')
    device_name = config.devices[device]['name'].replace(" ", "")
    reportfile = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'report/' + device_name + 'Report' + id + '.html'))
    outfile = open(reportfile, "w+")
    print("Created file: ", reportfile)
    return reportfile


def set_up_test_suite(testCases):
    suite = unittest.TestSuite()
    if "Select All" in testCases:
        tests = config.testcases
    else:
        tests = testCases

    for testcase in tests:
        suite.addTest(eval(config.testcases[testcase]['unittestCommand']))
        print("Added test case:", testcase)
    return suite


class RunTests(unittest.TestCase):
    device = ""
    testCases = []

    def test_main(self):
        # Run HTMLTestRunner. Verify the HTML report.
        self.systemReadySuite = unittest.defaultTestLoader.loadTestsFromTestCase(SystemReady.SystemReady)
        self.networkConnectionSuite = unittest.defaultTestLoader.loadTestsFromTestCase(NetworkConnection.NetworkConnection)

        # suite of TestCases
        self.suite = set_up_test_suite(self.testCases)

        # Invoke TestRunner
        reportfile = create_file(self.device)
        outfile = open(reportfile, "w+")
        # runner = unittest.TextTestRunner(buf)       #DEBUG: this is the unittest baseline
        runner = TestRunner.HTMLTestRunner(
            stream=outfile,
            title='View Inc Automation',
            description='View Inc Automation TestCases for iOS and Android.'
        )

        runner.run(self.suite)
        # if runner.run(self.systemReadySuite).wasSuccessful():
        #     runner.run(self.suite)
        #     if runner.run(self.networkConnectionSuite).wasSuccessful():
        #         runner.run(self.suite2)
        # else:
        #     print("Unsuccessful launch of test suite. System was not ready.")
        outfile.close()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        testcases = sys.argv.pop()
        RunTests.testCases = testcases.split(";")
        RunTests.testCases.pop()
        RunTests.device = sys.argv.pop()
    unittest.main()
