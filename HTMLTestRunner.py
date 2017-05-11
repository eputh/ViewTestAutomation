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

import unittest
import os
import datetime
from bs4 import BeautifulSoup
import sys
import time
import unittest
from random import randint

import SystemReady
import test
from third_party import HTMLTestRunner as TestRunner


class RunTests(unittest.TestCase):
    def test_main(self):
        # Run HTMLTestRunner. Verify the HTML report.
        self.systemReadySuite = unittest.defaultTestLoader.loadTestsFromTestCase(SystemReady.SystemReady)
        # suite of TestCases
        self.suite = unittest.TestSuite()
        self.suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(test.Test)
            # unittest.defaultTestLoader.loadTestsFromTestCase(Control.Control),
            # unittest.defaultTestLoader.loadTestsFromTestCase(LiveView.LiveView),
            #         unittest.defaultTestLoader.loadTestsFromTestCase(Schedule.Schedule),
            # unittest.defaultTestLoader.loadTestsFromTestCase(Authentication.authentication),
            # unittest.defaultTestLoader.loadTestsFromTestCase(SelectSite.SelectSite)
            #             unittest.defaultTestLoader.loadTestsFromTestCase(Zones.Zones)
        ])

        # Invoke TestRunner
        random = randint(1, 200)
        reportfile = os.path.abspath(os.path.join(os.path.dirname(__file__), 'report/ViewTestReport' + str(random) + '.html'))
        outfile = open(reportfile, "w+")
        # runner = unittest.TextTestRunner(buf)       #DEBUG: this is the unittest baseline
        runner = TestRunner.HTMLTestRunner(
            stream=outfile,
            title='View Inc Automation',
            description='View Inc Automation TestCases for iOS and Android.'
        )
        if runner.run(self.systemReadySuite).wasSuccessful():
            runner.run(self.suite)
        outfile.close()


# class HTMLTestRunner(unittest.TestProgram):
#
#     def __init__(self, stream=sys.stdout, verbosity=1):
#         self.stream = stream
#         self.soup = BeautifulSoup(self.stream, "html.parser")
#         self.verbosity = verbosity
#         self.startTime = datetime.datetime.now()
#
#     def run(self, test):
#         """
#         Run the given test case or test suite.
#         """
#         result = unittest.TextTestRunner().run(test)
#         self.stopTime = datetime.datetime.now()
#         self.generate_report()
#         print(sys.stderr, '\nTime Elapsed: %s' % (self.stopTime-self.startTime))
#         return result
#
#     def generate_report(self):
#         report = self.soup.find("div", {"class": "reports"})
#         print("tyring to generate report")
#         # device_report = self.soup.new_tag("div")
#         # device_report['class'] = "container bgcolor-" + str(randint(1, 10))
#         #
#         # col = self.soup.new_tag("div")
#         # col['class'] = "col-xs-offset-1 col-xs-10 col-sm-10 col-md-10 col-lg-10"
#         #
#         # heading = self.soup.new_tag("h2")
#         # heading.string = "Device: Device Name Here"
#         #
#         # col.append(heading)
#         # device_report.append(col)
#         # report.append(device_report)
#         #
#         # self.stream.write(str(report))
#
#     def end_report(self):
#         self.stream.write('</div></div></body></html>"')


if __name__ == '__main__':
    unittest.main()
