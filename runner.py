"""
########################################################################
#
# SYNOPSIS
#   runner :  Runner will run the test suite on all of connected devices
#               in parallel with one another
#
# AUTHOR
#  Emily Puth (emily.puth@viewglass.com)
#
#
# DESCRIPTION
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

import sys
import subprocess
import glob

# test = glob.glob('test.py')
# processes = []
# for test in tests:
# processes.append(Popen('python %s' % test, shell=True))
#
# for process in processes:
#     process.wait()

num_of_connected_devices = 3


def runTests():
    processes = []

    for i in range(0, num_of_connected_devices):
        p = subprocess.Popen([sys.executable, "SystemReady.py"])
        processes.append(p)

    for process in processes:
        process.wait()


if __name__ == '__main__':
    runTests()
