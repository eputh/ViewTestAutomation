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
device = 'RKumar iPhone'
site = "tintserver7700"

devices = {
    'Google1': {
        'deviceName': 'View Pixel'
    },

    'Nexus1': {
        'deviceName': 'Nexus5'
    },

    'Nexus2': {
        'deviceName': 'Nexus7'
    },
    'Samsung1': {
        'deviceName': 'Samsung Galaxy1'
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
        'password': 'Passw0rd!'
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