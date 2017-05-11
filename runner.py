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

from flask import Flask, render_template, redirect, url_for, request
from flask import make_response
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('ViewTestReport.html')


@app.route('/run_tests', methods=['GET', 'POST'])
def run_tests():
    if request.method == 'POST':
        num_of_connected_devices = request.form['param']
        print("Number of devices for testing: ", num_of_connected_devices)
        processes = []
        for i in range(0, int(num_of_connected_devices)):
            p = subprocess.Popen([sys.executable, "HTMLTestRunner.py"])
            processes.append(p)

        for process in processes:
            process.wait()

        result = "return this"
        resp = make_response('{"response": ' + result + '}')
        resp.headers['Content-Type'] = "application/json"
        return resp


if __name__ == '__main__':
    app.run(debug=True)
