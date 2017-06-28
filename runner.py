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
# Runner communicates with the test homepage, sending a list of the devices
# connected to the system, and receiving a list of the devices selected
# by the user for testing. It will also start the Selenium Grid Server and
# threads accordingly and concurrently
#
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
from datetime import datetime
from time import sleep

from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask import make_response
app = Flask(__name__)

from common import config


# find the path of the selenium-server-standalone jar file
# and execute the appropriate shell command
def start_selenium_grid():
    filename = os.path.abspath(os.getcwd()).replace("viewTestAutomation", "").replace("PycharmProjects", "") + "selenium-server-standalone-3.4.0.jar"
    subprocess.Popen("java -jar " + filename + " -role hub", shell=True)


# render the template provided in templates/
@app.route("/")
def home():
    start_selenium_grid()
    return render_template('ViewTestReport.html')


# map to the JavaScript beginTests function using a POST request
# grab the parameter (a string of all of the devices selected)
# for each device, start a thread that runs HTMLTestRunner.py
# this function is required to return something (in this case, I just passed "running"
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
        for d in devices:
            file = create_file(d)
            p = subprocess.Popen([sys.executable, "HTMLTestRunner.py", file])
            processes.append(p)

        for process in processes:
            process.wait()

        result = "return this"
        resp = make_response('{"response": ' + result + '}')
        resp.headers['Content-Type'] = "application/json"
        return resp
    return "running"


# this function is called on by getadbDevices in JavaScript
# executes the shell command "adb devices" and reads the output
# into a list and converts it to a JSON object that will passed
# back to the JavaScript function
@app.route('/get_adb_devices', methods=['GET', 'POST'])
def getadbDevices():
    cmd = 'adb devices'
    d = subprocess.check_output(cmd.split())
    devs = str(d)
    devs = devs.replace("\\tdevice", "").replace("'", "").split("\\r\\n")
    return jsonify(result=devs[1:len(devs)-2])


# for each device, execute the shell command to start the appropriate
# appium node servers
# the exact commands are specified in common.config.py
def set_appium_nodes(devices):
    for d in devices:
        os.system("start " + config.devices[d]['nodeCommand'])


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

if __name__ == '__main__':
    app.run(debug=True)
