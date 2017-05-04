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

import unittest

from android import Control
from android import SelectSite

from viewTestAutomation import SystemReady
from viewTestAutomation.third_party import HTMLTestRunner


class RunTests(unittest.TestCase):
    def test_main(self):
        # Run HTMLTestRunner. Verify the HTML report.
        self.systemReadySuite = unittest.defaultTestLoader.loadTestsFromTestCase(SystemReady.SystemReady)
        # suite of TestCases
        self.suite = unittest.TestSuite()
        self.suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Control.Control),
            # unittest.defaultTestLoader.loadTestsFromTestCase(LiveView.LiveView),
            #         unittest.defaultTestLoader.loadTestsFromTestCase(Schedule.Schedule),
            # unittest.defaultTestLoader.loadTestsFromTestCase(Authentication.authentication),
            unittest.defaultTestLoader.loadTestsFromTestCase(SelectSite.SelectSite)
            #             unittest.defaultTestLoader.loadTestsFromTestCase(Zones.Zones)
        ])

        # Invoke TestRunner
        outfile = open("ViewTestReport.html", "w")
        # runner = unittest.TextTestRunner(buf)       #DEBUG: this is the unittest baseline
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='View Inc Automation',
            description='View Inc Automation TestCases for iOS and Android.'
        )
        # if runner.run(self.systemReadySuite).wasSuccessful():
        runner.run(self.suite)


if __name__ == '__main__':
    unittest.main()
