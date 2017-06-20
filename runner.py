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

import os
import sys
import subprocess
from time import sleep
from sys import platform

from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask import make_response
app = Flask(__name__)

from common import config


@app.route("/")
def home():
    return render_template('ViewTestReport.html')


@app.route('/run_tests', methods=['GET', 'POST'])
def run_tests():
    if request.method == 'POST':
        connected_devices = request.form['param']
        devices = connected_devices.split(";")
        devices.pop(-1)
        print("Devices selected for testing:", devices)
        set_appium_nodes(devices)
        sleep(15)

        processes = []
        for i in range(0, len(devices)):
            p = subprocess.Popen([sys.executable, "HTMLTestRunner.py"])
            processes.append(p)

        for process in processes:
            process.wait()

        result = "return this"
        resp = make_response('{"response": ' + result + '}')
        resp.headers['Content-Type'] = "application/json"
        return resp
    return "running"


@app.route('/get_adb_devices', methods=['GET', 'POST'])
def getadbDevices():
    cmd = 'adb devices'
    d = subprocess.check_output(cmd.split())
    devs = str(d)
    devs = devs.replace("\\tdevice", "").replace("'", "").split("\\r\\n")
    return jsonify(result=devs[1:len(devs)-2])


def set_appium_nodes(devices):
    for d in devices:
        os.system("start " + config.devices[d]['nodeCommand'])


if __name__ == '__main__':
    app.run(debug=True)
