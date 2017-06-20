"""
########################################################################
#
# SYNOPSIS
#   config -- Shared configuration data for View automated tests
#
# AUTHOR
#  Prinal khandelwal (Pkhandelwal@viewglass.com)
#
#
# DESCRIPTION
#   This file contains the global configuration data for View plugins that's shared by
#   all the test class files.
#
# USAGE
#   import view_cfg
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

device = 'RKumar iPhone'
site = ["NC20test", "tintserver7700", "APPCloudTest1"]

# if a new device is added, make sure to update the ViewTestReport template
devices = {
    '0abad235030d17a3': {
        'name': 'Galaxy Tab S2',
        'hasData': False,
        'nodeCommand': 'appium --nodeconfig ' + os.path.abspath(os.path.join(os.getcwd(), 'capabilities/GalaxyTabS2.json')) + ' -p 4760 -bp 4765 -U 0abad235030d17a3'
    },

    'FA68W0308348': {
        'name': 'Google Pixel',
        'hasData': True,
        'nodeCommand': 'appium --nodeconfig ' + os.path.abspath(os.path.join(os.getcwd(), 'capabilities/GooglePixel.json')) + ' -p 4740 -bp 4745 -U FA68W0308348'
    },

    'HT6AE0100527': {
        'name': 'HTC 10',
        'hasData': True,
        'nodeCommand': 'appium --nodeconfig ' + os.path.abspath(os.path.join(os.getcwd(), 'capabilities/HTC10.json')) + ' -p 4730 -bp 4735 -U HT6AE0100527'
    },
    '09c119410bfc3c60': {
        'name': 'Nexus 5',
        'hasData': False,
        'nodeCommand': 'appium --nodeconfig ' + os.path.abspath(os.path.join(os.getcwd(), 'capabilities/nexus5.json')) + ' -p 3030 -bp 3035 -U 09c119410bfc3c60'
    },
    '092326c6': {
        'name': 'Nexus 7',
        'hasData': False,
        'nodeCommand': 'appium --nodeconfig ' + os.path.abspath(os.path.join(os.getcwd(), 'capabilities/nexus7.json')) + ' -p 4723 -bp 4725 -U 092326c6'
    },
    '45ddeb64': {
        'name': 'Samsung Galaxy S7',
        'hasData': True,
        'nodeCommand': 'appium --nodeconfig ' + os.path.abspath(os.path.join(os.getcwd(), 'capabilities/SamsungGalaxy.json')) + ' -p 4780 -bp 4785 -U 45ddeb64'
    },
    '98877638575030504c': {
        'name': 'Samsung Galaxy S8',
        'hasData': True,
        'nodeCommand': 'appium --nodeconfig ' + os.path.abspath(os.path.join(os.getcwd(), 'capabilities/SamsungGalaxyS8.json')) + ' -p 4810 -bp 4815 -U 98877638575030504c'
    },
    '98895a36453348354d': {
        'name': 'Samsung Galaxy S8 Plus',
        'hasData': True,
        'nodeCommand': 'appium --nodeconfig ' + os.path.abspath(os.path.join(os.getcwd(), 'capabilities/SamsungGalaxyS8Plus.json')) + ' -p 4790 -bp 4795 -U 98895a36453348354d'
    },
    'iPhone Simulator': {
        'name': 'iPhone Simulator',
        'hasData': False,
        'nodeCommand': 'appium --nodeconfig ' + os.path.abspath(os.path.join(os.getcwd(), 'capabilities/iPhone.json')) + ' -p 4820 -bp 4825'
    }
}

users = {
    'CRUDO': {
        'username': 'view.test10@viewglass.com',
        'password': 'Passw0rd!'
    },
    'RUO': {
        'username': 'view.test06@viewglass.com',
        'password': 'Passw0rd!'
    },
    'RO': {
        'username': 'view.test05@viewglass.com',
        'password': 'Passw0rd!',
        'testsite': 'B155salesOP'
    },
    'InvalidEmail': {
        'username': 'view.test05@vglass.com',
        'password': 'Passw0rd!'
    },
    'InvalidPwd': {
        'username': 'view.test05@ewglass.com',
        'password': 'Passw'
    },
    'PwdStartingSpecialChar': {
        'username': 'view.test05@viewglass.com',
        'password': '#Passw0d!'
    },
    'MissingEmail': {
        'username': '',
        'password': 'Passw0rd!'
    },
    'MissingPwd': {
        'username': 'view.test05viewglass.com',
        'password': ''
    },
    'UserNotConfiguredInVRM': {
        'username': 'view.test02@viewglass.com',
        'password': 'Passw0rd!'
    },
    '1dot2System': {
        'username': 'view.test02@viewglass.com',
        'password': 'Passw0rd!'
    },
    'SingleSite': {
        'username': 'view.test09@viewglass.com',
        'password': 'Passw0rd!'
    }
}

# virovar = dict(
#                Username = len("id = 'userBox_ip_EditText'"),
#                Email = len("id='userBox_ip_EditText'"),
#                Newuser = ("dummyc"),
#                Phone = "1234567",
#                Newmail = "dummy@viewglass.com",
#                Newpass = "dummya",
#                NZone = "PLACE 1",
#                NZoneG = "ZG A1",
#                NScene = "SCENE 1",
#                )

# states = dict(
#               A = "self.client.clickCoordinate(735, 815, 1)",
#               B = "self.client.clickCoordinate(285, 1125, 1)",
#               C = "self.client.clickCoordinate(345, 805, 1)",
#               D = "self.client.clickCoordinate(765, 1165, 1)",
#               )
# wallswitch = dict(
#                   A = "self.client.clickCoordinate(255, 1225, 1)",
#                   B = "self.client.clickCoordinate(518, 1225, 1)",
#                   C = "self.client.clickCoordinate(775, 1225, 1)",
#                   D ="self.client.clickCoordinate(254, 1390, 1)"
#                   )

tint_levels = [1, 2, 3, 4]

repeat = {
    'No Repeat': {
        'location': 'self.client.click("NATIVE", "xpath=//*[@text=\'No Repeat\']", 0, 1)'
    },
    'Everyday': {
        'location': 'self.client.click("NATIVE", "xpath=//*[@text=\'Everyday\']", 0, 1)'
    },
    'Weekly': {
        'location': 'self.client.click("NATIVE", "xpath=//*[@text=\'Weekly\']", 0, 1)'
    },
    'Monday to Friday': {
        'location': 'self.client.click("NATIVE", "xpath=//*[@text=\'Monday to Friday\']", 0, 1)'
    }
}